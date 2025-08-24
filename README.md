# M314 Colonial Marine Motion tracker

## Credits

This project is based on the fantastic work by MartinR1000 who was the inspiration for me.
[Github](https://github.com/martinr1000/AliensMotionTracker/tree/master)

I've also used the Weyland-Yutani Logo created by Marrowbone. I liked how it worked with the tracker.
[YouTube](www.youtube.com/watch?v=Ew5Pk1K_0Z8)

I've also remixed the 3D model from Thingiverse by DrMorbius
[Colonial Marines Motion Tracker](https://www.thingiverse.com/thing:1733311/files)

## Hardware

16Gb MicroSD Card (cloned with OS + software)\
GPIO Extender / T-Board + Ribbon Cable (for easier wiring access)\
[Adafruit 2.8" PiTFT Plus (Capacitive Touch)](https://thepihut.com/products/adafruit-pitft-plus-320x240-2-8-tft-capacitive-touchscreen) – ILI9341 driver\
Physical Control Buttons (wired to GPIO, via GPIOzero)\
[GY-271 QMC5883L Magnetometer Compass](https://ebay.us/m/zPIQNP)\
[MAX98357A](https://thepihut.com/products/adafruit-i2s-3w-class-d-amplifier-breakout-max98357a)\
[Speaker - 4 Ohm 3 Watt ](https://thepihut.com/products/speaker-40mm-diameter-4-ohm-3-watt)\

Other Electronics

Misc jumper wires / Dupont cables

Resistors (for buttons, if required—depending on pull-up configuration)

## Software

I opted to run Pi Buster 2021-12-02 due to easier build environment and some libraries based on MartinR1000's build simply worked. Running a more up-to-date version of PiOS meant it would have required more rewriting of his code to get this working.

### Installed Libraries

This project was built and tested with the following system and Python libraries.

#### System / Core

RPi.GPIO==0.7.0 – Low-level Raspberry Pi GPIO control

gpiozero==1.6.2 – High-level GPIO interface for Raspberry Pi

spidev==3.5 – SPI interface for Raspberry Pi

smbus2==0.5.0 – I²C/SMBus communication

#### Hardware & Device Support

qmc5883l==0.92 – QMC5883L magnetometer (compass) driver

#### Adafruit Tools

adafruit-platformdetect==3.79.0 – Detects hardware platform for Adafruit libraries

adafruit-python-shell==1.9.1 – Helper for running setup/install scripts

#### Graphics & Game Development

pygame==1.9.4.post1 – 2D graphics, input, and sound handling (used for HUD, sprites, etc.)

PyGObject==3.30.4 – Python bindings for GNOME/GTK (GUI support if needed)


