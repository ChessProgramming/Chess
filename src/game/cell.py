'''
Created on Mar 14, 2015

@author: Venkatesh
'''

from tkinter import *  # @UnusedWildImport
from piece.rook import Rook
from piece.queen import Queen

class Cell(Frame):
    '''
        A Cell is a single unit in a chess board
        
        A cell is a Button
    '''

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.button = Button(self, compound="left", command=lambda:print(self.location), # command have to be given properly
                             width = 85, height = 85)
        self.button.pack(side="top")

    def config(self, **kwargs):
        self.piece = kwargs['piece']
        self.location = kwargs['location']
        self.color = kwargs['color']
        
        self.button.config(image = self.piece.getimage())
        
        if(self.color == "white"):
            self.button.config(bg = "#FFD39B")
        else:
            self.button.config(bg = "#8B4513")
            
            
if __name__ == "__main__":
    root = Tk()
    flag = True
    
    for i in range(8):
        for j in range(8):
            if(flag == True):
                b = Cell(root)
                b.config(piece = Rook("white", [i , j]), location = [i , j], color = "white")
                b.grid(row=i, column=j)
            else:
                b = Cell(root)
                b.config(piece = Queen("white", [i , j]), location = [i , j], color = "black")
                b.grid(row=i, column=j)
            flag = not flag
        flag = not flag
    root.mainloop()
    
