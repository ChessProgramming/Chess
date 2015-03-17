'''
Created on Mar 14, 2015

@author: Venkatesh
'''
import abc
from abc import ABCMeta, abstractmethod

class Piece(abc):
    '''
        Abstract base class for all the pieces
        
        A piece should have color and current location
        Its type will be identified implicitly with the help of subclasses
    '''

    __metaclass__ = ABCMeta
    
    @abstractmethod
    def is_possible(self, location, board):
        '''
            location will have the new location
            board is a 2d array with -1 as black piece 
            0 as empty space and 1 as white piece
            and this method returns
            true if it is a legal move
            false if it is an illegal move
        '''
        pass
    
    @abstractmethod
    def get_all_moves(self, board):
        '''
            board is a 2d array with -1 as black piece 
            0 as empty space and 1 as white piece
            returns a list of all possible locations
        '''
        pass
        
    @abstractmethod
    def getimage(self):
        '''
            returns the PhotoImage object of the current piece 
        '''
        pass
    
    @abstractmethod
    def setlocation(self, location):
        pass