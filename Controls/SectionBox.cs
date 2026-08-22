using System.ComponentModel;

namespace ModMiiDownloader.Controls;
public class SectionBox : Panel {
    private const int TitleGap = 6;

    private string _title = "";

    public SectionBox() {
        SetStyle(ControlStyles.ResizeRedraw | ControlStyles.OptimizedDoubleBuffer |
                 ControlStyles.AllPaintingInWmPaint | ControlStyles.UserPaint, true);
        UpdatePadding();
    }

    [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
    public string Title {
        get => _title;
        set {
            if (_title == value) return;
            _title = value;
            UpdatePadding();
            Invalidate();
        }
    }

    protected override void OnFontChanged(EventArgs e) {
        base.OnFontChanged(e);
        UpdatePadding();
    }

    private void UpdatePadding() {
        int titleHeight = string.IsNullOrEmpty(_title) ? 4 : TextRenderer.MeasureText("Wg", Font).Height;
        Padding = new Padding(5, titleHeight + 5, 5, 5);
    }

    protected override void OnPaint(PaintEventArgs e) {
        base.OnPaint(e);

        Size titleSize = string.IsNullOrEmpty(_title)
            ? Size.Empty
            : TextRenderer.MeasureText(e.Graphics, _title, Font);

        int top = titleSize.Height / 2;
        var frame = new Rectangle(0, top, Width - 1, Height - top - 1);

        using var pen = new Pen(SystemColors.ControlDark);
        if (titleSize.IsEmpty) {
            e.Graphics.DrawRectangle(pen, frame);
            return;
        }

        int gapStart = (Width - titleSize.Width) / 2 - TitleGap / 2;
        int gapEnd = gapStart + titleSize.Width + TitleGap;

        e.Graphics.DrawLine(pen, frame.Left, frame.Top, Math.Max(frame.Left, gapStart), frame.Top);
        e.Graphics.DrawLine(pen, Math.Min(frame.Right, gapEnd), frame.Top, frame.Right, frame.Top);
        e.Graphics.DrawLine(pen, frame.Left, frame.Top, frame.Left, frame.Bottom);
        e.Graphics.DrawLine(pen, frame.Right, frame.Top, frame.Right, frame.Bottom);
        e.Graphics.DrawLine(pen, frame.Left, frame.Bottom, frame.Right, frame.Bottom);

        TextRenderer.DrawText(
            e.Graphics, _title, Font,
            new Point((Width - titleSize.Width) / 2, 0),
            Enabled ? ForeColor : SystemColors.GrayText);
    }
}
