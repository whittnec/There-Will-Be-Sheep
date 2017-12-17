#sprites for pee level characters
import pygame

class peeScrapie(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create scrapie sheep image
        self.image = pygame.transform.scale(pygame.image.load
        ('images/sheep_scrapie_piss.png'),(50, 50))
        self.rect = self.image.get_rect()
        self.increase = 7

    def charge(self):
        self.rect.x += self.increase

class poopPeeScrapie(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create poop covered scrapie image
        self.image = pygame.transform.scale(pygame.image.load
        ('images/sheep_scrapie_piss_poop.png'),(70, 70))
        self.rect = self.image.get_rect()
        
class normCell(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create blood
        self.image = pygame.transform.scale(pygame.image.load
        ('images/blood.png'),(40, 60))
        self.rect = self.image.get_rect()
        self.increase = 6

    def bloodTypes(self):
        #possible cloud formations
        return {
        1: "xxx/nxxx/nxxxx",
        2: "x/nx",
        3: "xxxxx",
        4: "x\n x\n x",
        5: "x/n/nx",
        6: "x\nxx"        
        }
        
        
class fallingFlagella(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create flagella
        self.image = pygame.transform.scale(pygame.image.load
        ('images/flagella.png'),(50, 50))
        self.rect = self.image.get_rect()
        self.increase = 15

    def charge(self):
        self.rect.y += self.increase

class smallPoop(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create poop image
        self.image = pygame.transform.scale(pygame.image.load
        ('images/poop_single.png'),(40, 40))
        self.rect = self.image.get_rect()
        self.state = None
        self.increase = 4
    
    def charge(self):
        self.rect.x -= self.increase

        