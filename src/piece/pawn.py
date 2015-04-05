'''
Created on Mar 14, 2015

@author: Venkatesh
'''

from piece import *  # @UnusedWildImport
from tkinter import PhotoImage


class Pawn():
    '''
    Pawn is a piece and it can move only forward
    '''


    piece_square_table1 = [
                            [0,  0,  0,  0,  0,  0,  0,  0],
                            [50, 50, 50, 50, 50, 50, 50, 50],
                            [10, 10, 20, 30, 30, 20, 10, 10],
                            [5,  5, 10, 25, 25, 10,  5,  5],
                            [0,  0,  0, 20, 20,  0,  0,  0],
                            [5, -5,-10,  0,  0,-10, -5,  5],
                            [5, 10, 10,-20,-20, 10, 10,  5],
                            [0,  0,  0,  0,  0,  0,  0,  0]
                           ]
    
    piece_square_table2 = [
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [5, 10, 10, -20, -20, 10, 10, 5],
                            [5, -5, -10, 0, 0, -10, -5, 5],
                            [0, 0, 0, 20, 20, 0, 0, 0],
                            [5, 5, 10, 25, 25, 10, 5, 5],
                            [10, 10, 20, 30, 30, 20, 10, 10],
                            [50, 50, 50, 50, 50, 50, 50, 50],
                            [0, 0, 0, 0, 0, 0, 0, 0]
                           ]
    def __init__(self, color, location, move):
        self.color = color
        self.location = location
        self.move = move   # +1 when it moves forward & -1 backward
        
        if(color == "white"):
            self.image = PhotoImage(file = "../../img/wP.png")
        else:
            self.image = PhotoImage(file = "../../img/bP.png")
        
    def is_possible(self, location, board):
        if(self.color == "white"):
            colour = 1
        else:
            colour = -1 
            
        if(self.move == 1):
            xDiff = location[0] - self.location[0]
            start = 1
        else:
            xDiff = self.location[0] - location[0]
            start = 6
            
        yDiff = self.location[1] - location[1]

        if(self.location[0] == start and yDiff == 0 and xDiff == 2): #checks whether its in initial position or not for two step move
            if(board[self.location[0] + self.move][self.location[1]] == 0 and board[self.location[0] + 2*self.move][self.location[1]] == 0):
                #checks for obstacle
                return True
        
        if(xDiff == 1 and yDiff == 0): #for single forward move
            if(board[self.location[0] + self.move ][self.location[1]] == 0):#checks for obstacle
                return True
            
        if(xDiff==1 and (yDiff==-1 or yDiff ==1)):  #for taking opponent piece
            if(board[location[0]][location[1]] * colour < 0 ):

                return True

        return False
     
    def get_all_moves(self, board ):
        newLocation = []
        
        if(self.color == "white"):
            colour = 1
        else:
            colour = -1 
            
        if(self.move == 1):
            start = 1
        else:
            start = 6
            
        if(self.location[0] + self.move >=0 and self.location[0] + self.move <=7): # boundary condition
            if(board[self.location[0] + self.move][self.location[1]] == 0): #for single forward move
                newLocation.append([self.location[0] + self.move, self.location[1]])
            
            if(self.location[1]-1 >= 0 and board[self.location[0] + self.move][self.location[1]-1]  *colour < 0): #for left cross move
                newLocation.append([self.location[0] + self.move, self.location[1]-1])
             
            if(self.location[1]+1 <= 7 and board[self.location[0] + self.move][self.location[1]+1] * colour < 0): #for right cross move
                newLocation.append([self.location[0] + self.move, self.location[1]+1])   
                
            if(self.location[0] == start and board[self.location[0] + self.move][self.location[1]] == 0 \
               and board[self.location[0] + 2*self.move][self.location[1]] == 0): #for double step from initial
                newLocation.append([self.location[0] + 2*self.move, self.location[1]])
                
        return newLocation

        
    @staticmethod
    def static_get_all_moves(curr_location, board, move):  # @DuplicatedSignature
        newLocation = []
        if(move == 1):
            start = 1
        else:
            start = 6
            
        colour = board[curr_location[0]][curr_location[1]]
        if(curr_location[0] + move >=0 and curr_location[0] + move <=7): # boundary condition
            if(board[curr_location[0] + move][curr_location[1]] == 0): #for single forward move
                newLocation.append([curr_location[0] + move, curr_location[1]])
            
            if(curr_location[1]-1 >= 0 and board[curr_location[0] + move][curr_location[1]-1] * colour < 0): #for left cross move
                newLocation.append([curr_location[0] + move, curr_location[1]-1])
             
            if(curr_location[1]+1 <= 7 and board[curr_location[0] + move][curr_location[1]+1] * colour < 0): #for right cross move
                newLocation.append([curr_location[0] + move, curr_location[1]+1])   
                
            if(curr_location[0] == start and board[curr_location[0] + move][curr_location[1]] == 0 \
               and board[curr_location[0] + 2*move][curr_location[1]] == 0): #for double step from initial
                newLocation.append([curr_location[0] + 2*move, curr_location[1]])
                
        return newLocation
         
    @staticmethod
    def static_get_capture_moves(curr_location, board, move):
        newLocation = []     
        colour = board[curr_location[0]][curr_location[1]]   
        if(curr_location[0] + move >=0 and curr_location[0] + move <=7): # boundary condition
            if(curr_location[1]-1 >= 0 and board[curr_location[0] + move][curr_location[1]-1] * colour < 0): #for left cross move
                newLocation.append([curr_location[0] + move, curr_location[1]-1])
             
            if(curr_location[1]+1 <= 7 and board[curr_location[0] + move][curr_location[1]+1] * colour < 0): #for right cross move
                newLocation.append([curr_location[0] + move, curr_location[1]+1])
        return newLocation

    @classmethod
    def static_get_piece_score(cls, i, j, mode):
        if(mode == 1):
            return cls.piece_square_table1[i][j]
        return cls.piece_square_table2[i][j]
    
    def getimage(self):
        return self.image
    
    
    def setlocation(self, location):
        self.location = location
        
    def getcolor(self):
        return self.color
