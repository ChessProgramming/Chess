'''
Created on Mar 14, 2015

@author: Venkatesh
'''
from piece.image import get_image
from piece.piece import Piece


class Knight(Piece):
    '''
        Knight is a piece which can move in L direction
    '''


    def __init__(self, color, location):
        self.color = color
        self.location = location
        
        if(color == "white"):
            self.image = get_image("wN")
        else:
            self.image = get_image("bN")
        
    def is_possible(self, location, board):  
        Piece.is_possible(self, location, board)
        xDiff = self.location[0] - location[0]
        yDiff = self.location[1] - location[1]
    
        if(self.color == "white"):
            colour = 1
        else:
            colour = -1  
              
    
        if( ( abs(xDiff) == 1 and abs(yDiff) == 2 ) or ( abs(xDiff) == 2 and abs(yDiff) == 1 ) ): #check whether its knight move 
            if(board[location[0]][location[1]] != colour): #checks whether the location is not occupied by the own piece
                return True

        return False        
    
    def get_all_moves(self, board):
        Piece.get_all_moves(self, board)
        lis  = [-1,-2,1,2]
        newLocation = []
        if(self.color == "white"):
            colour = 1
        else:
            colour = -1
            
        for i in lis:
            for j in lis:
                if(abs(i)!=abs(j)):
                    if(self.loaction[0]+i >= 0 and self.location[0]+i <= 7 and self.loaction[1]+j >= 0 and self.location[1]+j <= 7 ): #checks boundary condition
                        if(board[self.location[0]+i][self.location[1]+j] != colour): #checks whether the location is not occupied by the own piece
                            newLocation.append([self.location[0]+i,self.location[1]+j])
        return newLocation
        

    def getimage(self):
        return self.image
    
    
    def setlocation(self, location):
        self.location = location