#oil level instructions
import pygame

from sheep import Sheep
from oilCharacters import *
import oilPlay

sheep = Sheep()
oilScrapie = oilScrapie()
fire = firePic()
evilFace = evil()
rock = rock1()
class oilPlayExplanation(object):

    def __init__(self, width=800, height=600, fps=50):
        self.width = width
        self.height = height
        self.fps = fps
        self.img_back = pygame.image.load('images/rothko_black.jpg')
        self.background = pygame.transform.scale(self.img_back, 
        (self.width, self.height))
        self.space = 20
        self.letterSpace = 80
        self.all_sprites_list = pygame.sprite.Group()
        
        sheep.rect.x = self.width/3
        sheep.rect.y = self.height - (self.height/5)
        oilScrapie.rect.x = (2*self.space)
        oilScrapie.rect.y = self.height - (self.height/3)
        fire.rect.x = self.width - 9*self.space
        fire.rect.y = self.height - (self.height/8)
        evilFace.rect.x = self.width-(8*self.space)
        evilFace.rect.y = self.height/2
        rock.rect.x = self.width - (self.width//3)
        rock.rect.y = (4*self.space)
        self.all_sprites_list.add(sheep)
        self.all_sprites_list.add(oilScrapie)
        self.all_sprites_list.add(fire)
        self.all_sprites_list.add(evilFace)
        self.all_sprites_list.add(rock)
        
        pygame.init()
        pygame.mixer.music.load('music/blood.ogg')
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
            self.manager.go_to(oilPlay.oilPlay())
            
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
        
        title = header.render('OIL ROUND',3,(255,255,255))
        instruct1 = font.render("Avoid the falling rocks & fire.",
                                3, (255,255,255))
        instruct2 = font.render("Jump on faces to avoid sheep.", 3, (255,255,255))
        instruct3 = font.render("The sheep are bigger...", 3, (255,255,255))
        advance = go.render("PRESS 'C' to continue.",3,(255,255,255))
        screen.blit(title, (self.width/10, self.height/8))
        screen.blit(instruct1, (self.width/10, 
                    self.height/8+self.letterSpace))
        screen.blit(instruct2, (self.width/10, 
                    self.height/8+(1.5*self.letterSpace)))
        screen.blit(instruct3, (self.width/10, 
                    self.height/8+(2*self.letterSpace)))
        screen.blit(advance, (self.width/10, 
                    self.height/8+(2.7*self.letterSpace)))

