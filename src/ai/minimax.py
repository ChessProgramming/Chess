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
                    if(player > 0):
                        materialscore +=  PieceMap.getPoints(board[i][j])
                    elif(player < 0):
                        materialscore -=  PieceMap.getPoints(board[i][j])
                    f = PieceMap.getFun(board[i][j])
                    moves = []
                    if(abs(board[i][j]) == 6):
                        moves = f([i,j],board,pawn_move)
                    elif(abs(board[i][j] != 0)):
                        moves = f([i,j],board)
                    wmobility += len(moves)
                else:
                    if(player > 0):
                        materialscore -=  PieceMap.getPoints(board[i][j])
                    elif(player < 0):
                        materialscore +=  PieceMap.getPoints(board[i][j])
                    moves = []
                    if(abs(board[i][j]) == 6):
                        moves = f([i,j],board,pawn_move)
                    else:
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
