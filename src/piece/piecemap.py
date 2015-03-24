'''
Created on Mar 17, 2015

@author: Venkatesh
'''
from piece.king import King
from piece.queen import Queen
from piece.rook import Rook
from piece.bishop import Bishop
from piece.knight import Knight
from piece.pawn import Pawn

class PieceMap(object):
    '''
        Maps each piece with a number
        
                  White     Black
        King        1        -1
        Queen       2        -2
        Rook        3        -3
        Bishop      4        -4
        Knight      5        -5
        Pawn        6        -6
    '''
    
    @staticmethod
    def getnumber(piece):
        color = 1
        if(piece[0] == "b"):
            color = -1
            
        if(piece[1] == "K"):
            return color*1
        elif(piece[1] == "Q"):
            return color*2
        elif(piece[1] == "R"):
            return color*3
        elif(piece[1] == "B"):
            return color*4
        elif(piece[1] == "N"):
            return color*5
        elif(piece[1] == "P"):
            return color*6
        
    @staticmethod
    def getPoints(self, number):
        if(abs(number) == 1):
            return 200;
        elif(abs(number) == 2):
            return 9;
        elif(abs(number) == 3):
            return 5;
        elif(abs(number) == 4 or abs(number) == 5):
            return 3;
    
    @staticmethod   
    def getFun(number):
        if(abs(number) == 1):
            return King.static_get_all_moves
        elif(abs(number) == 2):
            return Queen.static_get_all_moves
        elif(abs(number) == 3):
            return Rook.static_get_all_moves
        elif(abs(number) == 4):
            return Bishop.static_get_all_moves
        elif(abs(number) == 5):
            return Knight.static_get_all_moves
        elif(abs(number) == 6):
            return Pawn.static_get_all_moves