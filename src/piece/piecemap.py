'''
Created on Mar 17, 2015

@author: Venkatesh
'''

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