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
        for i in range(8):
            self.cellarray.append([])
            
            for j in range(8):
                b = Cell(root)
                if(flag == True):
                    b.config(location=[i , j], color="white")
                    b.grid(row=i, column=j)
                else:
                    b.config(location=[i , j], color="black")
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
                    self.cellarray[i][j].setPiece(Knight(color, [i,j]))
                    
    def getboard(self):
        return self.board
    
if __name__ == "__main__":
    root = Tk()
    board = Board(root)
    board.initboard(playercolor = "black")
    root.mainloop()