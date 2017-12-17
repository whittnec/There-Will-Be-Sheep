#maze level (drawing it on & actual maze code)
import pygame
import random
from mazeCharacters import *  
import deathPage    
import ending

class makeMaze(object):
    #basic framework from: https://www.cs.cmu.edu/~112/notes/nQueens.py
    def __init__(self):
        self.matrix=[]
        self.row = 10
        self.col = 10
        #give the row and column of the starting point
        self.randRow = random.randint(0,self.row-1)
        self.randCol = random.randint(0,self.col-1)
        
    def makeMatrix(self):
        for i in range(self.row):
            mat=[]
            for j in range(self.col):
                #bWall = bottom wall exists
                #rWall = right wall exists
                #False = has not been checked yet
                matrixInner=['bWall','rWall',False]
                mat.append(matrixInner)
            self.matrix.append(mat)
        return self.matrix
        
    def checkBorders(self,randRow,randCol, directions, randPos):
        #find valid direction for points on the border
        if randRow==0 and directions[randPos]=='up':
            directions.remove('up')
            newRandPos = random.randint(0,len(directions)-1)
            return self.checkBorders(randRow,randCol, directions, newRandPos)
        elif randRow==self.row-1 and directions[randPos]=='down':
            directions.remove('down')
            newRandPos = random.randint(0,len(directions)-1)
            return self.checkBorders(randRow,randCol, directions, newRandPos)
        elif randCol==0 and directions[randPos] =='left':
            directions.remove('left')
            newRandPos = random.randint(0,len(directions)-1)
            return self.checkBorders(randRow,randCol, directions, newRandPos)
        elif randCol==self.row-1 and directions[randPos]=='right':
            directions.remove('right')
            newRandPos = random.randint(0,len(directions)-1)
            return self.checkBorders(randRow,randCol, directions, newRandPos)
        else:
            return (randRow,randCol, directions[randPos])
        
    def newMatrix(self,matrix,randRow,randCol, directions, randPos):
        #check if point is a border point
        goodInfo = self.checkBorders(randRow,randCol, directions, randPos)
        #gets a valid direction for this point
        direct = goodInfo[2]
        #assigns the next point's coordinates based on the valid direction
        if direct == 'up':
            newrandRow=randRow-1
            newrandCol=randCol
        elif direct == 'down':
            newrandRow=randRow+1
            newrandCol=randCol
        elif direct == 'left':
            newrandRow=randRow
            newrandCol=randCol-1
        elif direct == 'right':
            newrandRow=randRow
            newrandCol=randCol+1
        #says point has been visited and "knocks down" corresponding wall
        if ((matrix[newrandRow][newrandCol][2]==False) and 
                (direct=='up' or direct=='down')):
            matrix[newrandRow][newrandCol][0]=False
            matrix[newrandRow][newrandCol][2] = True
            return (matrix,newrandRow,newrandCol)
        elif ((matrix[newrandRow][newrandCol][2]==False) and 
                (direct=='left' or direct=='right')):
            matrix[newrandRow][newrandCol][1]=False
            matrix[newrandRow][newrandCol][2] = True
            return (matrix,newrandRow,newrandCol)
        else:
            #if point already checked, need to find another point
            return False
        
    def freeBoard(self,matrix):
        total=len(matrix[0])*len(matrix)
        count=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j][2] == True:
                    count+=1
        if count/total >=.85:
            return True
        else:
            return False
    
    def makMaze(self):
        matrix = self.makeMatrix()
        directions = ['up','down','left','right']
        #assign starting point as checked
        matrix[self.randRow][self.randCol][2]=True
        currentPt=(self.randRow,self.randCol)
        prevMatrix=matrix
        def solve(matrix,prevMatrix, directions, currentPt):
            #check if all points visited
            if self.freeBoard(matrix) == True:
                return matrix
            else:
                for row in range(self.row):
                    directions = ['up','down','left','right']
                    #choose where the next point will be
                    randPos = random.randint(0,3)
                    # identify the next candidate pt (isLegal)
                    temp = self.newMatrix(matrix,currentPt[0],currentPt[1], directions,randPos)
                    if temp!=False:
                        tempMatrix = temp[0]
                        rowPos = temp[1]
                        colPos = temp[2]
                        #hold current maze in case it's wrong
                        prevMatrix = matrix
                        #set the new maze for checking
                        matrix=tempMatrix
                        directions = ['up','down','left','right']
                        solution = solve(matrix,prevMatrix,directions, (rowPos,colPos))
                        if (solution != None):
                            prevMatrix=matrix
                            return solution
                        #set the matrix back to before
                        matrix = prevMatrix
                return None
        return solve(matrix,prevMatrix,directions, currentPt)
        
sheep=sheepBread()        
maze=makeMaze()
class couponPlay(object):
    def __init__(self, width=800, height=600, fps=50):
        self.width = width
        self.height = height
        self.fps = fps
        self.img_back = pygame.image.load('images/background.jpg')
        self.background = pygame.transform.scale(self.img_back, 
        (self.width, self.height))
        self.all_sprites_list = pygame.sprite.Group()
        self.bone_sprites = pygame.sprite.Group()
        self.red_sprites=pygame.sprite.Group()
        sheep.rect.x=10
        sheep.rect.y=self.height-(self.height/4)
        self.all_sprites_list.add(sheep)
        self.sheepDirection = 'right'
        self.startX= 100
        self.bufferY=-65
        self.xInc = 60
        self.yInc = 60
        #pause stuff
        self.space = 20
        self.pause = False
        self.widthTitle= self.width/3+self.space
        self.maze = maze.makMaze()
        for i in range(len(self.maze)):
            hX = self.startX
            hY = ((i*self.yInc)+self.bufferY)
            for j in range(len(self.maze[0])):
                if self.maze[i][j][0] == False:
                    vertical = vBone()
                    vertical.rect.x =hX-10
                    vertical.rect.y=hY+100
                    self.bone_sprites.add(vertical)
                    self.all_sprites_list.add(vertical)
                elif self.maze[i][j][1] == False:
                    horizontal = hBone()
                    horizontal.rect.x =hX+40
                    horizontal.rect.y =hY+60
                    self.bone_sprites.add(horizontal)
                    self.all_sprites_list.add(horizontal)
                hX+=self.xInc
        for j in range(2):
            go = self.startX-10
            for i in range(10):
                vertical = vBone()
                vertical.rect.x=go
                vertical.rect.y =(j*590)-20
                self.bone_sprites.add(vertical)
                self.all_sprites_list.add(vertical)
                go+=64
        location = 100
        for k in range(5):
            sheepRed=redSheep()
            sheepRed.rect.x=location
            sheepRed.rect.y =10
            self.red_sprites.add(sheepRed)
            self.all_sprites_list.add(sheepRed)
            location+=150
        pygame.init()
    
    def timerFired(self,dt):
        if self.pause == False:
            for i in self.red_sprites:
                i.chargeDirection()
    
    def update(self):
        if self.pause == False:
            sheep.moveUp()
            
            if sheep.rect.x >=self.width:
                self.manager.go_to(ending.theEnd())
            
            for red in self.red_sprites:
                if sheep.rect.colliderect(red):
                    self.manager.go_to(deathPage.death())
            
            for i in self.bone_sprites:
                boneHit = sheep.rect.colliderect(i)
                if boneHit == True:
                    if self.sheepDirection == 'right':
                        sheep.rect.right = i.rect.left
                    elif self.sheepDirection == 'left':
                        sheep.rect.left = i.rect.right
                    elif self.sheepDirection == 'up':
                        sheep.rect.top = i.rect.bottom
                    elif self.sheepDirection == 'down':
                        sheep.rect.bottom = i.rect.top
                    
    def keyPressed(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.sheepDirection='right'
        elif key[pygame.K_UP]:    
            self.sheepDirection='up'
        elif key[pygame.K_DOWN]:    
            self.sheepDirection='down'
        elif key[pygame.K_LEFT]:    
            self.sheepDirection='left'
        elif key[pygame.K_p]:
            self.pause = True
        elif key[pygame.K_u]:
            self.pause = False 
            
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.keyPressed()

    def render(self,screen):
        screen.blit(self.background,(0,0))
        self.all_sprites_list.draw(screen)
        font = pygame.font.Font("Acme-Regular.ttf", 25)
        paused = font.render("Press 'P' to pause",3,(0,0,0))
        unpaused = font.render("Press 'U' to unpause",3,(0,0,0))
        screen.blit(paused, (20, 10))
        screen.blit(unpaused, (20,35))
        if self.pause == True:
            header = pygame.font.Font("Acme-Regular.ttf", 60)
            title = header.render('PAUSED',3,(0,0,0))
            screen.blit(title, (self.widthTitle, self.height/5))
        elif self.pause == False:
            self.all_sprites_list.update() 