from utility_functions import printSolution

n = 8

""" f = open("var.txt", "r")
n = int(f.read().strip())
 """
#let user pick between 8, 16 and 25 later
#TODO: in main.py declare a variable n, ask user for n, store n in a var.txt file

def isSafe(board, row, col):
    #check left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    #check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    #check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def rezolvaNQ(board, col):
    #base case: If all queens are placed return True
    if col >= n:
        return True
    
    for i in range(n):
        if(isSafe(board, i, col)):
            #place queen
            board[i][col] = 1

            if rezolvaNQ(board, col + 1) == True:
                return True
            
            board[i][col] = 0

    #if it can't be placed in any row in this column
    return False

def rezolvaBT():
    board = [[0 for x in range(n)] for y in range(n)]

    if rezolvaNQ(board, 0) == False:
        print("Nu exista solutie")
        return False
    
    printSolution(board)
    return True

#test
#rezolvaBT()