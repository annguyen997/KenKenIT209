#-------------------------------------------------------------------------------
# An_Nguyen_Project_Driver
# Name: An Nguyen
# Python Version: Python 3.6
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
#                       violates the ethical guidelines as set forth by the
#                       instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: None
#-------------------------------------------------------------------------------
# Comments to grader: None
#-------------------------------------------------------------------------------
# Code: Code starts here
#-------------------------------------------------------------------------------

#Imports the GUI (GUI class) as well as Tkinter 
from An_Nguyen_Project_GUI import TheGUI
from tkinter import *

#Starts up the game
def main():
    """ The main function that starts and runs the KenKen Game """
    root = Tk() #Initializes the root menu for game to appear
    root.title("KenKen")
    root.geometry("650x710")
    f = TheGUI(root) #Initializes the graphics to display the game
    root.mainloop() #Runs the game

if __name__ == "__main__":
    """ If this is the main file to run the game, run the main() function """
    main()
