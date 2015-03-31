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
        stand_pat = self.evolution(state, player) * player
        if(stand_pat >= beta):
            return stand_pat
        if(alpha < stand_pat):
            alpha = stand_pat
                
        children = self.b.successor(player, state)
        for child in children:
            evalp = self.evalplus(state, player)
            if(evalp > alpha):
                score = -self.quiescence(-player, child, -alpha, -beta)
                if(score > stand_pat):
                    stand_pat = score
                    if(score >= beta):
                        return stand_pat
                    if(score > alpha):
                        alpha = stand_pat
            elif(evalp > stand_pat):
                stand_pat = evalp
        return stand_pat
    
    def quiescence1(self, player, state, alpha, beta, depth):
        best = self.evolution(state, player) * player
        if(best >= beta):
            return best
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
                if(state[i][j] * player > 0):
                    f = PieceMap.getCaptureFun(state[i][j])
                    moves = []
                    if(abs(state[i][j]) == 6):
                        moves = f([i,j],state,pawn_move)
                    elif(abs(state[i][j] != 0)):
                        moves = f([i,j],state)
                    if(depth <= 0 and len(moves) <= 0):
                        continue
                    for move in moves:
                        t = state[move[0]][move[1]]
                        state[move[0]][move[1]] = state[i][j]
                        temp = -self.quiescence1(-player, [[x for x in y] for y in state], -beta, max(alpha, best), depth-1)
                        state[move[0]][move[1]] = t
                        best = max(temp, best)
                        if(best >= beta):
                            return best
        return best
    
    def mc_prune(self, player, state, beta, depth, cut, M, C, R):
        c = self.b.isgameover(state, player)
        if(not c != None or depth == 0):
            return self.evolution(state, player)
            #return self.quiescence(player, state, beta-1, beta)
        
        children = self.b.successor(player, state)
        if(depth >= R and cut):
            c = 0
            i = 0
            for child in children:
                if(i >= M):
                    break
                
                score = -self.mc_prune(-player, child, 1-beta, depth-1-R, not cut, M, C, R)
                if(score >= beta):
                    c += 0
                    if(c == C):
                        return beta
                i += 1
                
        for child in children:
            score = -self.mc_prune(-player, child, 1-beta, depth-1, not cut, M, C, R)
            if(score >= beta):
                return beta
            
        
        return beta-1
        
    def negaCstar(self, player, state, mini, maxi, depth):  
        score = mini
        while(min != maxi):
            alpha = (mini + maxi) / 2
            score = self.alpha_beta(player, state, alpha, alpha+1, depth)
            if(score > alpha):
                mini = score
            else:
                maxi = score                
        return score
    
    def negascout(self, player, state, alpha, beta, depth, W):
        if(depth <= 0):
            return self.evolution(state, player)
        children = self.b.successor(player, state)
        
        a = alpha
        b = beta
        
        i = 0
        for child in children:
            if(i > W):
                break
            t = -self.negascout(-player, child, -b, -a, depth-1, W)
            if ( (t > a) and (t < beta) and (depth > 1) ):
                a = -self.negascout(-player, child, -beta, -t, depth-1, W)
            a = max(a, t)
            if(a >= beta):
                return a
            b = a+1
            i += 1
        return a
    
    def evalplus(self, board, player):
        '''if(self.b.ischeck(board, player)):
            return float('Inf')
            '''
        return self.evolution(board, player)