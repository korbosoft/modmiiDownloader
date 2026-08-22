namespace ModMiiDownloader.Controls;

using System.ComponentModel;
using System.Text;

public class MarkdownLabel : Label {
    private List<Run> _runs = [];
    private string _markdown = "";

    public MarkdownLabel() {
        SetStyle(ControlStyles.OptimizedDoubleBuffer | ControlStyles.AllPaintingInWmPaint |
                 ControlStyles.UserPaint | ControlStyles.ResizeRedraw, true);
        AutoSize = false;
        TextAlign = ContentAlignment.MiddleCenter;
    }

    [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
    public string Markdown {
        get => _markdown;
        set {
            _markdown = value;
            _runs = Parse(value);
            Text = string.Concat(_runs.Select(run => run.Text));
            Invalidate();
        }
    }

    protected override void OnPaint(PaintEventArgs e) {
        if (_runs.Count == 0) {
            base.OnPaint(e);
            return;
        }

        Color color = Enabled ? ForeColor : SystemColors.GrayText;
        List<Line> lines = Wrap(e.Graphics, ClientSize.Width);
        int totalHeight = lines.Sum(line => line.Height);

        int y = TextAlign switch {
            ContentAlignment.TopCenter or ContentAlignment.TopLeft or ContentAlignment.TopRight => 0,
            ContentAlignment.BottomCenter or ContentAlignment.BottomLeft or ContentAlignment.BottomRight =>
                ClientSize.Height - totalHeight,
            _ => (ClientSize.Height - totalHeight) / 2,
        };

        foreach (Line line in lines) {
            int x = (ClientSize.Width - line.Width) / 2;
            foreach ((Run? run, Font? font) in line.Runs) {
                TextRenderer.DrawText(e.Graphics, run.Text, font, new Point(x, y), color, TextFormatFlags.NoPadding);
                x += MeasureWidth(e.Graphics, run.Text, font);
            }

            y += line.Height;
        }
    }

    private List<Line> Wrap(Graphics graphics, int maxWidth) {
        var lines = new List<Line>();
        var current = new Line();

        foreach (Run run in _runs) {
            Font font = FontFor(run);

            foreach (string word in SplitKeepingSpaces(run.Text)) {
                if (word == "\n") {
                    lines.Add(current);
                    current = new Line();
                    continue;
                }

                int width = MeasureWidth(graphics, word, font);
                if (current.Width + width > maxWidth && current.Runs.Count > 0) {
                    lines.Add(current);
                    current = new Line();
                    if (word.Trim().Length == 0) continue;
                }

                current.Append(
                    new Run(word, run.Bold, run.Italic),
                    font,
                    width,
                    TextRenderer.MeasureText(graphics, "Wg", font).Height);
            }
        }

        if (current.Runs.Count > 0) lines.Add(current);
        return lines;
    }

    private static int MeasureWidth(Graphics graphics, string text, Font font) {
        const string sentinel = ".";

        int withSentinel = TextRenderer
            .MeasureText(graphics, text + sentinel, font, Size.Empty, TextFormatFlags.NoPadding).Width;
        int sentinelOnly = TextRenderer
            .MeasureText(graphics, sentinel, font, Size.Empty, TextFormatFlags.NoPadding).Width;

        return Math.Max(0, withSentinel - sentinelOnly);
    }

    private Font FontFor(Run run) {
        FontStyle style = Font.Style;
        if (run.Bold) style |= FontStyle.Bold;
        if (run.Italic) style |= FontStyle.Italic;
        return style == Font.Style ? Font : new Font(Font, style);
    }

    private static IEnumerable<string> SplitKeepingSpaces(string text) {
        var word = new StringBuilder();
        foreach (char c in text) {
            if (c == '\n') {
                if (word.Length > 0) {
                    yield return word.ToString();
                    word.Clear();
                }

                yield return "\n";
            } else if (c == ' ') {
                word.Append(c);
                yield return word.ToString();
                word.Clear();
            } else {
                word.Append(c);
            }
        }

        if (word.Length > 0) yield return word.ToString();
    }

    private static List<Run> Parse(string markdown) {
        var runs = new List<Run>();
        var text = new StringBuilder();
        bool bold = false;
        bool italic = false;

        void Flush() {
            if (text.Length == 0) return;
            runs.Add(new Run(text.ToString(), bold, italic));
            text.Clear();
        }

        for (int i = 0; i < markdown.Length; i++) {
            char c = markdown[i];
            if (c is '*' or '_') {
                Flush();

                if (i + 1 < markdown.Length && markdown[i + 1] == c) {
                    bold = !bold;
                    i++;
                } else if (c == '*') {
                    bold = !bold;
                } else {
                    italic = !italic;
                }

                continue;
            }

            text.Append(c);
        }

        Flush();
        return runs;
    }

    private sealed record Run(string Text, bool Bold, bool Italic);

    private sealed class Line {
        public List<(Run Run, Font Font)> Runs { get; } = [];
        public int Width { get; private set; }
        public int Height { get; private set; }

        public void Append(Run run, Font font, int width, int height) {
            Runs.Add((run, font));
            Width += width;
            Height = Math.Max(Height, height);
        }
    }
}
