from tkinter import *
from time import *

print("---------------Tic-Tac-Toe---------------\n")

class TheGame(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.myCanvas = Canvas(width=500, height=500, bg="black")
        self.myCanvas.grid()

        self.myCanvas.create_line(167, 0, 167, 500, fill="yellow")
        self.myCanvas.create_line(167*2, 0, 167*2, 500, fill="yellow")
        self.myCanvas.create_line(0, 167, 500, 167, fill="yellow")
        self.myCanvas.create_line(0, 167*2, 500, 167*2, fill="yellow")

        #Create a textbox in each square that say the number box.



keepGoing = True
while keepGoing == True:
    create_game = TheGame()
    create_game.mainloop()
    user_input = input("Please enter number coordinate:")
