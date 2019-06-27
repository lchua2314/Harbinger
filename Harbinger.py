#F*ck ya'll, we're creating a game.
#This game will use animations with the tkinter and time classes.
#The player model has been created.
#Edit anything how you'd like.
#Please DM me ideas to brainstorm and put it on the text document in the GitHub.

from tkinter import *
from time import *

class MainFrame (Frame):
    def __init__(self):
        Frame.__init__(self)

        self.myCanvas = Canvas(width=1500, height=1000, bg="SkyBlue1") #Background with window size
        self.myCanvas.grid() #Display it

        #Version
        self.myCanvas.create_text(90, 10, text="Harbinger - Alpha 1.0", fill="black", font=("Fixedsys", 5))
        
        #Creating the model of player 1 w/ label above it's head
        #Character is walking to the right of the screen
        self.myCanvas.create_text(75, 100, text="Player 1 Model", width=1000, fill="black", anchor="nw", justify="center", font=("Fixedsys", 16)) #Name of character

        #Creates the head of character
        self.myCanvas.create_oval(125, 125, 150, 150, fill="white") #Head
        
        #Torso
        self.myCanvas.create_rectangle(130, 150, 145, 175, fill="white") #Torso

        #HIS left arm
        self.myCanvas.create_oval(115, 150, 130, 165, fill="white") #left arm

        #HIS right arm
        self.myCanvas.create_oval(145, 150, 160, 165, fill="white") #right arm
        
        #HIS right leg
        self.myCanvas.create_oval(145, 175, 160, 183, fill="saddle brown") #right arm

        #HIS left leg
        self.myCanvas.create_oval(115, 175, 130, 183, fill="orange4") #right arm

        #Bandana
        self.myCanvas.create_polygon(125, 140, 150, 140, 150, 150, fill="black") #Creates a polygon (triangle) main
        self.myCanvas.create_polygon(125, 140, 120, 142, 120, 145, fill="black") #Knot down
        self.myCanvas.create_polygon(125, 140, 120, 138, 120, 141, fill="black") #Knot up

        #V-neck
        self.myCanvas.create_polygon(130, 150, 145, 155, 145, 175, 130, 175, fill="dark blue")
        
        #Coat
        self.myCanvas.create_polygon(130, 150, 129, 145, 142, 145, 135, 175, 115, 177, 130, 160, fill="gray14")
        
main_frame = MainFrame()
main_frame.mainloop()
