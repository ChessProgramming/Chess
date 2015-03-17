'''
Created on Mar 14, 2015

@author: Venkatesh
'''

from tkinter import Frame
from game.cell import Cell
from piece.rook import Rook
from piece.queen import Queen

class Board(Frame):
    '''
        It is the collection of 64 Cells
    '''


    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
    
        self.board = [[0 for _ in range(8)] for _ in range(8)]
        flag = True
    
        for i in range(8):
            for j in range(8):
                if(flag == True):
                    b = Cell(self)
                    b.config(piece=Rook("white", [i , j]), location=[i , j], color="white")
                    b.grid(row=i, column=j)
                else:
                    b = Cell(self)
                    b.config(piece=Queen("white", [i , j]), location=[i , j], color="black")
                    b.grid(row=i, column=j)
                flag = not flag
            flag = not flag
        
    def getboard(self):
        return self.board
    