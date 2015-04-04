'''
Created on Mar 14, 2015

@author: Venkatesh
'''
from piece.piecemap import PieceMap

class MiniMax():
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
    
    def minmax(self, player, state, depth):
            c = self.b.isgameover(state, player)
            if(c or depth == 0):
                return self.evolution(state, player)
    
            children = self.b.successor(player, state)
            if(player == 1):        # max player
                    return max([self.minmax(-1, s, depth - 1) for s in children])
            else:                   # min player
                    return min([self.minmax(1, s, depth - 1) for s in children])

    def quiescence(self, player, state, alpha, beta):
        stand_pat = self.evolution(state, player) * player
        if(stand_pat >= beta):
            return beta
        if(alpha < stand_pat):
            alpha = stand_pat
                
        children = self.b.capture_successor(player, state)
        for child in children:
            score = -self.quiescence(-player, child, -beta, -alpha)
            
            if(score >= beta):
                return beta
            if(score > alpha):
                alpha = score
        
        return alpha
    
    def strategicquiescence(self, player, state, alpha, beta):
        bestval = self.evolution(state, player) * player
        print(" bestval = %s" % (bestval))
        [print(i) for i in state]
        '''if(bestval >= beta):
            return bestval
        if(bestval > alpha):
            alpha = bestval
            
        children = self.b.capture_successor(player, state)
        for child in children:
            eval = self.evolution(child, -player) * -player
            if(eval > alpha):
                actval = -self.strategicquiescence(-player, child, -beta, -alpha)
                if(actval > bestval):
                    bestval = actval
                    if(bestval >= beta): return bestval
                    if(bestval > alpha): alpha = bestval
                    
            elif(eval > bestval): bestval = eval'''
                
        return bestval
    
    def alpha_beta(self, player, state, alpha, beta, depth):
        if(depth <= 0):
            return self.evolution(state, player)
        
        children = self.b.capture_successor(player, state)
        
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
                        player = 1
                        score = self.alpha_beta(1, child, alpha, beta, depth-1)
                        if(score <= alpha):
                                return score
                        if(score < beta):
                                beta = score
                return beta