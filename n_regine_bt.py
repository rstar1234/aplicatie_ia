from utility_functions import printSolution

class BTChess:
    def __init__(self, n) -> None:
        self.board = [[0 for x in range(n)] for y in range(n)]
        self.size = n
        
    def isSafe(self, row, col):
    #check left side
        for i in range(col):
            if self.board[row][i] == 1:
                return False
    #check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False
    #check lower diagonal on left side
        for i, j in zip(range(row, self.size, 1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False
        return True

    def rezolvaNQ(self, col):
    #base case: If all queens are placed return True
        if col >= self.size:
            return True
    
        for i in range(self.size):
            if(self.isSafe(i, col)):
            #place queen
                self.board[i][col] = 1

                if self.rezolvaNQ(col + 1) == True:
                    return True
            
                self.board[i][col] = 0

    #if it can't be placed in any row in this column
        return False

    def rezolvaBT(self):

        if self.rezolvaNQ(0) == False:
            print("Nu exista solutie")
            return False
    
        printSolution(self.board, self.size)
        return True

#test
# dimension = int(input("Enter board size: "))
# board = BTChess(dimension)

# board.rezolvaBT()