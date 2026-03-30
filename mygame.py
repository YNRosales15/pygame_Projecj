import pygame
from pygame.locals import *
pygame.init()

window_size = (400, 400) # sets the size of the window

screen = pygame.display.set_mode (window_size)
clock = pygame.time.Clock() # creates a clock to  control the frame rate

player_image = pygame.image.load(r"G:\pygame_Projecj\images\frog_face1.png").convert_alpha() # loads the image and converts it for better performance
player_FullBody = pygame.image.load(r"G:\pygame_Projecj\images\frog_fullbody.png").convert_alpha() # loads the image and converts it for better performance

running = True

while running:
    screen.blit(player_image, (100,100))
    screen.blit(player_FullBody, (200,200))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
    

    pygame.display.flip() # updates the display
    clock.tick(60) # limits the frame rate to 60 frames per second

pygame.quit()
