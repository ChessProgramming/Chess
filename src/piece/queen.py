'''
Created on Mar 14, 2015

@author: Venkatesh
'''
from piece.image import get_image
from piece.piece import Piece


class Queen(Piece):
    '''
        Queen is a piece and it can move in all the directions
    '''


    def __init__(self, color, location):
        self.color = color
        self.location = location
        
        if(color == "white"):
            self.image = get_image("wQ")
        else:
            self.image = get_image("bQ")
        
    def is_possible(self, location):
        Piece.is_possible(self, location)
        
    def get_all_moves(self):
        Piece.get_all_moves(self)