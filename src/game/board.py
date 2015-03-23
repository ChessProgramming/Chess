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

class Board():
    '''
        It is the collection of 64 Cells
    '''


    def __init__(self, root):
        self.cellarray = []
        self.touched = False
        self.touched_location = []
    
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
    
    
    def isgameover(self, location):  
        if(self.board[location[0]][location[1]] < 0): # when satisfied want to check whether white king is locked
            for i in range(8):
                for j in range(8):
                    if(self.board[i][j] > 0):
                        moves = self.cellarray[i][j].getPiece().get_all_moves(self.board)
                        start = self.board[i][j]
                        for m in moves:
                            #changing the board and sending to if check and then again reversing the board
                            end = self.board[m[0]][m[1]]
                            self.board[m[0]][m[1]] = start
                            self.board[i][j] = 0
                            if(not self.ischeck(m)):
                                self.board[i][j] = start
                                self.board[m[0]][m[1]] = end
                                return False
                            else:
                                self.board[i][j] = start
                                self.board[m[0]][m[1]] = end
                                
        elif(self.board[location[0]][location[1]] > 0): # when satisfied want to check whether black king is locked
            for i in range(8):
                for j in range(8):
                    if(self.board[i][j] < 0):
                        moves = self.cellarray[i][j].getPiece().get_all_moves(self.board)
                        start = self.board[i][j]
                        for m in moves:
                            #changing the board and sending to if check and then again reversing the board
                            end = self.board[m[0]][m[1]]
                            self.board[m[0]][m[1]] = start
                            self.board[i][j] = 0
                            if(not self.ischeck(m)):
                                self.board[i][j] = start
                                self.board[m[0]][m[1]] = end
                                return False
                            else:
                                self.board[i][j] = start
                                self.board[m[0]][m[1]] = end
            
        return True        
            
    
    def ischeck(self, location):
        for i in range(8):
            for j in range(8):
                if(self.board[i][j] == -1):
                    bK = [i,j]
                elif(self.board[i][j] == 1):
                    wK = [i,j]
        if(self.board[location[0]][location[1]] < 0):   #when satisfied  want to check whether black king in danger
            for i in range(8):
                for j in range(8):
                    if(self.board[i][j] > 0  and not (i == location[0] and j == location[1])):
                        if(bK in self.cellarray[i][j].getPiece().get_all_moves(self.board)):
                            return True
        elif(self.board[location[0]][location[1]] > 0):  #when satisfied  want to check whether white king in danger
            for i in range(8):
                for j in range(8):
                    if(self.board[i][j] < 0 and not (i == location[0] and j == location[1])):
                        if(wK in self.cellarray[i][j].getPiece().get_all_moves(self.board)):
                            return True
        return False
        
    
    def isstalemate(self):
        pass
    
    def getspecialmoves(self):
        pass
    
    def cellcallback(self, location):
        if(self.touched == False):
            if(self.isvalidtouch(location)):
                self.touched = True
                self.touched_location = location
                self.cellarray[location[0]][location[1]].changeColor(self.touched)
        else:
            self.touched = False
            self.cellarray[self.touched_location[0]][self.touched_location[1]].changeColor()
            piece = self.cellarray[self.touched_location[0]][self.touched_location[1]].getPiece() 
            if(piece != None):
                start = self.board[self.touched_location[0]][self.touched_location[1]]
                end = self.board[location[0]][location[1]]
                if(piece.is_possible(location, self.board)):
                    self.board[location[0]][location[1]] = start
                    self.board[self.touched_location[0]][self.touched_location[1]] = 0
<<<<<<< HEAD
                    if(not self.ischeck(location)):
                        self.cellarray[location[0]][location[1]].setPiece(piece)
                        piece.setlocation(location)
                        self.cellarray[self.touched_location[0]][self.touched_location[1]].setPiece(None)
                    else:
                        self.board[self.touched_location[0]][self.touched_location[1]] = start
                        self.board[location[0]][location[1]] = end
                           
                    if(self.isgameover(location)):
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
                            
                        if(self.ischeck(oppo)):
                            print("checkmate")
                        else:
                            print("stalemate")
    
=======
                    self.is_white_move = not self.is_white_move
                    
    def isvalidtouch(self, location):
        piece = self.cellarray[location[0]][location[1]].getPiece()
        if(piece != None):
            if(piece.getcolor() == "white" and self.is_white_move):
                return True
            if(not(piece.getcolor() == "white" or self.is_white_move)):
                return True
>>>>>>> added isvalid move additional ui updates
