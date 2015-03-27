'''
Created on Mar 14, 2015

@author: Venkatesh
'''
from piece.piecemap import PieceMap

class AlphaBeta():
    def __init__(self, board):
        self.b = board
        
    def evolution(self, board, player):
        materialscore = wmobility = bmobility = 0
        if(self.b.playercolor == "white"):
            if(player > 0):
                pawn_move = -1
            else:
                pawn_move = 1
        else:
            if(player < 0):
                pawn_move = 1                        
            else:
                pawn_move = -1
                
        for i in range(8):
            for j in range(8):
                if(player > 0):
                    if(board[i][j] > 0):
                        materialscore +=  PieceMap.getPoints(board[i][j])
                    elif(board[i][j] < 0):
                        materialscore -=  PieceMap.getPoints(board[i][j])
                    f = PieceMap.getFun(board[i][j])
                    moves = []
                    if(abs(board[i][j]) == 6):
                        moves = f([i,j],board,pawn_move)
                    elif(abs(board[i][j] != 0)):
                        moves = f([i,j],board)
                    wmobility += len(moves)
                else:
                    if(board[i][j] > 0):
                        materialscore -=  PieceMap.getPoints(board[i][j])
                    elif(board[i][j] < 0):
                        materialscore +=  PieceMap.getPoints(board[i][j])
                    f = PieceMap.getFun(board[i][j])
                    moves = []
                    if(abs(board[i][j]) == 6):
                        moves = f([i,j],board,pawn_move)
                    elif(abs(board[i][j]) != 0):
                        moves = f([i,j],board)
                    bmobility += len(moves)
                    
        mobilityscore = 0.1 * (wmobility - bmobility) * player
        return (materialscore + mobilityscore) * player
    
    def alpha_beta(self, player, state, alpha, beta, depth):
            c = self.b.isgameover(state, player)
            if(not c != None or depth == 0):
                return self.evolution(state, player)
            
            children = self.b.successor(player, state)
            if(player == 1):        # max player
                    for child in children:
                            score = self.alpha_beta(-1, child, alpha, beta, depth-1)
                            if(score >= beta):
                                    return score
                            if(score > alpha):
                                    alpha = score
                    return alpha
            else:                   # min player
                    for child in children:
                            score = self.alpha_beta(1, child, alpha, beta, depth-1)
                            if(score <= alpha):
                                    return score
                            if(score < beta):
                                    beta = score
                    return beta
                
    def quiescence(self, player, state, alpha, beta):
        stand_pat = self.evolution(state, player)
        if(stand_pat >= beta):
            return beta
        if(alpha < stand_pat):
            alpha = stand_pat
                
        children = self.b.successor(player, state)
        for child in children:
            score = -self.quiescence(-player, child, -alpha, -beta)
            
            if(score >= beta):
                return beta
            if(score > alpha):
                alpha = score
        return alpha    
    