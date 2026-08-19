namespace ModMiiDownloader.Model;

using System.Xml.Linq;

public sealed class CiosMap {
    private readonly XElement _group;

    private CiosMap(XElement group) => _group = group;

    public string? Name => _group.Attribute("name")?.Value;

    public bool HasBase(int ios) {
        return _group.Elements("base").Any(element => element.Attribute("ios")?.Value == ios.ToString());
    }

    public static CiosMap? Load(string path) {
        Log.Write($"Attempting to load \"{path}\"");
        try {
            XElement? group = XDocument.Load(path).Root?.Element("ciosgroup");
            if (group is null) {
                Log.Write("cIOS map doesn't exist");
                return null;
            }

            return new CiosMap(group);
        } catch (FileNotFoundException) {
            Log.Write($"There seems to be no cIOS map at \"{path}\"");
        } catch (DirectoryNotFoundException) {
            Log.Write($"There seems to be no cIOS map at \"{path}\"");
        } catch (Exception e) {
            Log.Error(e, $"load/parse cIOS map at \"{path}\"");
        }

        return null;
    }
}

public sealed class CiosMapSet {
    public CiosMap? Wii { get; private init; }
    public CiosMap? VWii { get; private init; }

    /// <summary>
    /// picks the first Wii map whose group matches the d2x revision ModMii asked for, then
    /// takes the vWii map from the same location so the two always come from one d2x install
    /// </summary>
    public static CiosMapSet Load(ConfigPaths paths, string? d2xRev) {
        CiosMap? wii = null;
        int matchedIndex = -1;

        for (int i = 0; i < paths.WiiMap.Count; i++) {
            CiosMap? map = LoadFrom(paths.WiiMap[i]);
            if (map is null) continue;

            if (d2xRev is null || map.Name == $"d2x-v{d2xRev}") {
                wii = map;
                matchedIndex = i;
                break;
            }

            Log.Write($"cIOS name ({map.Name}) doesn't match what I want (d2x-v{d2xRev})");
            matchedIndex = i;
        }

        if (wii is null)
            Log.Write("Failed to load/parse ciosmaps.xml, so no Wii d2x. This shouldn't ever happen?");
        else
            Log.Write("Successfully loaded & parsed ciosmaps.xml!");

        CiosMap? vWii = null;
        if (matchedIndex >= 0 && matchedIndex < paths.VWiiMap.Count)
            vWii = LoadFrom(paths.VWiiMap[matchedIndex]);

        if (vWii is null)
            Log.Write("Failed to load/parse ciosmaps_vWii.xml, so no vWii d2x. :/");
        else
            Log.Write("Successfully loaded & parsed ciosmaps_vWii.xml!");

        return new CiosMapSet { Wii = wii, VWii = vWii };
    }

    private static CiosMap? LoadFrom(string relativePath) {
        foreach (string path in AppPaths.Candidates(relativePath)) {
            var map = CiosMap.Load(path);
            if (map is not null) return map;
        }

        return null;
    }
}
