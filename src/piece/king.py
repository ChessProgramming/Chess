'''
Created on Mar 14, 2015

@author: Venkatesh
'''

from piece import *  # @UnusedWildImport
from tkinter import PhotoImage

class King():
    '''
        King is a piece and it can hop to all its adjacent locations
    '''


    piece_square_table1 = [
                            [-30,-40,-40,-50,-50,-40,-40,-30],
                            [-30,-40,-40,-50,-50,-40,-40,-30],
                            [-30,-40,-40,-50,-50,-40,-40,-30],
                            [-30,-40,-40,-50,-50,-40,-40,-30],
                            [-20,-30,-30,-40,-40,-30,-30,-20],
                            [-10,-20,-20,-20,-20,-20,-20,-10],
                            [20, 20,  0,  0,  0,  0, 20, 20],
                            [20, 30, 10,  0,  0, 10, 30, 20]
                           ]
    piece_square_table2 = [
                            [20, 30, 10, 0, 0, 10, 30, 20],
                            [20, 20, 0, 0, 0, 0, 20, 20],
                            [-10, -20, -20, -20, -20, -20, -20, -10],
                            [-20, -30, -30, -40, -40, -30, -30, -20],
                            [-30, -40, -40, -50, -50, -40, -40, -30],
                            [-30, -40, -40, -50, -50, -40, -40, -30],
                            [-30, -40, -40, -50, -50, -40, -40, -30],
                            [-30, -40, -40, -50, -50, -40, -40, -30]
                           ]
    def __init__(self, color, location):
        self.color = color
        self.location = location

        if(color == "white"):
            self.image = PhotoImage(file = "../../img/wK.png")
        else:
            self.image = PhotoImage(file = "../../img/bK.png")
        
    def is_possible(self, location, board):
        xDiff = self.location[0] - location[0]
        yDiff = self.location[1] - location[1]
        
        

        if(self.color == "white"):
            colour = 1
        else:
            colour = -1
            
        if((xDiff == -1 or xDiff == 1 or xDiff == 0) and (yDiff == -1 or yDiff == 1 or yDiff == 0)): #checks its in adjacent cell
            if(not(xDiff == 0 and yDiff == 0 )):  #checks not in same location
                if(board[location[0]][location[1]] * colour <= 0):
                    return True
                
        return False
 
    def get_all_moves(self, board):
        newLocation=[]
        if(self.color == "white"):
            colour = 1
        else:
            colour = -1
    
        #getting all location and checking for its own piece in that
        for i in range(-1,2):
            for j in range(-1,2):
                if(not(i==0 and j==0) ):
                    if(self.location[0]+i >=0 and self.location[0]+i <=7 and \
                       self.location[1]+j >=0 and self.location[1]+j <=7):
                        if(board[self.location[0] + i][self.location[1] + j] * colour <= 0): #checks whether the location not occupied by own piece
                            newLocation.append([self.location[0] + i, self.location[1] + j])   
                                     

        return newLocation
    
    @staticmethod
    def static_get_all_moves(curr_location, board):  # @DuplicatedSignature
        newLocation=[]
        
        colour = board[curr_location[0]][curr_location[1]]
        #getting all location and checking for its own piece in that
        for i in range(-1,2):
            for j in range(-1,2):
                if(not(i==0 and j==0) ):
                    if(curr_location[0]+i >=0 and curr_location[0]+i <=7 and \
                       curr_location[1]+j >=0 and curr_location[1]+j <=7):
                        if(board[curr_location[0]+i][curr_location[1]+j] * colour <= 0):    #checks whether the location not occupied by own piece
                            
                            newLocation.append([curr_location[0]+i,curr_location[1]+j])   
                            
                
        return newLocation
    
    @staticmethod
    def static_get_capture_moves(curr_location, board):  # @DuplicatedSignature
        newLocation=[]
        colour = board[curr_location[0]][curr_location[1]]
        #getting all location and checking for its own piece in that
        for i in range(-1,2):
            for j in range(-1,2):
                if(not(i==0 and j==0) ):
                    if(curr_location[0]+i >=0 and curr_location[0]+i <=7 and \
                       curr_location[1]+j >=0 and curr_location[1]+j <=7):
                        if(board[curr_location[0]+i][curr_location[1]+j] * colour < 0 ):    #checks whether the location not occupied by own piece
                            newLocation.append([curr_location[0]+i,curr_location[1]+j])           
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
