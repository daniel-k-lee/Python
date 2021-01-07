"""
File: crapsgui.py
Project 9.7
Pops up a window that allows the user to play the game of craps.
"""

from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter import *
from craps import Player
from die import Die


class CrapsGUI(EasyFrame):
   
    def __init__(self):
        """Creates the player, and sets up the Images and labels for the two dice to be displayed
, the text area for the game state, and the two command buttons."""
        EasyFrame.__init__(self, title = "Craps Game")
        self.setSize(220, 320)
        """Instantiate the model and initial values of the dice"""
        self.player = Player()
        self.v1 = Die()
        self.v2 = Die()
        """Add labels and buttons to the view"""
        self.dieLabel1 = self.addLabel(text=self.v1.getValue(), row=0, column=0)
        #self.dieLabel1 = dice1
        self.dieLabel2 = self.addLabel(text=self.v2.getValue(), row=0, column=1)
        self.stateArea = self.addTextArea(text="State", row=1, column=0, columnspan=2)
        self.rollButton = self.addButton(text="Roll", row=2, column=0, command=self.nextRoll)
        self.addButton = self.addButton(text="New game", row=2, column=1, command=self.newGame)
        self.refreshImages()

    def nextRoll(self):
        """Rolls the dice and updates the view with
        the results."""
        # Add your code here
        self.v1.roll()
        self.v2.roll()
        text = str((self.v1.getValue(), self.v2.getValue()))
        self.stateArea.setText(text)
        self.rollButton["state"] = "disabled"
        self.refreshImages()
            
    def newGame(self):
        """Create a new craps game and updates the view."""
        # Add your code here
        self.stateArea.setText("State")
        self.rollButton["state"] = "normal"
        
    def refreshImages(self):
        """Updates the images in the window."""
        # Add your code here
        dice1 = PhotoImage(file='DICE\{0}.gif'.format(self.v1.getValue()), master=self)
        self.dieLabel1.image=dice1
        self.dieLabel1.configure(image=dice1)
        dice2 = PhotoImage(file='DICE\{0}.gif'.format(self.v2.getValue()), master=self)
        self.dieLabel2.image=dice2
        self.dieLabel2.configure(image=dice2)                           
        

def main():
    CrapsGUI().mainloop()

if __name__ == "__main__":
    main()
