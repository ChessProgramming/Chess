'''
Created on Mar 14, 2015

@author: Venkatesh
'''
from tkinter import Frame

class Cell(Frame):
    '''
        A Cell is a single unit in a chess board
        
        A cell is a Button
    '''


    def __init__(self, color, location):
        self.color = color
        self.location = location
        
        self.piece = None       # It hold the actual piece in this cell
        
        # have to add code to make the cell as Button