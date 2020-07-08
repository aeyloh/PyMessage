#!/usr/bin/env python3
#PyMessage GUI
#Rylee Carter
#July 7th, 2020

#Importing main tkinter libs
#import tk as tkinter
#from tkinter import Tk, Menu
from tkinter import *

#Importing functions
from GUIFunctions import *

class Window:
    #Defining settings upon initialization
    def __init__(self, master):
        self.master = master

        #Changing title of the window
        master.title("PyMessage v0.0.1")

        #Creating a menu instance
        menu = Menu(master)
        master.config(menu = menu)

        file = Menu(menu, tearoff = 0)
        option = Menu(menu, tearoff = 0)
        about = Menu(menu, tearoff = 0)

        #Adding commands to 'File' section of toolbar
        file.add_command(label = "Open", command = emptyFunction)
        file.add_separator()
        file.add_command(label = "Exit", command = exitProgram)

        #Adding all options to the toolbar
        menu.add_cascade(label = "File", menu = file)
        menu.add_cascade(label = "Options", menu = option)
        menu.add_cascade(label = "About", menu = about)

#Not sure what this does, sometimes people put it at the beginning of the program
#but it works here too
root = Tk()

#Sizing of window
root.geometry("1280x720")

#I'm guessing this is the function that actually opens the window
window = Window(root)
root.mainloop()
