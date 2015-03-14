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
    def is_possible(self, location):
        '''
            location will have the new location and this method returns
            true if it is a legal move
            false if it is an illegal move
        '''
        pass
    
    @abstractmethod
    def get_all_moves(self):
        '''
            returns a list of all possible locations
        '''
        pass
        