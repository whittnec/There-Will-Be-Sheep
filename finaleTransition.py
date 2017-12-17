#transition to semifinal instructions/level
import pygame
import instructionsFinal 

class red(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #create scrapie sheep image
        self.image = pygame.transform.scale(pygame.image.load
        ('images/finalSheep.png'),(400, 400))
        self.rect = self.image.get_rect()

redSheep = red()
class finalTransition(object):

    def __init__(self,width=800, height=600, fps=50):
        self.width = width
        self.height = height
        self.fps = fps
        self.img_back = pygame.image.load('images/background.jpg')
        self.background = pygame.transform.scale(self.img_back, 
        (self.width, self.height))
        self.sheep = pygame.transform.scale(pygame.image.load
        ('images/sheep_normal.png'),(120, 120))
        #add red Sheep to sprite
        redSheep.rect.x = 0
        redSheep.rect.y = self.height//20
        self.all_sprites_list = pygame.sprite.Group()
        self.all_sprites_list.add(redSheep)
        self.increase = 3
        self.buffer = 80
        pygame.init()
        pygame.mixer.music.load('music/loveLevi.ogg')
        pygame.mixer.music.play(5)
        pygame.mixer.music.set_volume(0.8)
        
    def timerFired(self,dt):
        #slowly have red sheep advance
        redSheep.rect.x += self.increase

    def update(self):
        #once red sheep reaches end, go to instructions
        if redSheep.rect.x >= self.width:
            self.manager.go_to(instructionsFinal.instructions()) 

    def keyPressed(self):
        pass
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.keyPressed()

    def render(self,screen):
        screen.blit(self.background,(0,0))
        screen.blit(self.sheep,(self.width-(2*self.buffer),
                    self.height-(self.height/4)))
        self.all_sprites_list.update() 
        self.all_sprites_list.draw(screen)
