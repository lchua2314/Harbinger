#F*ck ya'll, we're creating a game.
#This game will use animations with the tkinter and time classes.
#The player model has been created.
#Edit anything how you'd like.
#Please DM me ideas to brainstorm and put it on the text document in the GitHub.

from tkinter import *
from time import *
import random #FOR BACKGROUND


class MainFrame (Frame):
    def __init__(self):
        Frame.__init__(self)

        self.__x, self.__y=0, 0 #THIS TELLS POSITIVE MOVEMENT
        self.__x3, self.__y3=0,0 #This tells negative movement
        self.__x2, self.__y2=0, 0 #THIS IS TELLING US WHAT FRAME IT IS SO ARMS IN OR ARMS OUT? IT WILL CHANGE EVERYTIME. MSG ME IF U DONT understand :)
        self.__sprint = 0
        #self.__name1 = 100
        #self.__name2 = 100
        
        #KEYBINDINGS
        def spaceKey(event): #Special ability
            print("'spacebar' key pressed")
            
        def sKey(event): #Drop down, prone
            print("'s' key pressed")
        
        def wKey(event): #Jump
            print("'w' key pressed")
            
        def leftClick(event): #Basic attack
            print("Left Click")

        def rightClick(event): #Take aim
            print("Right Click")

        def scroll(event): #Switch weapons
            print("Scroll Click")

        def aKey(event): #Move left
            print("'a' key pressed")
            self.__x3 -= 1
            if self.__x2 == 0 and self.__sprint == False:
                increment = 1*self.__x3 #Arms and legs out increment+self.__x 
                self.myCanvas.coords(a_head, 125+increment+self.__x, 125, 150+increment+self.__x, 150)
                self.myCanvas.coords(a_name, 138+increment+self.__x, 110)
                self.myCanvas.coords(a_torso, 130+increment+self.__x, 150, 145+increment+self.__x, 150, 145+increment+self.__x, 175, 130+increment+self.__x, 175)
                self.myCanvas.coords(a_Larm, 115+increment+self.__x, 150, 130+increment+self.__x, 165)
                self.myCanvas.coords(a_Rarm, 145+increment+self.__x, 150, 160+increment+self.__x, 165)
                self.myCanvas.coords(a_Rleg, 145+increment+self.__x, 175, 160+increment+self.__x, 183)
                self.myCanvas.coords(a_Lleg, 115+increment+self.__x, 175, 130+increment+self.__x, 183)
                self.myCanvas.coords(a_bandana1, 125+increment+self.__x+25, 140, 150+increment+self.__x-25, 140, 150+increment+self.__x-25, 150)
                self.myCanvas.coords(a_bandana2, 125+increment+self.__x+25, 140, 120+increment+self.__x+35, 142, 120+increment+self.__x+35, 145)
                self.myCanvas.coords(a_bandana3, 125+increment+self.__x+25, 140, 120+increment+self.__x+35, 138, 120+increment+self.__x+35, 141)
                self.myCanvas.coords(a_vneck, 130+increment+self.__x, 155, 145+increment+self.__x, 150, 145+increment+self.__x, 175, 130+increment+self.__x, 175)
                self.myCanvas.coords(a_coat, 145+increment+self.__x, 145, 133+increment+self.__x, 145, 140+increment+self.__x, 175, 160+increment+self.__x, 177, 145+increment+self.__x, 160)
                self.__x2 = 1
                
            elif self.__x2 == 1 and self.__sprint == False:
                increment = 1*self.__x3 #Arms and legs in
                self.myCanvas.coords(a_head, 125+increment+self.__x, 125+3, 150+increment+self.__x, 150+3)
                self.myCanvas.coords(a_name, 138+increment+self.__x, 110)
                self.myCanvas.coords(a_torso, 130+increment+self.__x, 150+3, 145+increment+self.__x, 150+3, 145+increment+self.__x, 175+3, 130+increment+self.__x, 175+3)
                self.myCanvas.coords(a_Larm, 130+increment+self.__x, 160, 145+increment+self.__x, 175) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO
                self.myCanvas.coords(a_Rarm, 130+increment+self.__x, 160, 145+increment+self.__x, 175) #Arm hides behind torso
                self.myCanvas.coords(a_Rleg, 145+increment+self.__x-10, 175, 160+increment+self.__x-10, 183)
                self.myCanvas.coords(a_Lleg, 115+increment+self.__x+10, 175, 130+increment+self.__x+10, 183)
                self.myCanvas.coords(a_bandana1, 125+increment+self.__x+25, 140+3, 150+increment+self.__x-25, 140+3, 150+increment+self.__x-25, 150+3)
                self.myCanvas.coords(a_bandana2, 125+increment+self.__x+25, 140+3, 120+increment+self.__x+35, 142+3, 120+increment+self.__x+35, 145+3)
                self.myCanvas.coords(a_bandana3, 125+increment+self.__x+25, 140+3, 120+increment+self.__x+35, 138+3, 120+increment+self.__x+35, 141+3)
                self.myCanvas.coords(a_vneck, 130+increment+self.__x, 155+3, 145+increment+self.__x, 150+3, 145+increment+self.__x, 175+3, 130+increment+self.__x, 175+3)
                self.myCanvas.coords(a_coat, 145+increment+self.__x, 145+3, 133+increment+self.__x, 145+3, 140+increment+self.__x, 175+3, 160+increment+self.__x, 177+6, 145+increment+self.__x, 160+3)
                self.__x2 = 0

            elif self.__x2 == 0 and self.__sprint == True:
                increment = 1*self.__x3  #Arms and legs out
                self.myCanvas.coords(a_head, 145+increment+self.__x-40, 135, 170+increment+self.__x-40, 160) #(+20, +10) difference from walking
                self.myCanvas.coords(a_name, 138+increment+self.__x, 110)
                self.myCanvas.coords(a_torso, 140+increment+self.__x-4, 150, 150+increment+self.__x-24, 160, 125+increment+self.__x+26, 170, 115+increment+self.__x+46, 160) #(10, 0), (5,10), (-20,-5), (-15,-15)
                self.myCanvas.coords(a_Larm, 85+increment+self.__x+106, 150, 100+increment+self.__x+76, 165) #(-30,0)
                self.myCanvas.coords(a_Rarm, 175+increment+self.__x-74, 150, 190+increment+self.__x-104, 165) #(+30,0)
                self.myCanvas.coords(a_Rleg, 150+increment+self.__x-24, 170, 165+increment+self.__x-54, 178) #(+5,-5), (+5,-5)
                self.myCanvas.coords(a_Lleg, 110+increment+self.__x+56, 170, 125+increment+self.__x+26, 178) #(-5,-5), (-5,-5)
                self.myCanvas.coords(a_bandana1, 145+increment+self.__x-14, 150, 170+increment+self.__x-64, 150, 170+increment+self.__x-64, 160) #(+20,10) for all bandana
                self.myCanvas.coords(a_bandana2, 145+increment+self.__x-14, 150, 140+increment+self.__x-4, 152, 140+increment+self.__x-4, 160)
                self.myCanvas.coords(a_bandana3, 145+increment+self.__x-14, 150, 140+increment+self.__x-4, 148, 140+increment+self.__x-4, 151) 
                self.myCanvas.coords(a_vneck, 140+increment+self.__x-4, 150, 145+increment+self.__x-14, 163, 125+increment+self.__x+26, 170, 115+increment+self.__x+46, 160) #(10,0), (0,8), (-20,-5), (-15,-15)
                self.myCanvas.coords(a_coat, 142+increment+self.__x-8, 145, 152+increment+self.__x-28, 155, 100+increment+self.__x+76, 175, 85+increment+self.__x+104, 157, 125+increment+self.__x+26, 155)
                self.__x3 -= 5
                #(12,0) (10,10), (-35,0), (-30,-20), (-5,-5)
                self.__x2 = 1
                
            elif self.__x2 == 1 and self.__sprint == True:
                increment = 1*self.__x3  #Arms and legs in
                self.myCanvas.coords(a_head, 145+increment+self.__x-40, 135+5, 170+increment+self.__x-40, 160+5) #(+20, +10) difference from walking
                self.myCanvas.coords(a_name, 138+increment+self.__x, 110)
                self.myCanvas.coords(a_torso, 140+increment+self.__x-4, 150+5, 150+increment+self.__x-24, 160+5, 125+increment+self.__x+26, 170+5, 115+increment+self.__x+46, 160+5) #(20, 10), (5,10)
                self.myCanvas.coords(a_Larm, 130+increment+self.__x+16, 160, 145+increment+self.__x-14, 175) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                self.myCanvas.coords(a_Rarm, 130+increment+self.__x+16, 160, 145+increment+self.__x-14, 175) #Arm hides behind torso (+30,0)
                self.myCanvas.coords(a_Rleg, 145+increment+self.__x-10, 175, 160+increment+self.__x-10, 183)
                self.myCanvas.coords(a_Lleg, 115+increment+self.__x+10, 175, 130+increment+self.__x+10, 183)
                self.myCanvas.coords(a_bandana1, 145+increment+self.__x-14, 150+5, 170+increment+self.__x-64, 150+5, 170+increment+self.__x-64, 160+5) #(+20,10) for all bandana
                self.myCanvas.coords(a_bandana2, 145+increment+self.__x-14, 150+5, 140+increment+self.__x-4, 152+5, 140+increment+self.__x-4, 160+5)
                self.myCanvas.coords(a_bandana3, 145+increment+self.__x-14, 150+5, 140+increment+self.__x-4, 148+5, 140+increment+self.__x-4, 151+5) 
                self.myCanvas.coords(a_vneck, 140+increment+self.__x-4, 150+5, 145+increment+self.__x-14, 163+5, 125+increment+self.__x+26, 170+5, 115+increment+self.__x+46, 160+5) #(10,0), (0,8), (-20,-5), (-15,-15)
                self.myCanvas.coords(a_coat, 142+increment+self.__x-8, 145+5, 152+increment+self.__x-28, 155+5, 100+increment+self.__x+76, 175+10, 85+increment+self.__x+104, 157+10, 125+increment+self.__x+26, 155+5)
                #(12,0) (10,10), (-35,0), (-30,-20), (-5,-5)
                self.__x3 -= 5
                self.__x2 = 0
                
            self.myCanvas.update()

        def dKey(event): #Move right
            print("'d' key pressed")
            self.__x += 1
            if self.__x2 == 0 and self.__sprint == False:
                increment = 1*self.__x #Arms and legs out increment+self.__x3 
                self.myCanvas.coords(a_head, 125+increment+self.__x3, 125, 150+increment+self.__x3, 150)
                self.myCanvas.coords(a_name, 138+increment+self.__x3, 110)
                self.myCanvas.coords(a_torso, 130+increment+self.__x3, 150, 145+increment+self.__x3, 150, 145+increment+self.__x3, 175, 130+increment+self.__x3, 175)
                self.myCanvas.coords(a_Larm, 115+increment+self.__x3, 150, 130+increment+self.__x3, 165)
                self.myCanvas.coords(a_Rarm, 145+increment+self.__x3, 150, 160+increment+self.__x3, 165)
                self.myCanvas.coords(a_Rleg, 145+increment+self.__x3, 175, 160+increment+self.__x3, 183)
                self.myCanvas.coords(a_Lleg, 115+increment+self.__x3, 175, 130+increment+self.__x3, 183)
                self.myCanvas.coords(a_bandana1, 125+increment+self.__x3, 140, 150+increment+self.__x3, 140, 150+increment+self.__x3, 150)
                self.myCanvas.coords(a_bandana2, 125+increment+self.__x3, 140, 120+increment+self.__x3, 142, 120+increment+self.__x3, 145)
                self.myCanvas.coords(a_bandana3, 125+increment+self.__x3, 140, 120+increment+self.__x3, 138, 120+increment+self.__x3, 141)
                self.myCanvas.coords(a_vneck, 130+increment+self.__x3, 150, 145+increment+self.__x3, 155, 145+increment+self.__x3, 175, 130+increment+self.__x3, 175)
                self.myCanvas.coords(a_coat, 130+increment+self.__x3, 145, 142+increment+self.__x3, 145, 135+increment+self.__x3, 175, 115+increment+self.__x3, 177, 130+increment+self.__x3, 160)
                self.__x2 = 1
                
            elif self.__x2 == 1 and self.__sprint == False:
                increment = 1*self.__x #Arms and legs in
                self.myCanvas.coords(a_head, 125+increment+self.__x3, 125+3, 150+increment+self.__x3, 150+3)
                self.myCanvas.coords(a_name, 138+increment+self.__x3, 110)
                self.myCanvas.coords(a_torso, 130+increment+self.__x3, 150+3, 145+increment+self.__x3, 150+3, 145+increment+self.__x3, 175+3, 130+increment+self.__x3, 175+3)
                self.myCanvas.coords(a_Larm, 130+increment+self.__x3, 160, 145+increment+self.__x3, 175) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO
                self.myCanvas.coords(a_Rarm, 130+increment+self.__x3, 160, 145+increment+self.__x3, 175) #Arm hides behind torso
                self.myCanvas.coords(a_Rleg, 145+increment+self.__x3-10, 175, 160+increment+self.__x3-10, 183)
                self.myCanvas.coords(a_Lleg, 115+increment+self.__x3+10, 175, 130+increment+self.__x3+10, 183)
                self.myCanvas.coords(a_bandana1, 125+increment+self.__x3, 140+3, 150+increment+self.__x3, 140+3, 150+increment+self.__x3, 150+3)
                self.myCanvas.coords(a_bandana2, 125+increment+self.__x3, 140+3, 120+increment+self.__x3, 142+3, 120+increment+self.__x3, 145+3)
                self.myCanvas.coords(a_bandana3, 125+increment+self.__x3, 140+3, 120+increment+self.__x3, 138+3, 120+increment+self.__x3, 141+3)
                self.myCanvas.coords(a_vneck, 130+increment+self.__x3, 150+3, 145+increment+self.__x3, 155+3, 145+increment+self.__x3, 175+3, 130+increment+self.__x3, 175+3)
                self.myCanvas.coords(a_coat, 130+increment+self.__x3, 145+3, 142+increment+self.__x3, 145+3, 135+increment+self.__x3, 175+3, 115+increment+self.__x3, 177+6, 130+increment+self.__x3, 160)
                self.__x2 = 0

            elif self.__x2 == 0 and self.__sprint == True:
                increment = 1*self.__x  #Arms and legs out
                self.myCanvas.coords(a_head, 145+increment+self.__x3, 135, 170+increment+self.__x3, 160) #(+20, +10) difference from walking
                self.myCanvas.coords(a_name, 138+increment+self.__x3, 110)
                self.myCanvas.coords(a_torso, 140+increment+self.__x3, 150, 150+increment+self.__x3, 160, 125+increment+self.__x3, 170, 115+increment+self.__x3, 160) #(10, 0), (5,10), (-20,-5), (-15,-15)
                self.myCanvas.coords(a_Larm, 85+increment+self.__x3, 150, 100+increment+self.__x3, 165) #(-30,0)
                self.myCanvas.coords(a_Rarm, 175+increment+self.__x3, 150, 190+increment+self.__x3, 165) #(+30,0)
                self.myCanvas.coords(a_Rleg, 150+increment+self.__x3, 170, 165+increment+self.__x3, 178) #(+5,-5), (+5,-5)
                self.myCanvas.coords(a_Lleg, 110+increment+self.__x3, 170, 125+increment+self.__x3, 178) #(-5,-5), (-5,-5)
                self.myCanvas.coords(a_bandana1, 145+increment+self.__x3, 150, 170+increment+self.__x3, 150, 170+increment+self.__x3, 160) #(+20,10) for all bandana
                self.myCanvas.coords(a_bandana2, 145+increment+self.__x3, 150, 140+increment+self.__x3, 152, 140+increment+self.__x3, 160)
                self.myCanvas.coords(a_bandana3, 145+increment+self.__x3, 150, 140+increment+self.__x3, 148, 140+increment+self.__x3, 151) 
                self.myCanvas.coords(a_vneck, 140+increment+self.__x3, 150, 145+increment+self.__x3, 163, 125+increment+self.__x3, 170, 115+increment+self.__x3, 160) #(10,0), (0,8), (-20,-5), (-15,-15)
                self.myCanvas.coords(a_coat, 142+increment+self.__x3, 145, 152+increment+self.__x3, 155, 100+increment+self.__x3, 175, 85+increment+self.__x3, 157, 125+increment+self.__x3, 155)
                self.__x += 5
                #(12,0) (10,10), (-35,0), (-30,-20), (-5,-5)
                self.__x2 = 1
                
            elif self.__x2 == 1 and self.__sprint == True:
                increment = 1*self.__x  #Arms and legs in
                self.myCanvas.coords(a_head, 145+increment+self.__x3, 135+5, 170+increment+self.__x3, 160+5) #(+20, +10) difference from walking
                self.myCanvas.coords(a_name, 138+increment+self.__x3, 110)
                self.myCanvas.coords(a_torso, 140+increment+self.__x3, 150+5, 150+increment+self.__x3, 160+5, 125+increment+self.__x3, 170+5, 115+increment+self.__x3, 160+5) #(20, 10), (5,10)
                self.myCanvas.coords(a_Larm, 130+increment+self.__x3, 160, 145+increment+self.__x3, 175) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                self.myCanvas.coords(a_Rarm, 130+increment+self.__x3, 150, 145+increment+self.__x3, 175) #Arm hides behind torso (+30,0)
                self.myCanvas.coords(a_Rleg, 145+increment+self.__x3-10, 175, 160+increment+self.__x3-10, 183)
                self.myCanvas.coords(a_Lleg, 115+increment+self.__x3+10, 175, 130+increment+self.__x3+10, 183)
                self.myCanvas.coords(a_bandana1, 145+increment+self.__x3, 150+5, 170+increment+self.__x3, 150+5, 170+increment+self.__x3, 160+5) #(+20,10) for all bandana
                self.myCanvas.coords(a_bandana2, 145+increment+self.__x3, 150+5, 140+increment+self.__x3, 152+5, 140+increment+self.__x3, 155+5)
                self.myCanvas.coords(a_bandana3, 145+increment+self.__x3, 150+5, 140+increment+self.__x3, 148+5, 140+increment+self.__x3, 151+5)
                self.myCanvas.coords(a_vneck, 140+increment+self.__x3, 150+5, 145+increment+self.__x3, 163+5, 125+increment+self.__x3, 170+5, 115+increment+self.__x3, 160+5) #(10,0), (0,8), (-20,-5), (-15,-15)
                self.myCanvas.coords(a_coat, 142+increment+self.__x3, 145+5, 152+increment+self.__x3, 155+5, 100+increment+self.__x3, 175+10, 85+increment+self.__x3, 157+10, 125+increment+self.__x3, 155+5)
                #(12,0) (10,10), (-35,0), (-30,-20), (-5,-5)
                self.__x += 5
                self.__x2 = 0
                
            self.myCanvas.update()


        def shiftKey(event): #Sprint/Walk toggle
            print("'Shift' key pressed")
            if self.__sprint == True:
                self.__sprint = False
            else:
                self.__sprint = True

        def ctrlKey(event): #Prone
            print("'Control' key pressed")

        def randomRects(num): #FOR BACKGROUND
            for i in range(0,num):
                x1=random.randrange(1000)
                y1=random.randrange(1000)
                x2=x1+random.randrange(1000)
                y2=y1+random.randrange(1000)
                self.myCanvas.create_rectangle(x1,y1,x2,y2,outline="black")

        self.master.title("Harbinger - Alpha 1.3: Keybinding Update") #Titles the window "Harbinger"

        self.myCanvas = Canvas(width=1500, height=1000, bg="SkyBlue1") #Background with window size. bg= "SkyBlue1"
        self.myCanvas.grid() #Display it

        #randomRects(300) #BACKGROUND
        
        a_description = self.myCanvas.create_text(0, 0, text="""Press 'd' or 'a' to move. Hold 'd' or 'a' to walk. Press Shift to change from walking to running. Vise-vera."""
                                                  """ Press left and right mouse buttons do nothing but show up on the interpeter."""
                                                  """ Will try to make him jump and crouch next update""",
                                                  width=1000, fill="black", anchor="nw", font=("Fixedsys", 16))#Top left corner of screen text
        
        #Creating the model of player 1 w/ label above it's head
        #Character is walking to the right of the screen
        #Name of the character
        a_name = self.myCanvas.create_text(138, 110, text="Player", width=1000, fill="green", anchor="center", font=("Fixedsys", 16))

        #Creates the head of character
        a_head = self.myCanvas.create_oval(125, 125, 150, 150, fill="white")

        #HIS RIGHT ARM ANIMATIONS NEEDS TO BE BEHIND TORSO BC IT WOULD SHOW
        a_Rarm = self.myCanvas.create_oval(130, 160, 145, 175, fill="white")
        
        #Torso
        a_torso = self.myCanvas.create_polygon(130, 150, 145, 150, 145, 175, 130, 175, fill="white")

        #Moved Left arm to bottom bc it is needed for the animations

        #HIS right arm (FRONT ARM) MOVED TO BOTTOM FOR ANIMATIONS
        
        
        #HIS right leg (FRONT LEG)
        a_Rleg = self.myCanvas.create_oval(135, 175, 150, 183, fill="saddle brown")

        #HIS left leg (BACK LEG)
        a_Lleg = self.myCanvas.create_oval(125, 175, 140, 183, fill="saddle brown")

        #Bandana
        a_bandana1 = self.myCanvas.create_polygon(125, 140, 150, 140, 150, 150, fill="black") #Creates a polyon (triangle). Main part of banadana


        #V-neck
        a_vneck = self.myCanvas.create_polygon(130, 150, 145, 155, 145, 175, 130, 175, fill="dark blue")
        
        #Coat
        a_coat = self.myCanvas.create_polygon(130, 145, 142, 145, 135, 175, 115, 177, 130, 160, fill="gray14")

        #HIS left arm PLACED HERE BC NEEDED FOR ANIMATION (BACK ARM)
        a_Larm = self.myCanvas.create_oval(130, 160, 145, 175, fill="white")

        #Other bandanna parts moved here so they overlap the coat
        a_bandana2 = self.myCanvas.create_polygon(125, 140, 120, 142, 120, 145, fill="black") #Knot down
        a_bandana3 = self.myCanvas.create_polygon(125, 140, 120, 138, 120, 141, fill="black") #Knot up

        #KEYBINDINGS
        self.myCanvas.bind("<Button-1>", leftClick)
        self.myCanvas.bind("<Button-2>", scroll)
        self.myCanvas.bind("<Button-3>", rightClick)
        self.myCanvas.bind("<a>", aKey)
        self.myCanvas.bind("<d>", dKey)
        self.myCanvas.bind("<s>", sKey)
        self.myCanvas.bind("<w>", wKey)
        self.myCanvas.bind("<Shift_R>", shiftKey)
        self.myCanvas.bind("<Shift_L>", shiftKey)
        self.myCanvas.bind("<Control_L>", ctrlKey)
        self.myCanvas.bind("<Control_R>", ctrlKey)
        self.myCanvas.bind("<space>", spaceKey)
        self.myCanvas.focus_set() #Tells Python to use keyboard so left and right arrow keys work now

        #IDK HOW TO CREATE A BUTTON IN THE MAIN WINDOW WILL DO LATER
        #button1=Button(main_frame,text="Click Me")
        #button1.bind("<Button-1>",printName)
        #button1.pack()
        
main_frame = MainFrame()
main_frame.mainloop()
