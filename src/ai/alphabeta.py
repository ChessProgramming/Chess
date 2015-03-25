'''
Created on Mar 14, 2015

@author: Venkatesh
'''
from piece.piecemap import PieceMap

class AlphaBeta():
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
    
    def alpha_beta(self, player, state, alpha, beta, depth):
            c = self.b.isgameover(state)
            if(not c != None or depth == 0):
                return self.evolution(state)
            
            children = self.b.sucessor(player, state)
            if(player == 1):        # max player
                    for child in children:
                            score = self.alpha_beta(-1, child, alpha, beta, depth)
                            if(score >= beta):
                                    return score
                            if(score > alpha):
                                    alpha = score
                    return alpha
            else:                   # min player
                    for child in children:
                            score = self.alpha_beta(1, child, alpha, beta, depth)
                            if(score <= alpha):
                                    return score
                            if(score < beta):
                                    beta = score
                    return beta
