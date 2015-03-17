'''
Created on Mar 14, 2015

@author: Venkatesh
'''
from piece import *
from tkinter import PhotoImage


class Queen(Piece):
    '''
        Queen is a piece and it can move in all the directions
    '''


    def __init__(self, color, location):
        self.color = color
        self.location = location
        
        if(color == "white"):
            self.image = PhotoImage(file = "../../img/wQ.png")
        else:
            self.image = PhotoImage(file = "../../img/bQ.png")
        

    def is_possible(self, location,board):
        xDiff = self.location[0] - location[0]
        yDiff = self.location[1] - location[1]
        if(self.color == "white"):
            colour = 1
        else:
            colour = -1

        #check rook moves
        if((xDiff == 0 or yDiff == 0) and (not(xDiff == 0 and yDiff == 0))): #check whether its in rook move
            if(board[location[0]][location[1]] != colour):   #check whether the location is not occupied by own piece
                x = self.location[0]
                y = self.location[1]
                xinc=0
                yinc =0
                
                if(x  > location[0]):
                    xinc =-1
                else:
                    xinc = 1
                
                if(y > location[1]):
                    yinc = -1
                else:
                    yinc = 1

            #moves in vertical direction in search of obstracle in between

                while(xinc !=0 and x != location[0]):
                    x = x +    xinc
                    if(x != location[0]):
                        if(board[x][location[1]]!=0):
                            return False    
            #moves in horizontal direction in search of obstracle in between
            
                while(yinc !=0 and y != location[1]):
                    y = y + yinc
                    if(y != location[1]):
                        if(board[location[0]][y] != 0):
                            return False
            else:
                return False

        #check bishop move
        if( abs(xDiff) == abs(yDiff)):  #checks whether its in diagonal location 
            if( board[location[0]][location[1]] != colour): #cheks whether the location is not occupied by the own piece
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
    
    def get_all_moves(self,board):
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
    
        # rook moves
        #checks for the moves in down direction
        while(x > 0):
            x -= 1
            if(board[x][self.location[1]] == 0):
                newLocation.append([x,self.location[1]])
                continue    
            if(board[x][self.location[1]] == colour):
                break
            if(board[x][self.location[1]] == colour*-1):
                newLocation.append([x,self.location[1]])
                break
        
        x = self.location[0]
        
        #checks for the moves in up direction
        while(x < 7):
            x +=1
            if(board[x][self.location[1]] == 0):
                newLocation.append([x,self.location[1]])
                continue
            if(board[x][self.location[1]] == colour):
                break 
            if(board[x][self.location[1]] == colour*-1):
                newLocation.append([x,self.location[1]])
                break
    
        #checks for the moves in left direction
        while(y > 0):
            y -= 1
            if(board[self.location[0]][y] == 0):
                newLocation.append([self.location[0],y])
                continue
            if(board[self.location[0]][y] == colour):
                break 
            if(board[self.location[0]][y] == colour*-1):
                newLocation.append([self.location[0],y])
                break
        
        y = self.location[1]
    
        #checks for the moves right direction
        while(y < 7):
            y +=1
            if(board[self.location[0]][y] == 0):
                newLocation.append([self.location[0],y])
                continue
            if(board[self.location[1]][y] == colour):
                break
            if(board[self.location[1]][y] == colour*-1):
                newLocation.append([self.location[0],y])
                break
    
        return newLocation


    def getimage(self):
        return self.image
    
    
    def setlocation(self, location):
        self.location = location