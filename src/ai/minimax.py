'''
Created on Mar 14, 2015

@author: Venkatesh
'''
from piece.piecemap import PieceMap

class MiniMax():
    def __init__(self, board):
        self.b = board
        
    def evolution(self, board):
        value = 0
        for i in range(8):
            for j in range(9):
                if(board[i][j] > 0):
                    value +=  PieceMap.getPoints(board[i][j])
                elif(board[i][j] < 0):
                    value -=  PieceMap.getPoints(board[i][j])
        return value
    
    def minmax(self, player, state, depth):
            c = self.b.isgameover(state)
            if(c or depth == 0):
                return self.evolution(state)
    
            children = successor(player, state)
            if(player == 1):        # max player
                    return max([self.minmax(2, s, depth - 1) for s in children])
            else:                   # min player
                    return min([self.minmax(1, s, depth - 1) for s in children])
