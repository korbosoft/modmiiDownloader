namespace ModMiiDownloader.Forms;

using ModMiiDownloader.Controls;
using ModMiiDownloader.Model;
using ModMiiDownloader.Resources;
using System.Text;

public class MainForm : Form {
    private const string UnknownD2xRev = "korboscrewedup";

    private static readonly (string Page, string Category, string Title)[] Sections =
    [
        ("nus", "sysmenus", "System Menus"),
        ("nus", "realsigned", "Non-Fakesigned IOSs/MIOS"),
        ("nus", "fakesigned", "Fakesigned IOSs"),
        ("nus", "content", "Content Files"),
        ("nus", "channels", "Channels"),
        ("nus", "other", "Other WADs"),
        ("wiiHaxx", "exploits", "Exploits"),
        ("wiiHaxx", "wiiHomebrew", "Wii-Only Homebrew"),
        ("wiiHaxx", "bothHomebrew", "(v)Wii Homebrew"),
        ("wiiHaxx", "hbc", "Homebrew Channels"),
        ("wiiHaxx", "vWiiHomebrew", "vWii Only Homebrew"),
        ("cios", "hermes", "Hermes cIOSs"),
        ("cios", "cmios", "cMIOSs"),
        ("misc", "pc", "PC Programs"),
        ("misc", "wiiuHomebrew", "Wii U Homebrew"),
    ];

    private readonly Dictionary<string, DownloadListSection> _sections = new(StringComparer.Ordinal);
    private readonly DownloaderConfig _config;

    private readonly FillTabControl _tabs = new();
    private readonly ComboBox _channelEffect = new();
    private readonly ThemeGrid _themeGrid;
    private readonly D2xCheckGrid _d2x;
    private readonly WaninCheckGrid _wanin = new();
    private readonly ToolStripStatusLabel _statusLabel = new();

    private readonly string? _d2xRev;
    private StatusStrip? _status;
    private Control? _bottomBar;
    private bool _enterD2xSettings;
    private bool _restoring;

    public MainForm(DownloaderConfig config) {
        _config = config;
        _themeGrid = new ThemeGrid(config);
        _d2x = new D2xCheckGrid(config);

        string? queue = QueueVars.Read(config.Paths.TempCheck);
        if (queue is not null) {
            Dictionary<string, string> vars = QueueVars.Parse(queue);
            _d2xRev = vars.TryGetValue("d2x-beta-rev", out string? rev) && rev != "" ? rev : UnknownD2xRev;
        }

        Text = "ModMii";
        Icon = Icons.App;
        if (SystemFonts.MessageBoxFont is Font systemFont) Font = systemFont;
        StartPosition = FormStartPosition.CenterScreen;
        ClientSize = new Size(957, 650);
        MinimumSize = new Size(957 + (Width - ClientSize.Width), 650 + (Height - ClientSize.Height));

        BuildUi();
        LoadContent();

        if (queue is not null) RestoreQueue(queue);

        WireStatusUpdates();
        UpdateStatus();
    }

    public DownloaderConfig Config => _config;

    public string? D2xRev => _d2xRev;

    public IReadOnlyDictionary<string, DownloadListSection> SectionsByCategory => _sections;

    public IEnumerable<Control> CheckBoxRoots => [_d2x, _wanin, _themeGrid];

    // ---------------------------------------------------------------- layout

    private void BuildUi() {
        _tabs.Dock = DockStyle.Fill;
        _tabs.ImageList = new ImageList { ImageSize = new Size(Icons.Scale(24), Icons.Scale(24)), ColorDepth = ColorDepth.Depth32Bit };
        for (int i = 1; i <= 5; i++) _tabs.ImageList.Images.Add(i.ToString(), Icons.Get(i.ToString(), 24));

        _tabs.TabPages.Add(BuildNusTab());
        _tabs.TabPages.Add(BuildHomebrewTab());
        _tabs.TabPages.Add(BuildThemesTab());
        _tabs.TabPages.Add(BuildCiosTab());
        _tabs.TabPages.Add(BuildMiscTab());

        for (int i = 0; i < _tabs.TabPages.Count; i++) _tabs.TabPages[i].ImageKey = (i + 1).ToString();

        _status = new StatusStrip { SizingGrip = false };
        _statusLabel.Spring = true;
        _statusLabel.TextAlign = ContentAlignment.MiddleLeft;
        _status.Items.Add(_statusLabel);
        _status.Click += (_, _) => ShowSearch();
        _statusLabel.Click += (_, _) => ShowSearch();

        _bottomBar = BuildBottomBar();

        Controls.Add(_tabs);
        Controls.Add(_bottomBar);
        Controls.Add(_status);
    }

    private TabPage BuildNusTab() {
        TabPage page = NewPage("NUS");
        TableLayoutPanel table = NewTable(3, 2);

        for (int i = 0; i < 6; i++)
            table.Controls.Add(NewSection(Sections[i]), i % 3, i / 3);

        page.Controls.Add(table);
        return page;
    }

    private TabPage BuildHomebrewTab() {
        TabPage page = NewPage("(v)Wii Apps");
        TableLayoutPanel table = NewTable(3, 2);

        table.Controls.Add(NewSection(Sections[6]), 0, 0);  // exploits
        table.Controls.Add(NewSection(Sections[7]), 1, 0);  // wiiHomebrew

        DownloadListSection both = NewSection(Sections[8]);                 // (v)Wii homebrew
        table.Controls.Add(both, 2, 0);
        table.SetRowSpan(both, 2);

        table.Controls.Add(NewSection(Sections[9]), 0, 1);  // hbc
        table.Controls.Add(NewSection(Sections[10]), 1, 1); // vWiiHomebrew

        page.Controls.Add(table);
        return page;
    }

    private TabPage BuildThemesTab() {
        TabPage page = NewPage("System Menu Themes");

        var layout = new TableLayoutPanel { Dock = DockStyle.Fill, ColumnCount = 1, RowCount = 2 };
        layout.RowStyles.Add(new RowStyle(SizeType.Percent, 100));
        layout.RowStyles.Add(new RowStyle(SizeType.AutoSize));

        _themeGrid.Dock = DockStyle.Fill;
        _themeGrid.Margin = Padding.Empty;
        layout.Controls.Add(_themeGrid, 0, 0);

        var bar = new TableLayoutPanel {
            Dock = DockStyle.Fill,
            ColumnCount = 4,
            RowCount = 1,
            AutoSize = true,
            AutoSizeMode = AutoSizeMode.GrowAndShrink,
            Margin = new Padding(0, 4, 0, 0),
        };
        bar.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 50));
        bar.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 50));
        bar.ColumnStyles.Add(new ColumnStyle(SizeType.AutoSize));
        bar.ColumnStyles.Add(new ColumnStyle(SizeType.AutoSize));

        bar.Controls.Add(NewWarning(
            "ONLY INSTALL THEMES FOR _YOUR SPECIFIC SYSTEM MENU VERSION AND REGION!_", italic: true), 0, 0);
        bar.Controls.Add(NewWarning(
            "DON'T INSTALL THEMES WITHOUT PROTECTION: _BOOTMII, PRIILOADER AND NAND BACKUP_", italic: true), 1, 0);

        bar.Controls.Add(new Label {
            Text = "Channel Effect:",
            AutoSize = true,
            Anchor = AnchorStyles.Right,
            Margin = new Padding(8, 6, 4, 6),
        }, 2, 0);

        _channelEffect.DropDownStyle = ComboBoxStyle.DropDownList;
        _channelEffect.Items.AddRange(["No-Spin", "Spin", "Fast-Spin"]);
        _channelEffect.SelectedIndex = 0;
        _channelEffect.Anchor = AnchorStyles.Right;
        _channelEffect.Margin = new Padding(0, 4, 0, 4);
        bar.Controls.Add(_channelEffect, 3, 0);

        layout.Controls.Add(bar, 0, 1);
        page.Controls.Add(layout);
        return page;
    }

    private TabPage BuildCiosTab() {
        TabPage page = NewPage("cIOSs && cMIOSs");

        var layout = new TableLayoutPanel { Dock = DockStyle.Fill, ColumnCount = 1, RowCount = 3 };
        layout.RowStyles.Add(new RowStyle(SizeType.Percent, 100));
        layout.RowStyles.Add(new RowStyle(SizeType.AutoSize));
        layout.RowStyles.Add(new RowStyle(SizeType.AutoSize));

        TableLayoutPanel grids = NewTable(3, 2);
        grids.ColumnStyles.Clear();
        grids.ColumnStyles.Add(new ColumnStyle(SizeType.AutoSize));
        grids.ColumnStyles.Add(new ColumnStyle(SizeType.AutoSize));
        grids.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 100));

        _d2x.Dock = DockStyle.Fill;
        _wanin.Dock = DockStyle.Fill;
        grids.Controls.Add(_d2x, 0, 0);
        grids.SetRowSpan(_d2x, 2);
        grids.Controls.Add(_wanin, 1, 0);
        grids.SetRowSpan(_wanin, 2);
        grids.Controls.Add(NewSection(Sections[11]), 2, 0); // hermes
        grids.Controls.Add(NewSection(Sections[12]), 2, 1); // cmios

        layout.Controls.Add(grids, 0, 0);

        var buttons = new TableLayoutPanel {
            Dock = DockStyle.Fill,
            ColumnCount = 5,
            RowCount = 1,
            AutoSize = true,
            AutoSizeMode = AutoSizeMode.GrowAndShrink,
            Margin = new Padding(0, 4, 0, 0),
        };
        buttons.ColumnStyles.Add(new ColumnStyle(SizeType.AutoSize));
        buttons.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 60));
        buttons.ColumnStyles.Add(new ColumnStyle(SizeType.AutoSize));
        buttons.ColumnStyles.Add(new ColumnStyle(SizeType.AutoSize));
        buttons.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 40));

        Button d2xSettings = NewIconButton("d2x Version\nSettings", null);
        d2xSettings.Click += (_, _) => OpenD2xSettings();
        buttons.Controls.Add(d2xSettings, 0, 0);

        buttons.Controls.Add(NewInfo(
            "Note: The number in brackets indicates the base IOS; e.g., cIOS249 [56] = cIOS in slot 249 based on IOS56"),
            1, 0);

        Button wiiRecommended = NewIconButton("Select Recommended\n(Wii)", "recommended");
        wiiRecommended.Click += (_, _) => _d2x.SelectWiiRecommended();
        buttons.Controls.Add(wiiRecommended, 2, 0);

        Button vWiiRecommended = NewIconButton("Select Recommended\n(vWii)", "recommended");
        vWiiRecommended.Click += (_, _) => _d2x.SelectVWiiRecommended();
        buttons.Controls.Add(vWiiRecommended, 3, 0);

        buttons.Controls.Add(NewInfo(
            "Unrecommended cIOSs are intended for compatibility testing or unique situations"), 4, 0);

        layout.Controls.Add(buttons, 0, 1);

        layout.Controls.Add(NewInfo(
            "Note: Only one cIOS can be installed to a slot (e.g. 249); To change a cIOS's slot either use " +
            "ModMii's Advanced Downloads Menu or open downloaded WADs using ModMii or ShowMiiWads to edit them"),
            0, 2);

        page.Controls.Add(layout);
        return page;
    }

    private TabPage BuildMiscTab() {
        TabPage page = NewPage("Wii U && PC Apps");
        TableLayoutPanel table = NewTable(2, 1);

        table.Controls.Add(NewSection(Sections[14]), 0, 0); // wiiuHomebrew
        table.Controls.Add(NewSection(Sections[13]), 1, 0); // pc

        page.Controls.Add(table);
        return page;
    }

    private TableLayoutPanel BuildBottomBar() {
        var bar = new TableLayoutPanel {
            Dock = DockStyle.Bottom,
            ColumnCount = 4,
            RowCount = 1,
            AutoSize = true,
            AutoSizeMode = AutoSizeMode.GrowAndShrink,
            Padding = new Padding(6, 4, 6, 4),
        };
        bar.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 100));
        bar.ColumnStyles.Add(new ColumnStyle(SizeType.AutoSize));
        bar.ColumnStyles.Add(new ColumnStyle(SizeType.AutoSize));
        bar.ColumnStyles.Add(new ColumnStyle(SizeType.AutoSize));

        MarkdownLabel warning = NewWarning(
            "Some of these files *_MAY CAUSE BRICK_* if you do not know what you are doing!", italic: false);
        warning.TextAlign = ContentAlignment.TopCenter;
        bar.Controls.Add(warning, 0, 0);

        bar.Controls.Add(BuildLegend(), 1, 0);

        Button search = NewIconButton("Search", "search");
        search.Click += (_, _) => ShowSearch();
        bar.Controls.Add(search, 2, 0);

        Button download = NewIconButton("Download", "download");
        download.Click += (_, _) => Close();
        bar.Controls.Add(download, 3, 0);

        AcceptButton = download;
        return bar;
    }

    private static TableLayoutPanel BuildLegend() {
        (string Icon, string Text)[] entries =
        [
            ("recommended", "Recommended"),
            ("update", "Auto-Updating"),
            ("semiRecommended", "Semi-Recommended"),
            ("semiAutoUpdate", "Updated when XFlak Remembers"),
        ];

        var legend = new TableLayoutPanel {
            ColumnCount = 4,
            RowCount = 2,
            AutoSize = true,
            AutoSizeMode = AutoSizeMode.GrowAndShrink,
            Margin = new Padding(8, 0, 8, 0),
        };

        for (int i = 0; i < entries.Length; i++) {
            (string? icon, string? text) = entries[i];
            int column = i % 2 == 0 ? 0 : 2;
            int row = i / 2;

            legend.Controls.Add(new PictureBox {
                Image = Icons.Get(icon, 24),
                SizeMode = PictureBoxSizeMode.AutoSize,
                Margin = new Padding(2, 1, 2, 1),
                Anchor = AnchorStyles.Left,
            }, column, row);

            legend.Controls.Add(new Label {
                Text = text,
                AutoSize = true,
                Anchor = AnchorStyles.Left,
                Margin = new Padding(2, 5, 8, 2),
            }, column + 1, row);
        }

        return legend;
    }

    // ------------------------------------------------------------- utilities

    private static TabPage NewPage(string title) {
        return new(title) {
            Padding = new Padding(6),
            UseVisualStyleBackColor = true,
        };
    }

    private static TableLayoutPanel NewTable(int columns, int rows) {
        var table = new TableLayoutPanel {
            Dock = DockStyle.Fill,
            ColumnCount = columns,
            RowCount = rows,
            Margin = Padding.Empty,
        };

        for (int i = 0; i < columns; i++) table.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 100f / columns));
        for (int i = 0; i < rows; i++) table.RowStyles.Add(new RowStyle(SizeType.Percent, 100f / rows));

        return table;
    }

    private DownloadListSection NewSection((string Page, string Category, string Title) definition) {
        var section = new DownloadListSection {
            Name = definition.Category,
            Title = definition.Title,
            Dock = DockStyle.Fill,
            Margin = new Padding(3),
        };

        _sections[definition.Category] = section;
        return section;
    }

    private static MarkdownLabel NewWarning(string markdown, bool italic) {
        var label = new MarkdownLabel {
            Dock = DockStyle.Fill,
            AutoSize = false,
            Margin = new Padding(4, 2, 4, 2),
            MinimumSize = new Size(0, 34),
            Font = UiFont(italic ? FontStyle.Bold | FontStyle.Italic : FontStyle.Bold),
            Markdown = markdown
        };
        return label;
    }

    private static Font UiFont(FontStyle style) {
        return new Font(SystemFonts.MessageBoxFont ?? DefaultFont, style);
    }

    private static Label NewInfo(string text) {
        return new() {
            Text = text,
            Dock = DockStyle.Fill,
            TextAlign = ContentAlignment.MiddleCenter,
            Font = UiFont(FontStyle.Bold),
            Margin = new Padding(6, 2, 6, 2),
            AutoSize = false,
            MinimumSize = new Size(0, 34),
        };
    }

    private static Button NewIconButton(string text, string? iconKey) {
        return new() {
            Text = text,
            AutoSize = true,
            AutoSizeMode = AutoSizeMode.GrowAndShrink,
            Image = iconKey is null ? null : Icons.Get(iconKey, 24),
            ImageAlign = ContentAlignment.MiddleLeft,
            TextImageRelation = TextImageRelation.ImageBeforeText,
            Padding = new Padding(6, 4, 6, 4),
            Margin = new Padding(3),
            Anchor = AnchorStyles.None,
        };
    }

    // --------------------------------------------------------------- content

    private void LoadContent() {
        foreach ((string? page, string? category, string _) in Sections)
            _sections[category].Load(_config, page, category);

        _d2x.Setup(CiosMapSet.Load(_config.Paths, _d2xRev));

        foreach (DownloadListSection section in _sections.Values) _ = section.List.Handle;
    }

    private void WireStatusUpdates() {
        foreach (DownloadListSection section in _sections.Values)
            section.List.ItemSelectionChanged += (_, _) => UpdateStatus();

        foreach (Control root in CheckBoxRoots) {
            foreach (CheckBox box in CheckBoxTools.All(root))
                box.CheckedChanged += (_, _) => UpdateStatus();
        }
    }

    // ----------------------------------------------------------------- queue

    public string MakeQueue() {
        var builder = new StringBuilder();

        foreach (DownloadListSection section in _sections.Values) builder.Append(section.GetSelected());
        builder.Append(_wanin.GetSelected());
        builder.Append(_d2x.GetSelected());
        builder.Append(_themeGrid.GetSelected());
        builder.Append(QueueVars.Line("effect", _channelEffect.SelectedItem?.ToString() ?? ""));
        builder.Append(QueueVars.Line("nextpage", (_tabs.SelectedIndex + 1).ToString()));

        return builder.ToString();
    }

    private void RestoreQueue(string queue) {
        _restoring = true;
        try {
            Dictionary<string, string> vars = QueueVars.Parse(queue);

            if (vars.TryGetValue("effect", out string? effect) && effect != "") {
                int index = _channelEffect.Items.IndexOf(effect);
                if (index >= 0) _channelEffect.SelectedIndex = index;
            }

            if (vars.TryGetValue("nextpage", out string? nextPage) &&
                int.TryParse(nextPage, out int page) &&
                page >= 1 && page <= _tabs.TabPages.Count) {
                _tabs.SelectedIndex = page - 1;
            }

            IEnumerable<string> queued = vars
                .Where(pair => pair.Value == "*" || pair.Key is "No-Spin" or "Spin" or "Fast-Spin")
                .Select(pair => pair.Key);

            foreach (string? key in queued) {
                foreach (DownloadListSection section in _sections.Values) section.SelectChild(key);
                _wanin.SelectChild(key);
                _d2x.SelectChild(key);
                _themeGrid.SelectChild(key);
            }
        } finally {
            _restoring = false;
        }
    }

    private void SaveQueue() {
        string queue = MakeQueue();
        if (_enterD2xSettings) queue += QueueVars.Line("nextgoto", "betaswitch");

        if (!QueueVars.Write(_config.Paths.TempCheck, queue))
            Log.Write("Could not write the queue to any of the configured locations.");
    }

    private void OpenD2xSettings() {
        _enterD2xSettings = true;
        Close();
    }

    protected override void OnFormClosing(FormClosingEventArgs e) {
        SaveQueue();
        base.OnFormClosing(e);
    }

    // ---------------------------------------------------------------- status

    public void UpdateStatus() {
        if (_restoring) return;

        int count = CountQueued();
        string text = count switch {
            0 => "No items",
            1 => "1 item",
            _ => $"{count} items",
        };

        _statusLabel.Text = $"{text} in queue";
    }

    private int CountQueued() {
        int count = _sections.Values.Sum(section => section.List.SelectedItems.Count);

        foreach (Control root in CheckBoxRoots)
            count += CheckBoxTools.All(root).Count(box => box.Enabled && box.Checked);

        return count;
    }

    private void ShowSearch() {
        using var dialog = new SearchForm(this);
        dialog.ShowDialog(this);
        UpdateStatus();
    }
}
