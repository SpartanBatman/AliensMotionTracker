#!/bin/sh
# auto-start.sh

sleep 2

# Show logo, keep process running in background and hides the console from the screen.
sudo fbi -T 1 -d /dev/fb1 -noverbose -a /home/pi/AliensMotionTracker/resources/startup/USCM_Logo.png &
FBI_PID=$!

sleep 10

fbcp &

# Kill fbi just before launching tracker so console doesn’t pop up
sudo kill $FBI_PID

# Launch tracker
sudo SDL_AUDIODRIVER=alsa AUDIODEV=hw:0,0 SDL_VIDEODRIVER=fbcon SDL_FBDEV=/dev/fb1 python3 /home/pi/AliensMotionTracker/main.py
