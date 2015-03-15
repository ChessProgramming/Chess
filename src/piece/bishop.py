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
        
    def is_possible(self, location):
        Piece.is_possible(self, location)
        
    def get_all_moves(self):
        Piece.get_all_moves(self)
        
        