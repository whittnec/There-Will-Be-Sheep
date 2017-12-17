#sprite for poop
import pygame

class singlePoop(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create poop image
        self.image = pygame.transform.scale(pygame.image.load
        ('images/poop_single.png'),(70, 70))
        self.rect = self.image.get_rect()
        self.increase = 6
    
    def charge(self):
        self.rect.x -= self.increase