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

    piece_square_table1 = [
                            [-20,-10,-10,-10,-10,-10,-10,-20],
                            [-10,  0,  0,  0,  0,  0,  0,-10],
                            [-10,  0,  5, 10, 10,  5,  0,-10],
                            [-10,  5,  5, 10, 10,  5,  5,-10],
                            [-10,  0, 10, 10, 10, 10,  0,-10],
                            [-10, 10, 10, 10, 10, 10, 10,-10],
                            [-10,  5,  0,  0,  0,  0,  5,-10],
                            [-20,-10,-10,-10,-10,-10,-10,-20]
                           ]
    
    piece_square_table2 = [
                            [-20, -10, -10, -10, -10, -10, -10, -20],
                            [-10, 5, 0, 0, 0, 0, 5, -10],
                            [-10, 10, 10, 10, 10, 10, 10, -10],
                            [-10, 0, 10, 10, 10, 10, 0, -10],
                            [-10, 5, 5, 10, 10, 5, 5, -10],
                            [-10, 0, 5, 10, 10, 5, 0, -10],
                            [-10, 0, 0, 0, 0, 0, 0, -10],
                            [-20, -10, -10, -10, -10, -10, -10, -20],
                           ]
    
    def __init__(self, color, location):
        self.color = color
        self.location = location
        
        if(color == "white"):
            self.image = PhotoImage(file = "../../img/wB.png")
        else:
            self.image = PhotoImage(file = "../../img/bB.png")

    
    def is_possible(self, location, board):
        xDiff = self.location[0] - location[0]
        yDiff = self.location[1] - location[1]

        if(self.color == "white"):
            colour = 1
        else:
            colour = -1    
    
        if( abs(xDiff) == abs(yDiff)):  #checks whether its in diagonal location 
            if( board[location[0]][location[1]] * colour <=0): #checks whether the location is not occupied by the own piece
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
            
                #moves in location diagonal in search of obstacle
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
    
    def get_all_moves(self, board):  
        
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
            if(board[x][y] * colour >=0):
                break
            if(board[x][y] * colour <=0):
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
            if(board[x][y] * colour >=0):
                break
            if(board[x][y] * colour <=0):
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
            if(board[x][y] * colour >=0):
                break
            if(board[x][y] * colour <= 0):
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
            if(board[x][y] * colour >= 0):
                break
            if(board[x][y] * colour <=0):
                newLocation.append([x,y])
                break 

        return newLocation


    
    @staticmethod
    def static_get_all_moves(curr_location, board):  # @DuplicatedSignature
        newLocation=[]
        x=curr_location[0]
        y=curr_location[1]
        
        colour = board[curr_location[0]][curr_location[1]]
        
        #checks for the moves in top right diagonal
        while(x<=6 and y<=6):
            x=x+1
            y=y+1
            if(board[x][y] == 0):
                newLocation.append([x,y])
                continue
            if(board[x][y] * colour >= 0):
                break
            if(board[x][y] * colour <= 0):
                newLocation.append([x,y])
                break         

        x=curr_location[0]
        y=curr_location[1]

        #checks for the moves in bottom left diagonal
        while(x>=1 and y>=1):
            x=x-1
            y=y-1
            if(board[x][y] == 0):
                newLocation.append([x,y])
                continue 
            if(board[x][y] * colour >= 0):
                break
            if(board[x][y] * colour <= 0):
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
            if(board[x][y] * colour >= 0):
                break
            if(board[x][y] * colour <= 0):
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
            if(board[x][y] * colour >= 0):
                break
            if(board[x][y] * colour <= 0):
                newLocation.append([x,y])
                break 

        return newLocation
    @staticmethod
    def static_get_capture_moves(curr_location, board):  # @DuplicatedSignature
        newLocation=[]
        x=curr_location[0]
        y=curr_location[1]
        
        colour = board[curr_location[0]][curr_location[1]]
        
        #checks for the moves in top right diagonal
        while(x<=6 and y<=6):
            x=x+1
            y=y+1
            
            if(board[x][y] * colour > 0):
                break
            if(board[x][y] * colour < 0):
                newLocation.append([x,y])
                break         

        x=curr_location[0]
        y=curr_location[1]

        #checks for the moves in bottom left diagonal
        while(x>=1 and y>=1):
            x=x-1
            y=y-1
             
            if(board[x][y] * colour > 0):
                break
            if(board[x][y] * colour < 0):
                newLocation.append([x,y])
                break 

        x=curr_location[0]
        y=curr_location[1]

        #checks for the moves in bottom right diagonal 
        while(x>=1 and y<=6):
            x=x-1
            y=y+1
             
            if(board[x][y] * colour > 0):
                break
            if(board[x][y] * colour < 0):
                newLocation.append([x,y])
                break 

        x=curr_location[0]
        y=curr_location[1]

        #checks for the moves in top left diagonal
        while(x<=6 and y>=1):
            x=x+1
            y=y-1
             
            if(board[x][y] * colour > 0):
                break
            if(board[x][y] * colour < 0):
                newLocation.append([x,y])
                break 

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

