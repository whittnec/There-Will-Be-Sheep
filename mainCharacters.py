#sprites for main part of game
import pygame

class Scrapie(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create scrapie sheep image
        self.image = pygame.transform.scale(pygame.image.load
        ('images/sheep_scrapie.png'),(100, 100))
        self.rect = self.image.get_rect()
        self.increase = 6

    def charge(self):
        self.rect.x += self.increase

class Butcher(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create butcher wolf image
        self.image = pygame.transform.scale(pygame.image.load
        ('images/wolf.png'),(100, 100))
        self.rect = self.image.get_rect()
        self.increase = 6

    def charge(self):
        self.rect.x -= self.increase

class Cloud(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create cloud image
        self.image = pygame.transform.scale(pygame.image.load
        ('images/wool.png'),(100, 100))
        self.rect = self.image.get_rect()

    def cloudTypes(self):
        #possible cloud formations
        return {
        1: "xxxx",
        2: "xxx\nxxxxx",
        3: 'xxx\n  xxxxx\n   xxxxxxx\n',
        4: "x",
        5: "x\n x\n x\n x\n x",
        6: "x\nx\nx\nx\n",
        7: "x\nx\nx\nx\nxxxxxxxx"        
        }

class Drop(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create scrapie sheep image
        self.image = pygame.transform.scale(pygame.image.load
        ('images/oil_dot.png'),(275, 100))
        self.rect = self.image.get_rect()
        self.increase = 3
        
    def charge(self):
        self.rect.x -= self.increase

class Pee(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create scrapie sheep image
        self.image = pygame.transform.scale(pygame.image.load
        ('images/piss.png'),(100, 30))
        self.rect = self.image.get_rect()
        self.increase = 3
        
    def charge(self):
        self.rect.x -= self.increase

class poopScrap(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create poop covered scrapie image
        self.image = pygame.transform.scale(pygame.image.load
        ('images/scrapie_poop.png'),(100, 100))
        self.rect = self.image.get_rect()
        
class stupidBird(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create knife images
        self.image = pygame.transform.scale(pygame.image.load
        ('images/bird.png'),(50, 50))
        self.rect = self.image.get_rect()
        self.increaseX = 20
        self.increaseY = 12
        self.maxY = 225
        self.state = "down"

    def charge(self):
        self.rect.x += self.increaseX
        if self.rect.y >= self.maxY:
            self.state = "up"
        if self.state == "down":
            self.rect.y += self.increaseY
        if self.state == "up":
            self.rect.y -= self.increaseY
    
    def stateDirection(self):
        return self.state

        
