#instructions for maze level
import pygame
import coupons

class instructing(object):

    def __init__(self, width=800, height=600, fps=50):
        self.width = width
        self.height = height
        self.fps = fps
        #images
        self.background = pygame.transform.scale(pygame.image.load
        ('images/background.jpg'),(self.width, self.height))
        self.angel = pygame.transform.scale(pygame.image.load
        ('images/angel.png'),(30, 30))
        #dimension specifications
        self.space = 20
        self.letterSpace = 120
        self.buffer = 80
        self.widthTitle= self.width/2.4-16
        self.width1=self.width/2.8+18
        self.width2=self.width/5.2+self.space
        self.width5=self.width/15
        self.widthAd=self.width/3-(2*self.space)
        pygame.init()

    def timerFired(self,dt):
        pass

    def update(self):
        pass

            
    def handle_events(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_c]:
            self.manager.go_to(coupons.couponPlay())
            
    def render(self,screen):
        screen.blit(self.background,(0,0))
        font = pygame.font.Font("Acme-Regular.ttf", 40)
        screen.blit(self.background,(0,0))
        header = pygame.font.Font("Acme-Regular.ttf", 60)
        font = pygame.font.Font("Acme-Regular.ttf", 30)
        go = pygame.font.Font("Acme-Regular.ttf", 40)
        
        title = header.render('FINAL',3,(0,0,0))
        instruct1 = font.render("One last thing!", 3, (0,0,0))
        instruct2 = font.render("All that pooping has shrunken you.", 3, (0,0,0))
        instruct3 = font.render("Find your way out of the maze of bones.",3, (0,0,0))
        
        instruct5 = font.render(
        "Beware of the sheep moving around. Nothing can kill them.", 3, (0,0,0))
        advance = go.render("PRESS 'C' to continue.",3,(0,0,0))
        
        screen.blit(title, (self.widthTitle, self.height/9))
        
        screen.blit(instruct1, (self.width1,self.height/8+(self.buffer)))
                            
        screen.blit(instruct2, (self.width2+20, self.height/11+(2*self.buffer)))
                    
        screen.blit(instruct3, (self.width2-3, self.height/8+(2.6*self.buffer)))
        screen.blit(instruct5, (self.width5, self.height/8+(3.5*self.buffer)))
        screen.blit(advance, (self.widthAd,self.height/8+(4.5*self.buffer)))

        screen.blit(self.angel,(100,220))
