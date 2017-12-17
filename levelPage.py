#opening page (with difficulty and woodchipper)
import pygame
import instructionsMain
import instructionsExtra

class levels(object):

    def __init__(self, width=800, height=600, fps=50):
        self.width = width
        self.height = height
        self.fps = fps
        self.img_back = pygame.image.load('images/background.jpg')
        self.background = pygame.transform.scale(self.img_back, 
        (self.width, self.height))
        self.optionDimX = self.width//4  #width of squares
        self.optionDimY = self.width//10 #height of squares
        self.optionBordX = self.optionDimX+7 #width of border is
        self.optionBordY = self.optionDimY+8 #height of border
        self.startX = (self.width/13) #where the sq. starts on x axis
        self.startY = self.height/1.7  #where the sq. starts on y axis
        self.startXBord = self.startX - 5 #where x axis border starts
        self.startYBord = self.startY - 5  #where y axis border starts
        self.startXWord = self.startX + (self.optionDimX/3.3)
        self.startYWord = self.startY + (self.optionDimY/5)
        #beginning colors of borders
        self.eColor = (0,0,0)
        self.mColor = (0,0,0)
        self.hColor = (0,0,0)
        self.wColor = (0,0,0)
        self.highlight = (205,205,205)
        self.difficulty = 1
        pygame.init()
        
    def timerFired(self,dt):
        pass

    def update(self):
        pass
    
    def difficult(self):
        return self.difficulty
    
    def mouseMotion(self,x,y):
        self.eColor = (0,0,0)
        self.mColor = (0,0,0)
        self.hColor = (0,0,0)
        self.wColor = (0,0,0)
        #turn into gray border on hover
        (mouseX, mouseY) = pygame.mouse.get_pos()
        endX = self.startX+self.optionDimX
        endY = self.startY+self.optionDimY
        if self.startX<=mouseX<=endX and self.startY<=mouseY<=endY:
            self.eColor=self.highlight
        elif self.startX+240<=mouseX<=endX+240 and self.startY<=mouseY<=endY:
            self.mColor=self.highlight
        elif self.startX+480<=mouseX<=endX+480 and self.startY<=mouseY<=endY:
            self.hColor=self.highlight
        elif self.startX+198<=mouseX<=endX+198 and self.startY+120<=mouseY<=endY+120:
            self.wColor=self.highlight
        
    def mousePressed(self, x, y):
        #get which difficulty they pressed
        (mouseX, mouseY) = pygame.mouse.get_pos()
        endX = self.startX+self.optionDimX
        endY = self.startY+self.optionDimY
        if self.startX<=mouseX<=endX and self.startY<=mouseY<=endY:
            self.difficulty = 1.5
            self.manager.go_to(instructionsMain.instructionsM())
        elif self.startX+240<=mouseX<=endX+240 and self.startY<=mouseY<=endY:
            self.difficulty = 1
            self.manager.go_to(instructionsMain.instructionsM())
        elif self.startX+480<=mouseX<=endX+480 and self.startY<=mouseY<=endY:
            self.difficulty = 0.4
            self.manager.go_to(instructionsMain.instructionsM())
        elif self.startX+198<=mouseX<=endX+198 and self.startY+120<=mouseY<=endY+120:
            self.manager.go_to(instructionsExtra.wInstructions())
            
    def handle_events(self):
        """got this mousebuttondown thing from here:
        https://qwewy.gitbooks.io/pygame-module-manual/content/chapter1/
        framework.html"""
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.mousePressed(*(event.pos))
            elif (event.type == pygame.MOUSEMOTION and 
                    event.buttons == (0, 0, 0)):
                self.mouseMotion(*(event.pos))

    def render(self,screen):
        screen.blit(self.background,(0,0))
        header = pygame.font.Font("Acme-Regular.ttf",120)
        font = pygame.font.Font("Acme-Regular.ttf", 40)
        #easy border
        pygame.draw.rect(screen, self.eColor, 
        (self.startXBord,self.startYBord,self.optionBordX,self.optionBordY), 4)
        #medium border
        pygame.draw.rect(screen, self.mColor, 
        (self.startXBord+240,self.startYBord,self.optionBordX,self.optionBordY), 4)
        #hard border
        pygame.draw.rect(screen, self.hColor, 
        (self.startXBord+480,self.startYBord,self.optionBordX,self.optionBordY), 4)
        #wood border
        pygame.draw.rect(screen, self.wColor, 
        (self.startXBord+198,self.startYBord+120,self.optionBordX+85,self.optionBordY), 4)
        
        screen.blit(header.render("THERE WILL",3,(220,20,60)),(100,70))
        screen.blit(header.render("BE SHEEP",3,(220,20,60)),(165,190))
        #easy rectangle
        pygame.draw.rect(screen, (255,255,255), 
        (self.startX,self.startY,self.optionDimX,self.optionDimY), 0)
        easy = font.render("Easy", 3, (0,0,0))
        screen.blit(easy, (self.startXWord, self.startYWord))
        #medium rectangle
        pygame.draw.rect(screen, (255,255,255), 
        (self.startX+240,self.startY,self.optionDimX,self.optionDimY), 0) 
        medium = font.render("Medium", 3, (0,0,0))
        screen.blit(medium, (self.startXWord+215, self.startYWord))
        #hard rectangle
        pygame.draw.rect(screen, (255,255,255), 
        (self.startX+480,self.startY,self.optionDimX,self.optionDimY), 0)
        hard = font.render("Hard", 3, (0,0,0))
        screen.blit(hard, (self.startXWord+480, self.startYWord))
        #wood rectangle
        pygame.draw.rect(screen, (255,255,255), 
        (self.startX+198,self.startY+120,self.optionDimX+85,self.optionDimY), 0)
        hard = font.render("Woodchipper", 3, (0,0,0))
        screen.blit(hard, (self.startXWord+170, self.startYWord+120))