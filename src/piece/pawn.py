'''
Created on Mar 14, 2015

@author: Venkatesh
'''
from piece.image import get_image
from piece.piece import Piece


class Pawn(Piece):
    '''
    Pawn is a piece and it can move only forward
    '''


    def __init__(self, color, location, move):
        self.color = color
        self.location = location
	self.move = move   # +1 when it moves forward & -1 backward
        
        if(color == "white"):
            self.image = get_image("wP")
        else:
            self.image = get_image("bP")
        
    def is_possible(self, location):
        Piece.is_possible(self, location)
	if(self.move == 1):
		xDiff = location[0] - self.location[0]
		yDiff = location[1] - self.location[1]
		start = 1
	else:
		xDiff = self.location[0] - location[0]
                yDiff = self.location[1] - location[1]
		start = 6

	if(self.location[0]==start and yDiff==0 and xDiff==2):
		return True

	if(xDiff==1 and (yDiff==0 or yDiff==-1 or yDiff==1)):
		return True

	return False
        
    def get_all_moves(self):
        Piece.get_all_moves(self)
        
        
