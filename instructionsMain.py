#instructions for main part of game
import pygame
import mainPlay

class instructionsM(object):

    def __init__(self, width=800, height=600, fps=50):
        self.width = width
        self.height = height
        self.fps = fps
        #images
        self.background = pygame.transform.scale(pygame.image.load
        ('images/background.jpg'),(self.width, self.height))
        #dimension specifications
        self.space = 20
        self.letterSpace = 90
        self.buffer = 80
        self.letterH = self.height//17
        self.widthTitle= self.width//3-(2*self.space)
        self.width1=self.width/3-self.space
        self.width2=self.width/4.7+self.space
        self.width3=self.width/9.5+self.space
        self.width5=self.width/18
        self.width4=self.width/18
        self.widthAd=self.width/3-(1.8*self.space)
        pygame.init()
        pygame.mixer.music.load('music/titleSheep.ogg')
        pygame.mixer.music.play(5)
        pygame.mixer.music.set_volume(0.5)

    def timerFired(self,dt):
        pass

    def update(self):
        pass

            
    def handle_events(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_c]:
            self.manager.go_to(mainPlay.mainPlay())
            
    def render(self,screen):
        screen.blit(self.background,(0,0))
        font = pygame.font.Font("Acme-Regular.ttf", 40)
        screen.blit(self.background,(0,0))
        header = pygame.font.Font("Acme-Regular.ttf", 60)
        font = pygame.font.Font("Acme-Regular.ttf", 30)
        go = pygame.font.Font("Acme-Regular.ttf", 40)
        
        title = header.render('HOW TO PLAY',3,(0,0,0))
        
        instruct1 = font.render("Use arrow keys to move.", 3, (0,0,0))
        
        instruct2 = font.render(
        "Scrapie sheep behind you will kill you.", 3, (0,0,0))
        instruct3 = font.render(
        "Press space to release poop and kill them.", 3, (0,0,0))
        
        instruct4 = font.render(
        "Jump over incoming oil pools, pee pools, and wolves.", 3, (0,0,0))
        instruct5 = font.render(
        "They can not kill you but lead to sublevels to delay your progress.", 
        3, (0,0,0))
        
        instruct6 = font.render(
        'Avoid the birds in the sky - they damage your vision.', 3, (0,0,0))
        
        instruct7 = font.render(
        "Jump on the clouds for cover. But you can't stay forever.", 
        3, (0,0,0))
        instruct8 = font.render("(You will fall through them)", 3, (0,0,0))
        
        advance = go.render("PRESS 'C' to continue.",3,(0,0,0))
        
        screen.blit(title, (self.widthTitle, self.letterH))
        
        screen.blit(instruct1, (self.width1,self.letterH+(1.1*self.buffer)))
                            
        screen.blit(instruct2, (self.width2, self.letterH+(1.8*self.buffer)))
        screen.blit(instruct3, (self.width2-self.space, 
        self.letterH+(2.2*self.buffer)))

        screen.blit(instruct4, (self.width3, self.letterH+(2.9*self.buffer)))        
        screen.blit(instruct5, (self.width5-self.space, 
        self.letterH+(3.3*self.buffer)))
        
        screen.blit(instruct6, (self.width2-(3.5*self.space), 
        self.letterH+(4*self.buffer)))
        
        screen.blit(instruct7, (self.width3-self.space, 
        self.letterH+(4.7*self.buffer)))        
        screen.blit(instruct8, (self.width1-self.space, 
        self.letterH+(5.1*self.buffer)))
        
        screen.blit(advance, (self.widthAd,self.letterH+(6*self.buffer)))
