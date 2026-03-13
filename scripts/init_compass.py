import smbus
import time

ADDR = 0x0D  # QMC5883L I2C address
REG_CTRL1 = 0x09
REG_CTRL2 = 0x0A
REG_DATA_START = 0x00

bus = smbus.SMBus(1)

def init_compass(max_attempts=5, delay=0.2):
    """
    Initialize the QMC5883L to continuous mode with retries.
    max_attempts: number of times to retry if sensor not ready
    delay: seconds between retries
    """
    for attempt in range(1, max_attempts + 1):
        try:
            # Soft reset
            bus.write_byte_data(ADDR, REG_CTRL2, 0x01)
            time.sleep(0.05)

            # Continuous measurement, 200Hz, 8x oversampling
            bus.write_byte_data(ADDR, REG_CTRL1, 0b00011100)
            time.sleep(0.05)

            # Test read: 6 bytes for X, Y, Z
            data = bus.read_i2c_block_data(ADDR, REG_DATA_START, 6)

            # If read successful and non-zero, done
            if any(data):
                print(f"Compass initialized successfully on attempt {attempt}.")
                return True
        except Exception as e:
            print(f"Attempt {attempt} failed: {e}")
            time.sleep(delay)

    print("Compass initialization failed after retries.")
    return False

# Wait briefly after power-on
time.sleep(0.2)
init_compass()