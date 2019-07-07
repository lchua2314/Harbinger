import tkinter as tk

def test(event):
    print('keysym:', event.keysym)

root = tk.Tk()

root.bind('<Key>', test)

root.mainloop()
