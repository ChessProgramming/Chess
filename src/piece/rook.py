'''
Created on Mar 14, 2015

@author: Venkatesh
'''
from piece.piece import Piece

class Rook(Piece):
    '''
        Rook is a piece it can move horizontally and vertically
    '''


    def __init__(self, color, location):
        self.color = color
        self.location = location
        self.image = None           # have to be updated with the corresponding image
        
    def is_possible(self, location):
        Piece.is_possible(self, location)
        
    def get_all_moves(self):
        Piece.get_all_moves(self)