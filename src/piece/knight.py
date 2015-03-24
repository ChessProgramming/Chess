'''
Created on Mar 14, 2015

@author: Venkatesh
'''
from piece import *  # @UnusedWildImport
from tkinter import PhotoImage

class Knight():
    '''
        Knight is a piece which can move in L direction
    '''


    def __init__(self, color, location):
        self.color = color
        self.location = location
        
        if(color == "white"):
            self.image = PhotoImage(file = "../../img/wN.png")
        else:
            self.image = PhotoImage(file = "../../img/bN.png")
        
    def is_possible(self, location, tboard):
        board = [[0 for _ in range(8)] for _ in range(8)]
        for i in range(8):
            for j in range(8):
                if(tboard[i][j] < 0):
                    board[i][j] = -1
                elif(tboard[i][j] > 0):
                    board[i][j] = 1
        xDiff = self.location[0] - location[0]
        yDiff = self.location[1] - location[1]
    
        if(self.color == "white"):
            colour = 1
        else:
            colour = -1  
              
    
        if( ( abs(xDiff) == 1 and abs(yDiff) == 2 ) or ( abs(xDiff) == 2 and abs(yDiff) == 1 ) ): #check whether its knight move 
            if(board[location[0]][location[1]] != colour): #checks whether the location is not occupied by the own piece
                return True

        return False        
    
    def get_all_moves(self, tboard):
        lis  = [-1,-2,1,2]
        board = [[0 for _ in range(8)] for _ in range(8)]
        for i in range(8):
            for j in range(8):
                if(tboard[i][j] < 0):
                    board[i][j] = -1
                elif(tboard[i][j] > 0):
                    board[i][j] = 1
        newLocation = []
        if(self.color == "white"):
            colour = 1
        else:
            colour = -1
            
        for i in lis:
            for j in lis:
                if(abs(i)!=abs(j)):
                    if(self.location[0]+i >= 0 and self.location[0]+i <= 7 and self.location[1]+j >= 0 and self.location[1]+j <= 7 ): #checks boundary condition
                        if(board[self.location[0]+i][self.location[1]+j] != colour): #checks whether the location is not occupied by the own piece
                            newLocation.append([self.location[0]+i,self.location[1]+j])
        return newLocation
       
    @staticmethod
    def static_get_all_moves(curr_location, board):
        lis  = [-1,-2,1,2]
        colour = board[curr_location[0]][curr_location[1]]
        newLocation = []      
        for i in lis:
            for j in lis:
                if(abs(i)!=abs(j)):
                    if(curr_location[0]+i >= 0 and curr_location[0]+i <= 7 and curr_location[1]+j >= 0 and curr_location[1]+j <= 7 ): #checks boundary condition
                        if(board[curr_location[0]+i][curr_location[1]+j] * colour <= 0): #checks whether the location is not occupied by the own piece
                            newLocation.append([curr_location[0]+i,curr_location[1]+j])
        return newLocation
    
    def getimage(self):
        return self.image
    
    
    def setlocation(self, location):
        self.location = location
        
    def getcolor(self):
        return self.color
