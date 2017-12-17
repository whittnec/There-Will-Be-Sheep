#sprites for maze part of game
import pygame 
class sheepBread(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create sheep image
        self.image = pygame.transform.scale(pygame.image.load
        ('images/angel.png'),(25, 25))
        self.rect = self.image.get_rect()
        self.moveRate = 10
            
    def moveUp(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.rect.x += self.moveRate
        elif key[pygame.K_UP]:    
            self.rect.y -= self.moveRate
        elif key[pygame.K_DOWN]:    
            self.rect.y += self.moveRate
        elif key[pygame.K_LEFT]:    
            self.rect.x -= self.moveRate

class redSheep(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create scrapie sheep image
        self.sizeX=60
        self.sizeY=60
        self.image = pygame.transform.scale(pygame.image.load
        ('images/finalSheep.png'),(self.sizeX, self.sizeY))
        self.rect = self.image.get_rect()
        self.maxY = 550
        self.minY = 10
        self.increaseY = 15
        self.state = "down"

    def chargeDirection(self):
        if self.rect.y <= self.minY:
            self.state = "down"
        elif self.rect.y >= self.maxY:
            self.state = "up"
        self.charge()
        
    def charge(self):
        if self.state == "up":
            self.rect.y-=self.increaseY
        if self.state == "down":
            self.rect.y+=self.increaseY

class hBone(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create vertical bone image
        self.hBone = pygame.transform.scale(pygame.image.load
        ('images/bone.png'),(50, 30))
        self.image = pygame.transform.rotate(self.hBone,90)
        self.rect = self.image.get_rect()
        
class vBone(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create horizontal bone image
        self.image = pygame.transform.scale(pygame.image.load
        ('images/bone.png'),(50, 30))
        self.rect = self.image.get_rect()