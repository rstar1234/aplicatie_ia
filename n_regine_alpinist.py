from random import randint
from utility_functions import printSolution

class AlpinistChess:
    def __init__(self, n) -> None:
        self.board = [[0 for x in range(n)] for y in range(n)]
        self.size = n
    #create a random state board as a starting point
    def randomBoard(self, state):
        for i in range(self.size):
            state[i] = randint(0, 100000) % self.size

            #place queen on the randomly chosen place
            self.board[state[i]][i] = 1

    def printBoard(self):
        for i in range(self.size):
            print(*self.board[i])

    def printState(self, state):
        print(*state)

    def compareStates(self, state1, state2):
        for i in range(self.size):
            if state1[i] != state2[i]:
                return False
        return True

    def fill(self, value):
        for i in range(self.size):
            for j in range(self.size):
                self.board[i][j] = value
        return self.board

    def calculateObjective(self, board, state):
        #Pentru fiecare regina intr-o coloane, verificam daca sunt alte regine atacate de prima regina, caz in care incrementam variabila attacking

        attacking = 0

        for i in range(self.size):
            row = state[i]
            col = i - 1
            while (col >= 0 and board[row][col] != 1):
                col -=1

            if (col >= 0 and board[row][col] == 1):
                attacking += 1

            #acelasi rand, la dreapta
            row = state[i]
            col = i + 1
            while (col < self.size and board[row][col] != 1):
                col += 1
         
            if (col < self.size and board[row][col] == 1) :
                attacking += 1

            #stanga sus (randul si coloana scad in acelasi timp)
            row = state[i] - 1
            col = i - 1
            while (col >= 0 and row >= 0 and board[row][col] != 1) :
                col-= 1
                row-= 1
         
            if (col >= 0 and row >= 0  and board[row][col] == 1) :
                attacking+= 1

            #dreapta jos (coloana creste, randul creste)
            row = state[i] + 1
            col = i + 1
            while (col < self.size and row < self.size  and board[row][col] != 1) :
                col+= 1
                row+= 1
         
            if (col < self.size and row < self.size and board[row][col] == 1) :
                attacking += 1

            #stanga jos (coloana scade, randul creste)
            row = state[i] + 1
            col = i - 1
            while (col >= 0 and row < self.size  and board[row][col] != 1) :
                col -= 1
                row += 1
         
            if (col >= 0 and row < self.size and board[row][col] == 1) :
                attacking += 1

            #dreapta sus (coloana creste, randul scade)
            row = state[i] - 1
            col = i + 1
            while (col < self.size and row >= 0  and board[row][col] != 1) :
                col += 1
                row -= 1
         
            if (col < self.size and row >= 0 and board[row][col] == 1) :
                attacking += 1

        #returneaza perechi
        return int(attacking / 2)

#functie ce genereaza o tabla, data o stare
    def generateBoard(self, state):
        self.board = self.fill(0)
        for i in range(self.size):
            self.board[state[i]][i] = 1
        return self.board

    def copyState(self, state1, state2):
        for i in range(self.size):
            state1[i] = state2[i]

    def getNeighbour(self, state):
        #optimal board and state with current board and state as starting points
        opBoard = [[0 for x in range(self.size)] for y in range(self.size)]
        opState = [0 for x in range(self.size)]
        self.copyState(opState, state)
        opBoard = self.generateBoard(opState)

        #optimal objective value
        opObjective = self.calculateObjective(opBoard, opState)

        neighbourBoard = [[0 for x in range(self.size)] for y in range(self.size)]
     
        neighbourState = [0 for x in range(self.size)]
        self.copyState(neighbourState, state)
        neighbourBoard = self.generateBoard(neighbourState)

        #iterating through all possible neighbors
        for i in range(self.size):
            for j in range(self.size):
                #condition for skipping the current state
                if j != state[i]:
                    #initializing temporary neighbour with the current neighbor
                    neighbourState[i] = j
                    neighbourBoard[neighbourState[i]][i] = 1
                    neighbourBoard[state[i]][i] = 0

                    #calculating the objective value of the neighbour
                    temp = self.calculateObjective(neighbourBoard, neighbourState)

                    if (temp <= opObjective) :
                        opObjective = temp
                        self.copyState(opState, neighbourState)
                        opBoard = self.generateBoard(opState)
                
                    #back to the original configuration for the next iteration
                    neighbourBoard[neighbourState[i]][i] = 0
                    neighbourState[i] = state[i]
                    neighbourBoard[state[i]][i] = 1

        self.copyState(state, opState)
        self.board = self.fill(0)
        self.board = self.generateBoard(state)

    def alg_alpinistului(self, state):
        neighbourBoard = [[0 for x in range(self.size)] for y in range(self.size)]
        neighbourState = [0 for x in range(self.size)]
 
        self.copyState(neighbourState, state)
        neighbourBoard = self.generateBoard(neighbourState)

        while True:
            self.copyState(state, neighbourState)
            self.board = self.generateBoard(state)

            #getting the optimal neighbour
            self.getNeighbour(neighbourState)

            if(self.compareStates(state, neighbourState)):
                self.printBoard()
                break
            elif self.calculateObjective(self.board, state) == self.calculateObjective(neighbourBoard, neighbourState):
                neighbourState[randint(0, 100000) % self.size]  = randint(0, 100000) % self.size
                neighbourBoard = self.generateBoard(neighbourState)

#testing

# n = int(input("Marimea tablei: "))
# board = AlpinistChess(n)
# state = [0] * n
# board.alg_alpinistului(state)