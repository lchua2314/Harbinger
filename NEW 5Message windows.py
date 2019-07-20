from tkinter import*
import tkinter.messagebox

root=Tk()

tkinter.messagebox.showinfo("Window Title", "Did you know that the World just blew up?")

answer=tkinter.messagebox.askquestion("Question1", "Are you human?")

if answer == "yes":
    tkinter.messagebox.showinfo("Congrats", "Thank god! It's good to know another human is out there.")
elif answer == "no":
    tkinter.messagebox.showinfo("Alien", "You are 100% confirmed alien.")

root.mainloop()
