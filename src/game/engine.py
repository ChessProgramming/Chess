'''
Created on Mar 18, 2015

@author: Venkatesh
'''
from tkinter import Tk, Menu
from game.board import Board
import sys

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        self.resizable(0, 0)  # Disables the maximize button
        w = 80 * 8 + 10  # screen width
        h = 80 * 8 + 10  # screen height
        ws = self.winfo_screendepth() / 2 + w / 2  # x position for the window
        self.geometry('%dx%d+%d+%d' % (w, h, ws, 0))        
        
        menubar = Menu(self)
        
        ''' adding menu called games '''
        gamemenu = Menu(menubar, tearoff=0)
        gamemenu.add_command(label="New", command=lambda: print("hi"), accelerator="Ctrl+N", underline=0)
        gamemenu.add_separator()
        gamemenu.add_command(label="Exit", command=lambda: self.quit, accelerator="Ctrl+Q", underline=1)
        menubar.add_cascade(label="Game", menu=gamemenu, underline=0)
        
        self.config(menu = menubar)
        
        ''' adding keyboard shortcuts to the app.. '''
        self.bind_all("<Control-q>", self.quit)
        self.bind_all("<Control-n>", self.newCallback)
        
    def quit(self, event):
        sys.exit(0)
        
    def newCallback(self, event):
        pass
        

if __name__ == "__main__":
    root = App()
    
    board = Board(root)
    board.initboard(playercolor="black")
    
    root.mainloop()
