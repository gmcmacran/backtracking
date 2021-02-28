############################################
# Overview
# 
# Can N queens be placed on a chess
# board of size N such that no queen
# is attacking another queen?
# 
# Solve using backtracking.
############################################
import numpy as np

class NQueens:
    
    def __init__(self, size = 8):
        self.__size = size
        self.__board = np.zeros([self.__size, self.__size])
    
    def __setQueen(self, row, column):
        self.__board[row, column] = 1
        
    def __removeQueen(self, row, column):
        self.__board[row, column] = 0
    
    def __isUnderAttack(self, row, column):
        result = False
        
        # Check rows on left side
        for i in range(0, column):
            if self.__board[row, i] == 1:
                result = True
                
        # Check upper diagonal on left side
        for i, j in zip(reversed(range(row + 1)), reversed(range(column + 1))):
            if self.__board[i, j] == 1:
                result = True
                
        # Check lower diagonal on left side
        for i, j in zip(range(row, self.__size), reversed(range(column + 1))):
            if self.__board[i, j] == 1:
                result = True
        
        return result
    
    # backtracking function
    def placeQueens(self, currColumn = 0):
        
        # base case
        if currColumn == self.__size:
            return True
        
        else:
            queenPlace = False
            row = 0;
            
            while(not queenPlace and (row < self.__size)):
                if (self.__isUnderAttack(row, currColumn)):
                    row = row + 1
                
                else:
                    # Place queen and consider next column.
                    self.__setQueen(row, currColumn)
                    queenPlace = self.placeQueens(currColumn = currColumn + 1)
                    
                    # Backtrack if needed
                    if not queenPlace:
                        self.__removeQueen(row, currColumn)
                        row = row +1
            return queenPlace
        
    def solve(self):
        if self.placeQueens() == True:
            print(self.__board)
        else:
            print("No solution found.")
        


temp = NQueens(8)
temp.solve()
