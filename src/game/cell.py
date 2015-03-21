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
        self.button = Button(self, compound="left", width = 75, height = 75)
        self.button.pack(side="top")
        self.empty = PhotoImage(file = "../../img/empty.png")

    def config(self, **kwargs):
        self.location = kwargs['location']
        self.color = kwargs['color']
        self.command = kwargs['command']
        
        if(self.color == "white"):
            self.button.config(bg = "#D3B770", command = lambda: self.command(self.location))      #FFD39B
        else:
            self.button.config(bg = "#8C481C", command = lambda: self.command(self.location))      #8B4513
            
    def setPiece(self, piece = None):
        self.piece = piece
        if(self.piece != None):
            self.button.config(image = self.piece.getimage())
        else:
            self.button.config(image = self.empty)
    
    def getPiece(self):
        return self.piece
    
    def changeColor(self, touched = False):
        if(touched):
            self.button.config(bg = "#80FF80")
        else:
            if(self.color == "white"):
                self.button.config(bg = "#D3B770")      #FFD39B
            else:
                self.button.config(bg = "#8C481C")      #8B4513
    
