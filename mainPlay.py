#main part of game
import pygame
import random
import levelPage 
from sheep import Sheep
from poop_single import singlePoop
from mainCharacters import *
import oilPlayExplanation
import dogPlayExplanation 
import pissPlayExplanation
from finaleTransition import finalTransition
import instructionsFinal
from finale import final
import deathPage

sheep = Sheep()
class mainPlay(object):
    
    def __init__(self,width=800, height=600, fps=50):
        self.width = width
        self.height = height
        self.fps = fps
        self.img_back = pygame.image.load('images/background.jpg')
        self.background = pygame.transform.scale(self.img_back, 
        (self.width, self.height))
        #helps with scrolling
        self.space = 20
        self.speedOffset = 4
        self.scrollValue = self.width-(self.width/2.5)
        #pause stuff
        self.pause = False
        self.widthTitle= self.width/3+self.space
        #keep track of all the sprites
        self.all_sprites_list = pygame.sprite.Group()
        self.scrapie_list = pygame.sprite.Group()
        self.butcher_list = pygame.sprite.Group()
        self.poop_list = pygame.sprite.Group()
        self.poopScrap_list = pygame.sprite.Group()
        self.clouds_list = pygame.sprite.Group()
        self.oilDrop_list=pygame.sprite.Group()
        self.pee_list=pygame.sprite.Group()
        self.bird_list = pygame.sprite.Group()
        sheep.rect.x = self.width/4
        sheep.rect.y = self.height - (self.height/5)
        self.all_sprites_list.add(sheep)
        #how many times sheep hits bird&how thick the cover is
        self.coverNum = 0
        self.birdRemove = -50
        #keeps track of how many sheep killed
        self.sheepKill = 0
        #once 18 sheep killed, can go to finale
        self.levelUp = 18
        pygame.init()
        pygame.mixer.music.load('music/shaunSheep.ogg')
        pygame.mixer.music.play(5)
        pygame.mixer.music.set_volume(0.5)

    def timerFired(self,dt):
        if self.pause == False:
            #makes the scrapie sheep, butcher, poop, oil, pee, bird move
            for scraps in self.scrapie_list:
                scraps.charge()
            for butcher in self.butcher_list:
                butcher.charge() 
            for oil in self.oilDrop_list:
                oil.charge()
            for pee in self.pee_list:
                pee.charge()
            #make sure poops from previous keyPresses don't come back
            for poop in self.poop_list:
                if poop.rect.x <= 0:
                    self.poop_list.remove(poop)
                    self.all_sprites_list.remove(poop)
                else:
                    poop.charge()
            #make sure birds from previous times don't come back
            for birdy in self.bird_list:
                if birdy.stateDirection() == "up" and birdy.rect.y<=self.birdRemove:
                    self.all_sprites_list.add(birdy)
                    self.bird_list.remove(birdy)
                else:
                    birdy.charge()


    def update(self):
        #makes clouds based on patterns in mainCharacters file
        def makeClouds(cloudForm,xLoc,yLoc,add=0):
            if len(cloudForm) == 0:
                print("a")
            elif cloudForm[0] == 'x':
                cloud = Cloud()
                cloud.rect.x = xLoc+add
                cloud.rect.y = yLoc
                self.clouds_list.add(cloud)
                self.all_sprites_list.add(cloud)
                return makeClouds(cloudForm[1:],xLoc,yLoc,add+100)
            elif cloudForm[0] == '\n':
                return makeClouds(cloudForm[1:],xLoc,yLoc-50,add)
        #difficulty based on chosen option (see levels file)        
        factor = levelPage.levels().difficult()
        #randomly makes clouds
        if self.pause == False:    
            if random.randint(0,(120)) == 0:
                numClouds = random.randint(1,7)
                cloudForm = Cloud().cloudTypes()[numClouds]
                xLoc = random.randint(self.width-self.space,self.width)
                yLoc = random.randint(self.height/2-self.space,
                                        self.height/2+self.space)
                makeClouds(cloudForm,xLoc,yLoc,add=0)
            #randomly make oil spots
            if random.randint(0, (240*factor)) == 0:
                oilSpot = Drop()
                oilSpot.rect.x = self.width -(self.width/10)
                oilSpot.rect.y = self.height - (self.height/10)
                self.all_sprites_list.add(oilSpot)  
                self.oilDrop_list.add(oilSpot)
            #randomly make pee spots
            if random.randint(0, (300*factor)) == 0:
                pee = Pee()
                pee.rect.x = self.width -(self.width/10)
                pee.rect.y = self.height-self.space
                self.all_sprites_list.add(pee)  
                self.pee_list.add(pee)
            #randomly makes scrapie sheep
            if random.randint(0, (70*factor)) == 0:
                scrapie = Scrapie()
                scrapie.rect.x = 0
                scrapie.rect.y = self.height - (self.height/6)
                self.all_sprites_list.add(scrapie)    
                self.scrapie_list.add(scrapie) 
            #randomly makes butchers
            if random.randint(0, (180*factor)) == 0:
                butcher = Butcher()
                butcher.rect.x = self.width
                butcher.rect.y = self.height - (self.height/6)
                self.all_sprites_list.add(butcher)    
                self.butcher_list.add(butcher) 
            #randomly makes bird
            if random.randint(0, (250*factor)) == 0:
                bird = stupidBird()
                bird.rect.x = self.width/6
                bird.rect.y = 0
                self.all_sprites_list.add(bird)    
                self.bird_list.add(bird) 
    
            #let sheep smoothly move
            sheep.moveUp()
        
            #check for collisions between sheep and butcher
            for butchers in self.butcher_list:
                butcherHit = sheep.rect.colliderect(butchers)
                if butcherHit == True:
                    self.manager.go_to(dogPlayExplanation.dogPlayExplanation())
            #check for collisions between sheep and pee pools
            for pee in self.pee_list:
                peeHit = sheep.rect.colliderect(pee)
                if peeHit == True:
                    self.manager.go_to(pissPlayExplanation.pissPlayExplanation())
            #check for collisions between sheep and oil pools
            for oils in self.oilDrop_list:
                oilHit = sheep.rect.colliderect(oils)
                if oilHit == True:
                    self.manager.go_to(oilPlayExplanation.oilPlayExplanation())        
            #check for collisions between scrapie and poop
            for poop in self.poop_list:
                for scrap in self.scrapie_list:
                    poopHit = scrap.rect.colliderect(poop)
                    if poopHit == True:
                        poopScrapie = poopScrap()
                        poopScrapie.rect.x = scrap.rect.x
                        poopScrapie.rect.y = scrap.rect.y
                        self.all_sprites_list.remove(scrap)
                        self.all_sprites_list.remove(poop)
                        self.scrapie_list.remove(scrap)
                        self.poop_list.remove(poop)
                        self.all_sprites_list.add(poopScrapie)
                        self.poopScrap_list.add(poopScrapie)
                        self.sheepKill+=1
                        if self.sheepKill==self.levelUp:
                            self.manager.go_to(finalTransition())
            #check for collisions b/t sheep and bird-->increase difficulty to see
            for birdy in self.bird_list:
                birdHit = sheep.rect.colliderect(birdy)
                if birdHit == True:
                    self.coverNum += 1
            #check when sheep jumps on a cloud
            for clouds in self.clouds_list:
                cloudHit = sheep.rect.colliderect(clouds)
                if cloudHit == True:
                    sheep.rect.y = clouds.rect.y-(3*self.space)
        #check for collisions between sheep and scrapie
        for scraps in self.scrapie_list:
            scrapieHit = sheep.rect.colliderect(scraps)
            if scrapieHit == True:
                self.manager.go_to(deathPage.death())
        #scrolling (need to move everything also)
        if sheep.rect.right >= self.scrollValue:
            dx = sheep.rect.right - self.scrollValue
            sheep.rect.right = self.scrollValue
            for i in self.all_sprites_list:
                if i != sheep:
                    if i not in self.scrapie_list:
                        i.rect.x -= dx
                    else:
                        i.rect.x -= dx - self.speedOffset   

    def keyPressed(self):
        #releases poop on space
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            if self.pause==False:
                singlePoopy = singlePoop()
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
        #if hit by bird, make screen harder to see (add translucent cover)
        cover = pygame.Surface(screen.get_size()).convert()
        cover.fill((255, 255, 255))
        cover.set_alpha(5*self.coverNum)
        screen.blit(cover,(0,0))
            

