'''
Created on Mar 14, 2015

@author: Venkatesh
'''

from game.cell import Cell
from piece.king import King
from piece.rook import Rook
from piece.queen import Queen
from piece.bishop import Bishop
from piece.knight import Knight
from piece.pawn import Pawn

from tkinter import Toplevel
import sys
from ai.alphabeta import AlphaBeta
from piece.piecemap import PieceMap
from ai.minimax import MiniMax


class Board():
    '''
        It is the collection of 64 Cells
    '''


    def __init__(self, root):
        self.cellarray = []
        self.touched = False
        self.touched_location = []
        self.algo = MiniMax(self)
    
        self.is_white_move = True
        flag = True
        for i in range(8):
            self.cellarray.append([])
            
            for j in range(8):
                b = Cell(root)
                if(flag == True):
                    b.config(location=[i , j], color="white", command = self.cellcallback)
                    b.grid(row=i, column=j)
                else:
                    b.config(location=[i , j], color="black", command = self.cellcallback)
                    b.grid(row=i, column=j)
                    
                self.cellarray[i].append(b)
                flag = not flag
            flag = not flag
    
    def initboard(self, **kwargs):
        self.playercolor = kwargs["playercolor"]
        
        if(self.playercolor == "white"):
            self.board = [
                          [-3, -5, -4, -2, -1, -4, -5, -3],
                          [-6, -6, -6, -6, -6, -6, -6, -6],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [6, 6, 6, 6, 6, 6, 6, 6],
                          [3, 5, 4, 2, 1, 4, 5, 3]
                         ]
        else:
            self.board = [
                          [3, 5, 4, 1, 2, 4, 5, 3],
                          [6, 6, 6, 6, 6, 6, 6, 6],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [-6, -6, -6, -6, -6, -6, -6, -6],
                          [-3, -5, -4, -1, -2, -4, -5, -3]
                         ]
                   
        for i in range(8):
            for j in range(8):
                color = "white"
                if(self.board[i][j] < 0):
                    color = "black"
                    
                if(abs(self.board[i][j]) == 1):
                    self.cellarray[i][j].setPiece(King(color, [i,j]))
                elif(abs(self.board[i][j]) == 2):
                    self.cellarray[i][j].setPiece(Queen(color, [i,j]))
                elif(abs(self.board[i][j]) == 3):
                    self.cellarray[i][j].setPiece(Rook(color, [i,j]))
                elif(abs(self.board[i][j]) == 4):
                    self.cellarray[i][j].setPiece(Bishop(color, [i,j]))
                elif(abs(self.board[i][j]) == 5):
                    self.cellarray[i][j].setPiece(Knight(color, [i,j]))
                elif(abs(self.board[i][j]) == 6):
                    if(self.playercolor == "white"):
                        if(color == "white"):
                            self.cellarray[i][j].setPiece(Pawn(color, [i,j], -1))
                        else:
                            self.cellarray[i][j].setPiece(Pawn(color, [i,j], 1))
                    else:
                        if(color == "white"):
                            self.cellarray[i][j].setPiece(Pawn(color, [i,j], 1))
                        else:
                            self.cellarray[i][j].setPiece(Pawn(color, [i,j], -1))
                            
                elif(abs(self.board[i][j]) == 0):
                    self.cellarray[i][j].setPiece(None)
                  
    def getboard(self):
        return self.board
    
    
    def isgameover(self, board, colour):  
        if(self.playercolor == "white"):
            if(colour > 0):
                pawn_move = -1
            else:
                pawn_move = 1
        else:
            if(colour < 0):
                pawn_move = 1                        
            else:
                pawn_move = -1
        if(colour < 0): # when satisfied want to check whether white king is locked
            for i in range(8):
                for j in range(8):
                    if(board[i][j] > 0):
                        f = PieceMap.getFun(board[i][j])
                        if(abs(board[i][j]) == 6):
                            moves = f([i,j],board,pawn_move)
                        else:
                            moves = f([i,j],board)
                        start = board[i][j]
                        for m in moves:
                            #changing the board and sending to if check and then again reversing the board
                            end = board[m[0]][m[1]]
                            board[m[0]][m[1]] = start
                            board[i][j] = 0
                            if(not self.ischeck(board,m)):
                                board[i][j] = start
                                board[m[0]][m[1]] = end
                                return False
                            else:
                                board[i][j] = start
                                board[m[0]][m[1]] = end
                                
        elif(colour > 0): # when satisfied want to check whether black king is locked
            for i in range(8):
                for j in range(8):
                    if(board[i][j] < 0):
                        f = PieceMap.getFun(board[i][j])
                        if(abs(board[i][j]) == 6):
                            moves = f([i,j],board,pawn_move)
                        else:
                            moves = f([i,j],board)
                        start = board[i][j]
                        for m in moves:
                            #changing the board and sending to if check and then again reversing the board
                            end = board[m[0]][m[1]]
                            board[m[0]][m[1]] = start
                            board[i][j] = 0
                            if(not self.ischeck(board, m)):
                                board[i][j] = start
                                board[m[0]][m[1]] = end
                                return False
                            else:
                                board[i][j] = start
                                board[m[0]][m[1]] = end
            
        return True        
            
    def ischeck(self, board, location):
        if(self.playercolor == "white"):
            if(board[location[0]][location[1]] > 0):
                pawn_move = -1
            else:
                pawn_move = 1
        else:
            if(board[location[0]][location[1]] < 0):
                pawn_move = 1                        
            else:
                pawn_move = -1
        for i in range(8):
            for j in range(8):
                if(board[i][j] == -1):
                    bK = [i,j]
                elif(board[i][j] == 1):
                    wK = [i,j]
        if(board[location[0]][location[1]] < 0):   #when satisfied  want to check whether black king in danger
            for i in range(8):
                for j in range(8):
                    if(board[i][j] > 0  and not (i == location[0] and j == location[1])):
                        f = PieceMap.getFun(board[i][j])
                        if(abs(board[i][j]) == 6):
                            moves = f([i,j],board,pawn_move)
                        else:
                            moves = f([i,j],board)
                        if(bK in moves):
                            return True
        elif(board[location[0]][location[1]] > 0):  #when satisfied  want to check whether white king in danger
            for i in range(8):
                for j in range(8):
                    if(board[i][j] < 0 and not (i == location[0] and j == location[1])):
                        f = PieceMap.getFun(board[i][j])
                        if(abs(board[i][j]) == 6):
                            moves = f([i,j],board,pawn_move)
                        else:
                            moves = f([i,j],board)
                        if(wK in moves):
                            return True
        return False
        
    def sucessor(self, colour, board): 
        allmoves = []
        if(self.playercolor == "white"):
            if(colour > 0):
                pawn_move = -1
            else:
                pawn_move = 1
        else:
            if(colour < 0):
                pawn_move = 1                        
            else:
                pawn_move = -1
                
        if(colour > 0): 
            for i in range(8):
                for j in range(8):
                    if(board[i][j] > 0):
                        start = board[i][j]
                        f = PieceMap.getFun(board[i][j])
                        if(abs(board[i][j]) == 6):
                            moves = f([i,j],board,pawn_move)
                        else:
                            moves = f([i,j],board)
                        for move in moves:
                            end = board[move[0]][move[1]]
                            board[i][j] = 0
                            board[move[0]][move[1]] = start
                            if(not self.ischeck(board, move)):
                                allmoves.append(move)
                            board[i][j] = start
                            board[move[0]][move[1]] = end
        elif(colour < 0):
            for i in range(8):
                for j in range(8):
                    if(board[i][j] < 0):
                        start = board[i][j]
                        f = PieceMap.getFun(board[i][j])
                        if(abs(board[i][j]) == 6):
                            moves = f([i,j],board,pawn_move)
                        else:
                            moves = f([i,j],board)
                        for move in moves:
                            end = board[move[0]][move[1]]
                            board[i][j] = 0
                            board[move[0]][move[1]] = start
                            if(not self.ischeck(board, move)):
                                allmoves.append(move)
                            board[i][j] = start
                            board[move[0]][move[1]] = end
                            
        return allmoves
                        
        
    def isstalemate(self):
        pass
    
    def getspecialmoves(self):
        pass
    
    def cellcallback(self, location):
        if(self.touched == False):
            if(self.isvalidtouch(location)):
                self.touched = True
                self.touched_location = location
                self.cellarray[location[0]][location[1]].changeColor("#ADD6FF")
                self.possible_moves = self.cellarray[location[0]][location[1]].getPiece().get_all_moves(self.board)
                for loc in self.possible_moves:
                    self.cellarray[loc[0]][loc[1]].changeColor("#CCFF99")  #80FF80  
        else:
            self.touched = False
            self.cellarray[self.touched_location[0]][self.touched_location[1]].changeColor()
            piece = self.cellarray[self.touched_location[0]][self.touched_location[1]].getPiece()
            for loc in self.possible_moves:
                self.cellarray[loc[0]][loc[1]].changeColor()
                
            if(piece != None):
                start = self.board[self.touched_location[0]][self.touched_location[1]]
                end = self.board[location[0]][location[1]]
                if(piece.is_possible(location, self.board)):
                    self.board[location[0]][location[1]] = start
                    self.board[self.touched_location[0]][self.touched_location[1]] = 0

                    if(not self.ischeck(self.board, location)):
                        self.cellarray[location[0]][location[1]].setPiece(piece)
                        piece.setlocation(location)
                        self.cellarray[self.touched_location[0]][self.touched_location[1]].setPiece(None)
                    else:
                        self.board[self.touched_location[0]][self.touched_location[1]] = start
                        self.board[location[0]][location[1]] = end
                           
                    if(self.isgameover(self.board, self.board[location[0]][location[1]])):
                        for i in range(8):
                            for j in range(8):
                                if(self.board[i][j] == -1):
                                    bK = [i,j]
                                elif(self.board[i][j] == 1):
                                    wK = [i,j]
                        if(self.board[location[0]][location[1]] > 0):
                            oppo = bK
                        else:
                            oppo = wK
                            
                        if(self.ischeck(self.board, oppo)):
                            print("checkmate")
                            top = Toplevel()
                            top.after_cancel(sys.exit(0))
                        else:
                            print("stalemate")
                            self.is_white_move = not self.is_white_move
                    
                    self.is_white_move = not self.is_white_move
                    
                    if(self.playercolor == "white" and not self.is_white_move):
                        ''' computer is a black(min) player and it has to play '''
                        children = self.sucessor(-1, self.board)
                        print(len(children))
                    elif(self.playercolor == "black" and self.is_white_move):
                        ''' computer is a white(max) player and it has to play '''
                        
                    
    def isvalidtouch(self, location):
        piece = self.cellarray[location[0]][location[1]].getPiece()
        if(piece != None):
            if(piece.getcolor() == "white" and self.is_white_move):
                return True
            if(not(piece.getcolor() == "white" or self.is_white_move)):
                return True
        return False