using ModMiiDownloader.Model;
using System.Text;
using System.Text.RegularExpressions;

namespace ModMiiDownloader.Controls;

/// <summary>
/// The checkbox helpers from utils.py. Control names carry the ModMii variable name, so
/// lookups are by name and by the same regexes the Qt build used.
/// </summary>
public static class CheckBoxTools {
    public static IEnumerable<CheckBox> All(Control root) {
        foreach (Control child in root.Controls) {
            if (child is CheckBox box) yield return box;

            foreach (CheckBox nested in All(child)) yield return nested;
        }
    }

    /// <summary>Every checkbox whose name matches, unanchored, like QRegularExpression did.</summary>
    public static IEnumerable<CheckBox> Matching(Control root, string pattern) {
        var regex = new Regex(pattern, RegexOptions.CultureInvariant);
        return All(root).Where(box => regex.IsMatch(box.Name));
    }

    public static CheckBox? Find(Control root, string name) {
        return All(root).FirstOrDefault(box => box.Name == name);
    }

    /// <summary>
    /// Checks everything if anything enabled is still unchecked, otherwise clears the lot.
    /// Disabled boxes count as checked so they never keep the toggle stuck on "select".
    /// </summary>
    public static void Toggle(IEnumerable<CheckBox> boxes) {
        IList<CheckBox> list = boxes as IList<CheckBox> ?? [.. boxes];
        bool check = list.Any(box => box.Enabled && !box.Checked);

        foreach (CheckBox? box in list.Where(box => box.Enabled))
            box.Checked = check;
    }

    public static void Check(IEnumerable<CheckBox> boxes) {
        foreach (CheckBox? box in boxes.Where(box => box.Enabled))
            box.Checked = true;
    }

    public static void ToggleMatching(Control root, string pattern) {
        Toggle(Matching(root, pattern).ToList());
    }

    public static void CheckMatching(Control root, string pattern) {
        Check(Matching(root, pattern).ToList());
    }

    /// <summary>The "set name=*" lines for every checkbox under <paramref name="root"/>.</summary>
    public static string GetSelected(Control root) {
        var builder = new StringBuilder();

        foreach (CheckBox box in All(root))
            builder.Append(QueueVars.Line(box.Name, box.Enabled && box.Checked));

        return builder.ToString();
    }

    public static void SelectChild(Control root, string name) {
        CheckBox? box = Find(root, name);
        if (box is not null) box.Checked = true;
    }

    public static void UncheckAll(Control root) {
        foreach (CheckBox box in All(root)) box.Checked = false;
    }
}
