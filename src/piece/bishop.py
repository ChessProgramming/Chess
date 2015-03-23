'''
Created on Mar 14, 2015

@author: Venkatesh
'''

from piece import *  # @UnusedWildImport
from tkinter import PhotoImage


class Bishop():
    '''
        Bishop is a piece and it moves diagonally :p
    '''

    def __init__(self, color, location):
        self.color = color
        self.location = location
        
        if(color == "white"):
            self.image = PhotoImage(file = "../../img/wB.png")
        else:
            self.image = PhotoImage(file = "../../img/bB.png")

    
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
    
        if( abs(xDiff) == abs(yDiff)):  #checks whether its in diagonal location 
            if( board[location[0]][location[1]] != colour): #checks whether the location is not occupied by the own piece
                x = self.location[0]
                y = self.location[1]

                if(x > location[0] ):
                        xinc=-1
                else:
                        xinc=1

                if(y >location[1]):
                        yinc=-1
                else:
                        yinc=1
            
                #moves in location diagonal in search of obstracle
                while(x != location[0] and y != location[1]):
                    x = x + xinc
                    y = y + yinc
                    if(x != location[0] and y != location[1]):
                        if(board[x][y] !=0 ):
                            return False
            else:
                return False
        else:
            return False

        return True
    
    def get_all_moves(self, tboard):  
        
        board = [[0 for _ in range(8)] for _ in range(8)]
        for i in range(8):
            for j in range(8):
                if(tboard[i][j] < 0):
                    board[i][j] = -1
                elif(tboard[i][j] > 0):
                    board[i][j] = 1
        newLocation=[]
        x=self.location[0]
        y=self.location[1]

        if(self.color == "white"):
            colour = 1
        else:
            colour = -1

        # bishop moves
        #checks for the moves in top right diagonal
        while(x<=6 and y<=6):
            x=x+1
            y=y+1
            if(board[x][y] == 0):
                newLocation.append([x,y])
                continue
            if(board[x][y] == colour):
                break
            if(board[x][y] == colour*-1):
                newLocation.append([x,y])
                break         

        x=self.location[0]
        y=self.location[1]

        #checks for the moves in bottom left diagonal
        while(x>=1 and y>=1 ):
            x=x-1
            y=y-1
            if(board[x][y] == 0):
                newLocation.append([x,y]) 
                continue
            if(board[x][y] == colour):
                break
            if(board[x][y] == colour*-1):
                newLocation.append([x,y])
                break 

        x=self.location[0]
        y=self.location[1]

        #checks for the moves in bottom right diagonal 
        while(x>=1 and y<=6):
            x=x-1
            y=y+1
            if(board[x][y] == 0):
                newLocation.append([x,y]) 
                continue
            if(board[x][y] == colour):
                break
            if(board[x][y] == colour*-1):
                newLocation.append([x,y])
                break 

        x=self.location[0]
        y=self.location[1]

        #checks for the moves in top left diagonal
        while(x<=6 and y>=1):
            x=x+1
            y=y-1
            if(board[x][y] == 0):
                newLocation.append([x,y])
                continue 
            if(board[x][y] == colour):
                break
            if(board[x][y] == colour*-1):
                newLocation.append([x,y])
                break 

        return newLocation

    '''
    @staticmethod
    def get_all_moves(tboard, curr_location,colour):  # @DuplicatedSignature
        
        board = [[0 for _ in range(8)] for _ in range(8)]
        for i in range(8):
            for j in range(8):
                if(tboard[i][j] < 0):
                    board[i][j] = -1
                elif(tboard[i][j] > 0):
                    board[i][j] = 1
        newLocation=[]
        x=curr_location[0]
        y=curr_location[1]
    
        #checks for the moves in top right diagonal
        while(x<=6 and y<=6):
            x=x+1
            y=y+1
            if(board[x][y] == 0):
                newLocation.append([x,y])
                continue
            if(board[x][y] == colour):
                break
            if(board[x][y] == colour*-1):
                newLocation.append([x,y])
                break         

        x=curr_location[0]
        y=curr_location[1]

        #checks for the moves in bottom left diagonal
        while(x>=1 and y>=1 ):
            x=x-1
            y=y-1
            if(board[x][y] == 0):
                newLocation.append([x,y])
                continue 
            if(board[x][y] == colour):
                break
            if(board[x][y] == colour*-1):
                newLocation.append([x,y])
                break 

        x=curr_location[0]
        y=curr_location[1]

        #checks for the moves in bottom right diagonal 
        while(x>=1 and y<=6):
            x=x-1
            y=y+1
            if(board[x][y] == 0):
                newLocation.append([x,y])
                continue 
            if(board[x][y] == colour):
                break
            if(board[x][y] == colour*-1):
                newLocation.append([x,y])
                break 

        x=curr_location[0]
        y=curr_location[1]

        #checks for the moves in top left diagonal
        while(x<=6 and y>=1):
            x=x+1
            y=y-1
            if(board[x][y] == 0):
                newLocation.append([x,y])
                continue 
            if(board[x][y] == colour):
                break
            if(board[x][y] == colour*-1):
                newLocation.append([x,y])
                break 

        return newLocation

    '''
    
    def getimage(self):
        return self.image
    
    
    def setlocation(self, location):
        self.location = location
        
    def getcolor(self):
        return self.color

