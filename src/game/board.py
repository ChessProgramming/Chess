'''
Created on Mar 14, 2015

@author: Venkatesh
'''

from tkinter import Tk
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
        flag = True
        self.cellarray = []
        
        self.touched = False
        self.touched_location = []
    
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
    
    def isgameover(self):
        pass
    
    def ischeckmate(self):
        pass
    
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
                    if(not self.ischeck(location)):
                        self.cellarray[location[0]][location[1]].setPiece(piece)
                        piece.setlocation(location)
                        self.cellarray[self.touched_location[0]][self.touched_location[1]].setPiece(None)
                    else:
                        self.board[self.touched_location[0]][self.touched_location[1]] = start
                        self.board[location[0]][location[1]] = end
    