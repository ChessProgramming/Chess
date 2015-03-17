'''
Created on Mar 14, 2015

@author: Venkatesh
'''
from tkinter import Frame, Button

class Cell(Frame):
    '''
        A Cell is a single unit in a chess board
        
        A cell is a Button
    '''


    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.button = Button(self, compound="left", command=lambda:print(self.color), # command have to given properly
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