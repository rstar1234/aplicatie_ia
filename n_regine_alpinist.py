from random import randint
from utility_functions import printSolution

n = 8

#create a random state board as a starting point
def randomBoard(board, state):
    for i in range(n):
        state[i] = randint(0, 100000) % n

        #place queen on the randomly chosen place
        board[state[i]][i] = 1

def printBoard(board):
     
    for i in range(n):
        print(*board[i])

def printState(state):
    print(*state)

def compareStates(state1, state2):
    for i in range(n):
        if state1[i] != state2[i]:
            return False
    return True

def fill(board, value):
    for i in range(n):
        for j in range(n):
            board[i][j] = value

def calculateObjective(board, state):
    #Pentru fiecare regina intr-o coloane, verificam daca sunt alte regine atacate de prima regina, caz in care incrementam variabila attacking

    attacking = 0

    for i in range(n):
        row = state[i]
        col = i - 1
        while (col >= 0 and board[row][col] != 1):
            col -=1

        if (col >= 0 and board[row][col] == 1):
            attacking += 1

        #acelasi rand, la dreapta
        row = state[i]
        col = i + 1
        while (col < n and board[row][col] != 1):
            col += 1
         
        if (col < n and board[row][col] == 1) :
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
        while (col < n and row < n  and board[row][col] != 1) :
            col+= 1
            row+= 1
         
        if (col < n and row < n and board[row][col] == 1) :
            attacking += 1

        #stanga jos (coloana scade, randul creste)
        row = state[i] + 1
        col = i - 1
        while (col >= 0 and row < n  and board[row][col] != 1) :
            col -= 1
            row += 1
         
        if (col >= 0 and row < n and board[row][col] == 1) :
            attacking += 1

        #dreapta sus (coloana creste, randul scade)
        row = state[i] - 1
        col = i + 1
        while (col < n and row >= 0  and board[row][col] != 1) :
            col += 1
            row -= 1
         
        if (col < n and row >= 0 and board[row][col] == 1) :
            attacking += 1

    #returneaza perechi
    return int(attacking / 2)

#functie ce genereaza o tabla, data o stare
def generateBoard( board, state):
    fill(board, 0);
    for i in range(n):
        board[state[i]][i] = 1

def copyState( state1, state2):
 
    for i in range(n):
        state1[i] = state2[i]

def getNeighbour(board, state):
    #optimal board and state with current board and state as starting points
    opBoard = [[0 for x in range(n)] for y in range(n)]
    opState = [0 for x in range(n)]
    copyState(opState, state)
    generateBoard(opBoard, opState)

    #optimal objective value
    opObjective = calculateObjective(opBoard, opState)

    neighbourBoard = [[0 for x in range(n)] for y in range(n)]
     
    neighbourState = [0 for x in range(n)]
    copyState(neighbourState, state)
    generateBoard(neighbourBoard, neighbourState)

    #iterating through all possible neighbors
    for i in range(n):
        for j in range(n):
            #condition for skipping the current state
            if j != state[i]:
                #initializing temporary neighbour with the current neighbor
                neighbourState[i] = j
                neighbourBoard[neighbourState[i]][i] = 1
                neighbourBoard[state[i]][i] = 0

                #calculating the objective value of the neighbour
                temp = calculateObjective( neighbourBoard, neighbourState)

                if (temp <= opObjective) :
                    opObjective = temp
                    copyState(opState, neighbourState)
                    generateBoard(opBoard, opState)
                
                #back to the original configuration for the next iteration
                neighbourBoard[neighbourState[i]][i] = 0
                neighbourState[i] = state[i]
                neighbourBoard[state[i]][i] = 1

    copyState(state, opState)
    fill(board, 0)
    generateBoard(board, state)

def alg_alpinistului(board, state):
    neighbourBoard = [[0 for x in range(n)] for y in range(n)]
    neighbourState = [0 for x in range(n)]
 
    copyState(neighbourState, state)
    generateBoard(neighbourBoard, 
    neighbourState)

    while True:
        copyState(state, neighbourState)
        generateBoard(board, state)

        #getting the optimal neighbour
        getNeighbour(neighbourBoard, neighbourState)

        if(compareStates(state, neighbourState)):
            printBoard(board)
            break
        elif calculateObjective(board, state) == calculateObjective(neighbourBoard, neighbourState):
            neighbourState[randint(0, 100000) % n]  = randint(0, 100000) % n
            generateBoard(neighbourBoard, neighbourState)

#testing
state = [0] * n
board = [[0 for x in range(n)] for y in range(n)]

#randomBoard(board, state)
#alg_alpinistului(board, state)
