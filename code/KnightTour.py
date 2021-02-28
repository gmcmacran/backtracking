############################################
# Overview
# 
# Find a tour of a knight such that the
# knight lands on all squares and never 
# returns to a previous square.
# 
# Solve using backtracking.
############################################
import numpy as np

class KnightTour:
    
    def __init__(self, size):
        self.__size = size
        self.__board = np.zeros([self.__size, self.__size])
        
        for i in range(size):
            for j in range(size):
                self.__board[i, j] = -1
        
    def __onBoard(self, row, col):
        output = False
        if row >= 0 and row < self.__size and col >= 0 and col < self.__size:
            output = True
        return output
    
    def __isSafe(self, row, col, num):
        if not self.__onBoard(row, col):
            return False
        
        # Not open
        elif self.__board[row,col] != -1:
            return False
        else:
            return True
    
    def __assign(self, row, col, num):
        self.__board[row, col] = num
        
    def __unassign(self, row, col):
        self.__board[row, col] = -1
    
    # backtracking function
    def findTour(self, row, col, currNum):
        
        ## base case
        if currNum == self.__size*self.__size:
            return True
        
        else:
            NextMoveWorked = False
            
            if self.__isSafe(row, col, currNum):
                self.__assign(row, col, currNum)
                
                # next move
                NextMoveWorked=self.findTour(row+2,col-1,currNum+1) #move 1
                
                if(not NextMoveWorked):
                    NextMoveWorked=self.findTour(row+2,col+1,currNum+1) #move 2
                    
                if(not NextMoveWorked):
                    NextMoveWorked=self.findTour(row+1,col+2,currNum+1) #move 3
                    
                if(not NextMoveWorked):
                    NextMoveWorked=self.findTour(row+1,col-2,currNum+1) #move 4
                    
                if(not NextMoveWorked):
                    NextMoveWorked=self.findTour(row-2,col+1,currNum+1) #move 5
                    
                if(not NextMoveWorked):
                    NextMoveWorked=self.findTour(row-2,col-1,currNum+1) #move 6
                    
                if(not NextMoveWorked):
                    NextMoveWorked=self.findTour(row-1,col-2,currNum+1) #move 7
                    
                if(not NextMoveWorked):
                    NextMoveWorked=self.findTour(row-1,col+2,currNum+1) #move 8
                    
                #if no next move worked, unassign current square. backtracking.
                if(not NextMoveWorked):
                    self.__unassign(row,col)
        return NextMoveWorked
        
    def solve(self):
        if self.findTour(0, 0, 0) == True:
            print(self.__board)
        else:
            print("No solution found.")
            
temp = KnightTour(6)
temp.solve()
 