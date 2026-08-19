namespace ModMiiDownloader.Model;

/// <summary>
/// paths are attempted relative to working dir, then exe dir 
/// </summary>
public static class AppPaths {
    public static IEnumerable<string> Candidates(IEnumerable<string> relative) {
        IList<string> list = relative as IList<string> ?? [.. relative];

        foreach (string path in list)
            yield return path;

        string baseDir = AppContext.BaseDirectory;
        foreach (string path in list) {
            string full = Path.Combine(baseDir, path);
            if (!string.Equals(full, Path.GetFullPath(path), StringComparison.OrdinalIgnoreCase))
                yield return full;
        }
    }

    public static IEnumerable<string> Candidates(params string[] relative) {
        return Candidates((IEnumerable<string>)relative);
    }
}
