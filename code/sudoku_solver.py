############################################
# Overview
# 
# Solve the world's hardest sudoku puzzle.
# Can change initilization to solve any
# sudoku puzzle that is 9x9.
# 
# Solve using backtracking.
############################################
import numpy as np


class sudokuPuzzle:
    
    def __init__(self):
        self.__size = 9
        # World's easiest sudoku puzzle
        self.__board = np.zeros([self.__size, self.__size], dtype = 'ulonglong')
        
        # set up puzzle
        # Picking "world's hardest sudoku puzzle" based on math
        # See https://puzzling.stackexchange.com/questions/252/how-do-i-solve-the-worlds-hardest-sudoku
        self.__board[0, 0] = 8
        self.__board[1, 2] = 3
        self.__board[1, 3] = 6
        self.__board[2, 1] = 7
        self.__board[2, 4] = 9
        self.__board[2, 6] = 2
        self.__board[3, 1] = 5
        self.__board[3, 5] = 7
        self.__board[4, 4] = 4
        self.__board[4, 5] = 5
        self.__board[4, 6] = 7
        self.__board[5, 3] = 1
        self.__board[5, 7] = 3
        self.__board[6, 2] = 1
        self.__board[6, 7] = 6
        self.__board[6, 8] = 8
        self.__board[7, 2] = 8
        self.__board[7, 3] = 5
        self.__board[7, 7] = 1
        self.__board[8, 1] = 9
        self.__board[8, 6] = 4
        
    def __assign(self, row, col, num):
           self.__board[row, col] = num
           
    def __unassign(self, row, col):
            self.__board[row, col] = 0
            
    def __usedInRow(self, row, num):
        output = False
        for col in range(0, self.__size):
            if self.__board[row, col] == num:
                output = True
        return output
        
    def __usedInCol(self, col, num):
        output = False
        for row in range(0, self.__size):
            if self.__board[row, col] == num:
                output = True
        return output
        
    def __usedInBox(self, boxStartRow, boxStartCol, num):
        output = False
        for row in range(0, 3):
            for col in range(0, 3):
                if self.__board[row + boxStartRow, col + boxStartCol] == num:
                    output = True
        return output
        
    def __isValid(self, row, col, num):
        output = False
        if not self.__usedInRow(row, num) and not self.__usedInCol(col, num) and not self.__usedInBox(row - row%3, col - col%3, num):
            output = True
        return output
        
    # backtracking function
    def findSolution(self, row, col):
        solved = False
            
        ## base case
        if row == self.__size:
            return True
        
        # square open
        if self.__board[row, col] == 0:
            for num in range(1, self.__size + 1):
                ## if looks promising
                if self.__isValid(row, col, num):
                    ## make tentative assignment.
                    self.__assign(row, col, num)
                        
                    ## move on to next square
                    if col < self.__size - 1:
                        solved = self.findSolution(row, col + 1)
                    if col == self.__size - 1:
                        solved = self.findSolution(row + 1, 0)
                        
                    ## if failure. Increase num and try again
                    if not solved:
                        self.__unassign(row, col)
        ## board[row][col]!=0. Move on to next square. This square cannot be changed.
        else:
            if col < self.__size - 1:
                solved = self.findSolution(row, col + 1)
            if col == self.__size - 1:
                solved = self.findSolution(row + 1, 0)
        return solved
    
    # Can use http://www.birot.hu/sudoku.php to check answers
    def solve(self):
        if self.findSolution(0, 0):
            print(self.__board)
        else:
            print("No solution found.")
    def getSolution(self):
        return self.__board
                

temp = sudokuPuzzle()
temp.solve()
result = temp.getSolution()

def checkResults(result):
    
    output = True
    
    # check rows
    for i in range(0, result.shape[0]):
        if np.unique(result[i]).shape[0] != 9:
            print ("Failed furst check")
            output = False
            
    # check columns
    for i in range(0, result.shape[1]):
        if np.unique(result[:,i]).shape[0] != 9:
            print ("Failed second check")
            output = False
    
    # Start at upper left of each box
    def check_box(startRow, startCol):
        temp = np.zeros([3, 3])
        for i in range(0, 3):
            for j in range(0, 3):
                temp[i, j] = result[startRow + i, startCol + j]
        return np.unique(temp).shape[0] == 9
    
    if not check_box(0, 0):
         print ("First box failed")
         output = False
    
    if not check_box(0, 3):
         print ("Second box failed")
         output = False
         
    if not check_box(0, 6):
         print ("Third box failed")
         output = False
    
    if not check_box(3, 0):
         print ("Fourth box failed")
         output = False
    
    if not check_box(3, 3):
         print ("Fifth box failed")
         output = False
         
    if not check_box(6, 6):
         print ("Sixth box failed")
         output = False
         
    if not check_box(6, 0):
         print ("Seventh box failed")
         output = False
    
    if not check_box(6, 3):
         print ("Eighth box failed")
         output = False
         
    if not check_box(6, 6):
         print ("Ninth box failed")
         output = False
            
    return output
    
checkResults(result)
