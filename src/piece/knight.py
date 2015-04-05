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

    piece_square_table1 = [
                            [-50,-40,-30,-30,-30,-30,-40,-50],
                            [-40,-20,  0,  0,  0,  0,-20,-40],
                            [-30,  0, 10, 15, 15, 10,  0,-30],
                            [-30,  5, 15, 20, 20, 15,  5,-30],
                            [-30,  0, 15, 20, 20, 15,  0,-30],
                            [-30,  5, 10, 15, 15, 10,  5,-30],
                            [-40,-20,  0,  5,  5,  0,-20,-40],
                            [-50,-40,-30,-30,-30,-30,-40,-50]
                           ]
    piece_square_table2 = [
                           [-50, -40, -30, -30, -30, -30, -40, -50],
                           [-40, -20, 0, 5, 5, 0, -20, -40],
                           [-30, 5, 10, 15, 15, 10, 5, -30],
                           [-30, 0, 15, 20, 20, 15, 0, -30],
                           [-30, 5, 15, 20, 20, 15, 5, -30],
                           [-30, 0, 10, 15, 15, 10, 0, -30],
                           [-40, -20, 0, 0, 0, 0, -20, -40],
                           [-50, -40, -30, -30, -30, -30, -40, -50]
                           ]
    def __init__(self, color, location):
        self.color = color
        self.location = location
        
        if(color == "white"):
            self.image = PhotoImage(file = "../../img/wN.png")
        else:
            self.image = PhotoImage(file = "../../img/bN.png")
        
    def is_possible(self, location, board):
        xDiff = self.location[0] - location[0]
        yDiff = self.location[1] - location[1]
    
        if(self.color == "white"):
            colour = 1
        else:
            colour = -1  
              
    
        if( ( abs(xDiff) == 1 and abs(yDiff) == 2 ) or ( abs(xDiff) == 2 and abs(yDiff) == 1 ) ): #check whether its knight move 
            if(board[location[0]][location[1]] * colour <= 0): #checks whether the location is not occupied by the own piece
                return True

        return False        
    
    def get_all_moves(self, board):
        lis  = [-1,-2,1,2]
        newLocation = []
        if(self.color == "white"):
            colour = 1
        else:
            colour = -1
            
        for i in lis:
            for j in lis:
                if(abs(i)!=abs(j)):
                    if(self.location[0]+i >= 0 and self.location[0]+i <= 7 and self.location[1]+j >= 0 and self.location[1]+j <= 7 ): #checks boundary condition
                        if(board[self.location[0]+i][self.location[1]+j] * colour <= 0): #checks whether the location is not occupied by the own piece
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

    @staticmethod
    def static_get_capture_moves(curr_location, board):
        lis  = [-1,-2,1,2]
        colour = board[curr_location[0]][curr_location[1]]
        newLocation = []      
        for i in lis:
            for j in lis:
                if(abs(i)!=abs(j)):
                    if(curr_location[0]+i >= 0 and curr_location[0]+i <= 7 and curr_location[1]+j >= 0 and curr_location[1]+j <= 7 ): #checks boundary condition
                        if(board[curr_location[0]+i][curr_location[1]+j] * colour < 0): #checks whether the location is not occupied by the own piece
                            newLocation.append([curr_location[0]+i,curr_location[1]+j])
        return newLocation
    def getimage(self):
        return self.image
    
    @classmethod
    def static_get_piece_score(cls, i, j, mode):
        if(mode == 1):
            return cls.piece_square_table1[i][j]
        return cls.piece_square_table2[i][j]
    
    def setlocation(self, location):
        self.location = location
        
    def getcolor(self):
        return self.color
