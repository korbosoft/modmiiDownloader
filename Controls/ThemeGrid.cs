using ModMiiDownloader.Model;

namespace ModMiiDownloader.Controls;

public class ThemeGrid : Panel {
    private const string ThemesUrl = "https://modmii.github.io/WiiThemes.html";

    private const string StockTheme = "Original";

    private static readonly (string Caption, string Key, bool HasWads)[] Rows =
    [
        ("4.3U", "43U", true),
        ("4.2U", "42U", true),
        ("4.1U", "41U", true),
        ("4.3E", "43E", true),
        ("4.2E", "42E", true),
        ("4.1E", "41E", true),
        ("4.3J", "43J", true),
        ("4.2J", "42J", true),
        ("4.1J", "41J", true),
        ("4.3K", "43K", true),
        ("4.2K", "42K", true),
        ("4.1K", "41K", true),
        ("vWii U", "vU", false),
        ("vWii E", "vE", false),
        ("vWii J", "vJ", false),
    ];

    private readonly List<Column> _columns = [];

    public ThemeGrid(DownloaderConfig config) {
        BuildColumns(config.Themes);

        var table = new TableLayoutPanel {
            Dock = DockStyle.Fill,
            ColumnCount = _columns.Count + 1,
            RowCount = Rows.Length + 1,
            Margin = Padding.Empty,
        };

        Button youtube = HeaderButton("Youtube\nPreview");
        youtube.Name = "youtube";
        youtube.Click += (_, _) => DownloadListSection.OpenUrl(ThemesUrl);
        table.Controls.Add(youtube, 0, 0);

        for (int column = 0; column < _columns.Count; column++) {
            string pattern = _columns[column].TogglePattern;
            Button button = HeaderButton(_columns[column].Caption);
            button.Click += (_, _) => CheckBoxTools.ToggleMatching(this, pattern);
            table.Controls.Add(button, column + 1, 0);
        }

        for (int row = 0; row < Rows.Length; row++) {
            (string? caption, string? key, bool hasWads) = Rows[row];

            Button rowButton = RowButton(caption);
            rowButton.Name = $"s{key}";
            rowButton.Click += (_, _) => CheckBoxTools.ToggleMatching(this, key);
            table.Controls.Add(rowButton, 0, row + 1);

            for (int column = 0; column < _columns.Count; column++) {
                if (_columns[column].IsWad && !hasWads) continue;

                table.Controls.Add(ThemeBox(_columns[column].VariableFor(key)), column + 1, row + 1);
            }
        }

        table.ColumnStyles.Clear();
        table.ColumnStyles.Add(new ColumnStyle(SizeType.AutoSize));
        for (int i = 0; i < _columns.Count; i++)
            table.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 100f / _columns.Count));

        table.RowStyles.Clear();

        // The header captions are two lines ("Original" / "APP"), so that row gets a double
        // share — a taller UI font clipped the second line at an equal one. Every row stays
        // percent-based so the grid still fills its box; an autosized row leaves a gap.
        const int headerShare = 2;
        float unit = 100f / (Rows.Length + headerShare);

        table.RowStyles.Add(new RowStyle(SizeType.Percent, unit * headerShare));
        for (int i = 0; i < Rows.Length; i++)
            table.RowStyles.Add(new RowStyle(SizeType.Percent, unit));

        Controls.Add(table);
    }

    public string GetSelected() {
        return CheckBoxTools.GetSelected(this);
    }

    public void SelectChild(string name) {
        CheckBoxTools.SelectChild(this, name);
    }

    private void BuildColumns(IEnumerable<string> themes) {
        IList<string> list = themes as IList<string> ?? [.. themes];

        foreach (string theme in list)
            _columns.Add(new Column(theme, IsWad: false));

        foreach (string? theme in list.Where(theme => theme != StockTheme))
            _columns.Add(new Column(theme, IsWad: true));
    }

    private sealed record Column(string Theme, bool IsWad) {
        public string Caption {
            get {
                string name = Theme == StockTheme ? Theme : Theme.Split('_').Last();
                return $"{name}\n{(IsWad ? "WAD" : Theme == StockTheme ? "APP" : "CSM")}";
            }
        }

        private string Prefix => Theme == StockTheme ? "O_" : $"{Theme}_";

        public string VariableFor(string row) {
            return IsWad ? $"{Prefix}{row}_W" : $"{Prefix}{row}";
        }

        public string TogglePattern => IsWad
            ? $@"{Prefix}\d\d._W"
            : Theme == StockTheme
                ? "O_"
                : $@"{Prefix}...?$";
    }

    /// <summary>Column caption. Autosized, because its two lines size the header row.</summary>
    private static Button HeaderButton(string caption) {
        return new() {
            Text = caption,
            Dock = DockStyle.Fill,
            FlatStyle = FlatStyle.System,
            Margin = new Padding(1),
            TextAlign = ContentAlignment.MiddleCenter,
            AutoSize = true,
            AutoSizeMode = AutoSizeMode.GrowAndShrink,
        };
    }

    /// <summary>Row label. Fills its share of the grid rather than shrinking to the text.</summary>
    private static Button RowButton(string caption) {
        return new() {
            Text = caption,
            Dock = DockStyle.Fill,
            FlatStyle = FlatStyle.System,
            Margin = new Padding(1),
            TextAlign = ContentAlignment.MiddleCenter,
        };
    }

    private static CheckBox ThemeBox(string name) {
        return new() {
            Name = name,
            Text = "",
            AutoSize = false,
            Dock = DockStyle.Fill,
            CheckAlign = ContentAlignment.MiddleCenter,
            Margin = new Padding(1),
            UseVisualStyleBackColor = true,
        };
    }
}
