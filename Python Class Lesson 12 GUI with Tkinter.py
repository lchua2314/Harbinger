#Lesson 12: GUI with Tkinter

#Using the same Tkinter class

from tkinter import * #Same stuff as Graphics Lesson 7 except...

class MyFrame(Frame):
   def __init__(self):
       Frame.__init__(self)
       #Creating text inside the window and window name.
       self.master.geometry("200x200") #Creates a bigger window.
       self.master.title("My GUI") #Titles the window "My GUI"
       self.grid()

       self.message = Label(self, text = "Hello World!") #Here. Creates Label with text in window.
       self.message.grid() #Called grid() a second time so self.message gets displayed for Label object. The other grid() is for the Grame object.


       #Button - Will stop the program until user presses the button. This is also called event-driven programming (also when doing user input)
       #Uses the Frame class
       self.button_click_here = Button( self, text = "Click Here", #Creates Button object (button displayed in window) with the text "Click Here"
           command = self.click_here_click ) #If button is clicked, click_here_click method is ran.
       self.button_click_here.grid() #Bc Button object is a new class, you have to call grid() method to display it.



       #Updating text in the window.
       #Need to make a control variable so that that gui can be updated at Runtime. That's the only difference between control variable and a regular variable.
       self.my_text = StringVar() #Sets the variable to StringVar() method.
       #This is a special data type that allows the value of the string contained in the Label control to be changed at runtime.
     
       self.message = Label(self, textvariable = self.my_text) #Tells the Label object to set textvariable on window But not to display it.
       self.message.grid() #Displays new text.


   def click_here_click(self):
       print ("You did it!" ) #If button is clicked, this statement will print the output but not in the window itself.
       self.my_text.set("You did it!") #Sets the my_text variable to "You did it!"

frame01 = MyFrame()
frame01.mainloop()


#User input
#Created a new Frame class because it would get too messy to update the other class.
from tkinter import *

class MyFrame2(Frame):
   def __init__(self):
       Frame.__init__(self)
       self.master.geometry("300x200")
       self.master.title("My GUI")
       self.grid()

       self.prompt = Label(self, text = "What's your name?") #Creating a Label object and assigning it to a variable.
       self.prompt.grid() #Displays the variable Label object

       self.input = Entry(self) #Creates input variable and assigns it to the Entry object
       self.input.grid() #Displays the variable Entry object

       self.button_submit = Button( self, text = "Submit", #Creats a Button object and assigns it to button_submit variable
           command = self.submit_click ) #If button is clicked, submit_click method is ran.
       self.button_submit.grid() #Displays the button

       self.my_text = StringVar() 
       self.message = Label(self, textvariable = self.my_text)
       self.message.grid()

   def submit_click(self):
       output_message = "Hi " + self.input.get() #Gets the input and assigns it to output_message variable
       self.my_text.set(output_message) #Sets the my_text variable to the above.

frame04 = MyFrame2()
frame04.mainloop()

#The Grid Layout Manager
#Think of the the grid as rows and columns. Each new display gets displayed in the next row. So to change the next displays to the next column (side-by-side)
#You need to do the following.

#This class will place the input bar to the right of the first diplay (the question, "What's your name?")
from tkinter import *

class MyFrame3(Frame):
   def __init__(self):
       Frame.__init__(self)
       self.master.geometry("300x200")
       self.master.title("My GUI")
       self.grid()

       self.prompt = Label(self, text = "What's your name?")
       self.prompt.grid(row = 0, column = 0) #We set it at the top left corner of the window.

       self.input = Entry(self)
       self.input.grid(row = 0, column = 1) #We set it to the right of the "What's your name?" string

       self.button_submit = Button( self, text = "Submit",
           command = self.submit_click )
       self.button_submit.grid(columnspan = 2, pady = 10) #pady - spaces out the display by a certain ammount by adding pixels around the display in the Y-directions
                                                          #THere is also padx
       self.my_text = StringVar()
       self.message = Label(self, textvariable = self.my_text)
       self.message.grid(columnspan = 2) #Makes the display in the middle of the column. 

   def submit_click(self):
       output_message = "Hi " + self.input.get()
       self.my_text.set(output_message)

frame05 = MyFrame3()
frame05.mainloop()

#Checkbutton and IntVar objects
#Allow you to create a window with check boxes.
from tkinter import *

class MyFrame4(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.geometry("300x200")
        self.master.title("Text Sampler")
        self.grid()

        self.sample_label = Label(self, text="Some Sample Text", font = "Courier 10")
        self.sample_label.grid(row = 0, column = 0, columnspan = 2)

        self.bold_on = IntVar() #Stores 0 (unchecked box from window display) or 1 (checked box from window display)
        self.check_bold = Checkbutton(self, text = "Bold",
                variable = self.bold_on, command = self.set_font)
        self.check_bold.grid(row = 1, column = 0)

        self.underline_on = IntVar()
        self.check_underline = Checkbutton(self, text = "Underline",
                variable = self.underline_on, command = self.set_font)
        self.check_underline.grid(row = 1, column = 1)

    def set_font(self):
        new_font = "Courier 10"

        if self.bold_on.get() == 1: 
            new_font = new_font + " bold"

        if self.underline_on.get() == 1:
            new_font = new_font + " underline"
       
        self.sample_label.config( font = new_font) #Updates the font option.

frame04 = MyFrame4()
frame04.mainloop()

#Changing font size

from tkinter import *

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.geometry("300x200")
        self.master.title("Text Sampler")
        self.grid()

        self.sample_label = Label(self, text="Some Sample Text", font = "Courier 10")
        self.sample_label.grid(row = 0, column = 0, columnspan = 2)

        self.bold_on = IntVar()
        self.check_bold = Checkbutton(self, text = "Bold",
                variable = self.bold_on, command = self.set_font)
        self.check_bold.grid(row = 1, column = 0)

        self.underline_on = IntVar()
        self.check_underline = Checkbutton(self, text = "Underline",
                variable = self.underline_on, command = self.set_font)
        self.check_underline.grid(row = 1, column = 1)

        self.point_size = StringVar()
        self.point_size.set("10")
        self.ten_point = Radiobutton(self, text = "10 point",
                variable = self.point_size, value = "10",
                command = self.set_font)
        self.ten_point.grid(row = 2, column = 0)

        self.twelve_point = Radiobutton(self, text = "12 point",
                variable = self.point_size, value = "12",
                command = self.set_font)
        self.twelve_point.grid(row = 2, column = 1)

    def set_font(self):
        new_font = "Courier"

        if self.point_size.get() == "10":
            new_font = new_font + " 10"
        else:
            new_font = new_font + " 12"
    
        if self.bold_on.get() == 1:
            new_font = new_font + " bold"

        if self.underline_on.get() == 1:
            new_font = new_font + " underline"
      
        self.sample_label.config( font = new_font)

frame010 = MyFrame()
frame010.mainloop()

#If you want the user to have the option of choosing the font type.
#Add this somewhere in the class
#self.family = StringVar()
#self.times = Radiobutton(self, text = "Times",
   #variable = self.family, value = "times",
   #command = self.set_font)
#self.times.grid(row = 3, column = 0)

#Some assignment to do something.

# Introduction to Python Programming
# Lesson 12 Assignment
# Sample Solution

from tkinter import *

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.geometry("300x300")
        self.master.title("Lesson 12 Assignment")
        self.grid()

        # Prompt, Entry and Button
        self.prompt = Label(self, text = "Enter your text: ")
        self.prompt.grid(row = 0, column = 0)
      
        self.input = Entry(self)
        self.input.grid(row = 0, column = 1)

        self.button_submit = Button( self, text = "Submit",
                                       command = self.submit_click )
        self.button_submit.grid(row = 0, column = 2)

        # Display the text here
        self.my_text = StringVar()
        self.my_text.set("Enter your text above")
        self.message = Label(self, textvariable = self.my_text, font = "Courier 8")
        self.message.grid(row = 1, columnspan = 3, pady = 20)

        # Now for the options
        self.bold_on = IntVar()
        self.check_bold = Checkbutton(self, text = "Bold",
                variable = self.bold_on, command = self.set_font)
        self.check_bold.grid(row = 2, column = 0)

        self.underline_on = IntVar()
        self.check_underline = Checkbutton(self, text = "Underline",
                variable = self.underline_on, command = self.set_font)

        self.check_underline.grid(row = 2, column = 1)

        # And the font sizes
        self.point_size = StringVar()
        self.point_size.set("8")
        self.eight_point = Radiobutton(self, text = "8 point",
                variable = self.point_size, value = "8",
                command = self.set_font)
        self.eight_point.grid(row = 3, column = 0)

        self.ten_point = Radiobutton(self, text = "10 point",
                variable = self.point_size, value = "10",
                command = self.set_font)
        self.ten_point.grid(row = 3, column = 1)
      
        self.twelve_point = Radiobutton(self, text = "12 point",
                variable = self.point_size, value = "12",
                command = self.set_font)
        self.twelve_point.grid(row = 3, column = 2)

    def set_font(self):
        new_font = "Courier"

        if self.point_size.get() == "8":
            new_font = new_font + " 8"
        elif self.point_size.get() == "10":
            new_font = new_font + " 10"
        else:
            new_font = new_font + " 12"
      
        if self.bold_on.get() == 1:
            new_font = new_font + " bold"

        if self.underline_on.get() == 1:
            new_font = new_font + " underline"
       
        self.message.config( font = new_font)

    def submit_click(self):
        self.my_text.set(self.input.get())

asn_frame = MyFrame()
asn_frame.mainloop()

#Link(s):
#This is the large PDF file that I linked to in Lesson 7.
#It's a complete reference for the Tkinter module and includes information about all of the widgets we discussed in this lesson and more.
#https://effbot.org/tkinterbook/tkinter-index.htm
