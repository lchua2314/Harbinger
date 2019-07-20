#CALCULATOR
from tkinter import*
root=Tk()

label1=Label(root,text="Enter your expresson")

def evaluate(event):
    data=e.get()
    ans.configure(text="Answer: " + str(eval(data)))
    
e=Entry(root)

e.bind('<Return>', evaluate)
e.pack()
ans=Label(root)
ans.pack()

root.mainloop()
