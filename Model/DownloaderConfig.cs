namespace ModMiiDownloader.Model;

using System.Text.Json;
using System.Text.Json.Serialization;

public sealed class DownloaderConfig {
    private static readonly JsonSerializerOptions JsonOptions = new() {
        PropertyNameCaseInsensitive = true,
        ReadCommentHandling = JsonCommentHandling.Skip,
        AllowTrailingCommas = true,
    };

    public Dictionary<string, Dictionary<string, DownloadCategory>> DownloadList { get; init; } = [];
    public List<string> Themes { get; init; } = [];
    public Dictionary<string, string> CheckboxNames { get; init; } = [];
    public ConfigPaths Paths { get; init; } = new();
    public List<CiosSlot> RecommendedWiiCios { get; init; } = [];

    private Dictionary<string, string>? _displayNamesByCheckbox;

    public static DownloaderConfig Load() {
        IEnumerable<string> candidates = AppPaths.Candidates(
            "Support/subscripts/ModMiiDownloader/downloader.json",
            "downloader.json");

        Exception? last = null;
        foreach (string path in candidates) {
            Log.Write($"Attempting to load \"{path}\"");
            try {
                DownloaderConfig? config = JsonSerializer.Deserialize<DownloaderConfig>(File.ReadAllText(path), JsonOptions);
                if (config is not null) {
                    Log.Write($"Loaded \"{path}\"");
                    return config;
                }
            } catch (FileNotFoundException) { } catch (DirectoryNotFoundException) { } catch (Exception e) {
                last = e;
                Log.Error(e, $"load \"{path}\"");
            }
        }

        throw new FileNotFoundException("downloader.json could not be found or parsed.", last);
    }

    public IReadOnlyList<DownloadItemInfo> Items(string page, string category) {
        return DownloadList.TryGetValue(page, out Dictionary<string, DownloadCategory>? categories) && categories.TryGetValue(category, out DownloadCategory? cat)
            ? cat.Item
            : [];
    }

    public string? CheckboxDisplayName(string name) {
        return CheckboxNames.TryGetValue(name, out string? display) ? display : null;
    }

    public Dictionary<string, string> CheckboxNamesByDisplayName =>
        _displayNamesByCheckbox ??= CheckboxNames
            .GroupBy(pair => pair.Value)
            .ToDictionary(group => group.Key, group => group.First().Key);

    public bool IsRecommendedWiiCios(int slot, int baseIos) {
        return RecommendedWiiCios.Any(cios => cios.Slot == slot && cios.Base == baseIos);
    }
}

public sealed class DownloadCategory {
    public List<DownloadItemInfo> Item { get; init; } = [];
}

public sealed class DownloadItemInfo {
    public string Id { get; init; } = "";
    public string Name { get; init; } = "";
    [JsonPropertyName("altnames")] public List<string>? AltNames { get; init; }
    public string? ToolTip { get; init; }
    public List<string> Tags { get; init; } = [];
    public string? Url { get; init; }
    public string? Warning { get; init; }

    public bool HasTag(string tag) {
        return Tags.Contains(tag, StringComparer.OrdinalIgnoreCase);
    }

    public bool Disabled => HasTag("disabled");

    public bool HiddenHere => Platform.IsWine && HasTag("no-wine");
}

public sealed class ConfigPaths {
    public List<string> WiiMap { get; init; } = [];
    public List<string> VWiiMap { get; init; } = [];
    public List<string> Input { get; init; } = [];
    [JsonPropertyName("tempcheck")] public List<string> TempCheck { get; init; } = [];
}

public sealed class CiosSlot {
    public int Base { get; init; }
    public int Slot { get; init; }
}
