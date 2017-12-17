#transition page to ending scene
import pygame 
from sheep import Sheep 
import endingKill 

sheep = Sheep()
class theEnd(object):

    def __init__(self, width=800, height=600, fps=50):
        self.width = width
        self.height = height
        self.fps = fps
        #images
        self.background = pygame.transform.scale(pygame.image.load
        ('images/background.jpg'),(self.width, self.height))
        self.gate = pygame.transform.scale(pygame.image.load
        ('images/gate.png'),(300, 300))
        sheep.rect.x = 0
        sheep.rect.y = self.height - (self.height//6)
        self.all_sprites_list = pygame.sprite.Group()
        self.all_sprites_list.add(sheep)
        #dimension specifications
        self.space = 20
        self.buffer = 80
        self.letterSpace = 40
        self.widthTitle= self.width/15
        self.increase = 6
        pygame.init()

    def timerFired(self,dt):
        sheep.rect.x += self.increase

    def update(self):
        if sheep.rect.x >= self.width:
            self.manager.go_to(endingKill.endingOde()) 

    def handle_events(self):
        pass
            
    def render(self,screen):
        screen.blit(self.background,(0,0))
        font = pygame.font.Font("Acme-Regular.ttf", 40)
        screen.blit(self.background,(0,0))
        header = pygame.font.Font("Acme-Regular.ttf", 60)
        title = header.render("YOU'VE REACHED THE END!",3,(0,0,0))
        screen.blit(title, (self.widthTitle, self.height/4))
        self.all_sprites_list.update() 
        self.all_sprites_list.draw(screen)
        screen.blit(self.gate,(self.width-(3*self.buffer),
                    self.height//2 + self.space))