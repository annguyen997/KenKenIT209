#-------------------------------------------------------------------------------
# An_Nguyen_Project_Class
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
# Comments to grader: None
#-------------------------------------------------------------------------------
# Code: Code starts here
#-------------------------------------------------------------------------------

#! /usr/bin/python

class KenKen:
    """ The Game Board (KenKen) class that holds the components of the KenKen game """
    
    def __init__(self):
        """ The initializer method that creates the puzzles and
            associated lines to be displayed """
        
        #A big list that holds 3 puzzles
        self.puzzlelist = [['11+','','','','','2/','','5','11+','','5','16x','',\
        '20x','','4+','','','','','2/','','1-','','5'],['45x','','','7+','',\
        '1-','','5','','3+','','9+','','9+','','2/','','','','','','16x','',\
        '11+',''],['11+','','','','9+','15x','','','9+','','','8+','','','','5+',\
        '8+','225x','','','','','','','']]
        #lines of the puzzle - these indicate where the boundaries of the KenKen puzzle are located.
        self.lines1 = [[100, 0, 100,400],[200,0,200,400],[300,0, 300,200],\
        [300,400,300,500],[400,0, 400,400],[200,100,300,100],[100,200,200,200],\
        [300,200,500,200],[100,300,400,300],[0,400,100,400],[200,400,300,400],\
        [400,400,500,400],[400,400,400,500]] #13 lines for Puzzle 1
        self.lines2 = [[100,0,100,100],[100,200,100,300],[100,400,100,500],\
        [200,100,200,400],[300,0,300,100],[300,200,300,300],\
        [300,400,300,500],[400,100,400,200],[400,300,400,400],[100,100,500,100],\
        [100,200,200,200],[300,200,400,200],[0,300,500,300],[100,400,400,400]] #14 lines for Puzzle 2
        self.lines3 = [[100,0,100,400],[200,100,200,200],[200,400,200,500],\
        [300,0,300,400],[400,200,400,300],[400,400,400,500],\
        [100,200,200,200],[200,100,500,100],[300,200,400,200],\
        [100,300,300,300],[400,300,500,300],[0,400,200,400],[300,400,400,400]] #13 lines for Puzzle 3

        #Holds all 3 solution lists
        self.solution = [[[3,5,2,1,4],[4,2,5,3,1],[5,4,1,2,3],[1,3,4,5,2],\
        [2,1,3,4,5]],[[5,1,3,2,4],[4,3,5,1,2],[3,5,2,4,1],[1,2,4,5,3],[2,4,1,3,5]],\
        [[2,5,3,1,4],[3,1,4,2,5],[5,3,1,4,2],[4,2,5,3,1],[1,4,2,5,3]]]

    def getpuzzles(self):
        """ Provides the GUI class the list of all of the puzzles of this KenKen class """
        return self.puzzlelist  #A list of all puzzles (A multi-dimensional list)
    
    def getlines(self):
        """ Provides the GUI class the list of all of the lines for each of the three puzzles """
        return [self.lines1, self.lines2, self.lines3]          #Gives the GUI the layout of the puzzle

    def changer(self,event):
        """ Allows the values to update in the GUI"""
        #Changes the current user selection to another value (based on the coordinates of the number user pressed)
        row = int(event.x/100)  
        column = int(event.y/100)
        return row, column
        
    def checkit(self, numberlist, number):
        """ Checks if the user has won the game """
        if numberlist == self.solution[number]:  #If the user's current moves matches the solution set of a particular puzzle
            return True
        return False

    def surrender(self, number):
        """ Provides the solution of a particular puzzle to the GUI """
        return self.solution[number]  #Reveals the answer if player gives up (to GUI)
        
    def resetnum(self, checklist):
        """ Resets the GUI's memory of user's moves to all zeros """
        numbers = [] #Initializes an empty list 

        for m in range(5): #The column number for list (index of "numbers" list)
            subset = [] 
            for n in range(5): #The row number for list (i.e. "subset" list) 
                subset.append(0)
            numbers.append(subset)

        return numbers  #Returns a new multidimensional list with all zeros
