namespace ModMiiDownloader.Controls;

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
        if (_updatingItemSize || TabCount == 0) return;

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
