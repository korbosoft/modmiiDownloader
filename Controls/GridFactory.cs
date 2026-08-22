using ModMiiDownloader.Resources;

namespace ModMiiDownloader.Controls;

internal static class GridFactory {
    public static TableLayoutPanel Table(int columns, int rows) {
        return new() {
            Dock = DockStyle.Top,
            ColumnCount = columns,
            RowCount = rows,
            Margin = Padding.Empty,
            Padding = Padding.Empty,
            AutoSize = true,
            AutoSizeMode = AutoSizeMode.GrowAndShrink,
        };
    }

    public static Panel ScrollHost(Control content) {
        return new() {
            Dock = DockStyle.Fill,
            AutoScroll = true,
            Margin = Padding.Empty,
            Padding = Padding.Empty,
            Controls = { content },
        };
    }

    public static CheckBox Box(string name, string text, string iconKey = Icons.Blank, bool enabled = true) {
        var box = new CheckBox {
            Name = name,
            Text = text,
            AutoSize = true,
            Enabled = enabled,
            FlatStyle = FlatStyle.Standard,
            ImageAlign = ContentAlignment.MiddleLeft,
            TextImageRelation = TextImageRelation.ImageBeforeText,
            Anchor = AnchorStyles.Left,
            Margin = new Padding(2, 1, 2, 1),
            UseVisualStyleBackColor = true,
        };

        if (iconKey == Icons.Blank) return box;

        void FitIconToFont() {
            int size = Math.Max(8, box.Font.Height - 4);
            box.Image = Icons.GetExact(iconKey, size);
            box.MinimumSize = new Size(0, size + 4);
        }

        FitIconToFont();
        box.FontChanged += (_, _) => FitIconToFont();

        return box;
    }

    public static Label RowLabel(string name, string text, bool enabled = true) {
        return new() {
            Name = name,
            Text = text,
            AutoSize = true,
            Enabled = enabled,
            Anchor = AnchorStyles.Left,
            Margin = new Padding(2, 4, 6, 4),
        };
    }

    public static Button Toggle(string text = "Toggle All", bool enabled = true) {
        return new() {
            Text = text,
            Enabled = enabled,
            Height = 30,
            Dock = DockStyle.Fill,
            FlatStyle = FlatStyle.System,
            Margin = new Padding(2, 4, 2, 2),
        };
    }
}
