#F*ck ya'll, we're creating a game.
#This game will use animations with the tkinter and time classes.
#The player model has been created.
#Edit anything how you'd like.
#Please DM me ideas to brainstorm and put it on the text document in the GitHub.

from tkinter import *
from time import *

class MainFrame (Frame):
    def __init__(self):
        Frame.__init__(self)

        self.myCanvas = Canvas(width=1500, height=1000, bg="SkyBlue1") #Background with window size
        self.myCanvas.grid() #Display it

        #Version
        self.myCanvas.create_text(90, 10, text="Harbinger - Alpha 1.1", fill="black", font=("Fixedsys", 5))
        
        #Creating the model of player 1 w/ label above it's head
        #Character is walking to the right of the screen
        #Name of the character
        a_name = self.myCanvas.create_text(75, 100, text="Player 1 Model", width=1000, fill="black", anchor="nw", justify="center", font=("Fixedsys", 16))

        #Creates the head of character
        a_head = self.myCanvas.create_oval(125, 125, 150, 150, fill="white")
        
        #Torso
        a_torso = self.myCanvas.create_rectangle(130, 150, 145, 175, fill="white")

        #Moved Left arm to bottom bc it is needed for the animations

        #HIS right arm (FRONT ARM)
        a_Rarm = self.myCanvas.create_oval(145, 150, 160, 165, fill="white")
        
        #HIS right leg (FRONT LEG)
        a_Rleg = self.myCanvas.create_oval(145, 175, 160, 183, fill="saddle brown")

        #HIS left leg (BACK LEG)
        a_Lleg = self.myCanvas.create_oval(115, 175, 130, 183, fill="saddle brown")

        #Bandana
        a_bandana1 = self.myCanvas.create_polygon(125, 140, 150, 140, 150, 150, fill="black") #Creates a polyon (triangle). Main part of banadana
        a_bandana2 = self.myCanvas.create_polygon(125, 140, 120, 142, 120, 145, fill="black") #Knot down
        a_bandana3 = self.myCanvas.create_polygon(125, 140, 120, 138, 120, 141, fill="black") #Knot up

        #V-neck
        a_vneck = self.myCanvas.create_polygon(130, 150, 145, 155, 145, 175, 130, 175, fill="dark blue")
        
        #Coat
        a_coat = self.myCanvas.create_polygon(130, 150, 129, 145, 142, 145, 135, 175, 115, 177, 130, 160, fill="gray14")

        #HIS left arm PLACED HERE BC NEEDED FOR ANIMATION (BACK ARM)
        a_Larm = self.myCanvas.create_oval(115, 150, 130, 165, fill="white")

        #LE ENEMY(creating this guy in the left side of screen, negative coords are hard)
        e1_name = self.myCanvas.create_text(-75, 100, text="Enemy gange member", width=1000, fill="black", anchor="nw", justify="center", font=("Fixedsys", 16))
        e1_head = self.myCanvas.create_oval(-150, 150, -125, 125, fill="white")
        e1_torso = self.myCanvas.create_rectangle(-145, 175, -130, 150,  fill="white")
        e1_Rarm = self.myCanvas.create_oval(-160, 165, -145, 150,fill="white")
        e1_Rleg = self.myCanvas.create_oval(-160, 183, -145, 175,  fill="saddle brown")
        e1_Lleg = self.myCanvas.create_oval(-130, 183, -115, 175, fill="saddle brown")
        e1_bandana1 = self.myCanvas.create_polygon(-150, 140, -125, 140, -125, 150, fill="red") #Creates a polyon (triangle). Main part of banadana
       # e1_bandana2 = self.myCanvas.create_polygon(-150, 140, -120, 142, -120, 145, fill="red") #Knot down
       # e1_bandana3 = self.myCanvas.create_polygon(-125, 140, -120, 138, -120, 141, fill="red") #Knot up
        e1_vneck = self.myCanvas.create_polygon(-130, 150, -145, 155, -145, 175, -130, 175, fill="dark blue")
        e1_coat = self.myCanvas.create_polygon(-130, 150, -129, 145, -142, 145, -135, 175, -115, 177, -130, 160, fill="gray14")
        e1_Larm = self.myCanvas.create_oval(-115, 150, -130, 165, fill="white")
        
        #CREATING LE CAR4
        car_body = self.myCanvas.create_polygon([575,165,575,130,610,130,610,100,700,100,700,130,735,130,735,165],     outline='gray', 
            fill='gray')
        car_wheel_1 = self.myCanvas.create_oval(600, 160, 622, 183, fill="black")
        car_wheel_2 = self.myCanvas.create_oval(690, 160, 712, 183, fill="black")

        #Animation of character running across screen
        for count in range(55):
            increment = 10*count #Arms and legs out
            self.myCanvas.coords(a_head, 125+increment, 125, 150+increment, 150)
            self.myCanvas.coords(a_name, 75+increment, 100)
            self.myCanvas.coords(a_torso, 130+increment, 150, 145+increment, 175)
            self.myCanvas.coords(a_Larm, 115+increment, 150, 130+increment, 165)
            self.myCanvas.coords(a_Rarm, 145+increment, 150, 160+increment, 165)
            self.myCanvas.coords(a_Rleg, 145+increment, 175, 160+increment, 183)
            self.myCanvas.coords(a_Lleg, 115+increment, 175, 130+increment, 183)
            self.myCanvas.coords(a_bandana1, 125+increment, 140, 150+increment, 140, 150+increment, 150)
            self.myCanvas.coords(a_bandana2, 125+increment, 140, 120+increment, 142, 120+increment, 145)
            self.myCanvas.coords(a_bandana3, 125+increment, 140, 120+increment, 138, 120+increment, 141)
            self.myCanvas.coords(a_vneck, 130+increment, 150, 145+increment, 155, 145+increment, 175, 130+increment, 175)
            self.myCanvas.coords(a_coat, 130+increment, 150, 129+increment, 145, 142+increment, 145, 135+increment, 175, 115+increment, 177, 130+increment, 160)
            self.myCanvas.update()
            sleep(0.10)

            increment2 = 10*count #Arms and legs in
            self.myCanvas.coords(a_head, 125+increment2, 125+3, 150+increment2, 150+3)
            self.myCanvas.coords(a_name, 75+increment2, 100)
            self.myCanvas.coords(a_torso, 130+increment2, 150+3, 145+increment2, 175+3)
            self.myCanvas.coords(a_Larm, 130+increment, 160, 145+increment, 175) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO
            self.myCanvas.coords(a_Rarm, 130+increment, 150, 145+increment, 175) #Arm hides behind torso
            self.myCanvas.coords(a_Rleg, 145+increment2-10, 175, 160+increment2-10, 183)
            self.myCanvas.coords(a_Lleg, 115+increment2+10, 175, 130+increment2+10, 183)
            self.myCanvas.coords(a_bandana1, 125+increment2, 140+3, 150+increment2, 140+3, 150+increment2, 150+3)
            self.myCanvas.coords(a_bandana2, 125+increment2, 140+3, 120+increment2, 142+3, 120+increment2, 145+3)
            self.myCanvas.coords(a_bandana3, 125+increment2, 140+3, 120+increment2, 138+3, 120+increment2, 141+3)
            self.myCanvas.coords(a_vneck, 130+increment2, 150+3, 145+increment2, 155+3, 145+increment2, 175+3, 130+increment2, 175+3)
            self.myCanvas.coords(a_coat, 130+increment2, 150+3, 129+increment2, 145+3, 142+increment2, 145+3, 135+increment2, 175+3, 115+increment2, 177+3, 130+increment2, 160)
            

            self.myCanvas.update()
            sleep(0.10)
        
        #move enemy into screen
        for count in range(35):
            increment = 10*count
            self.myCanvas.coords(e1_name, -75+increment, 100)
            self.myCanvas.coords(e1_head, -125+increment, 125, -150+increment, 150)
            self.myCanvas.coords(e1_torso, -130+increment, 150, -145+increment, 175)
            self.myCanvas.coords(e1_Rarm, -145+increment, 150, -160+increment, 165)
            self.myCanvas.coords(e1_Rleg, -145+increment, 175, -160+increment, 183)
            self.myCanvas.coords(e1_Lleg, -115+increment, 175, -130+increment, 183)
            self.myCanvas.coords(e1_bandana1, -125+increment, 140, -150+increment, 140, -150+increment, -150) #Creates a polyon (triangle). Main part of banadana
           # self.myCanvas.coords(e1_bandana2, -125+increment, 140, -120+increment, 142, -120+increment, 145) #Knot down
           # self.myCanvas.coords(e1_bandana3,-125+increment, 140, -120+increment, 138, -120+increment, 141) #Knot up
            self.myCanvas.coords(e1_vneck,-130+increment, 150, -145+increment, 155, -145+increment, 175, -130+increment, 175)
            self.myCanvas.coords(e1_coat,-130+increment, 150, -129+increment, 145, -142+increment, 145, -135+increment, 175, -115+increment, 177, -130+increment, 160)
            self.myCanvas.coords(e1_Larm, -115+increment, 150, -130+increment, 165)
            self.myCanvas.update()
            sleep(0.10)
        #move car with guy inside
        for count in range(120):
            increment = 10*count
            self.myCanvas.coords(car_body, 575+increment,165,575+increment,130,610+increment,130,610+increment,100,700+increment,100,700+increment,130,735+increment,130,735+increment,165)
            self.myCanvas.coords(car_wheel_2, 690+increment, 160, 712+increment, 183)
            self.myCanvas.coords(car_wheel_1, 600+increment, 160, 622+increment, 183)
            self.myCanvas.coords(a_head, 675+increment, 125, 700+increment, 150)
            self.myCanvas.coords(a_name, 625+increment, 100)
            self.myCanvas.coords(a_torso, 680+increment, 150, 695+increment, 175)
            self.myCanvas.coords(a_Larm, 665+increment, 150, 680+increment, 165)
            self.myCanvas.coords(a_Rarm, 695+increment, 150, 710+increment, 165)
            self.myCanvas.coords(a_Rleg, 145+550+increment, 175, 160+550+increment, 183)
            self.myCanvas.coords(a_Lleg, 115+550+increment, 175, 130+550+increment, 183)
            self.myCanvas.coords(a_bandana1, 125+550+increment, 140, 150+550+increment, 140, 150+550+increment, 150)
            self.myCanvas.coords(a_bandana2, 125+550+increment, 140, 120+550+increment, 142, 120+550+increment, 145)
            self.myCanvas.coords(a_bandana3, 125+550+increment, 140, 120+550+increment, 138, 120+550+increment, 141)
            self.myCanvas.coords(a_vneck, 130+550+increment, 150, 145+550+increment, 155, 145+550+increment, 175, 130+550+increment, 175)
            self.myCanvas.coords(a_coat, 130+550+increment, 150, 129+550+increment, 145, 142+550+increment, 145, 135+550+increment, 175, 115+550+increment, 177, 130+550+increment, 160)
            self.myCanvas.update()
            
            sleep(0.05)
        
            
main_frame = MainFrame()
main_frame.mainloop()


