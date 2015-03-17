'''
Created on Mar 15, 2015

@author: Venkatesh
'''
from tkinter import PhotoImage

def get_image(piece):
    ''' This function returns an object of PhotoImage to the requested image file '''
    return PhotoImage(file = "../../img/" + piece + ".png")       