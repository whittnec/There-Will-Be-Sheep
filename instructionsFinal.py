#instructions for semifinal
import pygame
import mainPlay
import finale

class instructions(object):

    def __init__(self, width=800, height=600, fps=50):
        self.width = width
        self.height = height
        self.fps = fps
        #images
        self.background = pygame.transform.scale(pygame.image.load
        ('images/background.jpg'),(self.width, self.height))
        self.angel = pygame.transform.scale(pygame.image.load
        ('images/angel.png'),(120, 120))
        self.red = pygame.transform.scale(pygame.image.load
        ('images/finalSheep.png'),(120, 120))
        self.red = pygame.transform.flip(self.red,True,False)
        #dimension specifications
        self.space = 20
        self.letterSpace = 120
        self.buffer = 80
        self.widthTitle= self.width/3-self.space
        self.width1=self.width/4+(1.7*self.space)
        self.width2=self.width/4.7+self.space
        self.width5=self.width/5.8
        self.width4=self.width/18
        self.widthAd=self.width/3-(2*self.space)
        pygame.init()

    def timerFired(self,dt):
        pass

    def update(self):
        pass

            
    def handle_events(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_c]:
            self.manager.go_to(finale.final())
            
    def render(self,screen):
        screen.blit(self.background,(0,0))
        font = pygame.font.Font("Acme-Regular.ttf", 40)
        screen.blit(self.background,(0,0))
        header = pygame.font.Font("Acme-Regular.ttf", 60)
        font = pygame.font.Font("Acme-Regular.ttf", 30)
        go = pygame.font.Font("Acme-Regular.ttf", 40)
        
        title = header.render('SEMI-FINAL',3,(0,0,0))
        instruct1 = font.render("You've reached wing level!", 3, (0,0,0))
        instruct2 = font.render("You can move anywhere you want.", 3, (0,0,0))
        instruct3 = font.render("But the sheep can go anywhere too.",3, (0,0,0))
        instruct4 = font.render(
        "Be careful! Each hit on a large sheep spawns 4 smaller sheep.", 
        3, (0,0,0))
        
        instruct5 = font.render(
        'Do not let any red sheep touch or get past you.', 3, (0,0,0))
        advance = go.render("PRESS 'C' to continue.",3,(0,0,0))
        
        screen.blit(title, (self.widthTitle, self.height/11))
        
        screen.blit(instruct1, (self.width1,self.height/11+self.buffer))
                            
        screen.blit(instruct2, (self.width2, self.height/11+(1.7*self.buffer)))
                    
        screen.blit(instruct3, (self.width2, self.height/11+(2.4*self.buffer)))
        screen.blit(instruct5, (self.width5, self.height/11+(3.1*self.buffer)))
        screen.blit(instruct4, (self.width4, self.height/11+(3.8*self.buffer)))
        screen.blit(advance, (self.widthAd,self.height/11+(4.5*self.buffer)))

        screen.blit(self.angel,(self.width//12,self.height-(self.height/4)))
        screen.blit(self.red,(self.width-(2*self.buffer),
                    self.height-(self.height/4)))
