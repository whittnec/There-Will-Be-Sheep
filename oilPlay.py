#oil level of game
import pygame
import random

from sheep import Sheep
from poop_single import singlePoop
from oilCharacters import *
import mainPlay
import deathPage
import levelPage 

sheep = Sheep()
class oilPlay(object):
    
    #rock types
    rockTypes = [rock1(),rock2(),rock3()]

    def __init__(self,width=800, height=600, fps=50):
        self.width = width
        self.height = height
        self.fps = fps
        self.img_back = pygame.image.load('images/rothko_black.jpg')
        self.background = pygame.transform.scale(self.img_back, 
        (self.width, self.height))
        self.space = 20
        self.speedOffset = 4
        self.pause = False
        self.widthTitle= self.width/3+self.space
        self.scrollValue = self.width-(self.width/2.5)
        self.all_sprites_list = pygame.sprite.Group()
        self.oilScrapie_list = pygame.sprite.Group()
        self.poop_list = pygame.sprite.Group()
        self.oilPoopScrap_list = pygame.sprite.Group()
        self.face_list = pygame.sprite.Group()
        self.rocks_list = pygame.sprite.Group()
        self.fire_list = pygame.sprite.Group()
        sheep.rect.x = self.width/4
        sheep.rect.y = self.height - (self.height/5)
        self.all_sprites_list.add(sheep)
        self.killSheep = 0
        self.levelUp = 18
        pygame.init()

    def timerFired(self,dt):
        if self.pause == False:
            #makes the oilScrapie sheep, rocks, poop move
            for oilScraps in self.oilScrapie_list:
                oilScraps.charge()
            for poop in self.poop_list:
                if poop.rect.x <= 0:
                    self.poop_list.remove(poop)
                    self.all_sprites_list.remove(poop)
                else:
                    poop.charge()
            for rock in self.rocks_list:
                if rock.rect.y == self.height-self.space:
                    rock.rect.y = self.height-self.space
                else:
                    rock.charge()
                
    def keyReleased(self):
        pass
             
    def update(self):
        
        def makeFaces(facesForm,xLoc,yLoc,add=0):
            if len(facesForm) == 0:
                print("a")
            elif facesForm[0] == 'x':
                face = evil()
                face.rect.x = xLoc+add
                face.rect.y = yLoc
                self.face_list.add(face)
                self.all_sprites_list.add(face)
                return makeFaces(facesForm[1:],xLoc,yLoc,add+100)
            elif facesForm[0] == '\n':
                return makeFaces(facesForm[1:],xLoc,yLoc-50,add)
                
        #difficulty based on chosen option (see levels file)        
        factor = levelPage.levels().difficult()
        if self.pause == False:
            #randomly makes evil faces
            if random.randint(0,150) == 0:
                numFaces = random.randint(1,6)
                facesForm = evil().faceTypes()[numFaces]
                xLoc = random.randint(self.width-self.space,self.width)
                yLoc = random.randint(self.height/3,self.height/2+self.space)
                makeFaces(facesForm,xLoc,yLoc,add=0)
            #randomly makes fire 
            if random.randint(0, (130*factor)) == 0:
                fire = firePic()
                fire.rect.x = self.width - self.space
                fire.rect.y = self.height - (self.height/8)
                self.all_sprites_list.add(fire)    
                self.fire_list.add(fire)     
            #randomly makes oilScrapie sheep
            if random.randint(0, (50*factor)) == 0:
                oilScraps = oilScrapie()
                oilScraps.rect.x = 0
                oilScraps.rect.y = self.height - (self.height/3)
                self.all_sprites_list.add(oilScraps)    
                self.oilScrapie_list.add(oilScraps) 
            #randomly makes falling rocks
            if random.randint(0, (110*factor)) == 0:
                randomLocation = random.randint(self.width//2, self.width)
                randomRockNum = random.randint(0, 2) 
                selectedRock = self.rockTypes[randomRockNum]
                selectedRock.rect.x = randomLocation
                selectedRock.rect.y = 0
                self.all_sprites_list.add(selectedRock)    
                self.rocks_list.add(selectedRock) 
                
            sheep.moveUp()
        
        #check for collisions between sheep and rocks
        for i in self.rocks_list:
            i = sheep.rect.colliderect(i)
            if i == True:
                self.manager.go_to(deathPage.death())
        #check for collisions between sheep and oilScrapie
        for j in self.oilScrapie_list:
            oilScrapieHit = sheep.rect.colliderect(j)
            if oilScrapieHit == True:
                self.manager.go_to(deathPage.death())
        #check for collisions between sheep and fire
        for k in self.fire_list:
            k = sheep.rect.colliderect(k)
            if k == True:
                self.manager.go_to(deathPage.death())
        #check for collisions b/t oilScrapie and poop & replace w/ poop sheep
        for poop in self.poop_list:
            for scrap in self.oilScrapie_list:
                poopHit = scrap.rect.colliderect(poop)
                if poopHit == True:
                    poopoilScrapie = oilPoopScrap()
                    poopoilScrapie.rect.x = scrap.rect.x
                    poopoilScrapie.rect.y = scrap.rect.y - (1.5*self.space)
                    self.all_sprites_list.remove(scrap)
                    self.all_sprites_list.remove(poop)
                    self.oilScrapie_list.remove(scrap)
                    self.poop_list.remove(poop)
                    self.all_sprites_list.add(poopoilScrapie)
                    self.oilPoopScrap_list.add(poopoilScrapie)
                    self.killSheep+=1
                    if self.killSheep == self.levelUp:
                        self.manager.go_to(mainPlay.mainPlay())
        #check when sheep jumps on a face
        for faces in self.face_list:
            faceHit = sheep.rect.colliderect(faces)
            if faceHit == True:
                sheep.rect.y = faces.rect.y-(3*self.space)
                
        #scrolling (need to move everything also)
        if sheep.rect.right >= self.scrollValue:
            dx = sheep.rect.right - self.scrollValue
            sheep.rect.right = self.scrollValue
            for i in self.all_sprites_list:
                if i != sheep:
                    if i not in self.oilScrapie_list:
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
        paused = font.render("Press 'P' to pause",3,(255,255,255))
        unpaused = font.render("Press 'U' to unpause",3,(255,255,255))
        screen.blit(paused, (20, 10))
        screen.blit(unpaused, (20,35))
        if self.pause == True:
            header = pygame.font.Font("Acme-Regular.ttf", 60)
            title = header.render('PAUSED',3,(255,255,255))
            screen.blit(title, (self.widthTitle, self.height/5))
        elif self.pause == False:
            self.all_sprites_list.update() 

