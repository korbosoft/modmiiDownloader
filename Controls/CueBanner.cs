namespace ModMiiDownloader.Controls;

using System.Runtime.InteropServices;

internal static class CueBanner {
    private const int EmSetCueBanner = 0x1501;

    [DllImport("user32.dll", CharSet = CharSet.Unicode)]
    private static extern IntPtr SendMessage(IntPtr window, int message, IntPtr wParam, string lParam);

    public static void Set(TextBox box, string text) {
        void Apply() {
            SendMessage(box.Handle, EmSetCueBanner, (IntPtr)1, text);
        }

        if (box.IsHandleCreated) Apply();
        box.HandleCreated += (_, _) => Apply();
    }
}
