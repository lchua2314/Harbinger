from tkinter import *
from time import *

print("---------------Tic-Tac-Toe---------------\n")

class TheGame(Frame):
    def __init__(self):
        Frame.__init__(self)

        #Creates the board
        self.myCanvas = Canvas(width=500, height=500, bg="black")
        self.myCanvas.grid()

        #Creates the tiles
        self.myCanvas.create_line(167, 0, 167, 500, fill="yellow")
        self.myCanvas.create_line(167*2, 0, 167*2, 500, fill="yellow")
        self.myCanvas.create_line(0, 167, 500, 167, fill="yellow")
        self.myCanvas.create_line(0, 167*2, 500, 167*2, fill="yellow")

        #Create a textbox in each square that say the number box.
        self.myCanvas.create_text(500/6, 500/6, fill="blue", text="1", font=("Times", 32))
        self.myCanvas.create_text(3*500/6, 500/6, fill="blue", text="2", font=("Times", 32))
        self.myCanvas.create_text(5*500/6, 500/6, fill="blue", text="3", font=("Times", 32))
        self.myCanvas.create_text(500/6, 3*500/6, fill="blue", text="4", font=("Times", 32))
        self.myCanvas.create_text(3*500/6, 3*500/6, fill="blue", text="5", font=("Times", 32))
        self.myCanvas.create_text(5*500/6, 3*500/6, fill="blue", text="6", font=("Times", 32))
        self.myCanvas.create_text(500/6, 5*500/6, fill="blue", text="7", font=("Times", 32))
        self.myCanvas.create_text(3*500/6, 5*500/6, fill="blue", text="8", font=("Times", 32))
        self.myCanvas.create_text(5*500/6, 5*500/6, fill="blue", text="9", font=("Times", 32))

        

    def update_board_red (self): #red_input):
        #if red_input == 1:
        self.myCanvas.create_rectangle(25, 25, 500/4, 500/4, fill="red") 
       # elif red_input == 2:
            

#Creates a list of taken spots
taken = [-1,]
counter = 1
keepGoing = True
while keepGoing == True:
    create_game = TheGame()
    create_game.mainloop()
    
    checking_if_spot_taken = False
    while checking_if_spot_taken == False:
        user_input_red = int(input("Please enter number:"))
        spot_is_taken = False
        for count in range(counter):
            if user_input_red == taken [count-1]:
                spot_is_taken = True
        if spot_is_taken == True:
            continue
        else:
            taken.append(user_input_red)
            counter += 1
            break

    create_game.update_board_red()  
    #create_game.update_board_red(user_input_red) #Error here

    #Here is to check if the red user won or not.
