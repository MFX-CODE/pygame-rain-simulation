import pygame
from pygame.sprite import Sprite
from random import randint

class Clouds(Sprite):
    """ Create clouds in up of the screen to match the rain class."""
    def __init__(self, cloud, image_path, x_pos):
        """ Initialize the class attribute and create layers of cloud."""
        super().__init__()

        self.screen = cloud.screen
        self.screen_rect = cloud.screen.get_rect()

        # create the layers of cloud in the sky (y axis of the screen)
        self.image = pygame.image.load('image/clouds1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (350, 100))
        self.rect = self.image.get_rect()

        # choosing image position
        self.rect.x = x_pos
        self.rect.y = randint(0, 50)
        self.image.set_alpha(180)

        # draw image to the screen
    def blitme(self):
        """ Draw the cloud at its currect location."""
        self.screen.blit(self.image, self.rect)



