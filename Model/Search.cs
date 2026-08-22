namespace ModMiiDownloader.Model;

using System.Text.RegularExpressions;

public static class Search {
    private static readonly Regex Sanitizer = new(@"[^a-z0-9\s]", RegexOptions.Compiled | RegexOptions.CultureInvariant);

    /// <summary>lower-cases and drops non-alphanumeric characters; "cIOS249[56]" becomes "cios24956".</summary>
    public static string Sanitize(string text) {
        return Sanitizer.Replace(text.ToLowerInvariant(), "");
    }
}
