#sprites for dog characters
import pygame

class sheepDog(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create sheep dog image
        self.image = pygame.transform.scale(pygame.image.load
        ('images/sheep_dog.png'),(100, 100))
        self.rect = self.image.get_rect()
        self.increase = 7

    def charge(self):
        self.rect.x += self.increase
        
class poopSheepDog(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create poop covered scrapie image
        self.image = pygame.transform.scale(pygame.image.load
        ('images/sheep_dog_poop.png'),(100, 100))
        self.rect = self.image.get_rect()
        
class meatSlab(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create evil face image
        self.image = pygame.transform.scale(pygame.image.load
        ('images/meat.png'),(100, 100))
        self.rect = self.image.get_rect()
        self.increase = 6

    def slabTypes(self):
        #possible cloud formations
        return {
        1: "x/nxx",
        2: "xxx",
        3: "xx",
        4: "x\n x\n x\n x\n x",
        5: "xx",
        6: "xxx\nxx"        
        }
        
class Choppy(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create knife images
        self.image = pygame.transform.scale(pygame.image.load
        ('images/knife.png'),(50, 50))
        self.rect = self.image.get_rect()
        self.increase = 15

    def charge(self):
        self.rect.y += self.increase
        