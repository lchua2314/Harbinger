from tkinter import*
import random
root=Tk()
canvas=Canvas(root,width=10000,height=10000,bg="white")
canvas.pack()

def randomRects(num):
    for i in range(0,num):
        x1=random.randrange(1000)
        y1=random.randrange(1000)
        x2=x1+random.randrange(1000)
        y2=y1+random.randrange(1000)
        canvas.create_rectangle(x1,y1,x2,y2)

randomRects(1000)
root.mainloop()
