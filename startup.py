import os
import subprocess

class StartupGraphics:
    def __init__(self, scope, resources):
        self.scope = scope
        self.resources = resources

    def kill_fbcp(self):
        """Kill fbcp if it is running."""
        try:
            subprocess.run(["pkill", "fbcp"], check=True)
            print("fbcp terminated")
        except subprocess.CalledProcessError:
            print("fbcp not running")

    def draw(self):
        # Get absolute path to the startup video
        video_path = os.path.join(
            os.path.dirname(__file__),
            "resources",
            "startup",
            "Startup-vid.mp4"
        )

        if not os.path.isfile(video_path):
            print(f"[Startup] ERROR: Video file not found: {video_path}")
            return

        print(f"[Startup] Playing intro video with omxplayer: {video_path}")

        # omxplayer command
        cmd = [
            "omxplayer",
            "--no-osd",
            "--orientation", "180",
            "--aspect-mode", "fill",
            "--blank",
            video_path
        ]

        try:
            # This will block until the video finishes
            subprocess.run(cmd, check=True)
        except FileNotFoundError:
            print("[Startup] ERROR: omxplayer not found. Install with: sudo apt install omxplayer")
        except subprocess.CalledProcessError as e:
            print(f"[Startup] ERROR: omxplayer exited with code {e.returncode}")

        # Kill fbcp after video finishes
        self.kill_fbcp()

