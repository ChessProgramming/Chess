'''
Created on Mar 14, 2015

@author: Venkatesh
'''

from tkinter import *  # @UnusedWildImport

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
        self.location = kwargs['location']
        self.color = kwargs['color']
        
        if(self.color == "white"):
            self.button.config(bg = "#D3B770")      #FFD39B
        else:
            self.button.config(bg = "#8C481C")      #8B4513
            
    def setPiece(self, piece = None):
        self.piece = piece
        if(self.piece != None):
            self.button.config(image = self.piece.getimage())
            
    
