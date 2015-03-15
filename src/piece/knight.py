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
        
    def is_possible(self, location):
        Piece.is_possible(self, location)
        
    def get_all_moves(self):
        Piece.get_all_moves(self)