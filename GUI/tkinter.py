#Py(i)Message GUI
#Rylee Carter
#July 7th, 2020

#Importing main tkinter libs
from tkinter import *

#Importing open file dialog libs, fyi there's another way to do this using 'from import' but I
#haven't had issues this way
import tkinter.filedialog

#Importing ImageTk libs
import PIL
from PIL import ImageTk
from PIL import Image

#Creating class, window, and inheriting from the Frame class, which is a tkinter module
class Window(Frame):

    #Defining settings upon initialization
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):

        #Changing title of the window
        self.master.title("PyMessage v0.0.1")

        #Creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu = menu)

        file = Menu(menu, tearoff = 0)

        #Initializing the toolbar as the variable name 'filemenu'
        #filemenu = Menu(menubar, tearoff = 0)

        #Adding commands to 'File' section of toolbar
        file.add_command(label = "Open", command = self.openFileDialog)
        file.add_separator()
        file.add_command(label = "Exit", command = self.exitProgram)
        #Adding the 'File' option to the toolbar
        menu.add_cascade(label = "File", menu = file)
        
        #Not sure what this does, sometimes people put it at the beginning of the program
        #but it works here too
        root = Tk()

        #Sizing of window
        root.geometry("1280x720")

        #I'm guessing this is the function that actually opens the window
        app = Window(root)
        root.mainloop()
