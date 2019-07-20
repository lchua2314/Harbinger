from tkinter import*

root=Tk()

def random():
    print("This is a statement")

mainMenu=Menu(root) #White bar up top

root.configure(menu=mainMenu)

subMenu=Menu(mainMenu)

mainMenu.add_cascade(label="File",menu=subMenu)

subMenu.add_command(label="Random Func", command = random)

subMenu.add_command(label="New File", command=random)

subMenu.add_separator()

subMenu.add_command(label="Supercalafragilistic", command=random)

root.mainloop()
