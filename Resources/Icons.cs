namespace ModMiiDownloader.Resources;

using Svg;
using System.Reflection;

public static class Icons {
    private static readonly Dictionary<string, string> Files = new(StringComparer.Ordinal) {
        ["recommended"] = "heart-solid.svg",
        ["semiRecommended"] = "heart.svg",
        ["download"] = "download.svg",
        ["update"] = "update.svg",
        ["semiAutoUpdate"] = "semiauto-update.svg",
        ["theme"] = "theme.svg",
        ["program"] = "program.svg",
        ["settings"] = "settings.svg",
        ["shield"] = "shield.svg",
        ["nus"] = "nus.svg",
        ["search"] = "search.svg",
        ["check"] = "check.svg",
        ["minus"] = "minus.svg",
        ["plus"] = "plus.svg",
        ["0"] = "number0.svg",
        ["1"] = "number1.svg",
        ["2"] = "number2.svg",
        ["3"] = "number3.svg",
        ["4"] = "number4.svg",
        ["5"] = "number5.svg",
        ["6"] = "number6.svg",
        ["7"] = "number7.svg",
        ["8"] = "number8.svg",
        ["9"] = "number9.svg",
    };

    public const string Blank = "blank";

    private static readonly Assembly Assembly = typeof(Icons).Assembly;
    private static readonly Dictionary<(string Key, int Size), Bitmap> Cache = [];
    private static Icon? _appIcon;
    public static float DpiScale { get; set; } = 1f;

    public static int Scale(int logicalSize) {
        return Math.Max(1, (int)Math.Round(logicalSize * DpiScale));
    }

    /// <summary>rasterizes <paramref name="key"/> at a logical size (16/24/etc), DPI scaling included</summary>
    public static Bitmap Get(string key, int logicalSize) {
        return GetExact(key, Scale(logicalSize));
    }

    /// <summary>rasterizes <paramref name="key"/> at an exact pixel size, for icons that match a control's font height.</summary>
    public static Bitmap GetExact(string key, int size) {
        size = Math.Max(1, size);
        if (Cache.TryGetValue((key, size), out Bitmap? cached)) return cached;

        Bitmap bitmap = key == Blank ? Empty(size) : Render(key, size);
        Cache[(key, size)] = bitmap;
        return bitmap;
    }

    public static Icon App {
        get {
            if (_appIcon is not null) return _appIcon;

            using Stream? stream = Assembly.GetManifestResourceStream("assets/icon.png");
            if (stream is null) return _appIcon = SystemIcons.Application;

            using var bitmap = new Bitmap(stream);
            return _appIcon = Icon.FromHandle(bitmap.GetHicon());
        }
    }

    private static Bitmap Render(string key, int size) {
        if (!Files.TryGetValue(key, out string? file))
            return Empty(size);

        using Stream? stream = Assembly.GetManifestResourceStream($"assets/{file}");
        if (stream is null) return Empty(size);

        using var reader = new StreamReader(stream);
        string markup = reader.ReadToEnd()
            .Replace("#000000", ColorTranslator.ToHtml(SystemColors.ControlText));

        try {
            var document = SvgDocument.FromSvg<SvgDocument>(markup);
            return document.Draw(size, size);
        } catch (Exception e) {
            Model.Log.Error(e, $"render \"{file}\"");
            return Empty(size);
        }
    }

    private static Bitmap Empty(int size) {
        var bitmap = new Bitmap(size, size, System.Drawing.Imaging.PixelFormat.Format32bppArgb);
        bitmap.MakeTransparent();
        return bitmap;
    }
}
