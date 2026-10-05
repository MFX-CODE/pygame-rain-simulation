import pygame
from pygame.sprite import Sprite
import random 

class Raindrops(Sprite):
    """ Create a raindrops falling from the sky."""
    def __init__(self, drops, x, y):
        """ Initialize the class attribute and make single raindrops."""
        super().__init__()

        self.screen = drops.screen
        self.settings = drops.settings

        self.image = pygame.Surface((self.settings.rain_width,
                                      self.settings.rain_height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # blue body
        pygame.draw.rect(self.image, (180, 200, 255), (0, 0, 3, 12))
        # White tip
        pygame.draw.rect(self.image, (255, 255, 255), (0, 0, 3, 5))
        # Rain speed
        self.speed = random.uniform(5.0, 9.0)
 
        self.y = float(self.rect.y)
    def update(self):
        """ make the image of rain move down like a falling rain."""
        self.y += self.speed
        self.rect.y = self.y



        
