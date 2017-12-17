#dog level
import pygame
import random
from sheep import Sheep
from poop_single import singlePoop
from dogCharacters import *
import mainPlay
import deathPage
import levelPage 

sheep = Sheep()
class dogPlay(object):

    def __init__(self,width=800, height=600, fps=50):
        self.width = width
        self.height = height
        self.fps = fps
        self.img_back = pygame.image.load('images/rothko_red.jpg')
        self.background = pygame.transform.scale(self.img_back, 
        (self.width, self.height))
        self.space = 20
        self.speedOffset = 4
        self.pause = False
        self.widthTitle= self.width/3+self.space
        self.scrollValue = self.width-(self.width/2.5)
        self.all_sprites_list = pygame.sprite.Group()
        self.sheep_dog_list = pygame.sprite.Group()
        self.poop_list = pygame.sprite.Group()
        self.poop_sheep_dog_list = pygame.sprite.Group()
        self.meats_list = pygame.sprite.Group()
        self.knife_list = pygame.sprite.Group()
        sheep.rect.x = self.width/4
        sheep.rect.y = self.height - (self.height/5)
        self.all_sprites_list.add(sheep)
        self.killSheep = 0
        self.levelUp = 18
        pygame.init()

    def timerFired(self,dt):
        if self.pause == False:
            #makes the sheep dogs, knives, poop move
            for sheepDogs in self.sheep_dog_list:
                sheepDogs.charge()
            for poop in self.poop_list:
                if poop.rect.x <= 0:
                    self.poop_list.remove(poop)
                    self.all_sprites_list.remove(poop)
                else:
                    poop.charge()
            for knife in self.knife_list:
                if knife.rect.y == self.height-self.space:
                    knife.rect.y = self.height-self.space
                else:
                    knife.charge()
             
    def update(self):
        
        def makeMeats(meatsForms,xLoc,yLoc,add=0):
            if len(meatsForms) == 0:
                print("a")
            elif meatsForms[0] == 'x':
                meat = meatSlab()
                meat.rect.x = xLoc+add
                meat.rect.y = yLoc
                self.meats_list.add(meat)
                self.all_sprites_list.add(meat)
                return makeMeats(meatsForms[1:],xLoc,yLoc,add+100)
            elif meatsForms[0] == '\n':
                return makeMeats(meatsForms[1:],xLoc,yLoc-50,add)
        
        #difficulty based on chosen option (see levels file)        
        factor = levelPage.levels().difficult()        
        if self.pause == False:
            #randomly makes meats
            if random.randint(0,120) < 1:
                numMeats = random.randint(1,6)
                meatsForms = meatSlab().slabTypes()[numMeats]
                xLoc = random.randint(self.width-self.space,self.width)
                yLoc = random.randint(self.height/2-self.space,self.height/2+self.space)
                makeMeats(meatsForms,xLoc,yLoc,add=0)    
            #randomly makes dog sheep
            if random.randint(0, (40*factor)) < 1:
                sheepDogs = sheepDog()
                randomLocation = random.randint(self.height//2, self.height-(self.height/4))
                sheepDogs.rect.x = 0
                sheepDogs.rect.y = randomLocation
                self.all_sprites_list.add(sheepDogs)    
                self.sheep_dog_list.add(sheepDogs) 
            #randomly makes falling knifes
            if random.randint(0, (120*factor)) < 1:
                knife = Choppy()
                randomLocation = random.randint(self.width//2, self.width)
                knife.rect.x = randomLocation
                knife.rect.y = 0
                self.all_sprites_list.add(knife)    
                self.knife_list.add(knife) 
                
            sheep.moveUp()
        
        #check for collisions between sheep and knives
        for i in self.knife_list:
            i = sheep.rect.colliderect(i)
            if i == True:
                self.manager.go_to(deathPage.death())
        #check for collisions between sheep and sheep dogs
        for j in self.sheep_dog_list:
            sheepDogHit = sheep.rect.colliderect(j)
            if sheepDogHit == True:
                self.manager.go_to(deathPage.death())
        #check for collisions between sheep dogs and poop
        for poop in self.poop_list:
            for scrap in self.sheep_dog_list:
                poopHit = scrap.rect.colliderect(poop)
                if poopHit == True:
                    pSD = poopSheepDog()
                    pSD.rect.x = scrap.rect.x
                    pSD.rect.y = scrap.rect.y - (1.5*self.space)
                    self.all_sprites_list.remove(scrap)
                    self.all_sprites_list.remove(poop)
                    self.sheep_dog_list.remove(scrap)
                    self.poop_list.remove(poop)
                    self.all_sprites_list.add(pSD)
                    self.poop_sheep_dog_list.add(pSD)
                    self.killSheep+=1
                    if self.killSheep == self.levelUp:
                        self.manager.go_to(mainPlay.mainPlay())
                        
        #check when sheep jumps on a meat slab
        for meats in self.meats_list:
            meatHit = sheep.rect.colliderect(meats)
            if meatHit == True:
                sheep.rect.y = meats.rect.y-(3*self.space)
                
        #scrolling (need to move everything also)
        if sheep.rect.right >= self.scrollValue:
            dx = sheep.rect.right - self.scrollValue
            sheep.rect.right = self.scrollValue
            for i in self.all_sprites_list:
                if i != sheep:
                    if i not in self.sheep_dog_list:
                        i.rect.x -= dx
                    else:
                        i.rect.x -= dx - self.speedOffset   
                         
    def keyPressed(self):
        #releases poop
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            if self.pause == False:
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
