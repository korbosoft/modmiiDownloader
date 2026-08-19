namespace ModMiiDownloader.Controls;

/// <summary>Waninkoko cIOSs: a fixed list of revision/base pairs, each installable to 249 or 250.</summary>
public class WaninCheckGrid : SectionBox {
    // Label, then the variable suffix each slot's checkbox uses.
    private static readonly (string Label, string Suffix)[] Rows =
    [
        ("Wanin-v21 [37]", "37_v21"),
        ("Wanin-v21 [38]", "38_v21"),
        ("Wanin-v21 [53]", "53_v21"),
        ("Wanin-v21 [55]", "55_v21"),
        ("Wanin-v21 [56]", "56_v21"),
        ("Wanin-v21 [57]", "57_v21"),
        ("Wanin-v21 [58]", "58_v21"),
        ("Wanin-v20 [38]", "38_v20"),
        ("Wanin-v20 [56]", "56_v20"),
        ("Wanin-v20 [57]", "57_v20"),
        ("Wanin-v19 [37]", "37_v19"),
        ("Wanin-v19 [38]", "38_v19"),
        ("Wanin-v19 [57]", "57_v19"),
        ("Wanin-v17b [38]", "v17b"),
        ("Wanin-v14 [38]", "v14"),
    ];

    private readonly TableLayoutPanel _table;
    private readonly Button _toggle;

    public WaninCheckGrid() {
        AutoSize = true;
        AutoSizeMode = AutoSizeMode.GrowAndShrink;
        Title = "Waninkoko cIOSs";

        _table = GridFactory.Table(3, Rows.Length);

        for (int row = 0; row < Rows.Length; row++) {
            (string? label, string? suffix) = Rows[row];
            _table.Controls.Add(GridFactory.RowLabel($"w{suffix}", label), 0, row);
            _table.Controls.Add(GridFactory.Box($"c249_{suffix}", "249"), 1, row);
            _table.Controls.Add(GridFactory.Box($"c250_{suffix}", "250"), 2, row);
        }

        _table.ColumnStyles.Clear();
        for (int i = 0; i < 3; i++) _table.ColumnStyles.Add(new ColumnStyle(SizeType.AutoSize));

        _table.RowStyles.Clear();
        for (int i = 0; i < Rows.Length; i++) _table.RowStyles.Add(new RowStyle(SizeType.AutoSize));

        _toggle = GridFactory.Toggle();
        _toggle.Dock = DockStyle.Bottom;
        _toggle.Click += (_, _) => CheckBoxTools.Toggle(CheckBoxTools.All(this).ToList());

        Controls.Add(GridFactory.ScrollHost(_table));
        Controls.Add(_toggle);
    }

    /// <summary>
    /// The rows live in a scrolling host, which does not report their size, so the box would
    /// collapse in its autosized column. Measure the grid itself instead.
    /// </summary>
    public override Size GetPreferredSize(Size proposedSize) {
        if (_table is null) return base.GetPreferredSize(proposedSize);

        Size grid = _table.PreferredSize;
        return new Size(
            grid.Width + Padding.Horizontal + 6,
            grid.Height + Padding.Vertical + _toggle.Height + 8);
    }

    public string GetSelected() {
        return CheckBoxTools.GetSelected(this);
    }

    public void SelectChild(string name) {
        CheckBoxTools.SelectChild(this, name);
    }
}
