import pygame

class Sheep(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create sheep image
        self.image = pygame.transform.scale(pygame.image.load
        ('images/sheep_normal.png'),(100, 100))
        self.rect = self.image.get_rect()
        self.moveY = 0
        self.moveX = 0
        self.moveRate = 10
        
    def gravity(self):
        #gravity stuff from here: https://www.youtube.com/watch?v=LhL6V3zjLSg
        if self.moveY == 0:
            self.moveY = 1
        else:
            self.moveY += 0.3
            
        if ((self.rect.y >= 600 - self.rect.height) and (self.moveY >= 0)):
            self.moveY = 0
            self.rect.y = 600 - self.rect.height
            
    def jump(self):
        self.rect.y += self.moveRate
        self.rect.y -= self.moveRate
 
        if self.rect.bottom >= 600:
            self.moveY = -(self.moveRate)
            
    def moveUp(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= .8*self.moveRate
        elif key[pygame.K_RIGHT]:
            self.rect.x += .8*self.moveRate
        elif key[pygame.K_UP]:    
            self.jump()
        elif key[pygame.K_DOWN]:    
            self.rect.y += self.moveRate
        elif key[pygame.K_LEFT] and self.moveX < 0:
            self.moveX = 0
        elif key[pygame.K_RIGHT] and self.moveX > 0:
            self.moveX = 0
    
    def update(self):
        self.gravity()
        self.rect.x += self.moveX
        self.rect.y += self.moveY
