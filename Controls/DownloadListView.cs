namespace ModMiiDownloader.Controls;

using ModMiiDownloader.Resources;

public sealed class DownloadEntryEventArgs(DownloadEntry entry, ListViewItem item) : EventArgs {
    public DownloadEntry Entry { get; } = entry;
    public ListViewItem Item { get; } = item;
}

public class DownloadListView : ListView {
    private const int WmMouseMove = 0x0200;
    private const int WmLButtonDown = 0x0201;
    private const int WmLButtonUp = 0x0202;
    private const int WmLButtonDblClk = 0x0203;
    private const int WmCaptureChanged = 0x0215;

    private static readonly Color LinkColor = SystemColors.HotTrack;
    private static readonly Color VisitedLinkColor = Color.FromArgb(128, 0, 128);

    private bool _suppressSelectionGuard;

    private int _anchorIndex = -1;
    private int _pressedIndex = -1;
    private int _dragLastIndex = -1;
    private bool _dragging;
    private bool _dragMoved;
    private bool _dragSelects;

    private readonly System.Windows.Forms.Timer _edgeScroll = new() { Interval = 60 };

    public DownloadListView() {
        View = View.Details;
        HeaderStyle = ColumnHeaderStyle.None;
        FullRowSelect = true;
        MultiSelect = true;
        OwnerDraw = true;
        LabelEdit = false;
        ShowItemToolTips = true;
        DoubleBuffered = true;
        BorderStyle = BorderStyle.FixedSingle;
        Columns.Add(new ColumnHeader { Text = "", Width = 200 });

        // only exists to give every row a consistent height
        SmallImageList = new ImageList { ImageSize = new Size(1, Icons.Scale(16) + 6) };

        _edgeScroll.Tick += (_, _) => ScrollWhileDragging();
    }

    public event EventHandler<DownloadEntryEventArgs>? EntryClicked;
    public event EventHandler<DownloadEntryEventArgs>? EntryDoubleClicked;

    public IEnumerable<DownloadEntry> Entries =>
        Items.Cast<ListViewItem>().Select(item => (DownloadEntry)item.Tag!);

    public IEnumerable<DownloadEntry> SelectedEntries =>
        SelectedItems.Cast<ListViewItem>().Select(item => (DownloadEntry)item.Tag!);

    public ListViewItem Add(DownloadEntry entry) {
        var item = new ListViewItem(entry.Name) { Tag = entry };
        if (!string.IsNullOrEmpty(entry.ToolTip)) item.ToolTipText = entry.ToolTip;
        Items.Add(item);
        return item;
    }

    public void SetEntries(IEnumerable<DownloadEntry> entries) {
        BeginUpdate();
        Items.Clear();
        foreach (DownloadEntry entry in entries) Add(entry);
        EndUpdate();
    }

    public ListViewItem? Find(string id) {
        return Items.Cast<ListViewItem>().FirstOrDefault(item => ((DownloadEntry)item.Tag!).Id == id);
    }

    public void Select(string id) {
        ListViewItem? item = Find(id);
        if (item is not null && !((DownloadEntry)item.Tag!).Disabled) item.Selected = true;
    }

    public void Toggle(string id) {
        ListViewItem? item = Find(id);
        if (item is not null && !((DownloadEntry)item.Tag!).Disabled) item.Selected = !item.Selected;
    }

    public void DeselectAll() {
        foreach (ListViewItem item in Items) item.Selected = false;
    }

    public void ToggleAll() {
        bool select = Items.Cast<ListViewItem>()
            .Any(item => !((DownloadEntry)item.Tag!).Disabled && !item.Selected);

        BeginUpdate();
        foreach (ListViewItem item in Items) {
            if (((DownloadEntry)item.Tag!).Disabled) continue;
            item.Selected = select;
        }

        EndUpdate();
    }

    protected override void OnResize(EventArgs e) {
        base.OnResize(e);
        if (Columns.Count > 0) Columns[0].Width = Math.Max(16, ClientSize.Width);
    }

    protected override void OnItemSelectionChanged(ListViewItemSelectionChangedEventArgs e) {
        if (e.IsSelected && !_suppressSelectionGuard && e.Item?.Tag is DownloadEntry { Disabled: true }) {
            _suppressSelectionGuard = true;
            e.Item.Selected = false;
            _suppressSelectionGuard = false;
            return;
        }

        base.OnItemSelectionChanged(e);
    }

    protected override void WndProc(ref Message m) {
        switch (m.Msg) {
            case WmLButtonDown: {
                    ListViewHitTestInfo hit = HitTest(PointFromMessage(m));
                    if (hit.Item is null) break;

                    Focus();
                    var entry = (DownloadEntry)hit.Item.Tag!;
                    int index = hit.Item.Index;
                    _pressedIndex = index;

                    if (entry.Disabled) {
                        _dragMoved = false;
                        return;
                    }

                    if ((ModifierKeys & Keys.Shift) != 0 && _anchorIndex >= 0 && _anchorIndex < Items.Count) {
                        ApplyRange(_anchorIndex, index, Items[_anchorIndex].Selected);
                        hit.Item.Focused = true;
                        return;
                    }

                    hit.Item.Selected = !hit.Item.Selected;
                    hit.Item.Focused = true;

                    _anchorIndex = index;
                    _dragLastIndex = index;
                    _dragSelects = hit.Item.Selected;
                    _dragging = true;
                    _dragMoved = false;
                    Capture = true;
                    return;
                }

            case WmMouseMove: {
                    if (!_dragging) break;

                    Point point = PointFromMessage(m);
                    if (point.Y < 0 || point.Y >= ClientSize.Height) {
                        _edgeScroll.Start();
                        return;
                    }

                    _edgeScroll.Stop();
                    ListViewHitTestInfo hit = HitTest(point);
                    if (hit.Item is not null) ExtendDragTo(hit.Item.Index);
                    return;
                }

            case WmLButtonUp: {
                    bool wasDragging = _dragging;
                    int pressed = _pressedIndex;
                    _pressedIndex = -1;

                    if (wasDragging) EndDrag();

                    if (!_dragMoved && pressed >= 0 && pressed < Items.Count) {
                        ListViewItem item = Items[pressed];
                        EntryClicked?.Invoke(this, new DownloadEntryEventArgs((DownloadEntry)item.Tag!, item));
                        return;
                    }

                    if (!wasDragging) break;
                    return;
                }

            case WmCaptureChanged:
                EndDrag();
                break;

            case WmLButtonDblClk: {
                    ListViewHitTestInfo hit = HitTest(PointFromMessage(m));
                    if (hit.Item is null) break;

                    var entry = (DownloadEntry)hit.Item.Tag!;
                    if (entry.Disabled) return;

                    EntryDoubleClicked?.Invoke(this, new DownloadEntryEventArgs(entry, hit.Item));
                    return;
                }
        }

        base.WndProc(ref m);
    }

    private void ExtendDragTo(int index) {
        if (index < 0 || index == _dragLastIndex) return;

        ApplyRange(_dragLastIndex, index, _dragSelects);
        _dragLastIndex = index;
        _dragMoved = true;
    }

    private void ApplyRange(int from, int to, bool selected) {
        int start = Math.Min(from, to);
        int end = Math.Max(from, to);

        BeginUpdate();
        for (int i = start; i <= end; i++) {
            if (i < 0 || i >= Items.Count) continue;
            if (((DownloadEntry)Items[i].Tag!).Disabled) continue;

            Items[i].Selected = selected;
        }

        EndUpdate();
    }

    private void ScrollWhileDragging() {
        if (!_dragging) {
            _edgeScroll.Stop();
            return;
        }

        Point point = PointToClient(MousePosition);
        int next = point.Y < 0 ? _dragLastIndex - 1
            : point.Y >= ClientSize.Height ? _dragLastIndex + 1
            : -1;

        if (next < 0 || next >= Items.Count) return;

        Items[next].EnsureVisible();
        ExtendDragTo(next);
    }

    private void EndDrag() {
        _dragging = false;
        _edgeScroll.Stop();
        if (Capture) Capture = false;
    }

    private static Point PointFromMessage(Message m) {
        return new(unchecked((short)(long)m.LParam), unchecked((short)((long)m.LParam >> 16)));
    }

    protected override void OnDrawSubItem(DrawListViewSubItemEventArgs e) {
        if (e.Item is null || e.Item.Tag is not DownloadEntry entry) {
            e.DrawDefault = true;
            return;
        }

        Graphics graphics = e.Graphics;
        Rectangle bounds = e.Bounds;

        Color background = e.Item.Selected
            ? (Focused ? SystemColors.Highlight : SystemColors.GradientInactiveCaption)
            : e.ItemIndex % 2 == 1
                ? AlternateRowColor
                : BackColor;

        using (var brush = new SolidBrush(background))
            graphics.FillRectangle(brush, bounds);

        int iconSize = Icons.Scale(16);
        Bitmap icon = Icons.Get(entry.IconKey, 16);
        int iconTop = bounds.Top + ((bounds.Height - iconSize) / 2);
        graphics.DrawImage(icon, new Rectangle(bounds.Left + 2, iconTop, iconSize, iconSize));

        Color color = entry.Disabled
            ? SystemColors.GrayText
            : e.Item.Selected
                ? SystemColors.HighlightText
                : entry.Url is not null
                    ? entry.Visited ? VisitedLinkColor : LinkColor
                    : ForeColor;

        Font font = entry.Url is not null ? UnderlinedFont : Font;
        var textBounds = new Rectangle(
            bounds.Left + iconSize + 6, bounds.Top,
            bounds.Width - iconSize - 8, bounds.Height);

        TextRenderer.DrawText(
            graphics, e.Item.Text, font, textBounds, color,
            TextFormatFlags.VerticalCenter | TextFormatFlags.Left | TextFormatFlags.EndEllipsis);

        if (e.Item.Focused && Focused)
            ControlPaint.DrawFocusRectangle(graphics, bounds);
    }

    private Font? _underlinedFont;

    private Font UnderlinedFont => _underlinedFont ??= new Font(Font, Font.Style | FontStyle.Underline);

    protected override void OnFontChanged(EventArgs e) {
        base.OnFontChanged(e);
        _underlinedFont?.Dispose();
        _underlinedFont = null;
    }

    private static Color AlternateRowColor {
        get {
            Color window = SystemColors.Window;
            Color control = SystemColors.Control;
            return Color.FromArgb(
                ((window.R * 12) + (control.R * 4)) / 16,
                ((window.G * 12) + (control.G * 4)) / 16,
                ((window.B * 12) + (control.B * 4)) / 16);
        }
    }

    protected override void Dispose(bool disposing) {
        if (disposing) {
            _underlinedFont?.Dispose();
            SmallImageList?.Dispose();
            _edgeScroll.Dispose();
        }

        base.Dispose(disposing);
    }
}
