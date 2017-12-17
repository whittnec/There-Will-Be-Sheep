#instructions for wood chipper level
import pygame
import mainPlay
import finale
import woodchip

class wInstructions(object):

    def __init__(self, width=800, height=600, fps=50):
        self.width = width
        self.height = height
        self.fps = fps
        #images
        self.background = pygame.transform.scale(pygame.image.load
        ('images/background.jpg'),(self.width, self.height))
        self.chipper = pygame.transform.scale(pygame.image.load
        ('images/wood.png'),(150, 200))
        self.sheep = pygame.transform.scale(pygame.image.load
        ('images/sheep_normal.png'),(100, 100))
        #dimension specifications
        self.space = 20
        self.letterSpace = 120
        self.buffer = 80
        self.widthTitle= (self.width/4)-10
        self.width1=(self.width/4)-20
        self.width2=(self.width/6)+25
        self.widthAd=(self.width/4)+22
        pygame.init()
        pygame.mixer.music.load('music/norwegian.ogg')
        pygame.mixer.music.play(5)
        pygame.mixer.music.set_volume(0.5)

    def timerFired(self,dt):
        pass

    def update(self):
        pass

            
    def handle_events(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_c]:
            self.manager.go_to(woodchip.woodChipper())
            
    def render(self,screen):
        screen.blit(self.background,(0,0))
        font = pygame.font.Font("Acme-Regular.ttf", 40)
        screen.blit(self.background,(0,0))
        header = pygame.font.Font("Acme-Regular.ttf", 60)
        font = pygame.font.Font("Acme-Regular.ttf", 30)
        go = pygame.font.Font("Acme-Regular.ttf", 40)
        
        #text
        title = header.render('WOODCHIPPER',3,(0,0,0))
        instruct1 = font.render("Use left & right arrow keys to move.", 3, (0,0,0))
        instruct2 = font.render("Move over the wind to push yourself up.",3, (0,0,0))
        instruct3 = font.render(
        'Do not fall into the woodchippers.', 3, (0,0,0))
        advance = go.render("PRESS 'C' to continue.",3,(0,0,0))
        #blitting
        screen.blit(title, (self.widthTitle, self.height/11))
        screen.blit(instruct1, (self.width1,self.height/11+(1.3*self.buffer)))
        screen.blit(instruct3, (self.width1+10, self.height/11+(2*self.buffer)))                    
        screen.blit(instruct2, (self.width2, self.height/11+(2.7*self.buffer)))
        screen.blit(advance, (self.widthAd,self.height/11+(3.4*self.buffer)))

        screen.blit(self.sheep,(40,60))
        #make woodchippers on screen
        x=25
        for i in range(5):
            screen.blit(self.chipper,(x,400))
            x+=150

