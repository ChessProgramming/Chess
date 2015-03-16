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

	if( ( abs(xDiff) == 1 and abs(yDiff) == 2 ) or ( abs(xDiff) == 2 and abs(yDiff) == 1 ) ): #check wh
		return True

	return False
        
    def get_all_moves(self):
        Piece.get_all_moves(self)
