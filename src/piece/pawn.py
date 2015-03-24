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


    def __init__(self, color, location, move):
        self.color = color
        self.location = location
        self.move = move   # +1 when it moves forward & -1 backward
        
        if(color == "white"):
            self.image = PhotoImage(file = "../../img/wP.png")
        else:
            self.image = PhotoImage(file = "../../img/bP.png")
        
    def is_possible(self, location, board):
<<<<<<< HEAD
=======
        
>>>>>>> updated ischeck and successor
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
<<<<<<< HEAD
            if(board[location[0]][location[1]] *colour <= 0):
=======
            if(board[location[0]][location[1]] * colour <= 0 ):
>>>>>>> updated ischeck and successor
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
            
            if(self.location[1]-1 >= 0 and board[self.location[0] + self.move][self.location[1]-1]  *colour > 0): #for left cross move
                newLocation.append([self.location[0] + self.move, self.location[1]-1])
             
            if(self.location[1]+1 <= 7 and board[self.location[0] + self.move][self.location[1]+1] * colour > 0): #for right cross move
                newLocation.append([self.location[0] + self.move, self.location[1]+1])   
                
            if(self.location[0] == start and board[self.location[0] + self.move][self.location[1]] == 0 \
               and board[self.location[0] + 2*self.move][self.location[1]] == 0): #for double step from initial
                newLocation.append([self.location[0] + 2*self.move, self.location[1]])
                
        return newLocation
<<<<<<< HEAD
        
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
    
=======
      
>>>>>>> updated ischeck and successor
    def getimage(self):
        return self.image
    
    
    def setlocation(self, location):
        self.location = location
        
    def getcolor(self):
        return self.color
