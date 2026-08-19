namespace ModMiiDownloader.Forms;

using ModMiiDownloader.Controls;
using ModMiiDownloader.Model;
using ModMiiDownloader.Resources;
using System.Text.RegularExpressions;

/// <summary>
/// Type-to-filter view over everything the tabs hold, including the cIOS and theme
/// checkboxes, with a queue pane that is written back to the main window on save.
/// </summary>
public partial class SearchForm : Form {
    [GeneratedRegex(@"^c(\d+)_(\d+)_")]
    private static partial Regex CiosName();

    private readonly MainForm _main;
    private readonly DownloaderConfig _config;

    private readonly TextBox _query = new();
    private readonly DownloadListSection _results = new() { Title = "Results" };
    private readonly DownloadListSection _queue = new() { Title = "Queue" };

    private readonly HashSet<string> _originalIds = [];

    public SearchForm(MainForm main) {
        _main = main;
        _config = main.Config;

        Text = "Search";
        Icon = Icons.App;
        ClientSize = new Size(450, 450);
        MinimumSize = new Size(360, 320);
        StartPosition = FormStartPosition.CenterParent;
        ShowInTaskbar = false;
        MinimizeBox = false;
        MaximizeBox = false;

        BuildUi();
        PopulateQueue();
    }

    private void BuildUi() {
        var layout = new TableLayoutPanel {
            Dock = DockStyle.Fill,
            ColumnCount = 1,
            RowCount = 4,
            Padding = new Padding(5),
        };
        layout.RowStyles.Add(new RowStyle(SizeType.AutoSize));
        layout.RowStyles.Add(new RowStyle(SizeType.AutoSize));
        layout.RowStyles.Add(new RowStyle(SizeType.Percent, 100));
        layout.RowStyles.Add(new RowStyle(SizeType.AutoSize));

        _query.Dock = DockStyle.Fill;
        _query.PlaceholderText = "Enter query here...";
        _query.Margin = new Padding(0, 0, 0, 5);
        _query.TextChanged += (_, _) => RunSearch(_query.Text);
        layout.Controls.Add(_query, 0, 0);

        var buttons = new TableLayoutPanel {
            Dock = DockStyle.Fill,
            ColumnCount = 2,
            RowCount = 1,
            AutoSize = true,
            AutoSizeMode = AutoSizeMode.GrowAndShrink,
            Margin = new Padding(0, 0, 0, 5),
        };
        buttons.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 50));
        buttons.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 50));

        Button add = PaneButton("Add Selected", "plus");
        add.Click += (_, _) => AddSelected();
        buttons.Controls.Add(add, 0, 0);

        Button remove = PaneButton("Remove Selected", "minus");
        remove.Click += (_, _) => RemoveSelected();
        buttons.Controls.Add(remove, 1, 0);

        layout.Controls.Add(buttons, 0, 1);

        var panes = new TableLayoutPanel { Dock = DockStyle.Fill, ColumnCount = 2, RowCount = 1 };
        panes.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 50));
        panes.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 50));

        foreach (DownloadListSection? pane in new[] { _results, _queue }) {
            pane.Dock = DockStyle.Fill;
            pane.Margin = new Padding(2);
            pane.ToggleButton.Visible = false;
        }

        // Refreshing is deferred so the list is not rebuilt while it is still handling the
        // click that triggered it.
        _results.List.EntryDoubleClicked += (_, e) => {
            AddToQueue(e.Entry);
            BeginInvoke(Refresh_Results);
        };

        _queue.List.EntryDoubleClicked += (_, e) => {
            RemoveFromQueue(e.Entry);
            BeginInvoke(Refresh_Results);
        };

        panes.Controls.Add(_results, 0, 0);
        panes.Controls.Add(_queue, 1, 0);
        layout.Controls.Add(panes, 0, 2);

        var done = new Button {
            Text = "Done",
            Dock = DockStyle.Fill,
            Height = 30,
            FlatStyle = FlatStyle.System,
            Margin = new Padding(0, 5, 0, 0),
        };
        done.Click += (_, _) => Close();
        layout.Controls.Add(done, 0, 3);

        AcceptButton = done;
        Controls.Add(layout);
    }

    private static Button PaneButton(string text, string iconKey) {
        return new() {
            Text = text,
            Dock = DockStyle.Fill,
            Height = 30,
            Image = Icons.Get(iconKey, 16),
            ImageAlign = ContentAlignment.MiddleLeft,
            TextImageRelation = TextImageRelation.ImageBeforeText,
            Margin = new Padding(2),
        };
    }

    // ----------------------------------------------------------------- queue

    private IEnumerable<DownloadEntry> QueueEntries => _queue.List.Entries;

    private HashSet<string> QueueIds => QueueEntries.Select(entry => entry.Id).ToHashSet(StringComparer.Ordinal);

    private void PopulateQueue() {
        foreach (DownloadListSection section in _main.SectionsByCategory.Values) {
            foreach (DownloadEntry entry in section.SelectedEntries)
                _queue.List.Add(entry);
        }

        foreach (Control root in _main.CheckBoxRoots) {
            foreach (CheckBox? box in CheckBoxTools.All(root).Where(box => box.Enabled && box.Checked)) {
                DownloadEntry? entry = CheckBoxEntry(box.Name);
                if (entry is not null) _queue.List.Add(entry);
            }
        }

        Sort(_queue.List);

        foreach (string id in QueueIds) _originalIds.Add(id);
    }

    /// <summary>Builds the queue row that stands in for a checkbox, or null if it has no display name.</summary>
    private DownloadEntry? CheckBoxEntry(string name) {
        string? display = _config.CheckboxDisplayName(name);
        if (display is null) return null;

        if (display.Contains("PLACEHOLDER") && _main.D2xRev is not null)
            display = display.Replace("PLACEHOLDER", $"d2x-v{_main.D2xRev}");

        return new DownloadEntry(name, display, CheckBoxIcon(name));
    }

    private string CheckBoxIcon(string name) {
        Match match = CiosName().Match(name);
        return !match.Success
            ? Icons.Blank
            : _config.IsRecommendedWiiCios(int.Parse(match.Groups[1].Value), int.Parse(match.Groups[2].Value))
            ? "recommended"
            : Icons.Blank;
    }

    private static void Sort(DownloadListView list) {
        var items = list.Items.Cast<ListViewItem>().ToList();
        items.Sort((left, right) => string.Compare(left.Text, right.Text, StringComparison.OrdinalIgnoreCase));

        list.BeginUpdate();
        list.Items.Clear();
        foreach (ListViewItem? item in items) list.Items.Add(item);
        list.EndUpdate();
    }

    // ---------------------------------------------------------------- search

    private void RunSearch(string query) {
        string clean = Sanitize(query);
        _results.List.Items.Clear();

        if (clean.Length == 0) return;

        HashSet<string> queued = QueueIds;
        var matches = new List<DownloadEntry>();

        foreach ((string? page, Dictionary<string, DownloadCategory>? categories) in _config.DownloadList) {
            foreach ((string? category, DownloadCategory _) in categories) {
                matches.AddRange(_config.Items(page, category)
                    .Where(info => !queued.Contains(info.Id) && !info.HiddenHere)
                    .Select(info => new DownloadEntry(info, page, category))
                    .Where(entry => entry.Matches(clean)));
            }
        }

        matches.AddRange(MatchingCheckBoxes(clean, queued));
        matches.Sort((left, right) => string.Compare(left.Name, right.Name, StringComparison.OrdinalIgnoreCase));

        foreach (DownloadEntry entry in matches) _results.List.Add(entry);

        if (matches.Count == 0)
            _results.List.Add(DownloadEntry.Placeholder($"No results for \"{query}\""));
    }

    private IEnumerable<DownloadEntry> MatchingCheckBoxes(string clean, HashSet<string> queued) {
        foreach (Control root in _main.CheckBoxRoots) {
            foreach (CheckBox box in CheckBoxTools.All(root)) {
                if (!box.Enabled || box.Checked || queued.Contains(box.Name)) continue;

                string? display = _config.CheckboxDisplayName(box.Name);
                if (display is null) continue;

                if (!Sanitize(display).Contains(clean, StringComparison.Ordinal) &&
                    !Sanitize(box.Name).Contains(clean, StringComparison.Ordinal)) {
                    continue;
                }

                DownloadEntry? entry = CheckBoxEntry(box.Name);
                if (entry is not null) yield return entry;
            }
        }
    }

    private static string Sanitize(string text) {
        return Model.Search.Sanitize(text);
    }

    private void Refresh_Results() {
        _results.List.DeselectAll();
        RunSearch(_query.Text);
    }

    // ------------------------------------------------------------ add/remove

    private void AddSelected() {
        foreach (DownloadEntry? entry in _results.SelectedEntries.ToList()) AddToQueue(entry);
        Refresh_Results();
    }

    private void RemoveSelected() {
        foreach (DownloadEntry? entry in _queue.SelectedEntries.ToList()) RemoveFromQueue(entry);
        Refresh_Results();
    }

    private void AddToQueue(DownloadEntry entry) {
        if (entry.Disabled || QueueIds.Contains(entry.Id)) return;

        _queue.List.Add(entry);
        Sort(_queue.List);
    }

    private void RemoveFromQueue(DownloadEntry entry) {
        ListViewItem? item = _queue.List.Find(entry.Id);
        if (item is not null) _queue.List.Items.Remove(item);
    }

    // ----------------------------------------------------------------- close

    protected override void OnFormClosing(FormClosingEventArgs e) {
        HashSet<string> current = QueueIds;
        if (current.SetEquals(_originalIds)) {
            base.OnFormClosing(e);
            return;
        }

        switch (Confirm(current)) {
            case DialogResult.Yes:
                Apply();
                break;
            case DialogResult.Cancel:
                e.Cancel = true;
                return;
        }

        base.OnFormClosing(e);
    }

    private DialogResult Confirm(HashSet<string> current) {
        int added = current.Except(_originalIds).Count();
        int removed = _originalIds.Except(current).Count();

        var details = new List<string>();
        if (added > 0) details.Add($"{added} new item{(added > 1 ? "s" : "")}");
        if (removed > 0) details.Add($"{removed} removed item{(removed > 1 ? "s" : "")}");

        string text = "Do you want to save your changes?";
        if (details.Count > 0) text += $"\n\n{string.Join("\n", details)}";

        // Yes saves, No discards, Cancel returns to the dialog.
        return MessageBox.Show(this, text, "Search", MessageBoxButtons.YesNoCancel, MessageBoxIcon.Question);
    }

    private void Apply() {
        foreach (DownloadListSection section in _main.SectionsByCategory.Values) section.DeselectAll();
        foreach (Control root in _main.CheckBoxRoots) CheckBoxTools.UncheckAll(root);

        foreach (DownloadEntry entry in QueueEntries) {
            if (entry.IsCheckBox) {
                foreach (Control root in _main.CheckBoxRoots) CheckBoxTools.SelectChild(root, entry.Id);
                continue;
            }

            if (entry.Category is not null &&
                _main.SectionsByCategory.TryGetValue(entry.Category, out DownloadListSection? section)) {
                section.SelectChild(entry.Id);
            }
        }
    }
}
