#Lesson 7: Creating Graphics with Tkinter

from tkinter import * #Imports the tkinter library
from time import * #Imports time library. Will be used for animations later.

print("Displaying Frame object \"frame01\" (blank window)")
frame01 = Frame() #Creates an object of the Frame class
frame01.mainloop() #Creates a window

#Inheritance - Creating a new class (derived class) that inherits
#all the variables and functions from another class (base class)
#while having it's own variables and funtions.

class MyFrame(Frame): #The "(Frame)" means to inherit the Frame class
    def __init__(self):
        Frame.__init__(self)

        #NOTE: Copy and paste one line at a time to see each of the effects in the CONSTRUCTOR ONLY.
        #Make sure the code outside is copied (The two lines below the class) so that the code will run.
        
        self.myCanvas = Canvas(width=500, height=500, bg="black") #Canvas widget - Allows you to create and draw
        self.myCanvas.grid() #shapes and text. This is good for graphs and charts.
                             #Think of Canvas like a container that can hold shapes.
        #grid() is a layout. Frame class uses a layout manager to
        #determine where to place everything. Grid goes by rows and columns.
        #The default color is the same as the Frame object though so that why in the arguements of the function "Canvas()" we put all that info (bg means background)

        self.myCanvas.create_rectangle(10, 10, 100, 100, fill="yellow")
        #Creates rectange; .create_rectangle(x-coordinate of upper-left hand location, y-coordinate..., x-coordinate of the lower-right corner, y-coordinate...)
        #The last arguement can be outline, fill, or width
        self.myCanvas.create_rectangle(100, 100, 200, 200, outline="red")
        #self.myCanvas.create_rectangle(10, 10, 100, 100, width="green") Creates an error. Try for yourself if you can solve it.
        
        self.myCanvas.create_oval(10, 10, 200, 100, fill="white") #Creates a white oval. It overlaps the yellow rectangle because this line of code is after the other line.
        #There is no create_square function or create_circle function because the above functions can create those images for you.
        
        self.myCanvas.create_line(1, 1, 200, 200, fill="green", arrow="first") #Creates a line. arrow="first" is where the arrow head will be. Other options are "both" or "last"
        #There are options for fill and width. However, I cannot get width to work.

        self.myCanvas.create_text(100, 100, fill="red", text="Sameple Text is Present") #Creates a text at a given location. text="" is required.
        self.myCanvas.create_text(200, 200, text="This line is too long and will wrap around to the next line. I swear on me mum! IT IS NOT LONG ENOUGH YET! Hehe xd")
        #It does not wrap around, because the width is not declared.
        self.myCanvas.create_text(300, 300, text="Hello World", width=70, fill="purple", anchor="nw", justify="center", font=("Times", 16))
        #width is the width of the invisible textbox. If the text is too big, it will wrap around (which it does in this line). justify can be "left", "right", or "center"
        #anchor means where the text should be in the textbox. "nw" means Northwest in the textbox. By default it is "center". Options: "n", "ne", "w", "e", "sw", "s", and "se"
        #font is ( <Font name>, <size> )


        #Animations
        #Will use the time library to pause the program so that image will be displayed on a delay instead of the computer's speed.
        self.myCanvas.update() #When you call this function, Python will go ahead and draw the Canvas as it is specified so fa in the program code.
        sleep(3) #Using time function to wait three seconds.
        self.myCanvas.create_rectangle(10, 10, 100, 100, fill="red") #Rectangle appears three seconds later.
        self.myCanvas.update()
        sleep(1)
        
        for count in range(10): #Creates a blue box every second that overlaps.
            increment = 10*count
            self.myCanvas.create_rectangle(350 + increment, 350 + increment, 400 + increment, 400 + increment, fill="blue")
            self.myCanvas.update()
            sleep(1)

        for count in range(10): #Same thing except that the blue squares disappear.
            increment = 10*count
            self.myCanvas.create_rectangle(350 + increment, 350 + increment, 400 + increment, 400 + increment, fill="blue")
            self.myCanvas.update()
            sleep(1)

            #Colors over the previous rectangle that is the same as the background so that it looks like the squares disappear.
            self.myCanvas.create_rectangle(350 + increment, 350 + increment, 400 + increment, 400 + increment, fill="black")

        #The above for loop is inefficient because we are creating 20 squares instead of moving them around. A better way to do this is the below.
        my_rect_id = self.myCanvas.create_rectangle(350, 350, 400, 400)
        self.myCanvas.update()

        for count in range(10):
            incement = 10*count
            self.myCanvas.coords(my_rect_id, 350 + increment, 350 + increment, 400 + increment, 400 + increment, fill="blue")
            self.myCanvas.update()
            sleep(1)
        #Using the coords() function will move the shape to a new location.
            
#Now create a MyFrame object and call on mainloop
print("Displaying \"frame02\" window.")
frame02 = MyFrame() #These are the only two lines we will need outside of the 
frame02.mainloop() #class, so I will place them in this Python file.


