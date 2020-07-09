#!/usr/bin/env python3
#PyMessage GUI
#Rylee Carter
#July 7th, 2020

#Importing main tkinter libs
from tkinter import *

#Importing functions
from GUIFunctions import *

#Defining vars
chatInput = ""

class Window:
    #Defining settings upon initialization
    def __init__(self, master):
        self.master = master

        #Changing title of the window
        master.title("PyMessage Pre-Alpha")

        #Creating a menu instance
        menu = Menu(master)
        master.config(menu = menu)

        #Menu Configuration
        file = Menu(menu, tearoff = 0)
        option = Menu(menu, tearoff = 0)
        about = Menu(menu, tearoff = 0)

        #Adding commands to 'File' section of toolbar
        file.add_command(label = "Open", command = emptyFunction)
        file.add_separator()
        file.add_command(label = "Exit", command = exitProgram)
        #Adding commands to 'Options' section of toolbar
        option.add_command(label = "Change Username", command = emptyFunction)
        #Adding commands to 'About' section of toolbar
        about.add_command(label = "Aeyloh")
        about.add_separator()
        about.add_command(label = "Twitter", command = openTwitterAeyloh)
        about.add_separator()
        about.add_command(label = "NorthHopper")
        about.add_separator()
        about.add_command(label = "Twitter", command = openTwitterHopper)
        about.add_separator()

        #Adding all options to the toolbar
        menu.add_cascade(label = "File", menu = file)
        menu.add_cascade(label = "Options", menu = option)
        menu.add_cascade(label = "About", menu = about)

        #Creating mainCanvas
        mainCanvas = Canvas(root, width = 1000, height = 720)
        mainCanvas.pack()

        #Creating chat input box
        chatInputBox = Entry(root, justify = LEFT, width = 150)
        mainCanvas.create_window(400, 700, window = chatInputBox)
        sendChat = Button(text = "Send", command = lambda: getChatInput(chatInputBox))
        mainCanvas.create_window(1020, 700, window = sendChat)

#Local functions

#Reading from the user entry box
def getChatInput(chatInputBox):
    chatInput = chatInputBox.get()
    print(chatInput)
    print("Send button pressed!")

#Not sure what this does, sometimes people put it at the beginning of the program
#but it works here too
root = Tk()

#Sizing of window
root.geometry("1280x720")

#I'm guessing this is the function that actually opens the window
window = Window(root)
root.mainloop()
