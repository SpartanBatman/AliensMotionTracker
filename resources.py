import pygame, sys, os
from PIL import Image

#load resources for the tracker
class resources:

    def __init__(self):

        current_file_path = __file__
        current_file_dir = os.path.dirname(__file__)
        resourcesDirPath = current_file_dir + "//resources"

        #Load the audio files
        self.click=pygame.mixer.Sound(resourcesDirPath + "/click.wav")
        self.audioBlip = []
        self.audioBlip.append(pygame.mixer.Sound(resourcesDirPath + "/trackerF.wav"))
        self.audioBlip.append(pygame.mixer.Sound(resourcesDirPath + "/trackerE.wav"))
        self.audioBlip.append(pygame.mixer.Sound(resourcesDirPath + "/trackerD.wav"))
        self.audioBlip.append(pygame.mixer.Sound(resourcesDirPath + "/trackerC.wav"))
        self.audioBlip.append(pygame.mixer.Sound(resourcesDirPath + "/trackerB.wav"))

        #Load the image files
        #self.info = Image.open(resourcesDirPath + "/hudBottom.png").convert("RGB")
        #self.info = Image.open(resourcesDirPath + "/motiontrackerhud.png").convert("RGB")
        #self.calibrationSplash = Image.open(resourcesDirPath + "/calibrationSplash.png").convert("RGB")

	#Load the image files
        self.info = Image.open(resourcesDirPath + "/hudBottom.png").convert("RGBA")
        self.hud = Image.open(resourcesDirPath + "/motiontrackerhud.png").convert("RGBA")
        self.calibrationSplash = Image.open(resourcesDirPath + "/calibrationSplash.png").convert("RGBA")
        #get the startup settings screens
        self.setup=[]
        self.setup.append(Image.open(resourcesDirPath + "//startup//start2//icon1.png").convert("RGB"))
        self.setup.append(Image.open(resourcesDirPath + "//startup//start2//icon2.png").convert("RGB"))
        self.setup.append(Image.open(resourcesDirPath + "//startup//start2//icon3.png").convert("RGB"))
        self.setup.append(Image.open(resourcesDirPath + "//startup//start2//icon4.png").convert("RGB"))
        self.setup.append(Image.open(resourcesDirPath + "//startup//start2//icon5.png").convert("RGB"))
        self.setup.append(Image.open(resourcesDirPath + "//startup//start2//icon6.png").convert("RGB"))
        self.setup.append(Image.open(resourcesDirPath + "//startup//start2//icon7.png").convert("RGB"))
        self.setup.append(Image.open(resourcesDirPath + "//startup//start2//icon8.png").convert("RGB"))
        self.setup.append(Image.open(resourcesDirPath + "//startup//start2//icon9.png").convert("RGB"))
        self.setup.append(Image.open(resourcesDirPath + "//startup//start2//icon10.png").convert("RGB"))
        self.setup.append(Image.open(resourcesDirPath + "//startup//start2//icon11.png").convert("RGB"))
        self.setup.append(Image.open(resourcesDirPath + "//startup//start2//icon12.png").convert("RGB"))
        self.setup.append(Image.open(resourcesDirPath + "//startup//start2//icon13.png").convert("RGB"))
        self.setup.append(Image.open(resourcesDirPath + "//startup//start2//icon14.png").convert("RGB"))
        self.setup.append(Image.open(resourcesDirPath + "//startup//start2//icon15.png").convert("RGB"))

        #get the weyland image animation frames
        self.w=[]
        self.w.append(Image.open(resourcesDirPath + "//startup//start1//wy1_5.png").convert("RGBA"))
        self.w.append(Image.open(resourcesDirPath + "//startup//start1//wy1_30.png").convert("RGBA"))
        self.w.append(Image.open(resourcesDirPath + "//startup//start1//wy1_55.png").convert("RGBA"))
        self.w.append(Image.open(resourcesDirPath + "//startup//start1//wy1_80.png").convert("RGBA"))
        self.w.append(Image.open(resourcesDirPath + "//startup//start1//wy1_105.png").convert("RGBA"))
        self.w.append(Image.open(resourcesDirPath + "//startup//start1//wy1_130.png").convert("RGBA"))
        self.w.append(Image.open(resourcesDirPath + "//startup//start1//wy1_155.png").convert("RGBA"))
        self.w.append(Image.open(resourcesDirPath + "//startup//start1//wy1_180.png").convert("RGBA"))
        self.w.append(Image.open(resourcesDirPath + "//startup//start1//wy1_205.png").convert("RGBA"))
        self.w.append(Image.open(resourcesDirPath + "//startup//start1//wy1_230.png").convert("RGBA"))
        self.w.append(Image.open(resourcesDirPath + "//startup//start1//wy1_255.png").convert("RGBA"))

        #get the yutani image animation frames
        self.y=[]
        self.y.append(Image.open(resourcesDirPath + "//startup//start1//wy2_5.png").convert("RGBA"))
        self.y.append(Image.open(resourcesDirPath + "//startup//start1//wy2_30.png").convert("RGBA"))
        self.y.append(Image.open(resourcesDirPath + "//startup//start1//wy2_55.png").convert("RGBA"))
        self.y.append(Image.open(resourcesDirPath + "//startup//start1//wy2_80.png").convert("RGBA"))
        self.y.append(Image.open(resourcesDirPath + "//startup//start1//wy2_105.png").convert("RGBA"))
        self.y.append(Image.open(resourcesDirPath + "//startup//start1//wy2_130.png").convert("RGBA"))
        self.y.append(Image.open(resourcesDirPath + "//startup//start1//wy2_155.png").convert("RGBA"))
        self.y.append(Image.open(resourcesDirPath + "//startup//start1//wy2_180.png").convert("RGBA"))
        self.y.append(Image.open(resourcesDirPath + "//startup//start1//wy2_205.png").convert("RGBA"))
        self.y.append(Image.open(resourcesDirPath + "//startup//start1//wy2_230.png").convert("RGBA"))
        self.y.append(Image.open(resourcesDirPath + "//startup//start1//wy2_255.png").convert("RGBA"))

        #get the weyland yutani logo image animation frames
        self.logo=[]
        self.logo.append(Image.open(resourcesDirPath + "//startup//start1//wy3_5.png").convert("RGBA"))
        self.logo.append(Image.open(resourcesDirPath + "//startup//start1//wy3_30.png").convert("RGBA"))
        self.logo.append(Image.open(resourcesDirPath + "//startup//start1//wy3_55.png").convert("RGBA"))
        self.logo.append(Image.open(resourcesDirPath + "//startup//start1//wy3_80.png").convert("RGBA"))
        self.logo.append(Image.open(resourcesDirPath + "//startup//start1//wy3_105.png").convert("RGBA"))
        self.logo.append(Image.open(resourcesDirPath + "//startup//start1//wy3_130.png").convert("RGBA"))
        self.logo.append(Image.open(resourcesDirPath + "//startup//start1//wy3_155.png").convert("RGBA"))
        self.logo.append(Image.open(resourcesDirPath + "//startup//start1//wy3_180.png").convert("RGBA"))
        self.logo.append(Image.open(resourcesDirPath + "//startup//start1//wy3_205.png").convert("RGBA"))
        self.logo.append(Image.open(resourcesDirPath + "//startup//start1//wy3_230.png").convert("RGBA"))
        self.logo.append(Image.open(resourcesDirPath + "//startup//start1//wy3_255.png").convert("RGBA"))

        #get the weyland yutani tagline image animation frames
        self.tag=[]
        self.tag.append(Image.open(resourcesDirPath + "//startup//start1//wy4_5.png").convert("RGBA"))
        self.tag.append(Image.open(resourcesDirPath + "//startup//start1//wy4_30.png").convert("RGBA"))
        self.tag.append(Image.open(resourcesDirPath + "//startup//start1//wy4_55.png").convert("RGBA"))
        self.tag.append(Image.open(resourcesDirPath + "//startup//start1//wy4_80.png").convert("RGBA"))
        self.tag.append(Image.open(resourcesDirPath + "//startup//start1//wy4_105.png").convert("RGBA"))
        self.tag.append(Image.open(resourcesDirPath + "//startup//start1//wy4_130.png").convert("RGBA"))
        self.tag.append(Image.open(resourcesDirPath + "//startup//start1//wy4_155.png").convert("RGBA"))
        self.tag.append(Image.open(resourcesDirPath + "//startup//start1//wy4_180.png").convert("RGBA"))
        self.tag.append(Image.open(resourcesDirPath + "//startup//start1//wy4_205.png").convert("RGBA"))
        self.tag.append(Image.open(resourcesDirPath + "//startup//start1//wy4_230.png").convert("RGBA"))
        self.tag.append(Image.open(resourcesDirPath + "//startup//start1//wy4_255.png").convert("RGBA"))

        #load the background contact images
        self.contactBack = []
        for i in range(0,4,1):
            imageName = resourcesDirPath + "/contactback" + str(i) + ".png"
            self.contactBack.append(Image.open(imageName).convert("RGBA"))

        #load the foreground contact images
        self.contactFore = []
        for i in range(0,4,1):
            imageName = resourcesDirPath + "/contactfore" + str(i) + ".png"
            self.contactFore.append(Image.open(imageName).convert("RGBA"))

        #load the radar wave images
        self.waves = []
        for i in range(0,16,1):
            imageName = resourcesDirPath + "/motiontrackerrings" + str(i) + ".png"
            self.waves.append(Image.open(imageName).convert("RGBA"))

        #load the fonts
        self.font = pygame.font.Font(None, 38)
        self.smallfont = pygame.font.Font(None, 25)
        self.displayScaleFont = pygame.font.Font(None, 20)
