'''
Created on Mar 14, 2015

@author: Venkatesh
'''
from piece.piece import Piece
from piece.image import get_image

class Bishop(Piece):
    '''
        Bishop is a piece and it moves diagonally :p
    '''

    def __init__(self, color, location):
        self.color = color
        self.location = location
        
        if(color == "white"):
            self.image = get_image("wB")
        else:
            self.image = get_image("bB")

    
    def is_possible(self, location, board):        
        Piece.is_possible(self, location, board)
    
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

    def get_all_moves(self, board):
        Piece.get_all_moves(self, board)
        newLocation=[]
        x=self.loaction[0]
        y=self.location[1]
    
        if(self.color == "white"):
            colour = 1
        else:
            colour = -1

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

        x=self.loaction[0]
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

        x=self.loaction[0]
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

        x=self.loaction[0]
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

