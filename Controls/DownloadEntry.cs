namespace ModMiiDownloader.Controls;

using ModMiiDownloader.Model;
using ModMiiDownloader.Resources;

public sealed class DownloadEntry {
    public DownloadEntry(DownloadItemInfo info, string page, string category) {
        Info = info;
        Id = info.Id;
        Name = info.Name;
        Page = page;
        Category = category;
    }

    public DownloadEntry(string id, string name, string iconKey) {
        Id = id;
        Name = name;
        IsCheckBox = true;
        CheckBoxIconKey = iconKey;
    }

    public static DownloadEntry Placeholder(string text) {
        return new("", text, Icons.Blank) { IsPlaceholder = true };
    }

    public DownloadItemInfo? Info { get; }
    public string Id { get; }
    public string Name { get; }
    public string? Page { get; }
    public string? Category { get; }

    public bool IsCheckBox { get; }
    public bool IsPlaceholder { get; private init; }
    private string? CheckBoxIconKey { get; }

    public string? Url => Info?.Url;
    public string? Warning => Info?.Warning;
    public string? ToolTip => Info?.ToolTip;
    public bool Disabled => IsPlaceholder || (Info?.Disabled ?? false);

    public bool Visited { get; set; }

    public string IconKey {
        get {
            if (IsCheckBox) return CheckBoxIconKey ?? Icons.Blank;
            if (Info is null) return Icons.Blank;

            if (Info.HasTag("recommended")) return "recommended";
            if (Info.HasTag("semi-recommended")) return "semiRecommended";
            if (Info.HasTag("auto-updates")) return "update";
            if (Info.HasTag("semi-auto-updates")) return "semiAutoUpdate";
            return Icons.Blank;
        }
    }

    public bool Matches(string sanitizedQuery) {
        if (Search.Sanitize(Name).Contains(sanitizedQuery, StringComparison.Ordinal)) return true;

        return Info?.AltNames?.Any(alt => Search.Sanitize(alt).Contains(sanitizedQuery, StringComparison.Ordinal))
               ?? false;
    }
}
