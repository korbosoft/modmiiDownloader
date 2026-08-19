namespace ModMiiDownloader;

using ModMiiDownloader.Forms;
using ModMiiDownloader.Model;
using ModMiiDownloader.Resources;

internal static class Program {
    [STAThread]
    private static int Main() {
        try {
            return Run();
        } catch (Exception e) {
            // Wine is missing pieces a real Windows always has, so a startup failure there
            // would otherwise be a silent exit with nothing for ModMii to report.
            Log.Error(e, "start the downloader");
            MessageBox.Show(
                $"The downloader could not start.\n\n{e.GetType().Name}: {e.Message}",
                "ModMii", MessageBoxButtons.OK, MessageBoxIcon.Error);
            return 1;
        }
    }

    private static int Run() {
        ApplicationConfiguration.Initialize();

        // Icons rasterise once at the display's scale, so the scale has to be known up front.
        using (var probe = new Form()) Icons.DpiScale = probe.DeviceDpi / 96f;

        DownloaderConfig config;
        try {
            config = DownloaderConfig.Load();
        } catch (Exception e) {
            Log.Error(e, "load downloader.json");
            MessageBox.Show(
                $"downloader.json could not be loaded, so there is nothing to download.\n\n{e.Message}",
                "ModMii", MessageBoxButtons.OK, MessageBoxIcon.Error);
            return 1;
        }

        using var form = new MainForm(config);
        Application.Run(form);
        return 0;
    }
}
