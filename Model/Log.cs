namespace ModMiiDownloader.Model;

public static class Log {
    public static void Write(string message) {
        try { Console.WriteLine(message); } catch { /* no console attached */ }

        System.Diagnostics.Debug.WriteLine(message);
    }

    public static void Error(Exception e, string doing) {
        Write($"{e.GetType().Name} occurred trying to {doing}:\n{e.Message}");
    }
}
