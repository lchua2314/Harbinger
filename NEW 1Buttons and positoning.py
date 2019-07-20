from tkinter import*

root=Tk()

theLabel=Label(root,text="This is our Tkinter window")
theLabel.pack()
theLabel=Label(root,text="This is our second sentence")
theLabel.pack()

topFrame=Frame(root)

topFrame.pack() #Python will know this is top based on the below code

botFrame=Frame(root)
botFrame.pack(side=BOTTOM)

theButton1=Button(None,text="Click Me!",fg="Blue")
theButton1.pack(side=LEFT)
theButton4=Button(None,text="Click Me!",fg="Yellow")
theButton4.pack(side=RIGHT,fill=X)

theButton3=Button(None,text="Click Me!",fg="Purple")
theButton3.pack(side=RIGHT,fill=Y)
theButton2=Button(None,text="Hello!",fg="Red")
theButton2.pack(side=LEFT)

root.mainloop()
