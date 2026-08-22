namespace ModMiiDownloader.Model;

public static class QueueVars {
    public static Dictionary<string, string> Parse(string text) {
        var vars = new Dictionary<string, string>(StringComparer.Ordinal);

        foreach (string raw in text.Replace("set ", "").Split('\n')) {
            string line = raw.TrimEnd('\r');
            int split = line.IndexOf('=');
            if (split < 0) continue;

            string key = line.Substring(0, split);
            string rest = line.Substring(split + 1);
            // NOTE: "a=b=c" keeps only "b"
            int next = rest.IndexOf('=');
            vars[key] = next < 0 ? rest : rest.Substring(0, next);
        }

        return vars;
    }

    public static string Line(string key, bool selected) {
        return $"set {key}={(selected ? "*" : "")}\n";
    }

    public static string Line(string key, string value) {
        return $"set {key}={value}\n";
    }

    /// <summary>reads the queue ModMii left behind, trying each configured location</summary>
    public static string? Read(IEnumerable<string> paths) {
        foreach (string path in AppPaths.Candidates(paths)) {
            Log.Write($"Attempting to load \"{path}\"");
            try {
                return File.ReadAllText(path);
            } catch (FileNotFoundException) { Log.Write($"No vars at \"{path}\""); } catch (DirectoryNotFoundException) { Log.Write($"No vars at \"{path}\""); } catch (Exception e) { Log.Error(e, $"load vars at \"{path}\""); }
        }

        return null;
    }

    /// <summary>writes the queue back for ModMii; first writable location wins.</summary>
    public static bool Write(IEnumerable<string> paths, string contents) {
        foreach (string path in AppPaths.Candidates(paths)) {
            Log.Write($"Attempting to write to \"{path}\"");
            try {
                File.WriteAllText(path, contents);
                Log.Write("Success! Exiting now...");
                return true;
            } catch (Exception e) {
                Log.Error(e, $"save queue at \"{path}\"");
            }
        }

        return false;
    }
}
