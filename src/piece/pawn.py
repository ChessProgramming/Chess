'''
Created on Mar 14, 2015

@author: Venkatesh
'''

from piece import *
from tkinter import PhotoImage, Tk


class Pawn(Piece):
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
            if(board[location[0]][location[1]] == -1*colour ):
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
            
            if(self.location[1]-1 >= 0 and board[self.location[0] + self.move][self.location[1]-1] == -1*colour): #for left cross move
                newLocation.append([self.location[0] + self.move, self.location[1]-1])
             
            if(self.location[1]+1 <= 7 and board[self.location[0] + self.move][self.location[1]+1] == -1*colour): #for right cross move
                newLocation.append([self.location[0] + self.move, self.location[1]+1])   
                
            if(self.location[0] == start and board[self.location[0] + self.move][self.location[1]] == 0 \
               and board[self.location[0] + 2*self.move][self.location[1]] == 0): #for double step from initial
                newLocation.append([self.location[0] + 2*self.move, self.location[1]])
                
        return newLocation
                
              
        
    def getimage(self):
        return self.image
    
    
    def setlocation(self, location):
        self.location = location
        