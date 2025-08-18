import os
import subprocess
import time

class StartupGraphics:
    def __init__(self, scope, resources):
        self.scope = scope
        self.resources = resources

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
            "--no-osd",        # no on-screen display
            "--orientation", "180",  # rotate 180 degrees
            "--aspect-mode", "fill",  # fill screen
            "--blank",
            video_path
        ]

        try:
            subprocess.run(cmd, check=True)
        except FileNotFoundError:
            print("[Startup] ERROR: omxplayer not found. Install with: sudo apt install omxplayer")
        except subprocess.CalledProcessError as e:
            print(f"[Startup] ERROR: omxplayer exited with code {e.returncode}")

        # Small delay so it doesn't instantly jump to main loop
#        time.sleep(0.2)
