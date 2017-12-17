#wood chipper level & characters
import pygame
import random
import levelPage 
import deathPage

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
        #adapted from: https://www.youtube.com/watch?v=LhL6V3zjLSg
        if self.moveY == 0:
            self.moveY = 1
        else:
            self.moveY += 0.2
            
        if ((self.rect.y >= 600 - self.rect.height) and (self.moveY >= 0)):
            self.moveY = 0
            self.rect.y = 600 - self.rect.height
            
    def moveUp(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= .8*self.moveRate
        elif key[pygame.K_RIGHT]:
            self.rect.x += .8*self.moveRate
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
        
class chipper(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create sheep image
        self.image = pygame.transform.scale(pygame.image.load
        ('images/wood.png'),(150, 200))
        self.rect = self.image.get_rect()
        
class whisp(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create sheep image
        self.image = pygame.transform.scale(pygame.image.load
        ('images/wind.png'),(80, 150))
        self.rect = self.image.get_rect()
        
class blood1(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create sheep image
        self.image = pygame.transform.scale(pygame.image.load
        ('images/bloodsq.png'),(40, 40))
        self.rect = self.image.get_rect()
        
class blood2(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create sheep image
        self.image = pygame.transform.scale(pygame.image.load
        ('images/bloodsqirt2.png'),(40, 40))
        self.rect = self.image.get_rect()


sheep = Sheep()
class woodChipper(object):
    
    def __init__(self,width=800, height=600, fps=50):
        self.width = width
        self.height = height
        self.fps = fps
        self.img_back = pygame.image.load('images/background.jpg')
        self.background = pygame.transform.scale(self.img_back, 
        (self.width, self.height))
        self.space = 20
        self.time = 0
        self.interval = 100
        self.up1 = 0
        self.up2 = 0
        self.toKill = False
        #pause stuff
        self.pause = False
        self.widthTitle= self.width/3+self.space
        self.all_sprites_list = pygame.sprite.Group()
        self.chippers_list = pygame.sprite.Group()
        self.wind_list = pygame.sprite.Group()
        sheep.rect.x = self.width/3
        sheep.rect.y = 0
        self.all_sprites_list.add(sheep)
        
        #make the wood chippers
        x=25
        for i in range(5):
            chip = chipper()
            chip.rect.x = x
            chip.rect.y = 400
            self.all_sprites_list.add(chip) 
            self.chippers_list.add(chip)
            x+=150
        pygame.init()

    def timerFired(self,dt):
        pass

    def update(self):
        #go back to you're dead page
        if self.toKill == True:
            pygame.time.delay(100)
            self.manager.go_to(deathPage.death())
        #counter for when to switch wind area
        self.time +=1
        
        #change position of up wind at given interval
        if self.time % self.interval ==0 or self.time==20:
            #get rid of previous wind drawing
            for i in self.all_sprites_list:
                if i in self.wind_list:
                    self.wind_list.remove(i)
                    self.all_sprites_list.remove(i)
            #choose random area that blows up
            rand = random.randint(1,5)
            self.up1 = (rand-1)*160
            self.up2 = rand*160
            blow = whisp()
            blow.rect.y = self.height//2
            blow.rect.x = ((self.up1 + self.up2)/2) -50
            self.all_sprites_list.add(blow)
            self.wind_list.add(blow)
        
        #let sheep smoothly move
        sheep.moveUp()
        #controls movement based on where sheep is
        if self.up1<=sheep.rect.x<=self.up2:
            sheep.moveY -=.45
        if sheep.rect.y<=0:
            sheep.rect.y+=10
        
        #check for collisions between sheep and wood chippers
        for chipping in self.chippers_list:
            if sheep.rect.colliderect(chipping) == True:
                #chainsaw noise
                sound = pygame.mixer.Sound("music/chop.ogg")
                sound.play(loops = 0)
                sound.set_volume(0.5)
                start = 10
                for i in range (10):
                    first = blood1()
                    first.rect.x = sheep.rect.x - start
                    first.rect.y = sheep.rect.y
                    self.all_sprites_list.add(first)
                    start-=10
                otherStart = 0
                for j in range(10):
                    second = blood2()
                    second.rect.x = sheep.rect.x + otherStart
                    second.rect.y = sheep.rect.y
                    self.all_sprites_list.add(second)
                    otherStart+=10
                self.toKill=True
                

    def keyPressed(self):
        #pauses
        key = pygame.key.get_pressed()
        if key[pygame.K_p]:
            self.pause = True
        elif key[pygame.K_u]:
            self.pause = False 
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.keyPressed()

    def render(self,screen):
        screen.blit(self.background,(0,0))
        self.all_sprites_list.draw(screen)
        font = pygame.font.Font("Acme-Regular.ttf", 25)
        paused = font.render("Press 'P' to pause",3,(0,0,0))
        unpaused = font.render("Press 'U' to unpause",3,(0,0,0))
        screen.blit(paused, (20, 10))
        screen.blit(unpaused, (20,35))
        if self.pause == True:
            header = pygame.font.Font("Acme-Regular.ttf", 60)
            title = header.render('PAUSED',3,(0,0,0))
            screen.blit(title, (self.widthTitle, self.height/5))
        elif self.pause == False:
            self.all_sprites_list.update() 

            