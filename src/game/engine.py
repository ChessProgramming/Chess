'''
Created on Mar 18, 2015

@author: Venkatesh
'''

from tkinter import *  # @UnusedWildImport
from game.board import Board
import sys

class MyOptionMenu(OptionMenu):
    def __init__(self, master, status, *options):
        self.var = StringVar(master)
        self.var.set(status)
        OptionMenu.__init__(self, master, self.var, *options)
        self.config(font=('calibri',(10)),bg='white', relief = GROOVE)
        self['menu'].config(font=('calibri',(10)),bg='white')

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
        gamemenu.add_command(label="New", command=self.callback_new, accelerator="Ctrl+N", underline=0)
        gamemenu.add_separator()
        gamemenu.add_command(label="Exit", command=lambda: self.quit, accelerator="Ctrl+Q", underline=1)
        menubar.add_cascade(label="Game", menu=gamemenu, underline=0)
        
        helpmenu = Menu(menubar, tearoff = 0)
        helpmenu.add_command(label="Rules of Chess", command=lambda: print("Rules has been clicked!!!"), underline=0)
        helpmenu.add_separator()
        helpmenu.add_command(label="About", command=lambda: print("About has been clicked!!!"), underline=0)
        menubar.add_cascade(label="Help", menu=helpmenu, underline=0)
        
        self.config(menu = menubar)
        
        ''' adding keyboard shortcuts to the app.. '''
        self.bind_all("<Control-q>", self.quit)
        self.bind_all("<Control-n>", self.callback_new)
        
    def quit(self, event):
        sys.exit(0)
        
<<<<<<< HEAD
    def newCallback(self, event):
        pass
    
=======
    def callback_new(self, event = 0):
        top = Toplevel(self)
        mymenu1 = MyOptionMenu(top, 'Select status', 'a','b','c')
        mymenu1.pack(side=BOTTOM)
        top.mainloop()
        
>>>>>>> added isvalid move additional ui updates

if __name__ == "__main__":
    root = App()
    
    board = Board(root)
    board.initboard(playercolor="white")
    
    root.mainloop()
