using ModMiiDownloader.Model;
using System.Text;

namespace ModMiiDownloader.Controls;

/// <summary>A titled list of downloadable items with the "Toggle All" button underneath.</summary>
public class DownloadListSection : SectionBox {
    public DownloadListSection() : this(new DownloadListView()) {
    }

    protected DownloadListSection(DownloadListView list) {
        List = list;
        List.Dock = DockStyle.Fill;
        List.EntryClicked += OnEntryClicked;

        ToggleButton = new Button {
            Text = "Toggle All",
            Dock = DockStyle.Bottom,
            Height = 30,
            Margin = new Padding(0, 5, 0, 0),
            FlatStyle = FlatStyle.System,
        };
        ToggleButton.Click += (_, _) => List.ToggleAll();

        var spacer = new Panel { Dock = DockStyle.Bottom, Height = 5 };

        Controls.Add(List);
        Controls.Add(spacer);
        Controls.Add(ToggleButton);
    }

    private IReadOnlyList<string> _hidden = [];

    public DownloadListView List { get; }

    public Button ToggleButton { get; }

    public IEnumerable<DownloadEntry> SelectedEntries => List.SelectedEntries;

    public void Load(DownloaderConfig config, string page, string category) {
        IReadOnlyList<DownloadItemInfo> items = config.Items(page, category);

        List.SetEntries(items
            .Where(info => !info.HiddenHere)
            .Select(info => new DownloadEntry(info, page, category)));

        // Items hidden on this platform still owe ModMii a variable, so keep their ids.
        _hidden = items.Where(info => info.HiddenHere && !info.Disabled)
            .Select(info => info.Id)
            .ToList();
    }

    public void SelectChild(string id) {
        List.Select(id);
    }

    public void DeselectAll() {
        List.DeselectAll();
    }

    /// <summary>
    /// The "set id=*" lines for this section. Disabled entries are left out entirely, the
    /// way the Qt build had it; entries hidden on this platform are written unselected.
    /// </summary>
    public string GetSelected() {
        var builder = new StringBuilder();

        foreach (ListViewItem item in List.Items) {
            var entry = (DownloadEntry)item.Tag!;
            if (entry.Disabled) continue;
            builder.Append(QueueVars.Line(entry.Id, item.Selected));
        }

        foreach (string id in _hidden)
            builder.Append(QueueVars.Line(id, selected: false));

        return builder.ToString();
    }

    private void OnEntryClicked(object? sender, DownloadEntryEventArgs e) {
        if (e.Entry.Url is not null) {
            e.Entry.Visited = true;
            List.Invalidate(e.Item.Bounds);
            OpenUrl(e.Entry.Url);
        }

        if (e.Entry.Warning is not null && e.Item.Selected) {
            DialogResult answer = MessageBox.Show(
                this, e.Entry.Warning, "Warning",
                MessageBoxButtons.YesNo, MessageBoxIcon.Warning);

            if (answer != DialogResult.Yes) e.Item.Selected = false;
        }
    }

    public static void OpenUrl(string url) {
        try {
            System.Diagnostics.Process.Start(new System.Diagnostics.ProcessStartInfo(url) { UseShellExecute = true });
        } catch (Exception e) {
            Log.Error(e, $"open \"{url}\"");
        }
    }
}
