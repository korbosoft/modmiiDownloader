using ModMiiDownloader.Model;
using ModMiiDownloader.Resources;

namespace ModMiiDownloader.Controls;

/// <summary>
/// The d2x slot/base grid, split into Wii and vWii tabs. Which bases exist depends on the
/// ciosmaps.xml that ships with the installed d2x revision, so most of it starts disabled.
/// </summary>
public class D2xCheckGrid : SectionBox {
    // Wii: base IOS -> the slots d2x can install it to, in the column order the Qt grid used.
    private static readonly (int Base, int[] Slots)[] WiiRows =
    [
        (37, [249, 250]),
        (38, [249, 250, 248]),
        (53, [249, 250]),
        (55, [249, 250]),
        (56, [249, 250]),
        (57, [249, 250]),
        (58, [249, 250, 251]),
        (60, [249, 250]),
        (70, [249, 250]),
        (80, [249, 250]),
    ];

    // vWii only ever gets one slot per base.
    private static readonly (int Base, int Slot)[] VWiiRows =
    [
        (38, 248),
        (56, 249),
        (57, 250),
        (58, 251),
    ];

    private readonly TabControl _tabs;
    private readonly Button _wiiToggle;
    private readonly Button _vWiiToggle;
    private readonly DownloaderConfig _config;

    private readonly Control _wiiGrid;
    private readonly Control _vWiiGrid;

    public D2xCheckGrid(DownloaderConfig config) {
        _config = config;
        AutoSize = true;
        AutoSizeMode = AutoSizeMode.GrowAndShrink;
        Title = "d2x cIOSs";

        _wiiToggle = GridFactory.Toggle(enabled: false);
        _wiiToggle.Click += (_, _) => CheckBoxTools.ToggleMatching(this, @"c\d+_\d+_d2x$");

        _vWiiToggle = GridFactory.Toggle(enabled: false);
        _vWiiToggle.Click += (_, _) => CheckBoxTools.ToggleMatching(this, "_vWii$");

        _wiiGrid = BuildWiiGrid();
        _vWiiGrid = BuildVWiiGrid();

        _tabs = new TabControl { Dock = DockStyle.Fill, Margin = Padding.Empty };
        _tabs.TabPages.Add(BuildTab("Wii", _wiiGrid, _wiiToggle));
        _tabs.TabPages.Add(BuildTab("vWii", _vWiiGrid, _vWiiToggle));

        Controls.Add(_tabs);
    }

    /// <summary>
    /// A TabControl does not measure its pages, so the box would collapse to the default
    /// panel width and clip the widest row. Measure both grids and ask for the larger.
    /// </summary>
    public override Size GetPreferredSize(Size proposedSize) {
        Size wii = _wiiGrid.PreferredSize;
        Size vWii = _vWiiGrid.PreferredSize;

        // Allow for the tab strip, the toggle button and the page's own border.
        return new Size(
            Math.Max(wii.Width, vWii.Width) + Padding.Horizontal + 20,
            Math.Max(wii.Height, vWii.Height) + Padding.Vertical + _wiiToggle.Height + 46);
    }

    /// <summary>Applies the loaded cIOS maps: enables the bases d2x actually supports.</summary>
    public void Setup(CiosMapSet maps) {
        if (maps.Wii is not null) {
            Title = $"{maps.Wii.Name} cIOSs";
            _wiiToggle.Enabled = true;

            foreach ((int baseIos, int[] _) in WiiRows) {
                bool available = maps.Wii.HasBase(baseIos);
                SetBaseEnabled($"b{baseIos}", $"{baseIos}_d2x$", available);
            }
        }

        if (maps.VWii is null) return;

        _vWiiToggle.Enabled = true;
        foreach ((int baseIos, int _) in VWiiRows) {
            bool available = maps.VWii.HasBase(baseIos);
            SetBaseEnabled($"bv{baseIos}", $"{baseIos}_d2x_vWii$", available);
        }
    }

    public void SelectWiiRecommended() {
        CheckBoxTools.Check(_config.RecommendedWiiCios
            .Select(cios => CheckBoxTools.Find(this, $"c{cios.Slot}_{cios.Base}_d2x"))
            .OfType<CheckBox>()
            .ToList());
    }

    public void SelectVWiiRecommended() {
        CheckBoxTools.CheckMatching(this, "_vWii$");
    }

    public string GetSelected() {
        return CheckBoxTools.GetSelected(this);
    }

    public void SelectChild(string name) {
        CheckBoxTools.SelectChild(this, name);
    }

    private void SetBaseEnabled(string labelName, string boxPattern, bool enabled) {
        Control? label = Controls.Find(labelName, searchAllChildren: true).FirstOrDefault();
        if (label is not null) label.Enabled = enabled;

        foreach (CheckBox box in CheckBoxTools.Matching(this, boxPattern))
            box.Enabled = enabled;
    }

    private static TabPage BuildTab(string title, Control content, Button toggle) {
        var page = new TabPage(title) { Padding = new Padding(4), UseVisualStyleBackColor = true };
        toggle.Dock = DockStyle.Bottom;
        page.Controls.Add(GridFactory.ScrollHost(content));
        page.Controls.Add(toggle);
        return page;
    }

    private Control BuildWiiGrid() {
        TableLayoutPanel table = GridFactory.Table(4, WiiRows.Length);

        for (int row = 0; row < WiiRows.Length; row++) {
            (int baseIos, int[]? slots) = WiiRows[row];
            table.Controls.Add(GridFactory.RowLabel($"b{baseIos}", $"[{baseIos}]", enabled: false), 0, row);

            for (int i = 0; i < slots.Length; i++) {
                // Recommended slots are marked up front; setting the image later would leave
                // the autosized checkbox too narrow for it.
                string icon = _config.IsRecommendedWiiCios(slots[i], baseIos) ? "recommended" : Icons.Blank;
                CheckBox box = GridFactory.Box($"c{slots[i]}_{baseIos}_d2x", slots[i].ToString(), icon, enabled: false);
                table.Controls.Add(box, i + 1, row);

                // With only two slots the second one stretches over the spare column.
                if (slots.Length == 2 && i == 1) table.SetColumnSpan(box, 2);
            }
        }

        StyleRows(table, WiiRows.Length);
        return table;
    }

    private Control BuildVWiiGrid() {
        TableLayoutPanel table = GridFactory.Table(2, VWiiRows.Length);

        for (int row = 0; row < VWiiRows.Length; row++) {
            (int baseIos, int slot) = VWiiRows[row];
            table.Controls.Add(GridFactory.RowLabel($"bv{baseIos}", $"[{baseIos}]", enabled: false), 0, row);
            table.Controls.Add(
                GridFactory.Box($"c{slot}_{baseIos}_d2x_vWii", slot.ToString(), "recommended", enabled: false),
                1, row);
        }

        StyleRows(table, VWiiRows.Length);
        return table;
    }

    /// <summary>Every row hugs its contents so nothing gets squeezed.</summary>
    private static void StyleRows(TableLayoutPanel table, int contentRows) {
        table.ColumnStyles.Clear();
        for (int i = 0; i < table.ColumnCount; i++)
            table.ColumnStyles.Add(new ColumnStyle(SizeType.AutoSize));

        table.RowStyles.Clear();
        for (int i = 0; i < contentRows; i++)
            table.RowStyles.Add(new RowStyle(SizeType.AutoSize));
    }
}
