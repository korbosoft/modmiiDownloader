namespace ModMiiDownloader.Controls;

/// <summary>
/// Tabs share the full width of the control, which is what the Qt build's CustomTabWidget
/// did. WinForms only offers fixed-width tabs, so the width is recalculated on resize.
/// </summary>
public class FillTabControl : TabControl {
    public FillTabControl() {
        SizeMode = TabSizeMode.Fixed;
        Appearance = TabAppearance.Normal;
    }

    protected override void OnResize(EventArgs e) {
        base.OnResize(e);
        UpdateItemSize();
    }

    protected override void OnControlAdded(ControlEventArgs e) {
        base.OnControlAdded(e);
        UpdateItemSize();
    }

    protected override void OnHandleCreated(EventArgs e) {
        base.OnHandleCreated(e);
        UpdateItemSize();
    }

    private bool _updatingItemSize;

    private void UpdateItemSize() {
        // Assigning ItemSize resizes the control, which would call straight back in here.
        if (_updatingItemSize || TabCount == 0) return;

        // The tab strip is inset by a few pixels on each side; leaving them out avoids a
        // second row appearing once the tabs no longer fit.
        int width = Math.Max(1, (ClientSize.Width - 8) / TabCount);
        int height = Math.Max(24, (ImageList?.ImageSize.Height ?? 0) + 10);
        var size = new Size(width, height);

        if (ItemSize == size) return;

        _updatingItemSize = true;
        try {
            ItemSize = size;
        } finally {
            _updatingItemSize = false;
        }
    }
}
