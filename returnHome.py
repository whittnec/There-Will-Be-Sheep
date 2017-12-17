#last page of game where you go back
import pygame
import levelPage

class returning(object):

    def __init__(self, width=800, height=600, fps=50):
        self.width = width
        self.height = height
        self.fps = fps
        self.img_back = pygame.image.load('images/rothko_white.jpg')
        self.background = pygame.transform.scale(self.img_back, 
        (self.width, self.height))
        self.startX = (self.width//3.5)+5
        self.startY = self.height/1.7
        self.optionDimX = self.width//2.5 #width of squares
        self.optionDimY = self.width//10 #height of squares
        self.startXBord = (self.width//3.5)+2 
        self.startYBord = self.height/1.7 - 3
        self.optionBordX = self.optionDimX + 6
        self.optionBordY = self.optionDimY + 6
        #beginning colors of borders
        self.color = (0,0,0)
        self.highlight = (205,205,205)
        pygame.init()
        
    def timerFired(self,dt):
        pass

    def update(self):
        pass
    
    def difficulty(self):
        return self.difficulty
    
    def mouseMotion(self,x,y):
        self.color = (0,0,0)
        #turn into gray border on hover
        (mouseX, mouseY) = pygame.mouse.get_pos()
        endX = self.startX+self.optionDimX
        endY = self.startY+self.optionDimY
        if self.startX<=mouseX<=endX and self.startY<=mouseY<=endY:
            self.color=self.highlight
        
    def mousePressed(self, x, y):
        (mouseX, mouseY) = pygame.mouse.get_pos()
        (mouseX, mouseY) = pygame.mouse.get_pos()
        endX = self.startX+self.optionDimX
        endY = self.startY+self.optionDimY
        if self.startX<=mouseX<=endX and self.startY<=mouseY<=endY:
            pygame.mixer.music.stop()
            self.manager.go_to(levelPage.levels())
            
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
        box = pygame.font.Font("Acme-Regular.ttf", 40)
        
        screen.blit(header.render("THERE WILL",3,(220,20,60)),(100,70))
        screen.blit(header.render("BE SHEEP",3,(220,20,60)),(165,190))
        
        pygame.draw.rect(screen, self.color, 
        (self.startXBord,self.startYBord,self.optionBordX,self.optionBordY), 4)
        pygame.draw.rect(screen, (255,255,255), 
        (self.startX, self.startY,self.optionDimX,self.optionDimY), 0)
        main = box.render("Back To Main Page", 3, (0,0,0))
        screen.blit(main, (self.startX+20, self.startY+15))


