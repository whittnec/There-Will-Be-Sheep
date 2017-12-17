#pee level instructions
import pygame
import random

from sheep import Sheep
from pissCharacters import *
import PISSPLAY

sheep = Sheep()
peeScrap = peeScrapie()
cell = normCell()
flag = fallingFlagella()

class pissPlayExplanation(object):

    def __init__(self, width=800, height=600, fps=50):
        self.width = width
        self.height = height
        self.fps = fps
        self.img_back = pygame.image.load('images/rothko_yellow.jpg')
        self.background = pygame.transform.scale(self.img_back, 
        (self.width, self.height))
        self.space = 20
        self.letterSpace = 80
        self.all_sprites_list = pygame.sprite.Group()
        
        sheep.rect.x = self.width/3 + self.space
        sheep.rect.y = self.height - (self.height/5)
        peeScrap.rect.x = (2*self.space)
        peeScrap.rect.y = self.height - (self.height/3)
        cell.rect.x = self.width//2 + (3*self.space)
        cell.rect.y = self.height//2
        flag.rect.x = self.width-(8*self.space)
        flag.rect.y = self.height/3
        self.all_sprites_list.add(sheep)
        self.all_sprites_list.add(peeScrap)
        self.all_sprites_list.add(cell)
        self.all_sprites_list.add(flag)
        
        pygame.init()
        pygame.mixer.music.load('music/balladThinMan.ogg')
        pygame.mixer.music.play(5)
        pygame.mixer.music.set_volume(0.5)
        
    def timerFired(self,dt):
        pass
        
    def update(self):
        pass
                                 
    def keyPressed(self):
        #starts oil play level
        key = pygame.key.get_pressed()
        if key[pygame.K_c]:
            self.manager.go_to(PISSPLAY.pissPlay())
            
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.keyPressed()

    def render(self,screen):
        self.all_sprites_list.update()  
        screen.blit(self.background,(0,0))
        self.all_sprites_list.draw(screen)
        header = pygame.font.Font("Acme-Regular.ttf", 60)
        font = pygame.font.Font("Acme-Regular.ttf", 30)
        go = pygame.font.Font("Acme-Regular.ttf", 40)
        
        title = header.render('PEE ROUND',3,(0,0,0))
        instruct1 = font.render("Avoid the flagella.", 3, (0,0,0))
        instruct2 = font.render("Blood drops protect you.",
                                3, (0,0,0))
        instruct3 = font.render("The sheep are urine molecules.", 3, (0,0,0))
        advance = go.render("PRESS 'C' to continue.",3,(0,0,0))
        screen.blit(title, (self.width/10, self.height/8))
        screen.blit(instruct1, (self.width/10, 
                    self.height/8+self.letterSpace))
        screen.blit(instruct2, (self.width/10, 
                    self.height/8+(1.5*self.letterSpace)))
        screen.blit(instruct3, (self.width/10, 
                    self.height/8+(2*self.letterSpace)))
        screen.blit(advance, (self.width/10, 
                    self.height/8+(2.7*self.letterSpace)))

