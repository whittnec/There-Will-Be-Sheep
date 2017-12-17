#ending scene
import pygame 
import random
from sheep import Sheep 
import mainCharacters
import finalCharacters
import dogCharacters
import oilCharacters
import pissCharacters
import returnHome
#from weather import temperature

sheep = Sheep()
class endingOde(object):

    def __init__(self, width=800, height=600, fps=50):
        self.width = width
        self.height = height
        self.fps = fps
        #images
        #self.pic = temperature()
        self.background = pygame.transform.scale(pygame.image.load
        ('images/background.jpg'),(self.width, self.height))
        sheep.rect.x = 0
        sheep.rect.y = self.height - (self.height/5)
        self.all_sprites_list = pygame.sprite.Group()
        self.all_sprites_list.add(sheep)
        #dimension specifications
        self.space = 20
        self.buffer = 80
        self.letterSpace = 40
        self.widthTitle= self.width/15
        self.increase = 1
        self.num = 4
        self.tick = 0
        self.timeUp=100
        self.y = -150
        pygame.init()
        pygame.mixer.music.load('music/ode.ogg')
        pygame.mixer.music.play(5)
        pygame.mixer.music.set_volume(0.5)

    def timerFired(self,dt):
        for i in self.all_sprites_list:
            if i == sheep:
                if sheep.rect.x<=self.width/2.3:
                    sheep.rect.x+=6
                else: 
                    sheep.rect.x+=0
            else:
                i.rect.y += self.increase

    def update(self):
        self.tick+=1
        
        if self.tick>=320 and self.tick%80==0:
            sSheep=finalCharacters.straightSheep()
            sSheep.rect.x=random.randint(10,self.width-100)
            sSheep.rect.y=self.y
            self.all_sprites_list.add(sSheep)
        if self.tick>=200 and self.tick%40==0:
            for k in range(self.num):
                rSheep=mainCharacters.Scrapie()
                rSheep.rect.x=random.randint(10,self.width-100)
                rSheep.rect.y=self.y
                self.all_sprites_list.add(rSheep)
        if self.tick>=250 and self.tick%50==0:
            for j in range(self.num):
                wolf=mainCharacters.Butcher()
                wolf.rect.x=random.randint(10,self.width-100)
                wolf.rect.y=self.y
                self.all_sprites_list.add(wolf)
        if self.tick>=280 and self.tick%40==0:  
            for n in range(self.num):
                pee=pissCharacters.peeScrapie()
                pee.rect.x=random.randint(10,self.width-100)
                pee.rect.y=self.y
                self.all_sprites_list.add(pee)
            for l in range(self.num):
                dog=dogCharacters.sheepDog()
                dog.rect.x=random.randint(10,self.width-100)
                dog.rect.y=self.y
                self.all_sprites_list.add(dog)
        if self.tick>=350 and self.tick%70==0:
            for m in range(2):
                oil=oilCharacters.oilScrapie()
                oil.rect.x=random.randint(10,self.width-100)
                oil.rect.y=self.y
                self.all_sprites_list.add(oil)
                 
        for item in self.all_sprites_list:
            if sheep.rect.colliderect(item) and item != sheep:
                self.manager.go_to(returnHome.returning())
            

    def handle_events(self):
        pass
            
    def render(self,screen):
        screen.blit(self.background,(0,0))
        self.all_sprites_list.update() 
        self.all_sprites_list.draw(screen)
