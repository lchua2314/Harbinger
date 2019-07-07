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

        self.__x, self.__y=1, 1 #THIS TELLS WHERE YOUR CHARACTER IS ON THE WINDOW AT ALL TIMES
        self.__x2, self.__y2=0, 0 #THIS IS TELLING US WHAT FRAME IT IS SO ARMS IN OR ARMS OUT? IT WILL CHANGE EVERYTIME. MSG ME IF U DONT understand :)
        self.__sprint = 0
        
        #KEYBINDINGS
        def leftClick(event):
            print("Left")

        def rightClick(event):
            print("Right")

        def scroll(event):
            print("Scroll")

        def aKey(event):
            print("'a' key pressed")

        def dKey(event):
            print("'d' key pressed")
            if self.__x2 == 0 and self.__sprint == False:
                increment = 1*self.__x #Arms and legs out INCREMENT X
                self.myCanvas.coords(a_head, 125+increment, 125, 150+increment, 150)
                self.myCanvas.coords(a_name, 100+increment, 100)
                self.myCanvas.coords(a_torso, 130+increment, 150, 145+increment, 150, 145+increment, 175, 130+increment, 175)
                self.myCanvas.coords(a_Larm, 115+increment, 150, 130+increment, 165)
                self.myCanvas.coords(a_Rarm, 145+increment, 150, 160+increment, 165)
                self.myCanvas.coords(a_Rleg, 145+increment, 175, 160+increment, 183)
                self.myCanvas.coords(a_Lleg, 115+increment, 175, 130+increment, 183)
                self.myCanvas.coords(a_bandana1, 125+increment, 140, 150+increment, 140, 150+increment, 150)
                self.myCanvas.coords(a_bandana2, 125+increment, 140, 120+increment, 142, 120+increment, 145)
                self.myCanvas.coords(a_bandana3, 125+increment, 140, 120+increment, 138, 120+increment, 141)
                self.myCanvas.coords(a_vneck, 130+increment, 150, 145+increment, 155, 145+increment, 175, 130+increment, 175)
                self.myCanvas.coords(a_coat, 130+increment, 145, 142+increment, 145, 135+increment, 175, 115+increment, 177, 130+increment, 160)

                self.myCanvas.coords(a_head, 125+increment, 125, 150+increment, 150)
                self.myCanvas.coords(a_name, 100+increment, 100)
                self.myCanvas.coords(a_torso, 130+increment, 150, 145+increment, 150, 145+increment, 175, 130+increment, 175)
                self.myCanvas.coords(a_Larm, 115+increment, 150, 130+increment, 165)
                self.myCanvas.coords(a_Rarm, 145+increment, 150, 160+increment, 165)
                self.myCanvas.coords(a_Rleg, 145+increment, 175, 160+increment, 183)
                self.myCanvas.coords(a_Lleg, 115+increment, 175, 130+increment, 183)
                self.myCanvas.coords(a_bandana1, 125+increment, 140, 150+increment, 140, 150+increment, 150)
                self.myCanvas.coords(a_bandana2, 125+increment, 140, 120+increment, 142, 120+increment, 145)
                self.myCanvas.coords(a_bandana3, 125+increment, 140, 120+increment, 138, 120+increment, 141)
                self.myCanvas.coords(a_vneck, 130+increment, 150, 145+increment, 155, 145+increment, 175, 130+increment, 175)
                self.myCanvas.coords(a_coat, 130+increment, 145, 142+increment, 145, 135+increment, 175, 115+increment, 177, 130+increment, 160)
                self.__x2 = 1
                
            elif self.__x2 == 1 and self.__sprint == False:
                increment2 = 1*self.__x #Arms and legs in
                self.myCanvas.coords(a_head, 125+increment2, 125+3, 150+increment2, 150+3)
                self.myCanvas.coords(a_name, 100+increment2, 100)
                self.myCanvas.coords(a_torso, 130+increment2, 150+3, 145+increment2, 150+3, 145+increment2, 175+3, 130+increment2, 175+3)
                self.myCanvas.coords(a_Larm, 130+increment2, 160, 145+increment2, 175) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO
                self.myCanvas.coords(a_Rarm, 130+increment2, 160, 145+increment2, 175) #Arm hides behind torso
                self.myCanvas.coords(a_Rleg, 145+increment2-10, 175, 160+increment2-10, 183)
                self.myCanvas.coords(a_Lleg, 115+increment2+10, 175, 130+increment2+10, 183)
                self.myCanvas.coords(a_bandana1, 125+increment2, 140+3, 150+increment2, 140+3, 150+increment2, 150+3)
                self.myCanvas.coords(a_bandana2, 125+increment2, 140+3, 120+increment2, 142+3, 120+increment2, 145+3)
                self.myCanvas.coords(a_bandana3, 125+increment2, 140+3, 120+increment2, 138+3, 120+increment2, 141+3)
                self.myCanvas.coords(a_vneck, 130+increment2, 150+3, 145+increment2, 155+3, 145+increment2, 175+3, 130+increment2, 175+3)
                self.myCanvas.coords(a_coat, 130+increment2, 145+3, 142+increment2, 145+3, 135+increment2, 175+3, 115+increment2, 177+3, 130+increment2, 160)

                self.myCanvas.coords(a_head, 125+increment2, 125+3, 150+increment2, 150+3)
                self.myCanvas.coords(a_name, 100+increment2, 100)
                self.myCanvas.coords(a_torso, 130+increment2, 150+3, 145+increment2, 150+3, 145+increment2, 175+3, 130+increment2, 175+3)
                self.myCanvas.coords(a_Larm, 130+increment2, 160, 145+increment2, 175) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO
                self.myCanvas.coords(a_Rarm, 130+increment2, 160, 145+increment2, 175) #Arm hides behind torso
                self.myCanvas.coords(a_Rleg, 145+increment2-10, 175, 160+increment2-10, 183)
                self.myCanvas.coords(a_Lleg, 115+increment2+10, 175, 130+increment2+10, 183)
                self.myCanvas.coords(a_bandana1, 125+increment2, 140+3, 150+increment2, 140+3, 150+increment2, 150+3)
                self.myCanvas.coords(a_bandana2, 125+increment2, 140+3, 120+increment2, 142+3, 120+increment2, 145+3)
                self.myCanvas.coords(a_bandana3, 125+increment2, 140+3, 120+increment2, 138+3, 120+increment2, 141+3)
                self.myCanvas.coords(a_vneck, 130+increment2, 150+3, 145+increment2, 155+3, 145+increment2, 175+3, 130+increment2, 175+3)
                self.myCanvas.coords(a_coat, 130+increment2, 145+3, 142+increment2, 145+3, 135+increment2, 175+3, 115+increment2, 177+3, 130+increment2, 160)
                self.__x2 = 0

            elif self.__x2 == 0 and self.__sprint == True:
                increment = 1*self.__x  #Arms and legs out
                self.myCanvas.coords(a_head, 145+increment, 135, 170+increment, 160) #(+20, +10) difference from walking
                self.myCanvas.coords(a_name, 100+increment, 100)
                self.myCanvas.coords(a_torso, 140+increment, 150, 150+increment, 160, 125+increment, 170, 115+increment, 160) #(10, 0), (5,10), (-20,-5), (-15,-15)
                self.myCanvas.coords(a_Larm, 85+increment, 150, 100+increment, 165) #(-30,0)
                self.myCanvas.coords(a_Rarm, 175+increment, 150, 190+increment, 165) #(+30,0)
                self.myCanvas.coords(a_Rleg, 150+increment, 170, 165+increment, 178) #(+5,-5), (+5,-5)
                self.myCanvas.coords(a_Lleg, 110+increment, 170, 125+increment, 178) #(-5,-5), (-5,-5)
                self.myCanvas.coords(a_bandana1, 145+increment, 150, 170+increment, 150, 170+increment, 160) #(+20,10) for all bandana
                self.myCanvas.coords(a_bandana2, 145+increment, 150, 140+increment, 152, 140+increment, 160)
                self.myCanvas.coords(a_bandana3, 145+increment, 150, 140+increment, 148, 140+increment, 151) 
                self.myCanvas.coords(a_vneck, 140+increment, 150, 145+increment, 163, 125+increment, 170, 115+increment, 160) #(10,0), (0,8), (-20,-5), (-15,-15)
                self.myCanvas.coords(a_coat, 142+increment, 145, 152+increment, 155, 100+increment, 175, 85+increment, 157, 125+increment, 155)
                #(12,0) (10,10), (-35,0), (-30,-20), (-5,-5)

                self.myCanvas.coords(a_head, 145+increment, 135, 170+increment, 160) #(+20, +10) difference from walking
                self.myCanvas.coords(a_name, 100+increment, 100)
                self.myCanvas.coords(a_torso, 140+increment, 150, 150+increment, 160, 125+increment, 170, 115+increment, 160) #(10, 0), (5,10), (-20,-5), (-15,-15)
                self.myCanvas.coords(a_Larm, 85+increment, 150, 100+increment, 165) #(-30,0)
                self.myCanvas.coords(a_Rarm, 175+increment, 150, 190+increment, 165) #(+30,0)
                self.myCanvas.coords(a_Rleg, 150+increment, 170, 165+increment, 178) #(+5,-5), (+5,-5)
                self.myCanvas.coords(a_Lleg, 110+increment, 170, 125+increment, 178) #(-5,-5), (-5,-5)
                self.myCanvas.coords(a_bandana1, 145+increment, 150, 170+increment, 150, 170+increment, 160) #(+20,10) for all bandana
                self.myCanvas.coords(a_bandana2, 145+increment, 150, 140+increment, 152, 140+increment, 160)
                self.myCanvas.coords(a_bandana3, 145+increment, 150, 140+increment, 148, 140+increment, 151) 
                self.myCanvas.coords(a_vneck, 140+increment, 150, 145+increment, 163, 125+increment, 170, 115+increment, 160) #(10,0), (0,8), (-20,-5), (-15,-15)
                self.myCanvas.coords(a_coat, 142+increment, 145, 152+increment, 155, 100+increment, 175, 85+increment, 157, 125+increment, 155)
                self.__x += 5
                #(12,0) (10,10), (-35,0), (-30,-20), (-5,-5)
                self.__x2 = 1
                
            elif self.__x2 == 1 and self.__sprint == True:
                increment2 = 1*self.__x  #Arms and legs in
                self.myCanvas.coords(a_head, 145+increment2, 135+5, 170+increment2, 160+5) #(+20, +10) difference from walking
                self.myCanvas.coords(a_name, 100+increment2, 100)
                self.myCanvas.coords(a_torso, 140+increment2, 150+5, 150+increment2, 160+5, 125+increment2, 170+5, 115+increment2, 160+5) #(20, 10), (5,10)
                self.myCanvas.coords(a_Larm, 130+increment2, 160, 145+increment2, 175) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                self.myCanvas.coords(a_Rarm, 130+increment2, 150, 145+increment2, 175) #Arm hides behind torso (+30,0)
                self.myCanvas.coords(a_Rleg, 145+increment2-10, 175, 160+increment2-10, 183)
                self.myCanvas.coords(a_Lleg, 115+increment2+10, 175, 130+increment2+10, 183)
                self.myCanvas.coords(a_bandana1, 145+increment2, 150+5, 170+increment2, 150+5, 170+increment2, 160+5) #(+20,10) for all bandana
                self.myCanvas.coords(a_bandana2, 145+increment2, 150+5, 140+increment2, 152+5, 140+increment2, 155+5)
                self.myCanvas.coords(a_bandana3, 145+increment2, 150+5, 140+increment2, 148+5, 140+increment2, 151+5)
                self.myCanvas.coords(a_vneck, 140+increment2, 150+5, 145+increment2, 163+5, 125+increment2, 170+5, 115+increment2, 160+5) #(10,0), (0,8), (-20,-5), (-15,-15)
                self.myCanvas.coords(a_coat, 142+increment2, 145+5, 152+increment2, 155+5, 100+increment2, 175+10, 85+increment2, 157+10, 125+increment2, 155+5)
                #(12,0) (10,10), (-35,0), (-30,-20), (-5,-5)

                self.myCanvas.coords(a_head, 145+increment2, 135+5, 170+increment2, 160+5) #(+20, +10) difference from walking
                self.myCanvas.coords(a_name, 100+increment2, 100)
                self.myCanvas.coords(a_torso, 140+increment2, 150+5, 150+increment2, 160+5, 125+increment2, 170+5, 115+increment2, 160+5) #(20, 10), (5,10)
                self.myCanvas.coords(a_Larm, 130+increment2, 160, 145+increment2, 175) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                self.myCanvas.coords(a_Rarm, 130+increment2, 150, 145+increment2, 175) #Arm hides behind torso (+30,0)
                self.myCanvas.coords(a_Rleg, 145+increment2-10, 175, 160+increment2-10, 183)
                self.myCanvas.coords(a_Lleg, 115+increment2+10, 175, 130+increment2+10, 183)
                self.myCanvas.coords(a_bandana1, 145+increment2, 150+5, 170+increment2, 150+5, 170+increment2, 160+5) #(+20,10) for all bandana
                self.myCanvas.coords(a_bandana2, 145+increment2, 150+5, 140+increment2, 152+5, 140+increment2, 155+5)
                self.myCanvas.coords(a_bandana3, 145+increment2, 150+5, 140+increment2, 148+5, 140+increment2, 151+5)
                self.myCanvas.coords(a_vneck, 140+increment2, 150+5, 145+increment2, 163+5, 125+increment2, 170+5, 115+increment2, 160+5) #(10,0), (0,8), (-20,-5), (-15,-15)
                self.myCanvas.coords(a_coat, 142+increment2, 145+5, 152+increment2, 155+5, 100+increment2, 175+10, 85+increment2, 157+10, 125+increment2, 155+5)
                #(12,0) (10,10), (-35,0), (-30,-20), (-5,-5)
                self.__x += 5
                self.__x2 = 0

            self.__x += 1
            self.myCanvas.update()

        def ctrlKey(event):
            print("'Ctrl' key pressed")
            if self.__sprint == True:
                self.__sprint = False
            else:
                self.__sprint = True

        self.master.title("Harbinger - Alpha 1.3: Keybinding Update") #Titles the window "Harbinger"

        self.myCanvas = Canvas(width=1500, height=1000, bg="SkyBlue1") #Background with window size
        self.myCanvas.grid() #Display it
        
        a_description = self.myCanvas.create_text(0, 0, text="""Press 'd' to move. Hold 'd' to walk. Press Ctrl to change from walking to running. Vise-vera."""
                                                              """Also, please find a way to get the sprint to move faster than walking"""
                                                  """Press left and right mouse buttons do nothing but show up on the interpeter. Same with 'a' and 'd'""",
                                                  width=1000, fill="black", anchor="nw", font=("Fixedsys", 16))#Top left corner of screen text
        
        #Creating the model of player 1 w/ label above it's head
        #Character is walking to the right of the screen
        #Name of the character
        a_name = self.myCanvas.create_text(100, 100, text="Player 1", width=1000, fill="black", anchor="nw", font=("Fixedsys", 16))

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
        a_bandana2 = self.myCanvas.create_polygon(125, 140, 120, 142, 120, 145, fill="black") #Knot down
        a_bandana3 = self.myCanvas.create_polygon(125, 140, 120, 138, 120, 141, fill="black") #Knot up

        #V-neck
        a_vneck = self.myCanvas.create_polygon(130, 150, 145, 155, 145, 175, 130, 175, fill="dark blue")
        
        #Coat
        a_coat = self.myCanvas.create_polygon(130, 145, 142, 145, 135, 175, 115, 177, 130, 160, fill="gray14")

        #HIS left arm PLACED HERE BC NEEDED FOR ANIMATION (BACK ARM)
        a_Larm = self.myCanvas.create_oval(130, 160, 145, 175, fill="white")

        #KEYBINDINGS
        self.myCanvas.bind("<Button-1>", leftClick)
        self.myCanvas.bind("<Button-2>", scroll)
        self.myCanvas.bind("<Button-3>", rightClick)
        self.myCanvas.bind("<a>", aKey)
        self.myCanvas.bind("<d>", dKey)
        self.myCanvas.bind("<Control_L>", ctrlKey)
        self.myCanvas.bind("<Control_R>", ctrlKey)
        self.myCanvas.focus_set() #Tells Python to use keyboard so left and right arrow keys work now

        #IDK HOW TO CREATE A BUTTON IN THE MAIN WINDOW WILL DO LATER
        #button1=Button(main_frame,text="Click Me")
        #button1.bind("<Button-1>",printName)
        #button1.pack()
        
main_frame = MainFrame()
main_frame.mainloop()
