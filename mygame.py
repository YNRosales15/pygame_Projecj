import pygame
from pygame.locals import *
pygame.init()

window_size = (750, 750) # sets the size of the window

screen = pygame.display.set_mode (window_size)
pygame.display.set_caption("alien invasion") # this sets the title of the window
clock = pygame.time.Clock() # creates a clock to  control the frame rate

white = (255, 255, 255) # defines the color white
green = (0, 255, 0) # defines the color green
red = (255, 0, 0) # defines the color red
black = (0, 0, 0) # defines the color black

class Frog(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # initializes the sprite
        self.image = pygame.Surface([50, 25]) # creates a surface for the sprite
        self.image = pygame.image.load(r"G:\pygame_Projecj\images\frog_face_withBar1.png").convert_alpha() # loads the image for the sprite
        self.rect = self.image.get_rect() # gets the reactangle of the sprite
        self.lives = 3 # sets thhe number of live the player has
    
    def draw(self):
        screen.blit(self.image, self.rect) #  draws the sprite on the screen
     
 
frog = Frog()
frog.rect.x= 375
frog.rect.y= 650

        
def redraw():
    screen.fill(black) # fills the screen with black
    frog.draw()
    pygame.display.update() # updates the display
    
run = True

while run:
    pygame.time.delay(100) # adds a delay to control the game speed\
        
    for event in pygame.event.get(): # checks for events (like key presses or mouse clicks)
        if event.type == QUIT:
            run = False
            
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        frog.rect.x += -10
        
    if key[pygame.K_RIGHT]:
        frog.rect.x += 10
            
    redraw()
    clock.tick(60) # limits the frame rate to 60 frames per second

pygame.quit()
