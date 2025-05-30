#!/usr/bin/python

import os
import sys
import time
import pygame
import random
from PIL import Image

# Delay on startup
time.sleep(5)

# GPIO setup
gpioAvailable = True
try:
    import RPi.GPIO as GPIO
except ImportError:
    gpioAvailable = False

# Set environment variables
os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_VIDEO_CENTERED"] = "1"

# Import internal modules
from audio import TrackerAudio
from resources import resources
from graphics import TrackerGraphics
from pyscope import pyscope
from startup import StartupGraphics
from calibration import Calibration
from calibrationGraphics import CalibrationGraphics

# GPIO pin assignments
BUTTON_PIN = 20
LED_PIN = 27

# State variables
numberOfButtonPresses = 0
buttonHoldTime = 0
buttonTimerStart = 0
ledState = False
ledOnTime = 1
ledOffTime = 1
changeLedState = True

# Setup GPIO
if gpioAvailable:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, ledState)

    def my_callback(channel):
        global numberOfButtonPresses, buttonHoldTime, buttonTimerStart
        if GPIO.input(BUTTON_PIN):
            buttonHoldTime = time.time() - buttonTimerStart
            buttonTimerStart = 0
        else:
            numberOfButtonPresses += 1
            buttonTimerStart = time.time()

    GPIO.add_event_detect(BUTTON_PIN, GPIO.BOTH, callback=my_callback, bouncetime=300)

# Initialize pygame and supporting modules
pygame.init()

# Initialize core components
scope = pyscope()
resources = resources()
ca = Calibration(scope, resources)
cg = CalibrationGraphics(scope, resources, ca)
sg = StartupGraphics(scope, resources)
tg = TrackerGraphics(scope, resources, ca)
ta = TrackerAudio(resources)

# Clock and startup
clock = pygame.time.Clock()
os.system("fbcp &")  # Optional screen mirroring
sg.draw()

# Tracker state
wave_size = 0
stateString = "TRACK"
done = False
qPress = False

startTime = time.time()

try:
    while not done:
        elapsedTime = time.time() - startTime

        # LED blink logic
        if (ledState and elapsedTime >= ledOnTime) or (not ledState and elapsedTime >= ledOffTime):
            ledState = not ledState
            if gpioAvailable:
                GPIO.output(LED_PIN, ledState)
            startTime = time.time()

        addContact = numberOfButtonPresses > 1
        if addContact:
            numberOfButtonPresses = 0

        if qPress:
            buttonHoldTime = time.time() - buttonTimerStart

        if buttonHoldTime > 4:
            buttonHoldTime = 0
            stateString = "CALIBRATE"
            ca.initCalibration()
            calibrationStep = 0

        if stateString == "CALIBRATE":
            xy = ca.calibrate(calibrationStep)
            if calibrationStep == 0:
                cg.initBackground()
                cg.update(xy, ca)
            elif calibrationStep >= 500:
                stateString = "TRACK"
            else:
                cg.update(xy, ca)
                calibrationStep += 1
        else:
            args = tg.update(wave_size, addContact, ca)
            if args != 999:
                ta.update(wave_size, args)
                wave_size = 0 if wave_size >= 15 else wave_size + 2

        clock.tick(30)

finally:
    print("clean exit")
    blank = Image.new("RGB", (320, 240), "black")
    scope.device.display(blank)
    if gpioAvailable:
        GPIO.cleanup()
    os.system("killall fbcp")
    pygame.quit()
