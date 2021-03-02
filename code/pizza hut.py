############################################
# Overview
# 
# Find a 10-dgit integer whose digits are all
# distinct and the first n digits are
# divisible n for n 1 to 10.
#
# Answer: 3,816,547,290 
#
# See
# https://blog.pizzahut.com/national-pi-day-math-problems-solved/
# 
# Solve using backtracking.
############################################
import numpy as np

class pizzaHut:
    def __init__(self):
        self.__N = 10
        self.__solution = np.empty( shape= 0 , dtype = 'ulonglong')
        # self.__solution = np.zeros(1, dtype = 'ulonglong')
        # self.__guess = np.zeros(1, dtype = 'ulonglong')
        # self.__solution = np.array([3,8,1,6,5,4,7,2,9,0], dtype = 'ulonglong')
        # self.__solution = np.array([3,8,1,6,5,4,7,2,9], dtype = 'ulonglong')
        # print(self.__solution)
        
        self.callCount = 0
        
    def __isValid(self):    
        output = True
        localN = self.__solution.shape[0]
        # localN = self.__N
        
        # uniqueness test.
        if np.unique(self.__solution).shape[0] != localN:
            output = False
            
        # division test
        sumCheck = self.__solution*self.__N **(self.__N -np.arange(1, self.__solution.shape[0]+1))
        sumCheck = np.cumsum(sumCheck)
        sumCheck = sumCheck / self.__N **(self.__N  - np.arange(1, self.__solution.shape[0]+1))
        sumCheck = sumCheck % np.arange(1, self.__solution.shape[0]+1)
        if np.any(sumCheck != 0):
            output = False
        
        return output
    
    # backtracking function
    def findSolution(self):
        # print(self.__solution)
        
        if self.__solution.shape[0] == self.__N and self.__isValid():
            result = True
        elif self.__solution.shape[0] == self.__N and not self.__isValid():
            result = False
        else:
            result = False
            for i in np.arange(0, self.__N):
                if self.__isValid() and not result:
                    # Try tacking on i
                    self.__solution = np.concatenate((self.__solution, np.array([i], dtype = 'ulonglong')), axis = 0)
                    result = self.findSolution()
                    
                    # Remove i if needed. (backtrack)
                    if not result:
                        self.__solution = self.__solution[:self.__solution.shape[0]-1]
        return result
    
    def solve(self):
        if self.findSolution() == True:
            print(self.__solution)
        else:
            print("No solution found.")
            
 
temp = pizzaHut()
temp.solve()
            
        
            
            
        
        
    
        
        