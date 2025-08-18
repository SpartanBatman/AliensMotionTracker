import smbus
import math
import logging

class Compass:
    def __init__(self, calibration, smoothing_factor=0.1):
        self.bus = smbus.SMBus(1)
        self.address = 0x0d  # QMC5883L default address
        self.x = 0
        self.y = 0
        self.z = 0
        self.calibration = calibration
        self.smbusAvailable = True
        self.smoothing_factor = smoothing_factor
        self.smoothed_bearing = None

        logging.basicConfig(filename='compass.log', level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(message)s')

        try:
            # Sensor init
            self.bus.write_byte_data(self.address, 0x0B, 0x01)  # Reset
            self.bus.write_byte_data(self.address, 0x09, 0x1D)  # 200Hz, 8 samples, continuous mode
            logging.info("[Compass] QMC5883L initialised successfully.")
        except OSError as e:
            logging.error(f"[Compass] Failed to initialize QMC5883L: {e}")
            self.smbusAvailable = False

    def read_word_2c(self, adr):
        # QMC5883L outputs little endian: LSB first, then MSB
        low = self.bus.read_byte_data(self.address, adr)
        high = self.bus.read_byte_data(self.address, adr + 1)
        val = (high << 8) | low
        if val >= 32768:  # signed conversion
            val -= 65536
        return val

    def updatexy(self, calibration):
        if not self.smbusAvailable:
            self.x, self.y, self.z = 0, 0, 0
            return

        try:
            raw_x = self.read_word_2c(0x00)
            raw_y = self.read_word_2c(0x02)
            raw_z = self.read_word_2c(0x04)

            # Apply offsets (hard-iron calibration)
            self.x = raw_x - calibration.xOffset
            self.y = raw_y - calibration.yOffset
            self.z = raw_z

            logging.debug(f"[Compass] Raw: X={raw_x}, Y={raw_y}, Z={raw_z}")
            logging.debug(f"[Compass] Calibrated: X={self.x:.2f}, Y={self.y:.2f}")

        except OSError as e:
            logging.error(f"[Compass] I2C read error: {e}")
            self.x, self.y, self.z = 0, 0, 0

    def getCompassBearing(self):
        if not self.smbusAvailable:
            return 0

        raw_bearing = math.degrees(math.atan2(self.y, self.x))
        if raw_bearing < 0:
            raw_bearing += 360

        # Initialize smoothed bearing on first run
        if self.smoothed_bearing is None:
            self.smoothed_bearing = raw_bearing
            delta = 0
        else:
            delta = raw_bearing - self.smoothed_bearing
            # Handle wrap-around
            if delta > 180:
                delta -= 360
            elif delta < -180:
                delta += 360

            # Exponential smoothing
            self.smoothed_bearing += self.smoothing_factor * delta
            # Keep in [0,360)
            self.smoothed_bearing %= 360

        logging.debug(f"[Compass] Raw: {raw_bearing:.2f}°, Δ: {delta:.2f}, Smoothed: {self.smoothed_bearing:.2f}°")

        return self.smoothed_bearing

