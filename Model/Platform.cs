namespace ModMiiDownloader.Model;

using System.Runtime.InteropServices;

public static class Platform {
    [DllImport("kernel32.dll", CharSet = CharSet.Unicode)]
    private static extern IntPtr GetModuleHandle(string moduleName);

    [DllImport("kernel32.dll", CharSet = CharSet.Ansi, ExactSpelling = true)]
    private static extern IntPtr GetProcAddress(IntPtr module, string procName);

    private static bool? _isWine;

    /// <summary>true when running under Wine, which exports wine_get_version from ntdll.</summary>
    public static bool IsWine => _isWine ??= DetectWine();

    private static bool DetectWine() {
        try {
            nint ntdll = GetModuleHandle("ntdll.dll");
            bool wine = ntdll != IntPtr.Zero && GetProcAddress(ntdll, "wine_get_version") != IntPtr.Zero;
            Log.Write(wine ? "Running under Wine" : "Running on Windows");
            return wine;
        } catch (Exception e) {
            Log.Error(e, "detect Wine");
            return false;
        }
    }
}
