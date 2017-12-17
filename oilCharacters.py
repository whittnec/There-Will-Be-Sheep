#sprites for oil level characters
import pygame

class oilScrapie(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create oil scrapie image
        self.image = pygame.transform.scale(pygame.image.load
        ('images/sheep_scrapie_oil.png'),(200, 200))
        self.rect = self.image.get_rect()
        self.increase = 7

    def charge(self):
        self.rect.x += self.increase
        
class oilPoopScrap(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create poop covered scrapie image
        self.image = pygame.transform.scale(pygame.image.load
        ('images/sheep_scrapie_oil_poop.png'),(225, 225))
        self.rect = self.image.get_rect()
        
class firePic(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create fire image
        self.image = pygame.transform.scale(pygame.image.load
        ('images/fire.png'),(75, 90))
        self.rect = self.image.get_rect()
        
class evil(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create evil face image
        self.image = pygame.transform.scale(pygame.image.load
        ('images/evilFace.png'),(100, 100))
        self.rect = self.image.get_rect()
        self.increase = 6

    def faceTypes(self):
        #possible cloud formations
        return {
        1: "xxxx",
        2: "xxx",
        3: "x",
        4: "x\n x\n x\n x\n x",
        5: "xx",
        6: "x\nxxxx"        
        }
        
class rock1(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create rock images
        self.image = pygame.transform.scale(pygame.image.load
        ('images/rock1.png'),(30, 30))
        self.rect = self.image.get_rect()
        self.increase = 15

    def charge(self):
        self.rect.y += self.increase
        
class rock2(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create evil face image
        self.image = pygame.transform.scale(pygame.image.load
        ('images/rock2.png'),(30, 30))
        self.rect = self.image.get_rect()
        self.increase = 15

    def charge(self):
        self.rect.y += self.increase
        
class rock3(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create evil face image
        self.image = pygame.transform.scale(pygame.image.load
        ('images/rock3.png'),(30, 30))
        self.rect = self.image.get_rect()
        self.increase = 15

    def charge(self):
        self.rect.y += self.increase