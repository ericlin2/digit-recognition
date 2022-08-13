import random

class Perceptron:
    
    def __init__(self):
        self.eta = 0.01
        self.maxError = 0
        self.sumError = 1
        self.max_epoch = 5000
        self.targetList = []
        self.weights = []
        self.errorList = []
        self.allWeights = []
        self.currentList= []
    
    def generateWeights(self):
        self.weights.clear()
        self.errorList.clear()
        
        for i in range(36):
            weight = random.random() + 1
            self.weights.append(weight)
            
        for i in range(300):
            self.errorList.append(100)
    
    def getOutput(self, inputArray, weightList):
        sum = 0
        sum += -1 * weightList[0]        
        for i in range(35):
            sum += (inputArray[i] * weightList[i+1])   

        if(sum > 0):
            return 1
        return 0 

    def getTarget(self, label, perceptronValue):
        if(label == perceptronValue):
            return 1
        return 0 
           
    def activating(self, inputList):        
        # loops through each perceptron
        for i in range(10):
            # generate weights
            self.iterations = 0
            self.sumError = 1
            self.generateWeights()
            self.targetList.clear()
        
            for j in range(300):
                self.targetList.append(self.getTarget(inputList[j][-1], i))
                
            while(self.sumError != 0 and self.iterations != self.max_epoch):
                self.iterations += 1
                #print("iteration:", self.iterations)
                
                # loops through all tests
                for h in range(300):
                    output = self.getOutput(inputList[h], self.weights)
                    target = self.targetList[h]
                    
                    # finds the error
                    error = target - output
                    self.errorList[h] = abs(error)
                    
                    self.weights[0] += self.eta * error * -1
                    for k in range(35):
                        self.weights[k+1] += self.eta * error * inputList[h][k] 
        
                self.sumError = 0
                for errors in self.errorList:
                    self.sumError += errors
            
            for j in range(36):
                self.allWeights.append(self.weights[j])
        
    def classification(self, array1D):       
        value = []
        sum = 0
        storedValue = -1
        
        for i in range(10): #loops through all 10 perceptrons
            tempArr = []
            for j in range(36):
                index = i*36 + j
                tempArr.append(self.allWeights[index])
                
            value.append(self.getOutput(array1D, tempArr))
        
        # tests for exclusivity
        for i in range(10):
            if(value[i] == 1):
                storedValue = i
            sum += value[i]

        print(value)
        if(sum > 1 or sum == 0):
            return "error"

        else:
            return storedValue
        
