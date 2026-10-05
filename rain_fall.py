import sys
import pygame
from settings import Settings
from clouds import Clouds
from raindrop import Raindrops
import random
class Rain:
    """ Create a rain falling from the sky with clouds."""
    def __init__(self):
        """ Initialize the attribute of rain and is appearances."""
        pygame.init() 
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption('RAINING')

        self.cloud_layer = pygame.sprite.Group()
        self.rains = pygame.sprite.Group()
        self._create_cloud_layer()
        self._create_rains()
        self.rain_timer = 0
        
    def run_file(self):
        """ Method in charge of looping and handling other methods."""
        self.clock = pygame.time.Clock()
        while True:
            self._update_rains()
            self._update_screen_()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _create_cloud_layer(self):
        """ Create 6 different clouds that overlap to form one big cloud."""
        cloud_images = [
            'image/clouds1.png',
            'image/clouds2.png',
            'image/clouds3.png',
            'image/darkclouds1.png',
            'image/darkclouds2.png',
            'image/darkclouds3.png'
        ]
    
        cloud_width = 300
        overlap = 50
        start_x = -overlap

        for i, img_path in enumerate(cloud_images):
            x_position = start_x + i * (cloud_width - overlap)
            cloud = Clouds(self, img_path, x_position)
            self.cloud_layer.add(cloud)

    def _update_rains(self):
        """ Create a single raindrop."""
        self._create_rains()
        self._rain_gauge()
        self.rains.update()
        self._rain_stop()

    def _create_rains(self):
        """ Create new rain drops from under the cloud layer"""
        for cloud in self.cloud_layer.sprites():
            if random.random() < 0.1:
                x = random.randint(cloud.rect.left, cloud.rect.right)
                y = cloud.rect.bottom
                new_drop = Raindrops(self, x, y)
                self.rains.add(new_drop)

    def _rain_gauge(self):
        """ guage the maximum standard of rain spawn"""
        self.rain_timer += 1
        if self.rain_timer > 3:
            self.rain_timer = 0

    def _rain_stop(self):
        """ remove drops that fall off the screen."""
        for drop in self.rains.sprites():
            if drop.rect.top > self.settings.screen_height:
                self.rains.remove(drop)

    def _update_screen_(self):
        """ Make an update of every change in the program."""
        self.screen.fill(self.settings.screen_color)
        for cloud in self.cloud_layer.sprites():
            cloud.blitme()
        self.rains.draw(self.screen)

        pygame.display.flip()
        self.clock.tick(90)

if __name__ == '__main__':
    R = Rain()
    R.run_file()