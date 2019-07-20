from tkinter import*

root=Tk()

def printName(event):
    print("Hello there!")

def leftClick(event):
    print("Left")

def rightClick(event):
    print("Right")

def scroll(event):
    print("Scroll")

def leftKey(event):
    print("Left key pressed")
    
def rightKey(event):
    print("Right key pressed")

root.geometry("500x500")

root.bind("<Button-1>", leftClick)
root.bind("<Button-2>", scroll)
root.bind("<Button-3>", rightClick)
root.bind("<Left>", leftKey)
root.bind("<Right>", rightKey)

button1=Button(root,text="Click Me")
button1.bind("<Button-1>",printName)
button1.pack()

root.mainloop()
