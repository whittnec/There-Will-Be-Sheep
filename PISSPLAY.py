#pee level of game
import pygame
import random

from sheep import Sheep
from pissCharacters import *
import mainPlay
import deathPage
import levelPage 

sheep = Sheep()
class pissPlay(object):
    
    def __init__(self,width=800, height=600, fps=50):
        self.width = width
        self.height = height
        self.fps = fps
        self.img_back = pygame.image.load('images/rothko_yellow.jpg')
        self.background = pygame.transform.scale(self.img_back, 
        (self.width, self.height))
        self.space = 20
        self.speedOffset = 4
        self.pause = False
        self.widthTitle= self.width/3+self.space
        self.scrollValue = self.width-(self.width/2.5)
        self.all_sprites_list = pygame.sprite.Group()
        self.peeScrap_list = pygame.sprite.Group()
        self.poop_list = pygame.sprite.Group()
        self.poopPeeScrap_list = pygame.sprite.Group()
        self.blood_list = pygame.sprite.Group()
        self.flagella_list=pygame.sprite.Group()
        sheep.rect.x = self.width/4
        sheep.rect.y = self.height - (self.height/5)
        self.all_sprites_list.add(sheep)
        self.killSheep = 0
        self.levelUp = 18
        pygame.init()

    def timerFired(self,dt):
        if self.pause == False:
            #makes the scrapie sheep, poop, flagella move
            for scraps in self.peeScrap_list:
                scraps.charge()
            for poop in self.poop_list:
                if poop.rect.x <= 0:
                    self.poop_list.remove(poop)
                    self.all_sprites_list.remove(poop)
                else:
                    poop.charge()
            for fla in self.flagella_list:
                fla.charge()
             
    def update(self):
        
        def makeBlood(bloodForm,xLoc,yLoc,add=0):
            if len(bloodForm) == 0:
                print("a")
            elif bloodForm[0] == 'x':
                blood = normCell()
                blood.rect.x = xLoc+add
                blood.rect.y = yLoc
                self.blood_list.add(blood)
                self.all_sprites_list.add(blood)
                return makeBlood(bloodForm[1:],xLoc,yLoc,add+100)
            elif bloodForm[0] == '\n':
                return makeBlood(bloodForm[1:],xLoc,yLoc-50,add)
        
        factor = levelPage.levels().difficult()
        if self.pause == False:
            #randomly makes blood droplets
            if random.randint(0,100) == 0:
                numBlood = random.randint(1,6)
                bloodForm = normCell().bloodTypes()[numBlood]
                xLoc = random.randint(self.width-self.space,self.width)
                yLoc = random.randint(self.height/2-self.space,self.height/2+self.space)
                makeBlood(bloodForm,xLoc,yLoc,add=0)
            #randomly make flagella fall
            if random.randint(0, (80*factor)) == 0:
                flagella = fallingFlagella()
                randLocation = random.randint(self.width/2,self.width)
                flagella.rect.x = randLocation
                flagella.rect.y = self.space
                self.all_sprites_list.add(flagella)  
                self.flagella_list.add(flagella)
            #randomly makes scrapie sheep
            if random.randint(0, (60*factor)) == 0:
                randLocation = random.randint(self.width/2,self.height-2.5*self.space)
                pScrapie = peeScrapie()
                pScrapie.rect.x = 0
                pScrapie.rect.y = randLocation
                self.all_sprites_list.add(pScrapie)    
                self.peeScrap_list.add(pScrapie) 
                
            sheep.moveUp()


        #check for collisions between sheep and flagella
        for i in self.flagella_list:
            flaHit = sheep.rect.colliderect(i)
            if flaHit == True:
                self.manager.go_to(deathPage.death())
        #check for collisions between sheep and scrapie
        for i in self.peeScrap_list:
            scrapieHit = sheep.rect.colliderect(i)
            if scrapieHit == True:
                self.manager.go_to(deathPage.death())
        #check for collisions between scrapie and poop
        for poop in self.poop_list:
            for pScrap in self.peeScrap_list:
                poopHit = pScrap.rect.colliderect(poop)
                if poopHit == True:
                    poopPeeScraps = poopPeeScrapie()
                    poopPeeScraps.rect.x = pScrap.rect.x
                    poopPeeScraps.rect.y = pScrap.rect.y -(1.2*self.space)
                    self.all_sprites_list.remove(pScrap)
                    self.all_sprites_list.remove(poop)
                    self.peeScrap_list.remove(pScrap)
                    self.poop_list.remove(poop)
                    self.all_sprites_list.add(poopPeeScraps)
                    self.poopPeeScrap_list.add(poopPeeScraps)
                    self.killSheep+=1
                    if self.killSheep == self.levelUp:
                        self.manager.go_to(mainPlay.mainPlay())
        #check when sheep jumps on blood
        for blood in self.blood_list:
            bloodHit = sheep.rect.colliderect(blood)
            if bloodHit == True:
                sheep.rect.y = blood.rect.y-(3*self.space)
                
        #scrolling (need to move everything also)
        if sheep.rect.right >= self.scrollValue:
            dx = sheep.rect.right - self.scrollValue
            sheep.rect.right = self.scrollValue
            for i in self.all_sprites_list:
                if i != sheep:
                    if i not in self.peeScrap_list:
                        i.rect.x -= dx
                    else:
                        i.rect.x -= dx - self.speedOffset   
                         
    def keyPressed(self):
        #releases poop
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            if self.pause == False:
                singlePoopy = smallPoop()
                singlePoopy.rect.x = sheep.rect.x - self.space
                singlePoopy.rect.y = sheep.rect.y + self.space
                self.all_sprites_list.add(singlePoopy)
                self.poop_list.add(singlePoopy)
        elif key[pygame.K_p]:
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

