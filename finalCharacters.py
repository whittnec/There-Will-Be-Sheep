#sprites for semi final
import pygame

class straightSheep(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create scrapie sheep image
        self.sizeX=150
        self.sizeY=150
        self.image = pygame.transform.scale(pygame.image.load
        ('images/finalSheep.png'),(self.sizeX, self.sizeY))
        self.rect = self.image.get_rect()
        self.increaseX= 8
        
    def charge(self):
        self.rect.x += self.increaseX
        
class redSheep(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create scrapie sheep image
        self.sizeX=150
        self.sizeY=150
        self.image = pygame.transform.scale(pygame.image.load
        ('images/finalSheep.png'),(self.sizeX, self.sizeY))
        self.rect = self.image.get_rect()
        self.maxY = 450
        self.minY = 10
        self.increaseY = 8
        self.increaseX= 1
        self.state = "down"

    def chargeDirection(self):
        if self.rect.y <= self.minY:
            self.state = "down"
        elif self.rect.y >= self.maxY:
            self.state = "up"
        self.charge()
        
    def charge(self):
        self.rect.x += self.increaseX
        if self.state == "up":
            self.rect.y-=self.increaseY
        if self.state == "down":
            self.rect.y+=self.increaseY
        
class smallSheep(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create scrapie sheep image
        self.sizeX=60
        self.sizeY=60
        self.image = pygame.transform.scale(pygame.image.load
        ('images/finalSheep.png'),(self.sizeX, self.sizeY))
        self.rect = self.image.get_rect()
        self.increaseX= 10
        
    def charge(self):
        self.rect.x += self.increaseX
        
class hugeSheep(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create scrapie sheep image
        self.sizeX=275
        self.sizeY=275
        self.image = pygame.transform.scale(pygame.image.load
        ('images/finalSheep.png'),(self.sizeX, self.sizeY))
        self.rect = self.image.get_rect()
        self.increaseX= 1
        self.state = "up"

    def chargeDirection(self):
        if self.rect.y <= self.minY:
            self.state = "down"
        if self.rect.y >= self.maxY:
            self.state = "up"
        self.charge()
        
    def charge(self):
        self.rect.x += self.increaseX
        
class singlePoop(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create poop image
        self.image = pygame.transform.scale(pygame.image.load
        ('images/poop_single.png'),(70, 70))
        self.rect = self.image.get_rect()
        self.increase = 30
    
    def charge(self):
        self.rect.x -= self.increase
        
class flySheep(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create sheep image
        self.image = pygame.transform.scale(pygame.image.load
        ('images/angel.png'),(120, 120))
        self.rect = self.image.get_rect()
        # self.moveY = 0
        # self.moveX = 0
        self.moveRate = 14
            
    def moveUp(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= self.moveRate
        elif key[pygame.K_RIGHT]:
            self.rect.x += self.moveRate
        elif key[pygame.K_UP]:    
            self.rect.y -= self.moveRate
        elif key[pygame.K_DOWN]:    
            self.rect.y += self.moveRate
            
class fractalSheep(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create scrapie sheep image
        self.sizeX=275
        self.sizeY=275
        self.image = pygame.transform.scale(pygame.image.load
        ('images/finalSheep.png'),(self.sizeX, self.sizeY))
        self.rect = self.image.get_rect()
        self.increaseX= 8
        
    def charge(self):
        self.rect.x += self.increaseX
