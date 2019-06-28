from tkinter import * #Imports the tkinter library
from time import * #Imports time library. Will be used for animations later.

class MyFrame(Frame): #The "(Frame)" means to inherit the Frame class
    def __init__(self):
        Frame.__init__(self)

        self.myCanvas = Canvas(width=500, height=500, bg="black") #Canvas widget - Allows you to create and draw
        self.myCanvas.grid() #shapes and text. This is good for graphs and charts.

frame02 = MyFrame() #These are the only two lines we will need outside of the 
frame02.mainloop() #class, so I will place them in this Python file.
