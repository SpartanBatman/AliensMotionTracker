
#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

sleep 10
fbcp &
sudo SDL_AUDIODRIVER=alsa AUDIODEV=hw:0,0 SDL_VIDEODRIVER=fbcon SDL_FBDEV=/dev/fb1 python3 /home/pi/AliensMotionTracker/main.py