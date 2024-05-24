from datetime import datetime
from utility_functions import printSolution

counter = 0
FIRST_GEN = 250

class GAChess:
    def __init__(self,n):
        self.board = self.createBoard(n)
        self.solutions = []
        self.size = n
        self.env = []
        self.goal = None
        self.goalIndex = -1

    def createBoard(self,n):
        board = [[0 for i in range(n)] for j in range(n)]
        return board

    def setBoard(self,board,gen):
        for i in range(self.size):
            board[gen[i]][i] = 1

    def generateDNA(self):
        from random import shuffle
        DNA = list(range(self.size))
        shuffle(DNA)
        while DNA in self.env:
            shuffle(DNA)
        return DNA

    def initializeFirstGeneration(self, val):
        for i in range(val):
            self.env.append(self.generateDNA())

    def utilityFunction(self,gen):
        hits = 0
        board = self.createBoard(self.size)
        self.setBoard(board,gen)
        col = 0

        for dna in gen:
            try:
                for i in range(col-1,-1,-1):
                    if board[dna][i] == 1:
                        hits+=1
            except IndexError:
                print(gen)
                quit()
            for i,j in zip(range(dna-1,-1,-1),range(col-1,-1,-1)):
                if board[i][j] == 1:
                    hits+=1
            for i,j in zip(range(dna+1,self.size,1),range(col-1,-1,-1)):
                if board[i][j] == 1:
                    hits+=1
            col+=1
        return hits

    def isSolution(self,gen):
        if self.utilityFunction(gen) == 0:
            return True
        return False

    def crossover(self,firstGen,secondGen):
        for i in range(1,len(firstGen)):
            if abs(firstGen[i-1] - firstGen[i])<2:
                firstGen[i],secondGen[i] = secondGen[i],firstGen[i]
            if abs(secondGen[i-1] - secondGen[i])<2:
                firstGen[i],secondGen[i] = secondGen[i],firstGen[i]

    def mutation(self,gen):
        bound = self.size//2
        from random import randint as rand
        leftSideIndex = rand(0,bound)
        RightSideIndex = rand(bound+1,self.size-1)
        newGen = []
        for dna in gen:
            if dna not in newGen:
                newGen.append(dna)
        for i in range(self.size):
            if i not in newGen:
                newGen.append(i)

        gen = newGen
        gen[leftSideIndex],gen[RightSideIndex] = gen[RightSideIndex],gen[leftSideIndex]
        return gen

    def reproduce(self):
        for i in range(1,len(self.env),2):
            firstGen = self.env[i-1][:]
            secondGen = self.env[i][:]
            self.crossover(firstGen,secondGen)
            firstGen = self.mutation(firstGen)
            secondGen = self.mutation(secondGen)
            self.env.append(firstGen)
            self.env.append(secondGen)

    def makeSelection(self):
        genUtilities = []
        newEnv = []

        for gen in self.env:
            genUtilities.append(self.utilityFunction(gen))
        if min(genUtilities) == 0:
            self.goalIndex = genUtilities.index(min(genUtilities))
            self.goal = self.env[self.goalIndex]
            return self.env
        minUtil=None
        while len(newEnv)<self.size:
            minUtil = min(genUtilities)
            minIndex = genUtilities.index(minUtil)
            newEnv.append(self.env[minIndex])
            genUtilities.remove(minUtil)
            self.env.remove(self.env[minIndex])

        return newEnv

    def solveGA(self):
        # init
        self.initializeFirstGeneration(FIRST_GEN)
        # what if randomly we already generated solution in the environment?
        #for gen in self.env:
        # if self.isSolution(gen):
        # return gen
        # start algo!
        count = 0
        while True:
            self.reproduce()
            self.env = self.makeSelection()
            count +=1
            if self.goalIndex >= 0:
                try:
                    #print(count)
                    return self.goal
                except IndexError:
                    #print(self.goalIndex)
                    pass
            else:
                continue
            
    def printSolution(self, solution):
        displayed_solution = [[0 for x in range(self.size)] for y in range(self.size)]
        for i in range(self.size):
            displayed_solution[i][solution[i]] = 1
        printSolution(displayed_solution, self.size)

# MAIN CODE
# dimension = int(input("Enter board dimension: "))
# chess = GAChess(dimension)

# start = datetime.now()
# solution = chess.solveGA()
# end = datetime.now()

# print("Solution (GA):")
# chess.printSolution(solution)
# print((end - start).microseconds / 1000)