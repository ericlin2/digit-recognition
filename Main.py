import pygame
from Numbers import Number
from Functions import Functions
from copy import deepcopy
from random import randint

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode([900, 600])
textFont = pygame.font.SysFont('Segoe UI', 35, bold=True)
numberFont = pygame.font.SysFont('Segoe UI', 64, bold=True)
classify = -1  
retrievedArray = 0
copy = []

run = True
screen.fill((254, 238, 213))
num = Number()
allAccess = num.accessNumbers() #stores all the default numbers
copyNumbers = deepcopy(allAccess) #makes copy of original set
button = Functions(allAccess, screen)

# GUI 

def numberSelector():
    Numbers = numberFont.render("0   1   2   3   4   5   6   7   8   9", False, (0,0,0))
    screen.blit(Numbers,(20, 510))
    for i in range(10):
        pygame.draw.rect(screen, (0,0,0), (0 + 90*i, 510, 90, 90), 1)
        
def drawGrid(topLeftX, topLeftY):
    for i in range(6): #vert lines
        pygame.draw.line(screen, (0,0,0), (65*i + topLeftX, topLeftY), (65*i + topLeftX, topLeftY + 455))
    for i in range(8): #hori lines
        pygame.draw.line(screen, (0,0,0),(topLeftX, 65*i + topLeftY), (topLeftX + 325, 65*i + topLeftY))

def textButtons():
    for i in range(5):
        pygame.draw.rect(screen, (181, 227, 227), (360, 60 + 85*i, 180, 50))
    
    generate = textFont.render("generate", False, (0,0,0))
    train = textFont.render("train", False, (0,0,0))
    addNoise = textFont.render("add noise", False, (0,0,0))
    classify = textFont.render("classify", False, (0,0,0))
    clear = textFont.render("clear", False, (0,0,0))
    screen.blit(generate,(375, 60))
    screen.blit(train,(410, 145))
    screen.blit(addNoise,(373, 230))
    screen.blit(classify,(390, 315))
    screen.blit(clear,(408, 400))

def numButtons(x, y):
    if(y > 500 and y < 600):
        selected = int(x/90)    
    return selected

def inputVisualizer(array):
    for i in range(7):
        for j in range(5):
            color = int((1 - array[i][j])*255)
            pygame.draw.rect(screen, (color,color,color), (65*j + 20, 65*i + 40, 65,65))
            
def outputVisualizer(array):
    for i in range(7):
        for j in range(5):
            color = int((1 - array[i][j])*255)
            pygame.draw.rect(screen, (color,color,color), (65*j + 555, 65*i + 40, 65,65))


while run:  
    for event in pygame.event.get():   
        if event.type == pygame.QUIT: 
            run = False            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # numbers
                if(pygame.mouse.get_pos()[1] > 510 and pygame.mouse.get_pos()[1] < 600):
                    pressed_number = numButtons(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                    
                    # retrieve array
                    retrievedArray = allAccess[pressed_number]
                    inputVisualizer(retrievedArray)
                    copy = deepcopy(retrievedArray)

                elif(pygame.mouse.get_pos()[0] > 360 and pygame.mouse.get_pos()[0] < 520):
                    #GENERATE
                    if(pygame.mouse.get_pos()[1] > 55 and pygame.mouse.get_pos()[1] < 115): 
                        button.generate()
                    #TRAIN
                    elif(pygame.mouse.get_pos()[1] > 140 and pygame.mouse.get_pos()[1] < 200): 
                        button.train()                       
                    #NOISE
                    elif(pygame.mouse.get_pos()[1] > 225 and pygame.mouse.get_pos()[1] < 285):
                        if(len(copy) != 0):
                            copied = button.manualNoise(copy)
                            retrievedArray = deepcopy(copied)
                            inputVisualizer(copied)                        
                    #CLASSIFY
                    elif(pygame.mouse.get_pos()[1] > 310 and pygame.mouse.get_pos()[1] < 370):
                        if(retrievedArray != 0):
                            classify = button.classify(retrievedArray)
                            if(classify == "error"):    
                                outputVisualizer(copyNumbers[11])                            
                            else:
                                outputVisualizer(copyNumbers[classify])                        
                    #CLEAR
                    elif(pygame.mouse.get_pos()[1] > 390 and pygame.mouse.get_pos()[1] < 455):
                        button.clear()

    numberSelector()
    drawGrid(20,40)
    textButtons()
    drawGrid(555,40)
        
    pygame.display.update()
    
pygame.quit()