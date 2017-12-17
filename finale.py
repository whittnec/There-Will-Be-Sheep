#semi final level
import pygame
import random

from finalCharacters import *
import deathPage
import couponsInstructions


sheep = flySheep()
    
class final(object):
    
    direction = ['top','left']

    def __init__(self, width=800, height=600, fps=50):
        self.width = width
        self.height = height
        self.fps = fps
        self.img_back = pygame.image.load('images/background.jpg')
        self.background = pygame.transform.scale(self.img_back, 
        (self.width, self.height))
        self.space = 20
        self.all_sprites_list = pygame.sprite.Group()
        self.poop_list = pygame.sprite.Group()
        self.redSheep_list = pygame.sprite.Group()
        self.straightSheep_list = pygame.sprite.Group()
        self.smSheep = pygame.sprite.Group()
        sheep.rect.x = self.width - (self.width/5)
        sheep.rect.y = self.height - (self.height/5)
        self.all_sprites_list.add(sheep)
        self.numSheep = 18
        self.numKill = 0 
        pygame.init()

    def timerFired(self,dt):
        #makes the red sheep and poop move
        for poop in self.poop_list:
            if poop.rect.x <= 0:
                self.poop_list.remove(poop)
                self.all_sprites_list.remove(poop)
            else:
                poop.charge()
        for straight in self.straightSheep_list:
            straight.charge()
        for redSheep in self.redSheep_list:
            redSheep.chargeDirection()
        for sm in self.smSheep:
            sm.charge()
             
    def update(self):
        #randomly create red sheep (coming from different parts of screen)
        if random.randint(0,60) == 0:
            enter = self.direction[random.randint(0,1)]
            if enter == 'left':
                redSheepy = straightSheep() 
                redSheepy.rect.x = 30
                redSheepy.rect.y = random.randint(self.height//2,
                                    self.height-(self.height//3))
                self.straightSheep_list.add(redSheepy)
                self.all_sprites_list.add(redSheepy)  
            elif enter == 'top':
                redSheeps = redSheep()
                redSheeps.rect.x = random.randint(0,self.width//2-180)
                redSheeps.rect.y = self.height/3
                self.redSheep_list.add(redSheeps)
                self.all_sprites_list.add(redSheeps)  
                    
        #let sheep move anywhere but not out of screen
        sheep.moveUp()
        if sheep.rect.y>=self.height-(5*self.space):
            sheep.rect.y=self.height-(5*self.space)
        elif sheep.rect.y<=0:
            sheep.rect.y = self.space
        elif sheep.rect.x>=self.width-(4*self.space):
            sheep.rect.x = self.width-(4*self.space)
            
        #recursively make the smaller sheep on collision
        def makeSmall(x,y,n):
            if n == 4:
                print('stop')
            else:
                small = smallSheep()
                small.rect.x=x-80
                small.rect.y=y-120
                makeSmall(x,y+60,n+1)
                self.smSheep.add(small)
                self.all_sprites_list.add(small)
                
        #check for red sheep and poop collisions
        for i in self.all_sprites_list:
            for j in self.poop_list:
                sheepHit = j.rect.colliderect(i)
                if i in self.redSheep_list or i in self.straightSheep_list:
                    if sheepHit == True:
                        makeSmall(i.rect.x,i.rect.y,0)
                        self.all_sprites_list.remove(i)
                        self.poop_list.remove(j)
                        self.all_sprites_list.remove(j)
                elif i in self.smSheep:
                    if sheepHit == True:
                        self.numKill += 1
                        self.smSheep.remove(i)
                        self.all_sprites_list.remove(i)
                        self.poop_list.remove(j)
                        self.all_sprites_list.remove(j)
                        if self.numKill >= 18:
                            self.manager.go_to(couponsInstructions.instructing())
                        
        #check for redSheep and sheep collision (end game)
            for i in self.all_sprites_list:
                if i not in self.poop_list and i!=sheep:
                    if sheep.rect.colliderect(i) == True:
                        self.manager.go_to(deathPage.death())
                    elif i.rect.x>=self.width:
                        self.manager.go_to(deathPage.death())
    
    def keyPressed(self):
        #releases poop
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            singlePoopy = singlePoop()
            singlePoopy.rect.x = sheep.rect.x - self.space
            singlePoopy.rect.y = sheep.rect.y + self.space
            self.all_sprites_list.add(singlePoopy)
            self.poop_list.add(singlePoopy)
            
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.keyPressed()

    def render(self,screen):
        self.all_sprites_list.update()  
        screen.blit(self.background,(0,0))
        self.all_sprites_list.draw(screen)
