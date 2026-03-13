#!/usr/bin/env python3
import RPi.GPIO as GPIO
import os
import time

BUTTON_PIN = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Power button ready on GPIO", BUTTON_PIN)

press_time = None

try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:  # button pressed
            if press_time is None:
                press_time = time.time()
        else:  # button released
            if press_time is not None:
                duration = time.time() - press_time
                if duration < 2:  # short press → reboot
                    print("Reboot requested")
                    os.system("sudo reboot")
                elif duration >= 2:  # long press → shutdown
                    print("Shutdown requested")
                    os.system("sudo shutdown -h now")
                press_time = None
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()