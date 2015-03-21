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


    def __init__(self, color, location):
        self.color = color
        self.location = location

        if(color == "white"):
            self.image = PhotoImage(file = "../../img/wK.png")
        else:
            self.image = PhotoImage(file = "../../img/bK.png")
        
    def is_possible(self, location, tboard):
        board = [[0 for _ in range(8)] for _ in range(8)]
        for i in range(8):
            for j in range(8):
                if(tboard[i][j] < 0):
                    board[i][j] = -1
                elif(tboard[i][j] > 0):
                    board[i][j] = 1
<<<<<<< HEAD
=======
                    
>>>>>>> added engine and ui updates
        xDiff = self.location[0] - location[0]
        yDiff = self.location[1] - location[1]

        if(self.color == "white"):
            colour = 1
        else:
            colour = -1


        if((xDiff == -1 or xDiff == 1 or xDiff == 0) and (yDiff == -1 or yDiff == 1 or yDiff == 0)): #checks its in adjacent cell
            if(not(xDiff == 0 and yDiff == 0 )):  #checks not in same location
                if(board[location[0]][location[1]] != colour):
                    return True
        return False
 
    def get_all_moves(self, tboard):
        board = [[0 for _ in range(8)] for _ in range(8)]
        for i in range(8):
            for j in range(8):
                if(tboard[i][j] < 0):
                    board[i][j] = -1
                elif(tboard[i][j] > 0):
                    board[i][j] = 1
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
                        if(board[self.location[0]][self.location[1]] != colour):    #checks whether the location not occupied by own piece
                            newLocation.append[self.location[0]+i,self.location[1]+j]            

        return newLocation

    def getimage(self):
        return self.image
    
    
    def setlocation(self, location):
        self.location = location