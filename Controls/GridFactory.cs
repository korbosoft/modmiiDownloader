using ModMiiDownloader.Resources;

namespace ModMiiDownloader.Controls;

/// <summary>Shared look for the cIOS and theme checkbox grids.</summary>
internal static class GridFactory {
    /// <summary>
    /// Grid tables dock to the top and keep their preferred height. Filling instead would let
    /// a short container compress the rows, which clips the icons in them.
    /// </summary>
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

    /// <summary>Scrolling host for a grid, so an undersized box scrolls rather than squashing.</summary>
    public static Panel ScrollHost(Control content) {
        return new() {
            Dock = DockStyle.Fill,
            AutoScroll = true,
            Margin = Padding.Empty,
            Padding = Padding.Empty,
            Controls = { content },
        };
    }

    /// <summary>
    /// A grid checkbox. Its name is the ModMii variable, so it doubles as the queue key.
    /// FlatStyle.Standard is needed because the system-drawn checkbox ignores Image, and the
    /// icon is sized off the font so it reads as a heart rather than a blob beside the label.
    /// </summary>
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

        // The icon is sized off the font, so it tracks the text at any DPI. Autosizing measures
        // the text alone, hence the minimum height that keeps the icon from being clipped.
        void FitIconToFont() {
            // Slightly under the text height so the icon reads as a mark beside the label
            // rather than competing with it.
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
