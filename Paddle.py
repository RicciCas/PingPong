import pygame
BLACK = (0,0,0)
 
class Paddle(pygame.sprite.Sprite):
    #This class represents a paddle
    
    def __init__(self, color, width, height):
        # Call the parent class 
        super().__init__()
        
        # Pass in the color of the Paddle, width and height
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Drawing the paddle 
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        # Fetch the rectangle object 
        self.rect = self.image.get_rect()
        
    def moveUp(self, pixels):
        self.rect.y -= pixels
        #Checking that you are not going too far 
        if self.rect.y < 0:
          self.rect.y = 0
          
    def moveDown(self, pixels):
        self.rect.y += pixels
        if self.rect.y > 400:
          self.rect.y = 400