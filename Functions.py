import pygame
import random
from random import randint
from copy import deepcopy
from Perceptron import Perceptron


class Functions:
    p = Perceptron()

    def __init__(self, testAccess, window):
        self.testAccess = testAccess
        self.final = []
        self.window = window

    def label(self, array):
        for i in range(300):
            if(i < 30):
                array[i].append(0)
            elif(i < 60):
                array[i].append(1)
            elif(i < 90):
                array[i].append(2)
            elif(i < 120):
                array[i].append(3)
            elif(i < 150):
                array[i].append(4)
            elif(i < 180):
                array[i].append(5)
            elif(i < 210):
                array[i].append(6)
            elif(i < 240):
                array[i].append(7)
            elif(i < 270):
                array[i].append(8)
            elif(i < 300):
                array[i].append(9)

        self.final = deepcopy(array)
        
    def generate(self):
        tempCopy = deepcopy(self.testAccess)
        outputList = [[0]*35 for k in range(300)]
        
        for i in range(10):
            for j in range(30):
                index2 = i*30 + j
                outputList[index2] = self.initialNoise(j, tempCopy[i])
                self.inputVisualizer(outputList[index2])

        # print(outputList)
        self.clear()
        self.label(self.TwoDtoOneD(outputList))

    def train(self):
        random.shuffle(self.final)

        # self.final is an array of 1D arrays
        if(len(self.final) != 0):
            self.p.activating(self.final)
            print("trained.")

    def initialNoise(self, number_of_noises, digit):
        outputList = deepcopy(digit)
        for i in range(number_of_noises):
            for j in range(7):
                for k in range(5):
                    percentage = random.random()
                    if(percentage < 0.10):
                        outputList[j][k] += 0.10 if outputList[j][k] < 0.5 else -0.10

        return outputList

    def manualNoise(self, digit):
        number_of_noises = randint(0, 15)

        for i in range(number_of_noises):
            row = randint(0, 6)
            col = randint(0, 4)

            original_val = digit[row][col]
            if(random.random() > digit[row][col]):
                new_val = original_val + 0.1
                digit[row][col] = new_val

            else:
                new_val = original_val - 0.1
                digit[row][col] = new_val

        return digit

    def classify(self, inputList):
        outputList = []
        for i in range(7):
            for j in range(5):
                outputList.append(inputList[i][j])

        classify = -1
        classify = self.p.classification(outputList)
        return classify

    def clear(self):
        self.inputVisualizer(self.testAccess[10])
        self.outputVisualizer(self.testAccess[10])

    # changes a 2D array into 1D
    def TwoDtoOneD(self, array2D):
        outputList = [[0]*35 for f in range(300)]

        for i in range(300):
            for j in range(7):
                for k in range(5):
                    index = j*5 + k
                    outputList[i][index] = array2D[i][j][k]

        return outputList



    def inputVisualizer(self, input2D):
        for i in range(7):
            for j in range(5):
                color = int((1 - input2D[i][j])*255)
                pygame.draw.rect(self.window, (color, color, color),
                                 (65*j + 20, 65*i + 40, 65, 65))
        pygame.time.delay(15)
        pygame.display.update()

    def outputVisualizer(self, input2D):
        for i in range(7):
            for j in range(5):
                color = int((1 - input2D[i][j])*255)
                pygame.draw.rect(self.window, (color, color, color),
                                 (65*j + 555, 65*i + 40, 65, 65))
