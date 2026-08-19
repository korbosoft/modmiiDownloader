namespace ModMiiDownloader.Model;

using System.Text.RegularExpressions;

public static partial class Search {
    [GeneratedRegex("[^a-z0-9\\s]")]
    private static partial Regex Sanitizer();

    /// <summary>Lower-cases and drops non-alphanumeric characters; "cIOS249[56]" becomes "cios24956".</summary>
    public static string Sanitize(string text) {
        return Sanitizer().Replace(text.ToLowerInvariant(), "");
    }
}
