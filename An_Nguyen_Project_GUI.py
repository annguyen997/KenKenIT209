#-------------------------------------------------------------------------------
# An_Nguyen_Project_GUI
# Name: An Nguyen
# Python Version: Python 3.6
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
#                       violates the ethical guidelines as set forth by the
#                       instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References:
# The KenKen website - www.kenkenpuzzle.com/
#-------------------------------------------------------------------------------
# Comments to grader: 
#-------------------------------------------------------------------------------
# Code: Code starts here
#-------------------------------------------------------------------------------

#! /usr/bin/python

from An_Nguyen_Project_Class import KenKen
from tkinter import *

class TheGUI(Frame):
    def __init__(self, master):
        """ Initializes the GUI for KenKen Game """
        Frame.__init__(self, master) #Creates the frame

        self.kenken = KenKen()                   #Initializes the KenKen Game
        self.puzzles = self.kenken.getpuzzles()  #Gets the puzzles of the game - Calls getpuzzles method of KenKen
        self.linelist = self.kenken.getlines()   #Gets the line boundaries of the game - Calls getlines method of KenKen

        self.choice = ['','1','2','3','4','5'] #The numbers allowed in a 5x5 KenKen

        #This keeps track of the puzzle number
        self.counter = 0

        #Creates the canvas that will display the game 
        self.w = Canvas(master, width=502, height=503)
        self.w.pack()

        #Shows the puzzle number to user 
        # self.tt = StringVar(self)
        self.lblPuz = StringVar(self)
        self.lblPuz.set("Puzzle " + str(self.counter + 1))  #Shows puzzle number
        self.lbl1 = Label(self, textvariable=self.lblPuz, font="Arial 20 bold").pack()

        #Displays instructions for the game when initialized.
        self.lbl2 = Label(self, text="To begin the puzzle, start clicking on any cell.\nChange numbers of a cell by clicking it again.", font="Arial 10 bold")
        self.lbl2.pack()

        self.create_widgets(self.counter) #Creates the widgets

        #Displays the numbers user inputted
        self.movelist = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

        self.w.bind("<ButtonRelease-1>", self.change) #Binds all cells in board grid to change() method 
        self.pack()

    def create_widgets(self, counter):
        """ Creates the widgets and canvas objects/components of the game in GUI """
        self.w.create_rectangle(3, 3, 500, 500) #Draws the rectangle onto canvas

        # Creates the puzzle board with all 25 cells in 5x5 grid 
        self.sqlist = []
        for i in range(0, 500, 100):
            for j in range(0, 500, 100):
                x = j + 100
                y = i + 100
                self.sqlist.append(self.w.create_rectangle(j, i, x, y))

        # Displays all of the bolded lines to the board 
        self.lines_to_print = self.linelist[self.counter]
        for line in self.lines_to_print:
            self.w.create_line(line, width="4")

        # Display the numbers and operations of puzzle to canvas
        self.currentpuzzle = self.puzzles[counter]

        x = 25
        y = 20
        for element in self.currentpuzzle:
            self.w.create_text(x, y, font="Arial 20 bold", text=element)
            y += 100

            if y == 520:
                y = 20
                x += 100

        # This displays the current values that the user can press in the puzzle.
        self.numbers = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        x = 50
        y = 60
        for m in range(len(self.numbers)):
            for n in range(len(self.numbers)):
                self.numbers[m][n] = self.w.create_text(x, y, font="Arial 30", text = self.choice[0])
                y += 100
            y = 60
            x += 100

        #Buttons of the KenKen Game
        self.buttonlist = []
        self.btn_win = Button(self, text="Win?")
        self.btn_win.bind("<ButtonRelease-1>", self.check)
        self.btn_reset = Button(self, text="Reset")
        self.btn_reset.bind("<ButtonRelease-1>", self.reset)
        self.btn_quit = Button(self, text="Surrender?")
        self.btn_quit.bind("<ButtonRelease-1>", self.surrend)
        self.btn_next = Button(self, text="Next Puzzle")
        self.btn_next.bind("<ButtonRelease-1>", self.next)
        self.btn_exit = Button(self, text="Exit")
        self.btn_exit.bind("<ButtonRelease-1>", self.click_Exit)
        self.btn_resetGame = Button(self, text="Reset Game")
        self.btn_resetGame.bind("<ButtonRelease-1>", self.resetGame)

        self.btn_resetGame.pack(side = BOTTOM)
        self.btn_quit.pack(side = BOTTOM, fill = Y, expand=YES)
        self.btn_win.pack(side = TOP, expand = YES)
        self.btn_reset.pack(side = LEFT, fill = X, expand = YES)
        self.btn_next.pack(side = LEFT, fill = X, expand = YES)
        self.btn_exit.pack(side = LEFT, fill = X, expand = YES)

        self.buttonlist.append(self.btn_quit)
        self.buttonlist.append(self.btn_win)
        self.buttonlist.append(self.btn_reset)
        self.buttonlist.append(self.btn_next)
        self.buttonlist.append(self.btn_exit)
        self.buttonlist.append(self.btn_resetGame)

    def click_Exit(self, event):
        """ Exits the KenKen game """
        exit()
        
    def check(self,event=None):
        """ Checks to see if the user wins the puzzle currently playing
            (may be called by other methods or direcly by Win? Button """
        if self.kenken.checkit(self.movelist, self.counter): #Calls the checkit method of the KenKen object
            #If user wins the game, display congratulatory message and instructions.
            self.lbl2["text"] = "Congratulations, you finished the puzzle!\nSelect Next Puzzle to go to another puzzle" + \
                                "\nor Exit to quit the game."
        elif event:
            #If user has not won the game yet, but checks with the "Win?" button in GUI - show message to continue playing.
            self.lbl2["text"] = "This puzzle is not done. Keep trying!"

    def change(self, event):
        """ Changes the displayed number when user selects a cell in the board """
        if(self.lbl2["text"]):
            self.lbl2["text"] = ""  #Clears any text (e.g. instructions or check) if there is any.

        #Updates the buttons to the current number
        row, column = self.kenken.changer(event)
        self.movelist[row][column] +=1 #Increase the value by one.
        
        if self.movelist[row][column] > 5: #If value in movelist is greater than 5, reset back to zero.
            self.movelist[row][column] = 0

        #Displays the new number to the board for user to see changes 
        self.w.itemconfigure(self.numbers[row][column], text = self.choice[self.movelist[row][column]])
        #As the user plays, it will continually check if the user wins or not
        self.check()

    def resetnums(self):
        """ Resets all the current numbers user selected """
        self.movelist = self.kenken.resetnum(self.movelist) #Redisplays all numbers as empty strings (zero for movelist).

    def reset(self, event):
        """ Resets the current puzzle """
        #Resets the current puzzle
        self.w.delete('all') #Deletes all widgets/components 
        self.resetnums()  #Call restnums() to reset self.movelist

        #Destroys all buttons on GUI
        #self.buttonlist.append(self.lbl)
        for i in range(len(self.buttonlist)):
            self.buttonlist[i].destroy()

        self.create_widgets(self.counter) #Calls the create_widgets() to redisplay all widgets and buttons
        self.lbl2["text"] = "" #Clears any text (e.g. instructions or check) if there is any.

    def resetGame(self, event):
        """ Resets the entire game, returns to first puzzle """
        self.counter = 0  #Resets back to puzzle one.
        self.reset(event) #Calls reset() function
        self.lblPuz.set("Puzzle " + str(self.counter + 1)) #Sets label to "Puzzle 1"

    def surrend(self, event):
        """ Shows the solution to the user if gives up on current puzzle """ 
        solution = self.kenken.surrender(self.counter) #Calls the surrender method of the KenKen object

        #Display the solution to the user 
        for row in range(len(solution)):  
            for column in range(len(solution)):
                self.w.itemconfigure(self.numbers[row][column], text=solution[row][column])

        #Displays instructions to the user 
        self.lbl2["text"] = "Select Next Puzzle to go to another puzzle" + \
                            ", Reset to reset the current puzzle,\n or Exit to quit the game."

    def next(self, event):
        """ Reset the number choices and create the next puzzle """ 
        self.counter += 1
        if self.counter == 3:  #If counter reaches three, reset back to zero.
            self.counter = 0

        self.reset(event)        #Calls the reset() method of GUI class 
        self.lblPuz.set("Puzzle " + str(self.counter + 1)) #Sets label to next puzzle number. 
        self.lbl2["text"] = ""   #Clears any text (e.g. instructions or check) if there is any.
