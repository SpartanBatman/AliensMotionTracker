import pygame
pygame.init()
# Setting game window dimensions
window_width = 320
window_height = 240
game_display = pygame.display.set_mode((window_width, window_height))
# Loading the image
bg_image = pygame.image.load('\resources\motiontrackerhud.png')
# Image initial position
x = 0
# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Moving the background
    x -= 1
    # Resetting the image when it leaves screen
    if x == -1 * bg_image.get_width():
        x = 0
    # Drawing image at position (x,0)
    game_display.blit(bg_image, (x, 0))
    pygame.display.update()
pygame.quit()
