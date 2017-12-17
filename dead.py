#sprite for dead sheep
import pygame

class deadSheep(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create dead sheep image
        self.image = pygame.transform.scale(pygame.image.load
        ('images/sheep_dead.png'),(100, 100))
        self.rect = self.image.get_rect()

