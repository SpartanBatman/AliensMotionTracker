import time
from PIL import Image

class StartupGraphics:
    def __init__(self, scope, resources):
        self.scope = scope
        self.resources = resources

        self.start1Time = 0
        self.start2Time = 3
        self.endTime = 8

        self.animationStepMultiplier = self.start2Time / 4.0
        self.opacityMultiplier = 255.0 / self.animationStepMultiplier

        self.yOpacityStartTime = self.animationStepMultiplier * 1
        self.logoOpacityStartTime = self.animationStepMultiplier * 2
        self.taglineOpacityStartTime = self.animationStepMultiplier * 3

        self.animation2StepMultiplier = (self.endTime - self.start2Time) / 15.0
        self.currentTime = 0
        self.status = "START1"

    def draw(self):
        startupTimerStart = time.time()
        done = False

        while not done:
            startupTimerCurrent = time.time()
            self.currentTime = startupTimerCurrent - startupTimerStart

            if self.start1Time <= self.currentTime < self.start2Time:
                self.status = "START1"
            elif self.currentTime <= self.endTime:
                self.status = "START2"
            else:
                done = True
                continue

            if self.status == "START1":
                self.draw1()
            elif self.status == "START2":
                self.draw2()

    def draw1(self):
        # Create a new base image (black background)
        base = Image.new("RGBA", (320, 240), (0, 0, 0, 255))

        # Calculate opacity
        if self.currentTime < self.yOpacityStartTime:
            opacity = self.currentTime * self.opacityMultiplier
        elif self.currentTime < self.logoOpacityStartTime:
            opacity = (self.currentTime * self.opacityMultiplier) - 255
        elif self.currentTime < self.taglineOpacityStartTime:
            opacity = (self.currentTime * self.opacityMultiplier) - 510
        else:
            opacity = (self.currentTime * self.opacityMultiplier) - 765

        # Determine which frame index to use based on opacity
        index = min(int(opacity // 25.5), 10)

        # Composite images in order with transparency preserved
        base.paste(self.resources.w[min(index, 10)], (0, 0), self.resources.w[min(index, 10)])

        if self.currentTime >= self.yOpacityStartTime:
            base.paste(self.resources.y[min(index, 10)], (0, 0), self.resources.y[min(index, 10)])
        if self.currentTime >= self.logoOpacityStartTime:
            base.paste(self.resources.logo[min(index, 10)], (0, 0), self.resources.logo[min(index, 10)])
        if self.currentTime >= self.taglineOpacityStartTime:
            base.paste(self.resources.tag[min(index, 10)], (0, 0), self.resources.tag[min(index, 10)])

        # Convert to RGB and display
        #self.scope.device.display(base.convert("RGB"))
        self.scope.device.display(base.convert("RGB").resize(self.scope.device.size))

    def draw2(self):
        # Calculate which frame to display in START2 animation
        currentTime = self.currentTime - self.start2Time
        step = min(int(currentTime / self.animation2StepMultiplier), 14)

        img = self.resources.setup[step]
        #self.scope.device.display(img.convert("RGB"))
        self.scope.device.display(img.convert("RGB").resize(self.scope.device.size))
