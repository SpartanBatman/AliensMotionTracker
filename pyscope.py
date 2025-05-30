from luma.core.interface.serial import spi
from luma.lcd.device import ili9341
from PIL import Image, ImageDraw, ImageFont

class pyscope:
    def __init__(self):
        # Set up the SPI display using luma.lcd
        self.serial = spi(port=0, device=0, gpio_DC=24, gpio_RST=25, bus_speed_hz=40000000)
        #self.device = ili9341(self.serial, width=320, height=240, rotate=0, double_buffer=True)
        self.device = ili9341(self.serial, width=320, height=240, rotate=0, double_buffer=True, framebuffer='diff_to_previous', hardware_acceleration=True)

        # Create a blank image and drawing context
        self.image = Image.new("RGB", (self.device.width, self.device.height), "black")
        self.draw = ImageDraw.Draw(self.image)

        # Load a default font
        self.font = ImageFont.load_default()

        # Clear the screen
        self.clear()

    def clear(self):
        self.draw.rectangle((0, 0, self.device.width, self.device.height), fill="black")
        self.device.display(self.image)

    def draw_text(self, position, text, fill="white"):
        self.draw.text(position, text, font=self.font, fill=fill)
        self.device.display(self.image)

    def draw_circle(self, center, radius, outline="white"):
        x, y = center
        self.draw.ellipse((x - radius, y - radius, x + radius, y + radius), outline=outline)
        self.device.display(self.image)

    def draw_line(self, start, end, fill="white"):
        self.draw.line([start, end], fill=fill)
        self.device.display(self.image)
