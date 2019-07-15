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

        self.__x, self.__y = 0,0 #Only one coordinate now. This coordinate is where the first shape is initialized. Not the graph.
        self.__Frame = 0 #Two frames-0 and 1. They alternate which makes the character move more lively.
        self.__sprint = False 
        self.__crouch = False
        self.__inAir = False #If player is mid-air, do not run the other animations (walking, crouching, sprinting) in the air. Just increment the player where they want to fall.
        self.__looking = "Right"
        
        #KEYBINDINGS
        def spaceKey(event): #Special ability
            print("'spacebar' key pressed")

        def eKey(event): #Block
            print("'e' key pressed")
        
        def qKey(event): #Switch weapons
            print("'q' key pressed")
            
        def sKey(event): #Drop down
            print("'s' key pressed")
            print("Making inAir equal True")
            self.__inAir = True
            print("Disabling 's' binding") #Makes sure the user does not spam this animation DURING the animation.
            self.myCanvas.unbind("<s>", self.__b_s)

            if self.__Frame == 0 and self.__sprint == False and self.__crouch == False and self.__looking == "Left": #Moving left without sprint or crouch FRAME #1
                for count in range(90):
                    self.__y += 1
                    self.myCanvas.coords(a_head, 125+self.__x, 125+self.__y, 150+self.__x, 150+self.__y)
                    self.myCanvas.coords(a_name, 138+self.__x, 110+self.__y)
                    self.myCanvas.coords(a_torso, 130+self.__x, 150+self.__y, 145+self.__x, 150+self.__y, 145+self.__x, 175+self.__y, 130+self.__x, 175+self.__y)
                    self.myCanvas.coords(a_Larm, 115+self.__x, 150+self.__y, 130+self.__x, 165+self.__y)
                    self.myCanvas.coords(a_Rarm, 145+self.__x, 150+self.__y, 160+self.__x, 165+self.__y)
                    self.myCanvas.coords(a_Rleg, 145+self.__x, 175+self.__y, 160+self.__x, 183+self.__y)
                    self.myCanvas.coords(a_Lleg, 115+self.__x, 175+self.__y, 130+self.__x, 183+self.__y)
                    self.myCanvas.coords(a_bandana1, 125+self.__x+25, 140+self.__y, 150+self.__x-25, 140+self.__y, 150+self.__x-25, 150+self.__y)
                    self.myCanvas.coords(a_bandana2, 125+self.__x+25, 140+self.__y, 120+self.__x+35, 142+self.__y, 120+self.__x+35, 145+self.__y)
                    self.myCanvas.coords(a_bandana3, 125+self.__x+25, 140+self.__y, 120+self.__x+35, 138+self.__y, 120+self.__x+35, 141+self.__y)
                    self.myCanvas.coords(a_vneck, 130+self.__x, 155+self.__y, 145+self.__x, 150+self.__y, 145+self.__x, 175+self.__y, 130+self.__x, 175+self.__y)
                    self.myCanvas.coords(a_coat, 145+self.__x, 145+self.__y, 133+self.__x, 145+self.__y, 140+self.__x, 175+self.__y, 160+self.__x, 177+self.__y, 145+self.__x, 160+self.__y)
                    self.myCanvas.update()
                    self.__Frame = 1
                
            elif self.__Frame == 1 and self.__sprint == False and self.__crouch == False and self.__looking == "Left": #Moving left without sprint or crouch FRAME #2
                for count in range(90):
                    self.__y += 1
                    self.myCanvas.coords(a_head, 125+self.__x, 125+3+self.__y, 150+self.__x, 150+3+self.__y)
                    self.myCanvas.coords(a_name, 138+self.__x, 110+self.__y)
                    self.myCanvas.coords(a_torso, 130+self.__x, 150+3+self.__y, 145+self.__x, 150+3+self.__y, 145+self.__x, 175+3+self.__y, 130+self.__x, 175+3+self.__y)
                    self.myCanvas.coords(a_Larm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO
                    self.myCanvas.coords(a_Rarm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #Arm hides behind torso
                    self.myCanvas.coords(a_Rleg, 145+self.__x-10, 175+self.__y, 160+self.__x-10, 183+self.__y)
                    self.myCanvas.coords(a_Lleg, 115+self.__x+10, 175+self.__y, 130+self.__x+10, 183+self.__y)
                    self.myCanvas.coords(a_bandana1, 125+self.__x+25, 140+3+self.__y, 150+self.__x-25, 140+3+self.__y, 150+self.__x-25, 150+3+self.__y)
                    self.myCanvas.coords(a_bandana2, 125+self.__x+25, 140+3+self.__y, 120+self.__x+35, 142+3+self.__y, 120+self.__x+35, 145+3+self.__y)
                    self.myCanvas.coords(a_bandana3, 125+self.__x+25, 140+3+self.__y, 120+self.__x+35, 138+3+self.__y, 120+self.__x+35, 141+3+self.__y)
                    self.myCanvas.coords(a_vneck, 130+self.__x, 155+3+self.__y, 145+self.__x, 150+3+self.__y, 145+self.__x, 175+3+self.__y, 130+self.__x, 175+3+self.__y)
                    self.myCanvas.coords(a_coat, 145+self.__x, 145+3+self.__y, 133+self.__x, 145+3+self.__y, 140+self.__x, 175+3+self.__y, 160+self.__x, 177+6+self.__y, 145+self.__x, 160+3+self.__y)
                    self.myCanvas.update()
                    self.__Frame = 0

            elif self.__Frame == 0 and self.__sprint == True and self.__crouch == False and self.__looking == "Left": #Moving left SPRINTING FRAME #1
                for count in range(90):
                    self.__y += 1
                    self.myCanvas.coords(a_head, 145+self.__x-40, 135+self.__y, 170+self.__x-40, 160+self.__y) #(+20, +10) difference from walking
                    self.myCanvas.coords(a_name, 138+self.__x, 110+self.__y)
                    self.myCanvas.coords(a_torso, 140+self.__x-4, 150+self.__y, 150+self.__x-24, 160+self.__y, 125+self.__x+26, 170+self.__y, 115+self.__x+46, 160+self.__y) #(10, 0), (5,10), (-20,-5), (-15,-15)
                    self.myCanvas.coords(a_Larm, 85+self.__x+106, 150+self.__y, 100+self.__x+76, 165+self.__y) #(-30,0)
                    self.myCanvas.coords(a_Rarm, 175+self.__x-74, 150+self.__y, 190+self.__x-104, 165+self.__y) #(+30,0)
                    self.myCanvas.coords(a_Rleg, 150+self.__x-24, 170+self.__y, 165+self.__x-54, 178+self.__y) #(+5,-5), (+5,-5)
                    self.myCanvas.coords(a_Lleg, 110+self.__x+56, 170+self.__y, 125+self.__x+26, 178+self.__y) #(-5,-5), (-5,-5)
                    self.myCanvas.coords(a_bandana1, 145+self.__x-14, 150+self.__y, 170+self.__x-64, 150+self.__y, 170+self.__x-64, 160+self.__y) #(+20,10) for all bandana
                    self.myCanvas.coords(a_bandana2, 145+self.__x-14, 150+self.__y, 140+self.__x-4, 152+self.__y, 140+self.__x-4, 160+self.__y)
                    self.myCanvas.coords(a_bandana3, 145+self.__x-14, 150+self.__y, 140+self.__x-4, 148+self.__y, 140+self.__x-4, 151+self.__y) 
                    self.myCanvas.coords(a_vneck, 140+self.__x-4, 150+self.__y, 145+self.__x-14, 163+self.__y, 125+self.__x+26, 170+self.__y, 115+self.__x+46, 160+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                    self.myCanvas.coords(a_coat, 142+self.__x-8, 145+self.__y, 152+self.__x-28, 155+self.__y, 100+self.__x+76, 175+self.__y, 85+self.__x+104, 157+self.__y, 125+self.__x+26, 155+self.__y)
                    self.myCanvas.update()
                    self.__Frame = 1
                
            elif self.__Frame == 1 and self.__sprint == True and self.__crouch == False and self.__looking == "Left": #Moving left SPRINTING FRAME #2
                for count in range(90):
                    self.__y += 1
                    self.myCanvas.coords(a_head, 145+self.__x-40, 135+5+self.__y, 170+self.__x-40, 160+5+self.__y) #(+20, +10) difference from walking
                    self.myCanvas.coords(a_name, 138+self.__x, 110+self.__y)
                    self.myCanvas.coords(a_torso, 140+self.__x-4, 150+5+self.__y, 150+self.__x-24, 160+5+self.__y, 125+self.__x+26, 170+5+self.__y, 115+self.__x+46, 160+5+self.__y) #(20, 10), (5,10)
                    self.myCanvas.coords(a_Larm, 130+self.__x+16, 160+self.__y, 145+self.__x-14, 175+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                    self.myCanvas.coords(a_Rarm, 130+self.__x+16, 160+self.__y, 145+self.__x-14, 175+self.__y) #Arm hides behind torso (+30,0)
                    self.myCanvas.coords(a_Rleg, 145+self.__x-10, 175+self.__y, 160+self.__x-10, 183+self.__y)
                    self.myCanvas.coords(a_Lleg, 115+self.__x+10, 175+self.__y, 130+self.__x+10, 183+self.__y)
                    self.myCanvas.coords(a_bandana1, 145+self.__x-14, 150+5+self.__y, 170+self.__x-64, 150+5+self.__y, 170+self.__x-64, 160+5+self.__y) #(+20,10) for all bandana
                    self.myCanvas.coords(a_bandana2, 145+self.__x-14, 150+5+self.__y, 140+self.__x-4, 152+5+self.__y, 140+self.__x-4, 160+5+self.__y)
                    self.myCanvas.coords(a_bandana3, 145+self.__x-14, 150+5+self.__y, 140+self.__x-4, 148+5+self.__y, 140+self.__x-4, 151+5+self.__y) 
                    self.myCanvas.coords(a_vneck, 140+self.__x-4, 150+5+self.__y, 145+self.__x-14, 163+5+self.__y, 125+self.__x+26, 170+5+self.__y, 115+self.__x+46, 160+5+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                    self.myCanvas.coords(a_coat, 142+self.__x-8, 145+5+self.__y, 152+self.__x-28, 155+5+self.__y, 100+self.__x+76, 175+10+self.__y, 85+self.__x+104, 157+10+self.__y, 125+self.__x+26, 155+5+self.__y)
                    self.myCanvas.update()
                    self.__Frame = 0

            elif self.__Frame == 0 and self.__sprint == False and self.__crouch == True and self.__looking == "Left": #Moving left CROUCHING FRAME #1
                for count in range(90):
                    self.__y += 1
                    self.myCanvas.coords(a_head, 145+self.__x-40, 135+self.__y, 170+self.__x-40, 160+self.__y) #(+20, +10) difference from walking
                    self.myCanvas.coords(a_name, 138+self.__x, 110+self.__y)
                    self.myCanvas.coords(a_torso, 140+self.__x-4, 150+self.__y, 150+self.__x-24, 160+self.__y, 125+self.__x+26, 170+self.__y, 115+self.__x+46, 160+self.__y) #(10, 0), (5,10), (-20,-5), (-15,-15)
                    self.myCanvas.coords(a_Larm, 130+self.__x+16, 160+self.__y, 145+self.__x-14, 175+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                    self.myCanvas.coords(a_Rarm, 130+self.__x+16, 160+self.__y, 145+self.__x-14, 175+self.__y) #Arm hides behind torso (+30,0)
                    self.myCanvas.coords(a_Rleg, 145+self.__x-5, 175+self.__y, 160+self.__x-5, 183+self.__y) #(+5,-5), (+5,-5)
                    self.myCanvas.coords(a_Lleg, 115+self.__x+5, 175+self.__y, 130+self.__x+5, 183+self.__y) #(-5,-5), (-5,-5)
                    self.myCanvas.coords(a_bandana1, 145+self.__x-14, 150+self.__y, 170+self.__x-64, 150+self.__y, 170+self.__x-64, 160+self.__y) #(+20,10) for all bandana
                    self.myCanvas.coords(a_bandana2, 145+self.__x-14, 150+self.__y, 140+self.__x-4, 152+self.__y, 140+self.__x-4, 160+self.__y)
                    self.myCanvas.coords(a_bandana3, 145+self.__x-14, 150+self.__y, 140+self.__x-4, 148+self.__y, 140+self.__x-4, 151+self.__y) 
                    self.myCanvas.coords(a_vneck, 140+self.__x-4, 150+self.__y, 145+self.__x-14, 163+self.__y, 125+self.__x+26, 170+self.__y, 115+self.__x+46, 160+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                    self.myCanvas.coords(a_coat, 142+self.__x-8, 145+self.__y, 152+self.__x-28, 155+self.__y, 85+self.__x+76, 183+self.__y, 80+self.__x+104, 183+self.__y, 125+self.__x+26, 155+self.__y)
                    self.myCanvas.update()
                    self.__Frame = 1
                
            elif self.__Frame == 1 and self.__sprint == False and self.__crouch == True and self.__looking == "Left": #Moving left CROUCHING FRAME #2
                for count in range(90):
                    self.__y += 1
                    self.myCanvas.coords(a_head, 145+self.__x-40, 135+2+self.__y, 170+self.__x-40, 160+2+self.__y) #(+20, +10) difference from walking
                    self.myCanvas.coords(a_name, 138+self.__x, 110+self.__y)
                    self.myCanvas.coords(a_torso, 140+self.__x-4, 150+2+self.__y, 150+self.__x-24, 160+2+self.__y, 125+self.__x+26, 170+2+self.__y, 115+self.__x+46, 160+2+self.__y) #(20, 10), (5,10)
                    self.myCanvas.coords(a_Larm, 130+self.__x-10, 160+2+self.__y, 145+self.__x-10, 175+2+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                    self.myCanvas.coords(a_Rarm, 130+self.__x-10, 160+2+self.__y, 145+self.__x-10, 175+2+self.__y) #Arm hides behind torso (+30,0)
                    self.myCanvas.coords(a_Rleg, 145+self.__x-10, 175+self.__y, 160+self.__x-10, 183+self.__y)
                    self.myCanvas.coords(a_Lleg, 115+self.__x+10, 175+self.__y, 130+self.__x+10, 183+self.__y)
                    self.myCanvas.coords(a_bandana1, 145+self.__x-14, 150+2+self.__y, 170+self.__x-64, 150+2+self.__y, 170+self.__x-64, 160+2+self.__y) #(+20,10) for all bandana
                    self.myCanvas.coords(a_bandana2, 145+self.__x-14, 150+2+self.__y, 140+self.__x-4, 152+2+self.__y, 140+self.__x-4, 160+2+self.__y)
                    self.myCanvas.coords(a_bandana3, 145+self.__x-14, 150+2+self.__y, 140+self.__x-4, 148+2+self.__y, 140+self.__x-4, 151+2+self.__y) 
                    self.myCanvas.coords(a_vneck, 140+self.__x-4, 150+2+self.__y, 145+self.__x-14, 163+2+self.__y, 125+self.__x+26, 170+2+self.__y, 115+self.__x+46, 160+2+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                    self.myCanvas.coords(a_coat, 142+self.__x-8, 145+2+self.__y, 152+self.__x-28, 155+2+self.__y, 85+self.__x+76, 183+2+self.__y, 80+self.__x+104, 183+2+self.__y, 125+self.__x+26, 155+2+self.__y)
                    self.myCanvas.update()
                    self.__Frame = 0
            #Moving Right
                    
            elif self.__Frame == 0 and self.__sprint == False and self.__crouch == False: #Moving right without sprinting or crouching FRAME #1
                for count in range(90):
                    self.__y += 1 #Arms and legs out self.__x 
                    self.myCanvas.coords(a_head, 125+self.__x, 125+self.__y, 150+self.__x, 150+self.__y)
                    self.myCanvas.coords(a_name, 138+self.__x, 110+self.__y)
                    self.myCanvas.coords(a_torso, 130+self.__x, 150+self.__y, 145+self.__x, 150+self.__y, 145+self.__x, 175+self.__y, 130+self.__x, 175+self.__y)
                    self.myCanvas.coords(a_Larm, 115+self.__x, 150+self.__y, 130+self.__x, 165+self.__y)
                    self.myCanvas.coords(a_Rarm, 145+self.__x, 150+self.__y, 160+self.__x, 165+self.__y)
                    self.myCanvas.coords(a_Rleg, 145+self.__x, 175+self.__y, 160+self.__x, 183+self.__y)
                    self.myCanvas.coords(a_Lleg, 115+self.__x, 175+self.__y, 130+self.__x, 183+self.__y)
                    self.myCanvas.coords(a_bandana1, 125+self.__x, 140+self.__y, 150+self.__x, 140+self.__y, 150+self.__x, 150+self.__y)
                    self.myCanvas.coords(a_bandana2, 125+self.__x, 140+self.__y, 120+self.__x, 142+self.__y, 120+self.__x, 145+self.__y)
                    self.myCanvas.coords(a_bandana3, 125+self.__x, 140+self.__y, 120+self.__x, 138+self.__y, 120+self.__x, 141+self.__y)
                    self.myCanvas.coords(a_vneck, 130+self.__x, 150+self.__y, 145+self.__x, 155+self.__y, 145+self.__x, 175+self.__y, 130+self.__x, 175+self.__y)
                    self.myCanvas.coords(a_coat, 130+self.__x, 145+self.__y, 142+self.__x, 145+self.__y, 135+self.__x, 175+self.__y, 115+self.__x, 177+self.__y, 130+self.__x, 160+self.__y)
                    self.myCanvas.update()
                    self.__Frame = 1
                
            elif self.__Frame == 1 and self.__sprint == False and self.__crouch == False: #Moving right without sprinting or crouching FRAME #2
                for count in range(90):
                    self.__y += 1
                    self.myCanvas.coords(a_head, 125+self.__x, 125+3+self.__y, 150+self.__x, 150+3+self.__y)
                    self.myCanvas.coords(a_name, 138+self.__x, 110+self.__y)
                    self.myCanvas.coords(a_torso, 130+self.__x, 150+3+self.__y, 145+self.__x, 150+3+self.__y, 145+self.__x, 175+3+self.__y, 130+self.__x, 175+3+self.__y)
                    self.myCanvas.coords(a_Larm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO
                    self.myCanvas.coords(a_Rarm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #Arm hides behind torso
                    self.myCanvas.coords(a_Rleg, 145+self.__x-10, 175+self.__y, 160+self.__x-10, 183+self.__y)
                    self.myCanvas.coords(a_Lleg, 115+self.__x+10, 175+self.__y, 130+self.__x+10, 183+self.__y)
                    self.myCanvas.coords(a_bandana1, 125+self.__x, 140+3+self.__y, 150+self.__x, 140+3+self.__y, 150+self.__x, 150+3+self.__y)
                    self.myCanvas.coords(a_bandana2, 125+self.__x, 140+3+self.__y, 120+self.__x, 142+3+self.__y, 120+self.__x, 145+3+self.__y)
                    self.myCanvas.coords(a_bandana3, 125+self.__x, 140+3+self.__y, 120+self.__x, 138+3+self.__y, 120+self.__x, 141+3+self.__y)
                    self.myCanvas.coords(a_vneck, 130+self.__x, 150+3+self.__y, 145+self.__x, 155+3+self.__y, 145+self.__x, 175+3+self.__y, 130+self.__x, 175+3+self.__y)
                    self.myCanvas.coords(a_coat, 130+self.__x, 145+3+self.__y, 142+self.__x, 145+3+self.__y, 135+self.__x, 175+3+self.__y, 115+self.__x, 177+6+self.__y, 130+self.__x, 160+self.__y)
                    self.myCanvas.update()
                    self.__Frame = 0

            elif self.__Frame == 0 and self.__sprint == True and self.__crouch == False: #Moving right SPRINTING FRAME #1
                for count in range(90):
                    self.__y += 1
                    self.myCanvas.coords(a_head, 145+self.__x, 135+self.__y, 170+self.__x, 160+self.__y) #(+20, +10) difference from walking
                    self.myCanvas.coords(a_name, 138+self.__x, 110+self.__y)
                    self.myCanvas.coords(a_torso, 140+self.__x, 150+self.__y, 150+self.__x, 160+self.__y, 125+self.__x, 170+self.__y, 115+self.__x, 160+self.__y) #(10, 0), (5,10), (-20,-5), (-15,-15)
                    self.myCanvas.coords(a_Larm, 85+self.__x, 150+self.__y, 100+self.__x, 165+self.__y) #(-30,0)
                    self.myCanvas.coords(a_Rarm, 175+self.__x, 150+self.__y, 190+self.__x, 165+self.__y) #(+30,0)
                    self.myCanvas.coords(a_Rleg, 150+self.__x, 170+self.__y, 165+self.__x, 178+self.__y) #(+5,-5), (+5,-5)
                    self.myCanvas.coords(a_Lleg, 110+self.__x, 170+self.__y, 125+self.__x, 178+self.__y) #(-5,-5), (-5,-5)
                    self.myCanvas.coords(a_bandana1, 145+self.__x, 150+self.__y, 170+self.__x, 150+self.__y, 170+self.__x, 160+self.__y) #(+20,10) for all bandana
                    self.myCanvas.coords(a_bandana2, 145+self.__x, 150+self.__y, 140+self.__x, 152+self.__y, 140+self.__x, 160+self.__y)
                    self.myCanvas.coords(a_bandana3, 145+self.__x, 150+self.__y, 140+self.__x, 148+self.__y, 140+self.__x, 151+self.__y) 
                    self.myCanvas.coords(a_vneck, 140+self.__x, 150+self.__y, 145+self.__x, 163+self.__y, 125+self.__x, 170+self.__y, 115+self.__x, 160+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                    self.myCanvas.coords(a_coat, 142+self.__x, 145+self.__y, 152+self.__x, 155+self.__y, 100+self.__x, 175+self.__y, 85+self.__x, 157+self.__y, 125+self.__x, 155+self.__y)
                    self.myCanvas.update()
                    self.__Frame = 1
                
            elif self.__Frame == 1 and self.__sprint == True and self.__crouch == False: #Moving right SPRINTING FRAME #2
                for count in range(90):
                    self.__y += 1
                    self.myCanvas.coords(a_head, 145+self.__x, 135+5+self.__y, 170+self.__x, 160+5+self.__y) #(+20, +10) difference from walking
                    self.myCanvas.coords(a_name, 138+self.__x, 110+self.__y)
                    self.myCanvas.coords(a_torso, 140+self.__x, 150+5+self.__y, 150+self.__x, 160+5+self.__y, 125+self.__x, 170+5+self.__y, 115+self.__x, 160+5+self.__y) #(20, 10), (5,10)
                    self.myCanvas.coords(a_Larm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                    self.myCanvas.coords(a_Rarm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #Arm hides behind torso (+30,0)
                    self.myCanvas.coords(a_Rleg, 145+self.__x-10, 175+self.__y, 160+self.__x-10, 183+self.__y)
                    self.myCanvas.coords(a_Lleg, 115+self.__x+10, 175+self.__y, 130+self.__x+10, 183+self.__y)
                    self.myCanvas.coords(a_bandana1, 145+self.__x, 150+5+self.__y, 170+self.__x, 150+5+self.__y, 170+self.__x, 160+5+self.__y) #(+20,10) for all bandana
                    self.myCanvas.coords(a_bandana2, 145+self.__x, 150+5+self.__y, 140+self.__x, 152+5+self.__y, 140+self.__x, 155+5+self.__y)
                    self.myCanvas.coords(a_bandana3, 145+self.__x, 150+5+self.__y, 140+self.__x, 148+5+self.__y, 140+self.__x, 151+5+self.__y)
                    self.myCanvas.coords(a_vneck, 140+self.__x, 150+5+self.__y, 145+self.__x, 163+5+self.__y, 125+self.__x, 170+5+self.__y, 115+self.__x, 160+5+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                    self.myCanvas.coords(a_coat, 142+self.__x, 145+5+self.__y, 152+self.__x, 155+5+self.__y, 100+self.__x, 175+10+self.__y, 85+self.__x, 157+10+self.__y, 125+self.__x, 155+5+self.__y)
                    self.myCanvas.update()
                    self.__Frame = 0

            elif self.__Frame == 0 and self.__sprint == False and self.__crouch == True: #Moving right CROUCHING FRAMe #1
                for count in range(90):
                    self.__y += 1
                    self.myCanvas.coords(a_head, 145+self.__x, 135+self.__y, 170+self.__x, 160+self.__y) #(+20, +10) difference from walking
                    self.myCanvas.coords(a_name, 138+self.__x, 110+self.__y)
                    self.myCanvas.coords(a_torso, 140+self.__x, 150+self.__y, 150+self.__x, 160+self.__y, 125+self.__x, 170+self.__y, 115+self.__x, 160+self.__y) #(10, 0), (5,10), (-20,-5), (-15,-15)
                    self.myCanvas.coords(a_Larm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                    self.myCanvas.coords(a_Rarm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #Arm hides behind torso (+30,0)
                    self.myCanvas.coords(a_Rleg, 145+self.__x-5, 175+self.__y, 160+self.__x-5, 183+self.__y) #(+5,-5), (+5,-5)
                    self.myCanvas.coords(a_Lleg, 115+self.__x+5, 175+self.__y, 130+self.__x+5, 183+self.__y) #(-5,-5), (-5,-5)
                    self.myCanvas.coords(a_bandana1, 145+self.__x, 150+self.__y, 170+self.__x, 150+self.__y, 170+self.__x, 160+self.__y) #(+20,10) for all bandana
                    self.myCanvas.coords(a_bandana2, 145+self.__x, 150+self.__y, 140+self.__x, 152+self.__y, 140+self.__x, 160+self.__y)
                    self.myCanvas.coords(a_bandana3, 145+self.__x, 150+self.__y, 140+self.__x, 148+self.__y, 140+self.__x, 151+self.__y) 
                    self.myCanvas.coords(a_vneck, 140+self.__x, 150+self.__y, 145+self.__x, 163+self.__y, 125+self.__x, 170+self.__y, 115+self.__x, 160+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                    self.myCanvas.coords(a_coat, 142+self.__x, 145+self.__y, 152+self.__x, 155+self.__y, 115+self.__x, 183+self.__y, 92+self.__x, 183+self.__y, 125+self.__x, 155+self.__y)
                    self.myCanvas.update()
                    self.__Frame = 1
                
            elif self.__Frame == 1 and self.__sprint == False and self.__crouch == True: #Moving right CROUCHING FRAMe #2
                for count in range(90):
                    self.__y += 1
                    self.myCanvas.coords(a_head, 145+self.__x, 135+2+self.__y, 170+self.__x, 160+2+self.__y) #(+20, +10) difference from walking
                    self.myCanvas.coords(a_name, 138+self.__x, 110+self.__y)
                    self.myCanvas.coords(a_torso, 140+self.__x, 150+2+self.__y, 150+self.__x, 160+2+self.__y, 125+self.__x, 170+2+self.__y, 115+self.__x, 160+2+self.__y) #(20, 10), (5,10)
                    self.myCanvas.coords(a_Larm, 130+self.__x+10, 160+2+self.__y, 145+self.__x+10, 175+2+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                    self.myCanvas.coords(a_Rarm, 130+self.__x+10, 160+2+self.__y, 145+self.__x+10, 175+2+self.__y) #Arm hides behind torso (+30,0)
                    self.myCanvas.coords(a_Rleg, 145+self.__x-10, 175+self.__y, 160+self.__x-10, 183+self.__y)
                    self.myCanvas.coords(a_Lleg, 115+self.__x+10, 175+self.__y, 130+self.__x+10, 183+self.__y)
                    self.myCanvas.coords(a_bandana1, 145+self.__x, 150+2+self.__y, 170+self.__x, 150+2+self.__y, 170+self.__x, 160+2+self.__y) #(+20,10) for all bandana
                    self.myCanvas.coords(a_bandana2, 145+self.__x, 150+2+self.__y, 140+self.__x, 152+2+self.__y, 140+self.__x, 155+2+self.__y)
                    self.myCanvas.coords(a_bandana3, 145+self.__x, 150+2+self.__y, 140+self.__x, 148+2+self.__y, 140+self.__x, 151+2+self.__y)
                    self.myCanvas.coords(a_vneck, 140+self.__x, 150+2+self.__y, 145+self.__x, 163+2+self.__y, 125+self.__x, 170+2+self.__y, 115+self.__x, 160+2+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                    self.myCanvas.coords(a_coat, 142+self.__x, 145+2+self.__y, 152+self.__x, 155+2+self.__y, 115+self.__x, 183+2+self.__y, 92+self.__x, 183+2+self.__y, 125+self.__x, 155+2+self.__y)
                    self.myCanvas.update()
                    self.__Frame = 0
            
            self.myCanvas.after(100, rebindS) #2000 ms = 2 seconds Later will need to redo this part because not all falling is going to be 2 seconds long.
            
        def rebindS(): #Rebinds S (falling should be done and can fall again)
            self.__b_s = self.myCanvas.bind("<s>", sKey)
            print("Rebinding 's' and making inAir=False")
            self.__inAir=False
        
        def wKey(event): #Jump
            print("'w' key pressed")
            print("Making inAir equal True")
            self.__inAir = True
            print("Disabling 'w' binding") #Makes sure the user does not spam this animation DURING the animation.
            self.myCanvas.unbind("<w>", self.__b_w)
            
            if self.__Frame == 0 and self.__sprint == False and self.__crouch == False and self.__looking == "Left": #Moving left without sprint or crouch FRAME #1
                for count in range(90):
                    self.__y -= 1
                    self.myCanvas.coords(a_head, 125+self.__x, 125+self.__y, 150+self.__x, 150+self.__y)
                    self.myCanvas.coords(a_name, 138+self.__x, 110+self.__y)
                    self.myCanvas.coords(a_torso, 130+self.__x, 150+self.__y, 145+self.__x, 150+self.__y, 145+self.__x, 175+self.__y, 130+self.__x, 175+self.__y)
                    self.myCanvas.coords(a_Larm, 115+self.__x, 150+self.__y, 130+self.__x, 165+self.__y)
                    self.myCanvas.coords(a_Rarm, 145+self.__x, 150+self.__y, 160+self.__x, 165+self.__y)
                    self.myCanvas.coords(a_Rleg, 145+self.__x, 175+self.__y, 160+self.__x, 183+self.__y)
                    self.myCanvas.coords(a_Lleg, 115+self.__x, 175+self.__y, 130+self.__x, 183+self.__y)
                    self.myCanvas.coords(a_bandana1, 125+self.__x+25, 140+self.__y, 150+self.__x-25, 140+self.__y, 150+self.__x-25, 150+self.__y)
                    self.myCanvas.coords(a_bandana2, 125+self.__x+25, 140+self.__y, 120+self.__x+35, 142+self.__y, 120+self.__x+35, 145+self.__y)
                    self.myCanvas.coords(a_bandana3, 125+self.__x+25, 140+self.__y, 120+self.__x+35, 138+self.__y, 120+self.__x+35, 141+self.__y)
                    self.myCanvas.coords(a_vneck, 130+self.__x, 155+self.__y, 145+self.__x, 150+self.__y, 145+self.__x, 175+self.__y, 130+self.__x, 175+self.__y)
                    self.myCanvas.coords(a_coat, 145+self.__x, 145+self.__y, 133+self.__x, 145+self.__y, 140+self.__x, 175+self.__y, 160+self.__x, 177+self.__y, 145+self.__x, 160+self.__y)
                    self.myCanvas.update()
                    self.__Frame = 1
                
            elif self.__Frame == 1 and self.__sprint == False and self.__crouch == False and self.__looking == "Left": #Moving left without sprint or crouch FRAME #2
                for count in range(90):
                    self.__y -= 1
                    self.myCanvas.coords(a_head, 125+self.__x, 125+3+self.__y, 150+self.__x, 150+3+self.__y)
                    self.myCanvas.coords(a_name, 138+self.__x, 110+self.__y)
                    self.myCanvas.coords(a_torso, 130+self.__x, 150+3+self.__y, 145+self.__x, 150+3+self.__y, 145+self.__x, 175+3+self.__y, 130+self.__x, 175+3+self.__y)
                    self.myCanvas.coords(a_Larm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO
                    self.myCanvas.coords(a_Rarm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #Arm hides behind torso
                    self.myCanvas.coords(a_Rleg, 145+self.__x-10, 175+self.__y, 160+self.__x-10, 183+self.__y)
                    self.myCanvas.coords(a_Lleg, 115+self.__x+10, 175+self.__y, 130+self.__x+10, 183+self.__y)
                    self.myCanvas.coords(a_bandana1, 125+self.__x+25, 140+3+self.__y, 150+self.__x-25, 140+3+self.__y, 150+self.__x-25, 150+3+self.__y)
                    self.myCanvas.coords(a_bandana2, 125+self.__x+25, 140+3+self.__y, 120+self.__x+35, 142+3+self.__y, 120+self.__x+35, 145+3+self.__y)
                    self.myCanvas.coords(a_bandana3, 125+self.__x+25, 140+3+self.__y, 120+self.__x+35, 138+3+self.__y, 120+self.__x+35, 141+3+self.__y)
                    self.myCanvas.coords(a_vneck, 130+self.__x, 155+3+self.__y, 145+self.__x, 150+3+self.__y, 145+self.__x, 175+3+self.__y, 130+self.__x, 175+3+self.__y)
                    self.myCanvas.coords(a_coat, 145+self.__x, 145+3+self.__y, 133+self.__x, 145+3+self.__y, 140+self.__x, 175+3+self.__y, 160+self.__x, 177+6+self.__y, 145+self.__x, 160+3+self.__y)
                    self.myCanvas.update()
                    self.__Frame = 0

            elif self.__Frame == 0 and self.__sprint == True and self.__crouch == False and self.__looking == "Left": #Moving left SPRINTING FRAME #1
                for count in range(90):
                    self.__y -= 1
                    self.myCanvas.coords(a_head, 145+self.__x-40, 135+self.__y, 170+self.__x-40, 160+self.__y) #(+20, +10) difference from walking
                    self.myCanvas.coords(a_name, 138+self.__x, 110+self.__y)
                    self.myCanvas.coords(a_torso, 140+self.__x-4, 150+self.__y, 150+self.__x-24, 160+self.__y, 125+self.__x+26, 170+self.__y, 115+self.__x+46, 160+self.__y) #(10, 0), (5,10), (-20,-5), (-15,-15)
                    self.myCanvas.coords(a_Larm, 85+self.__x+106, 150+self.__y, 100+self.__x+76, 165+self.__y) #(-30,0)
                    self.myCanvas.coords(a_Rarm, 175+self.__x-74, 150+self.__y, 190+self.__x-104, 165+self.__y) #(+30,0)
                    self.myCanvas.coords(a_Rleg, 150+self.__x-24, 170+self.__y, 165+self.__x-54, 178+self.__y) #(+5,-5), (+5,-5)
                    self.myCanvas.coords(a_Lleg, 110+self.__x+56, 170+self.__y, 125+self.__x+26, 178+self.__y) #(-5,-5), (-5,-5)
                    self.myCanvas.coords(a_bandana1, 145+self.__x-14, 150+self.__y, 170+self.__x-64, 150+self.__y, 170+self.__x-64, 160+self.__y) #(+20,10) for all bandana
                    self.myCanvas.coords(a_bandana2, 145+self.__x-14, 150+self.__y, 140+self.__x-4, 152+self.__y, 140+self.__x-4, 160+self.__y)
                    self.myCanvas.coords(a_bandana3, 145+self.__x-14, 150+self.__y, 140+self.__x-4, 148+self.__y, 140+self.__x-4, 151+self.__y) 
                    self.myCanvas.coords(a_vneck, 140+self.__x-4, 150+self.__y, 145+self.__x-14, 163+self.__y, 125+self.__x+26, 170+self.__y, 115+self.__x+46, 160+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                    self.myCanvas.coords(a_coat, 142+self.__x-8, 145+self.__y, 152+self.__x-28, 155+self.__y, 100+self.__x+76, 175+self.__y, 85+self.__x+104, 157+self.__y, 125+self.__x+26, 155+self.__y)
                    self.myCanvas.update()
                    self.__Frame = 1
                
            elif self.__Frame == 1 and self.__sprint == True and self.__crouch == False and self.__looking == "Left": #Moving left SPRINTING FRAME #2
                for count in range(90):
                    self.__y -= 1
                    self.myCanvas.coords(a_head, 145+self.__x-40, 135+5+self.__y, 170+self.__x-40, 160+5+self.__y) #(+20, +10) difference from walking
                    self.myCanvas.coords(a_name, 138+self.__x, 110+self.__y)
                    self.myCanvas.coords(a_torso, 140+self.__x-4, 150+5+self.__y, 150+self.__x-24, 160+5+self.__y, 125+self.__x+26, 170+5+self.__y, 115+self.__x+46, 160+5+self.__y) #(20, 10), (5,10)
                    self.myCanvas.coords(a_Larm, 130+self.__x+16, 160+self.__y, 145+self.__x-14, 175+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                    self.myCanvas.coords(a_Rarm, 130+self.__x+16, 160+self.__y, 145+self.__x-14, 175+self.__y) #Arm hides behind torso (+30,0)
                    self.myCanvas.coords(a_Rleg, 145+self.__x-10, 175+self.__y, 160+self.__x-10, 183+self.__y)
                    self.myCanvas.coords(a_Lleg, 115+self.__x+10, 175+self.__y, 130+self.__x+10, 183+self.__y)
                    self.myCanvas.coords(a_bandana1, 145+self.__x-14, 150+5+self.__y, 170+self.__x-64, 150+5+self.__y, 170+self.__x-64, 160+5+self.__y) #(+20,10) for all bandana
                    self.myCanvas.coords(a_bandana2, 145+self.__x-14, 150+5+self.__y, 140+self.__x-4, 152+5+self.__y, 140+self.__x-4, 160+5+self.__y)
                    self.myCanvas.coords(a_bandana3, 145+self.__x-14, 150+5+self.__y, 140+self.__x-4, 148+5+self.__y, 140+self.__x-4, 151+5+self.__y) 
                    self.myCanvas.coords(a_vneck, 140+self.__x-4, 150+5+self.__y, 145+self.__x-14, 163+5+self.__y, 125+self.__x+26, 170+5+self.__y, 115+self.__x+46, 160+5+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                    self.myCanvas.coords(a_coat, 142+self.__x-8, 145+5+self.__y, 152+self.__x-28, 155+5+self.__y, 100+self.__x+76, 175+10+self.__y, 85+self.__x+104, 157+10+self.__y, 125+self.__x+26, 155+5+self.__y)
                    self.myCanvas.update()
                    self.__Frame = 0

            elif self.__Frame == 0 and self.__sprint == False and self.__crouch == True and self.__looking == "Left": #Moving left CROUCHING FRAME #1
                for count in range(90):
                    self.__y -= 1
                    self.myCanvas.coords(a_head, 145+self.__x-40, 135+self.__y, 170+self.__x-40, 160+self.__y) #(+20, +10) difference from walking
                    self.myCanvas.coords(a_name, 138+self.__x, 110+self.__y)
                    self.myCanvas.coords(a_torso, 140+self.__x-4, 150+self.__y, 150+self.__x-24, 160+self.__y, 125+self.__x+26, 170+self.__y, 115+self.__x+46, 160+self.__y) #(10, 0), (5,10), (-20,-5), (-15,-15)
                    self.myCanvas.coords(a_Larm, 130+self.__x+16, 160+self.__y, 145+self.__x-14, 175+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                    self.myCanvas.coords(a_Rarm, 130+self.__x+16, 160+self.__y, 145+self.__x-14, 175+self.__y) #Arm hides behind torso (+30,0)
                    self.myCanvas.coords(a_Rleg, 145+self.__x-5, 175+self.__y, 160+self.__x-5, 183+self.__y) #(+5,-5), (+5,-5)
                    self.myCanvas.coords(a_Lleg, 115+self.__x+5, 175+self.__y, 130+self.__x+5, 183+self.__y) #(-5,-5), (-5,-5)
                    self.myCanvas.coords(a_bandana1, 145+self.__x-14, 150+self.__y, 170+self.__x-64, 150+self.__y, 170+self.__x-64, 160+self.__y) #(+20,10) for all bandana
                    self.myCanvas.coords(a_bandana2, 145+self.__x-14, 150+self.__y, 140+self.__x-4, 152+self.__y, 140+self.__x-4, 160+self.__y)
                    self.myCanvas.coords(a_bandana3, 145+self.__x-14, 150+self.__y, 140+self.__x-4, 148+self.__y, 140+self.__x-4, 151+self.__y) 
                    self.myCanvas.coords(a_vneck, 140+self.__x-4, 150+self.__y, 145+self.__x-14, 163+self.__y, 125+self.__x+26, 170+self.__y, 115+self.__x+46, 160+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                    self.myCanvas.coords(a_coat, 142+self.__x-8, 145+self.__y, 152+self.__x-28, 155+self.__y, 85+self.__x+76, 183+self.__y, 80+self.__x+104, 183+self.__y, 125+self.__x+26, 155+self.__y)
                    self.myCanvas.update()
                    self.__Frame = 1
                
            elif self.__Frame == 1 and self.__sprint == False and self.__crouch == True and self.__looking == "Left": #Moving left CROUCHING FRAME #2
                for count in range(90):
                    self.__y -= 1
                    self.myCanvas.coords(a_head, 145+self.__x-40, 135+2+self.__y, 170+self.__x-40, 160+2+self.__y) #(+20, +10) difference from walking
                    self.myCanvas.coords(a_name, 138+self.__x, 110+self.__y)
                    self.myCanvas.coords(a_torso, 140+self.__x-4, 150+2+self.__y, 150+self.__x-24, 160+2+self.__y, 125+self.__x+26, 170+2+self.__y, 115+self.__x+46, 160+2+self.__y) #(20, 10), (5,10)
                    self.myCanvas.coords(a_Larm, 130+self.__x-10, 160+2+self.__y, 145+self.__x-10, 175+2+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                    self.myCanvas.coords(a_Rarm, 130+self.__x-10, 160+2+self.__y, 145+self.__x-10, 175+2+self.__y) #Arm hides behind torso (+30,0)
                    self.myCanvas.coords(a_Rleg, 145+self.__x-10, 175+self.__y, 160+self.__x-10, 183+self.__y)
                    self.myCanvas.coords(a_Lleg, 115+self.__x+10, 175+self.__y, 130+self.__x+10, 183+self.__y)
                    self.myCanvas.coords(a_bandana1, 145+self.__x-14, 150+2+self.__y, 170+self.__x-64, 150+2+self.__y, 170+self.__x-64, 160+2+self.__y) #(+20,10) for all bandana
                    self.myCanvas.coords(a_bandana2, 145+self.__x-14, 150+2+self.__y, 140+self.__x-4, 152+2+self.__y, 140+self.__x-4, 160+2+self.__y)
                    self.myCanvas.coords(a_bandana3, 145+self.__x-14, 150+2+self.__y, 140+self.__x-4, 148+2+self.__y, 140+self.__x-4, 151+2+self.__y) 
                    self.myCanvas.coords(a_vneck, 140+self.__x-4, 150+2+self.__y, 145+self.__x-14, 163+2+self.__y, 125+self.__x+26, 170+2+self.__y, 115+self.__x+46, 160+2+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                    self.myCanvas.coords(a_coat, 142+self.__x-8, 145+2+self.__y, 152+self.__x-28, 155+2+self.__y, 85+self.__x+76, 183+2+self.__y, 80+self.__x+104, 183+2+self.__y, 125+self.__x+26, 155+2+self.__y)
                    self.myCanvas.update()
                    self.__Frame = 0
            #Moving Right
                    
            elif self.__Frame == 0 and self.__sprint == False and self.__crouch == False: #Moving right without sprinting or crouching FRAME #1
                for count in range(90):
                    self.__y -= 1 #Arms and legs out self.__x 
                    self.myCanvas.coords(a_head, 125+self.__x, 125+self.__y, 150+self.__x, 150+self.__y)
                    self.myCanvas.coords(a_name, 138+self.__x, 110+self.__y)
                    self.myCanvas.coords(a_torso, 130+self.__x, 150+self.__y, 145+self.__x, 150+self.__y, 145+self.__x, 175+self.__y, 130+self.__x, 175+self.__y)
                    self.myCanvas.coords(a_Larm, 115+self.__x, 150+self.__y, 130+self.__x, 165+self.__y)
                    self.myCanvas.coords(a_Rarm, 145+self.__x, 150+self.__y, 160+self.__x, 165+self.__y)
                    self.myCanvas.coords(a_Rleg, 145+self.__x, 175+self.__y, 160+self.__x, 183+self.__y)
                    self.myCanvas.coords(a_Lleg, 115+self.__x, 175+self.__y, 130+self.__x, 183+self.__y)
                    self.myCanvas.coords(a_bandana1, 125+self.__x, 140+self.__y, 150+self.__x, 140+self.__y, 150+self.__x, 150+self.__y)
                    self.myCanvas.coords(a_bandana2, 125+self.__x, 140+self.__y, 120+self.__x, 142+self.__y, 120+self.__x, 145+self.__y)
                    self.myCanvas.coords(a_bandana3, 125+self.__x, 140+self.__y, 120+self.__x, 138+self.__y, 120+self.__x, 141+self.__y)
                    self.myCanvas.coords(a_vneck, 130+self.__x, 150+self.__y, 145+self.__x, 155+self.__y, 145+self.__x, 175+self.__y, 130+self.__x, 175+self.__y)
                    self.myCanvas.coords(a_coat, 130+self.__x, 145+self.__y, 142+self.__x, 145+self.__y, 135+self.__x, 175+self.__y, 115+self.__x, 177+self.__y, 130+self.__x, 160+self.__y)
                    self.myCanvas.update()
                    self.__Frame = 1
                
            elif self.__Frame == 1 and self.__sprint == False and self.__crouch == False: #Moving right without sprinting or crouching FRAME #2
                for count in range(90):
                    self.__y -= 1
                    self.myCanvas.coords(a_head, 125+self.__x, 125+3+self.__y, 150+self.__x, 150+3+self.__y)
                    self.myCanvas.coords(a_name, 138+self.__x, 110+self.__y)
                    self.myCanvas.coords(a_torso, 130+self.__x, 150+3+self.__y, 145+self.__x, 150+3+self.__y, 145+self.__x, 175+3+self.__y, 130+self.__x, 175+3+self.__y)
                    self.myCanvas.coords(a_Larm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO
                    self.myCanvas.coords(a_Rarm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #Arm hides behind torso
                    self.myCanvas.coords(a_Rleg, 145+self.__x-10, 175+self.__y, 160+self.__x-10, 183+self.__y)
                    self.myCanvas.coords(a_Lleg, 115+self.__x+10, 175+self.__y, 130+self.__x+10, 183+self.__y)
                    self.myCanvas.coords(a_bandana1, 125+self.__x, 140+3+self.__y, 150+self.__x, 140+3+self.__y, 150+self.__x, 150+3+self.__y)
                    self.myCanvas.coords(a_bandana2, 125+self.__x, 140+3+self.__y, 120+self.__x, 142+3+self.__y, 120+self.__x, 145+3+self.__y)
                    self.myCanvas.coords(a_bandana3, 125+self.__x, 140+3+self.__y, 120+self.__x, 138+3+self.__y, 120+self.__x, 141+3+self.__y)
                    self.myCanvas.coords(a_vneck, 130+self.__x, 150+3+self.__y, 145+self.__x, 155+3+self.__y, 145+self.__x, 175+3+self.__y, 130+self.__x, 175+3+self.__y)
                    self.myCanvas.coords(a_coat, 130+self.__x, 145+3+self.__y, 142+self.__x, 145+3+self.__y, 135+self.__x, 175+3+self.__y, 115+self.__x, 177+6+self.__y, 130+self.__x, 160+self.__y)
                    self.myCanvas.update()
                    self.__Frame = 0

            elif self.__Frame == 0 and self.__sprint == True and self.__crouch == False: #Moving right SPRINTING FRAME #1
                for count in range(90):
                    self.__y -= 1
                    self.myCanvas.coords(a_head, 145+self.__x, 135+self.__y, 170+self.__x, 160+self.__y) #(+20, +10) difference from walking
                    self.myCanvas.coords(a_name, 138+self.__x, 110+self.__y)
                    self.myCanvas.coords(a_torso, 140+self.__x, 150+self.__y, 150+self.__x, 160+self.__y, 125+self.__x, 170+self.__y, 115+self.__x, 160+self.__y) #(10, 0), (5,10), (-20,-5), (-15,-15)
                    self.myCanvas.coords(a_Larm, 85+self.__x, 150+self.__y, 100+self.__x, 165+self.__y) #(-30,0)
                    self.myCanvas.coords(a_Rarm, 175+self.__x, 150+self.__y, 190+self.__x, 165+self.__y) #(+30,0)
                    self.myCanvas.coords(a_Rleg, 150+self.__x, 170+self.__y, 165+self.__x, 178+self.__y) #(+5,-5), (+5,-5)
                    self.myCanvas.coords(a_Lleg, 110+self.__x, 170+self.__y, 125+self.__x, 178+self.__y) #(-5,-5), (-5,-5)
                    self.myCanvas.coords(a_bandana1, 145+self.__x, 150+self.__y, 170+self.__x, 150+self.__y, 170+self.__x, 160+self.__y) #(+20,10) for all bandana
                    self.myCanvas.coords(a_bandana2, 145+self.__x, 150+self.__y, 140+self.__x, 152+self.__y, 140+self.__x, 160+self.__y)
                    self.myCanvas.coords(a_bandana3, 145+self.__x, 150+self.__y, 140+self.__x, 148+self.__y, 140+self.__x, 151+self.__y) 
                    self.myCanvas.coords(a_vneck, 140+self.__x, 150+self.__y, 145+self.__x, 163+self.__y, 125+self.__x, 170+self.__y, 115+self.__x, 160+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                    self.myCanvas.coords(a_coat, 142+self.__x, 145+self.__y, 152+self.__x, 155+self.__y, 100+self.__x, 175+self.__y, 85+self.__x, 157+self.__y, 125+self.__x, 155+self.__y)
                    self.myCanvas.update()
                    self.__Frame = 1
                
            elif self.__Frame == 1 and self.__sprint == True and self.__crouch == False: #Moving right SPRINTING FRAME #2
                for count in range(90):
                    self.__y -= 1
                    self.myCanvas.coords(a_head, 145+self.__x, 135+5+self.__y, 170+self.__x, 160+5+self.__y) #(+20, +10) difference from walking
                    self.myCanvas.coords(a_name, 138+self.__x, 110+self.__y)
                    self.myCanvas.coords(a_torso, 140+self.__x, 150+5+self.__y, 150+self.__x, 160+5+self.__y, 125+self.__x, 170+5+self.__y, 115+self.__x, 160+5+self.__y) #(20, 10), (5,10)
                    self.myCanvas.coords(a_Larm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                    self.myCanvas.coords(a_Rarm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #Arm hides behind torso (+30,0)
                    self.myCanvas.coords(a_Rleg, 145+self.__x-10, 175+self.__y, 160+self.__x-10, 183+self.__y)
                    self.myCanvas.coords(a_Lleg, 115+self.__x+10, 175+self.__y, 130+self.__x+10, 183+self.__y)
                    self.myCanvas.coords(a_bandana1, 145+self.__x, 150+5+self.__y, 170+self.__x, 150+5+self.__y, 170+self.__x, 160+5+self.__y) #(+20,10) for all bandana
                    self.myCanvas.coords(a_bandana2, 145+self.__x, 150+5+self.__y, 140+self.__x, 152+5+self.__y, 140+self.__x, 155+5+self.__y)
                    self.myCanvas.coords(a_bandana3, 145+self.__x, 150+5+self.__y, 140+self.__x, 148+5+self.__y, 140+self.__x, 151+5+self.__y)
                    self.myCanvas.coords(a_vneck, 140+self.__x, 150+5+self.__y, 145+self.__x, 163+5+self.__y, 125+self.__x, 170+5+self.__y, 115+self.__x, 160+5+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                    self.myCanvas.coords(a_coat, 142+self.__x, 145+5+self.__y, 152+self.__x, 155+5+self.__y, 100+self.__x, 175+10+self.__y, 85+self.__x, 157+10+self.__y, 125+self.__x, 155+5+self.__y)
                    self.myCanvas.update()
                    self.__Frame = 0

            elif self.__Frame == 0 and self.__sprint == False and self.__crouch == True: #Moving right CROUCHING FRAMe #1
                for count in range(90):
                    self.__y -= 1
                    self.myCanvas.coords(a_head, 145+self.__x, 135+self.__y, 170+self.__x, 160+self.__y) #(+20, +10) difference from walking
                    self.myCanvas.coords(a_name, 138+self.__x, 110+self.__y)
                    self.myCanvas.coords(a_torso, 140+self.__x, 150+self.__y, 150+self.__x, 160+self.__y, 125+self.__x, 170+self.__y, 115+self.__x, 160+self.__y) #(10, 0), (5,10), (-20,-5), (-15,-15)
                    self.myCanvas.coords(a_Larm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                    self.myCanvas.coords(a_Rarm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #Arm hides behind torso (+30,0)
                    self.myCanvas.coords(a_Rleg, 145+self.__x-5, 175+self.__y, 160+self.__x-5, 183+self.__y) #(+5,-5), (+5,-5)
                    self.myCanvas.coords(a_Lleg, 115+self.__x+5, 175+self.__y, 130+self.__x+5, 183+self.__y) #(-5,-5), (-5,-5)
                    self.myCanvas.coords(a_bandana1, 145+self.__x, 150+self.__y, 170+self.__x, 150+self.__y, 170+self.__x, 160+self.__y) #(+20,10) for all bandana
                    self.myCanvas.coords(a_bandana2, 145+self.__x, 150+self.__y, 140+self.__x, 152+self.__y, 140+self.__x, 160+self.__y)
                    self.myCanvas.coords(a_bandana3, 145+self.__x, 150+self.__y, 140+self.__x, 148+self.__y, 140+self.__x, 151+self.__y) 
                    self.myCanvas.coords(a_vneck, 140+self.__x, 150+self.__y, 145+self.__x, 163+self.__y, 125+self.__x, 170+self.__y, 115+self.__x, 160+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                    self.myCanvas.coords(a_coat, 142+self.__x, 145+self.__y, 152+self.__x, 155+self.__y, 115+self.__x, 183+self.__y, 92+self.__x, 183+self.__y, 125+self.__x, 155+self.__y)
                    self.myCanvas.update()
                    self.__Frame = 1
                
            elif self.__Frame == 1 and self.__sprint == False and self.__crouch == True: #Moving right CROUCHING FRAMe #2
                for count in range(90):
                    self.__y -= 1
                    self.myCanvas.coords(a_head, 145+self.__x, 135+2+self.__y, 170+self.__x, 160+2+self.__y) #(+20, +10) difference from walking
                    self.myCanvas.coords(a_name, 138+self.__x, 110+self.__y)
                    self.myCanvas.coords(a_torso, 140+self.__x, 150+2+self.__y, 150+self.__x, 160+2+self.__y, 125+self.__x, 170+2+self.__y, 115+self.__x, 160+2+self.__y) #(20, 10), (5,10)
                    self.myCanvas.coords(a_Larm, 130+self.__x+10, 160+2+self.__y, 145+self.__x+10, 175+2+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                    self.myCanvas.coords(a_Rarm, 130+self.__x+10, 160+2+self.__y, 145+self.__x+10, 175+2+self.__y) #Arm hides behind torso (+30,0)
                    self.myCanvas.coords(a_Rleg, 145+self.__x-10, 175+self.__y, 160+self.__x-10, 183+self.__y)
                    self.myCanvas.coords(a_Lleg, 115+self.__x+10, 175+self.__y, 130+self.__x+10, 183+self.__y)
                    self.myCanvas.coords(a_bandana1, 145+self.__x, 150+2+self.__y, 170+self.__x, 150+2+self.__y, 170+self.__x, 160+2+self.__y) #(+20,10) for all bandana
                    self.myCanvas.coords(a_bandana2, 145+self.__x, 150+2+self.__y, 140+self.__x, 152+2+self.__y, 140+self.__x, 155+2+self.__y)
                    self.myCanvas.coords(a_bandana3, 145+self.__x, 150+2+self.__y, 140+self.__x, 148+2+self.__y, 140+self.__x, 151+2+self.__y)
                    self.myCanvas.coords(a_vneck, 140+self.__x, 150+2+self.__y, 145+self.__x, 163+2+self.__y, 125+self.__x, 170+2+self.__y, 115+self.__x, 160+2+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                    self.myCanvas.coords(a_coat, 142+self.__x, 145+2+self.__y, 152+self.__x, 155+2+self.__y, 115+self.__x, 183+2+self.__y, 92+self.__x, 183+2+self.__y, 125+self.__x, 155+2+self.__y)
                    self.myCanvas.update()
                    self.__Frame = 0
            
            self.myCanvas.after(100, rebindW) #2000 ms = 2 seconds Later will need to redo this part because not all falling is going to be 2 seconds long.
            
        def rebindW(): #Rebinds W (falling should be done and can fall again)
            self.__b_w = self.myCanvas.bind("<w>", wKey)
            print("Rebinding 'w' and making inAir=False")
            self.__inAir=False
            
        def leftClick(event): #Basic attack
            print("Left Click")

        def rightClick(event): #Take aim
            print("Right Click")

        def scroll(event): 
            print("Scroll Click")

        def aKey(event): #Move left
            print("'a' key pressed")
            if self.__inAir == True:
                print("IN AIR A")
                return
            elif self.__Frame == 0 and self.__sprint == False and self.__crouch == False: #Moving left without sprint or crouch FRAME #1
                self.__x -= 1 #Arms and leg out
                self.myCanvas.coords(a_head, 125+self.__x, 125+self.__y, 150+self.__x, 150+self.__y)
                self.myCanvas.coords(a_name, 138+self.__x, 110+self.__y)
                self.myCanvas.coords(a_torso, 130+self.__x, 150+self.__y, 145+self.__x, 150+self.__y, 145+self.__x, 175+self.__y, 130+self.__x, 175+self.__y)
                self.myCanvas.coords(a_Larm, 115+self.__x, 150+self.__y, 130+self.__x, 165+self.__y)
                self.myCanvas.coords(a_Rarm, 145+self.__x, 150+self.__y, 160+self.__x, 165+self.__y)
                self.myCanvas.coords(a_Rleg, 145+self.__x, 175+self.__y, 160+self.__x, 183+self.__y)
                self.myCanvas.coords(a_Lleg, 115+self.__x, 175+self.__y, 130+self.__x, 183+self.__y)
                self.myCanvas.coords(a_bandana1, 125+self.__x+25, 140+self.__y, 150+self.__x-25, 140+self.__y, 150+self.__x-25, 150+self.__y)
                self.myCanvas.coords(a_bandana2, 125+self.__x+25, 140+self.__y, 120+self.__x+35, 142+self.__y, 120+self.__x+35, 145+self.__y)
                self.myCanvas.coords(a_bandana3, 125+self.__x+25, 140+self.__y, 120+self.__x+35, 138+self.__y, 120+self.__x+35, 141+self.__y)
                self.myCanvas.coords(a_vneck, 130+self.__x, 155+self.__y, 145+self.__x, 150+self.__y, 145+self.__x, 175+self.__y, 130+self.__x, 175+self.__y)
                self.myCanvas.coords(a_coat, 145+self.__x, 145+self.__y, 133+self.__x, 145+self.__y, 140+self.__x, 175+self.__y, 160+self.__x, 177+self.__y, 145+self.__x, 160+self.__y)
                self.__Frame = 1
                
            elif self.__Frame == 1 and self.__sprint == False and self.__crouch == False: #Moving left without sprint or crouch FRAME #2
                self.__x -= 1 #Arms and legs in
                self.myCanvas.coords(a_head, 125+self.__x, 125+3+self.__y, 150+self.__x, 150+3+self.__y)
                self.myCanvas.coords(a_name, 138+self.__x, 110+self.__y)
                self.myCanvas.coords(a_torso, 130+self.__x, 150+3+self.__y, 145+self.__x, 150+3+self.__y, 145+self.__x, 175+3+self.__y, 130+self.__x, 175+3+self.__y)
                self.myCanvas.coords(a_Larm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO
                self.myCanvas.coords(a_Rarm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #Arm hides behind torso
                self.myCanvas.coords(a_Rleg, 145+self.__x-10, 175+self.__y, 160+self.__x-10, 183+self.__y)
                self.myCanvas.coords(a_Lleg, 115+self.__x+10, 175+self.__y, 130+self.__x+10, 183+self.__y)
                self.myCanvas.coords(a_bandana1, 125+self.__x+25, 140+3+self.__y, 150+self.__x-25, 140+3+self.__y, 150+self.__x-25, 150+3+self.__y)
                self.myCanvas.coords(a_bandana2, 125+self.__x+25, 140+3+self.__y, 120+self.__x+35, 142+3+self.__y, 120+self.__x+35, 145+3+self.__y)
                self.myCanvas.coords(a_bandana3, 125+self.__x+25, 140+3+self.__y, 120+self.__x+35, 138+3+self.__y, 120+self.__x+35, 141+3+self.__y)
                self.myCanvas.coords(a_vneck, 130+self.__x, 155+3+self.__y, 145+self.__x, 150+3+self.__y, 145+self.__x, 175+3+self.__y, 130+self.__x, 175+3+self.__y)
                self.myCanvas.coords(a_coat, 145+self.__x, 145+3+self.__y, 133+self.__x, 145+3+self.__y, 140+self.__x, 175+3+self.__y, 160+self.__x, 177+6+self.__y, 145+self.__x, 160+3+self.__y)
                self.__Frame = 0

            elif self.__Frame == 0 and self.__sprint == True and self.__crouch == False: #Moving left SPRINTING FRAME #1
                self.__x -= 1 #Arms and legs out
                self.myCanvas.coords(a_head, 145+self.__x-40, 135+self.__y, 170+self.__x-40, 160+self.__y) #(+20, +10) difference from walking
                self.myCanvas.coords(a_name, 138+self.__x, 110+self.__y)
                self.myCanvas.coords(a_torso, 140+self.__x-4, 150+self.__y, 150+self.__x-24, 160+self.__y, 125+self.__x+26, 170+self.__y, 115+self.__x+46, 160+self.__y) #(10, 0), (5,10), (-20,-5), (-15,-15)
                self.myCanvas.coords(a_Larm, 85+self.__x+106, 150+self.__y, 100+self.__x+76, 165+self.__y) #(-30,0)
                self.myCanvas.coords(a_Rarm, 175+self.__x-74, 150+self.__y, 190+self.__x-104, 165+self.__y) #(+30,0)
                self.myCanvas.coords(a_Rleg, 150+self.__x-24, 170+self.__y, 165+self.__x-54, 178+self.__y) #(+5,-5), (+5,-5)
                self.myCanvas.coords(a_Lleg, 110+self.__x+56, 170+self.__y, 125+self.__x+26, 178+self.__y) #(-5,-5), (-5,-5)
                self.myCanvas.coords(a_bandana1, 145+self.__x-14, 150+self.__y, 170+self.__x-64, 150+self.__y, 170+self.__x-64, 160+self.__y) #(+20,10) for all bandana
                self.myCanvas.coords(a_bandana2, 145+self.__x-14, 150+self.__y, 140+self.__x-4, 152+self.__y, 140+self.__x-4, 160+self.__y)
                self.myCanvas.coords(a_bandana3, 145+self.__x-14, 150+self.__y, 140+self.__x-4, 148+self.__y, 140+self.__x-4, 151+self.__y) 
                self.myCanvas.coords(a_vneck, 140+self.__x-4, 150+self.__y, 145+self.__x-14, 163+self.__y, 125+self.__x+26, 170+self.__y, 115+self.__x+46, 160+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                self.myCanvas.coords(a_coat, 142+self.__x-8, 145+self.__y, 152+self.__x-28, 155+self.__y, 100+self.__x+76, 175+self.__y, 85+self.__x+104, 157+self.__y, 125+self.__x+26, 155+self.__y)
                self.__x -= 5
                #(12,0) (10,10), (-35,0), (-30,-20), (-5,-5)
                self.__Frame = 1
                
            elif self.__Frame == 1 and self.__sprint == True and self.__crouch == False: #Moving left SPRINTING FRAME #2
                self.__x -= 1 #Arms and legs in
                self.myCanvas.coords(a_head, 145+self.__x-40, 135+5+self.__y, 170+self.__x-40, 160+5+self.__y) #(+20, +10) difference from walking
                self.myCanvas.coords(a_name, 138+self.__x, 110+self.__y)
                self.myCanvas.coords(a_torso, 140+self.__x-4, 150+5+self.__y, 150+self.__x-24, 160+5+self.__y, 125+self.__x+26, 170+5+self.__y, 115+self.__x+46, 160+5+self.__y) #(20, 10), (5,10)
                self.myCanvas.coords(a_Larm, 130+self.__x+16, 160+self.__y, 145+self.__x-14, 175+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                self.myCanvas.coords(a_Rarm, 130+self.__x+16, 160+self.__y, 145+self.__x-14, 175+self.__y) #Arm hides behind torso (+30,0)
                self.myCanvas.coords(a_Rleg, 145+self.__x-10, 175+self.__y, 160+self.__x-10, 183+self.__y)
                self.myCanvas.coords(a_Lleg, 115+self.__x+10, 175+self.__y, 130+self.__x+10, 183+self.__y)
                self.myCanvas.coords(a_bandana1, 145+self.__x-14, 150+5+self.__y, 170+self.__x-64, 150+5+self.__y, 170+self.__x-64, 160+5+self.__y) #(+20,10) for all bandana
                self.myCanvas.coords(a_bandana2, 145+self.__x-14, 150+5+self.__y, 140+self.__x-4, 152+5+self.__y, 140+self.__x-4, 160+5+self.__y)
                self.myCanvas.coords(a_bandana3, 145+self.__x-14, 150+5+self.__y, 140+self.__x-4, 148+5+self.__y, 140+self.__x-4, 151+5+self.__y) 
                self.myCanvas.coords(a_vneck, 140+self.__x-4, 150+5+self.__y, 145+self.__x-14, 163+5+self.__y, 125+self.__x+26, 170+5+self.__y, 115+self.__x+46, 160+5+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                self.myCanvas.coords(a_coat, 142+self.__x-8, 145+5+self.__y, 152+self.__x-28, 155+5+self.__y, 100+self.__x+76, 175+10+self.__y, 85+self.__x+104, 157+10+self.__y, 125+self.__x+26, 155+5+self.__y)
                #(12,0) (10,10), (-35,0), (-30,-20), (-5,-5)
                self.__x -= 5
                self.__Frame = 0

            elif self.__Frame == 0 and self.__sprint == False and self.__crouch == True: #Moving left CROUCHING FRAME #1
                self.__x -= 0.5 #Arms and legs out self.__x 
                self.myCanvas.coords(a_head, 145+self.__x-40, 135+self.__y, 170+self.__x-40, 160+self.__y) #(+20, +10) difference from walking
                self.myCanvas.coords(a_name, 138+self.__x, 110+self.__y)
                self.myCanvas.coords(a_torso, 140+self.__x-4, 150+self.__y, 150+self.__x-24, 160+self.__y, 125+self.__x+26, 170+self.__y, 115+self.__x+46, 160+self.__y) #(10, 0), (5,10), (-20,-5), (-15,-15)
                self.myCanvas.coords(a_Larm, 130+self.__x+16, 160+self.__y, 145+self.__x-14, 175+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                self.myCanvas.coords(a_Rarm, 130+self.__x+16, 160+self.__y, 145+self.__x-14, 175+self.__y) #Arm hides behind torso (+30,0)
                self.myCanvas.coords(a_Rleg, 145+self.__x-5, 175+self.__y, 160+self.__x-5, 183+self.__y) #(+5,-5), (+5,-5)
                self.myCanvas.coords(a_Lleg, 115+self.__x+5, 175+self.__y, 130+self.__x+5, 183+self.__y) #(-5,-5), (-5,-5)
                self.myCanvas.coords(a_bandana1, 145+self.__x-14, 150+self.__y, 170+self.__x-64, 150+self.__y, 170+self.__x-64, 160+self.__y) #(+20,10) for all bandana
                self.myCanvas.coords(a_bandana2, 145+self.__x-14, 150+self.__y, 140+self.__x-4, 152+self.__y, 140+self.__x-4, 160+self.__y)
                self.myCanvas.coords(a_bandana3, 145+self.__x-14, 150+self.__y, 140+self.__x-4, 148+self.__y, 140+self.__x-4, 151+self.__y) 
                self.myCanvas.coords(a_vneck, 140+self.__x-4, 150+self.__y, 145+self.__x-14, 163+self.__y, 125+self.__x+26, 170+self.__y, 115+self.__x+46, 160+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                self.myCanvas.coords(a_coat, 142+self.__x-8, 145+self.__y, 152+self.__x-28, 155+self.__y, 85+self.__x+76, 183+self.__y, 80+self.__x+104, 183+self.__y, 125+self.__x+26, 155+self.__y)
                self.__Frame = 1
                
            elif self.__Frame == 1 and self.__sprint == False and self.__crouch == True: #Moving left CROUCHING FRAME #2
                self.__x -= 0.5 #Arms and legs in
                self.myCanvas.coords(a_head, 145+self.__x-40, 135+2+self.__y, 170+self.__x-40, 160+2+self.__y) #(+20, +10) difference from walking
                self.myCanvas.coords(a_name, 138+self.__x, 110+self.__y)
                self.myCanvas.coords(a_torso, 140+self.__x-4, 150+2+self.__y, 150+self.__x-24, 160+2+self.__y, 125+self.__x+26, 170+2+self.__y, 115+self.__x+46, 160+2+self.__y) #(20, 10), (5,10)
                self.myCanvas.coords(a_Larm, 130+self.__x-10, 160+2+self.__y, 145+self.__x-10, 175+2+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                self.myCanvas.coords(a_Rarm, 130+self.__x-10, 160+2+self.__y, 145+self.__x-10, 175+2+self.__y) #Arm hides behind torso (+30,0)
                self.myCanvas.coords(a_Rleg, 145+self.__x-10, 175+self.__y, 160+self.__x-10, 183+self.__y)
                self.myCanvas.coords(a_Lleg, 115+self.__x+10, 175+self.__y, 130+self.__x+10, 183+self.__y)
                self.myCanvas.coords(a_bandana1, 145+self.__x-14, 150+2+self.__y, 170+self.__x-64, 150+2+self.__y, 170+self.__x-64, 160+2+self.__y) #(+20,10) for all bandana
                self.myCanvas.coords(a_bandana2, 145+self.__x-14, 150+2+self.__y, 140+self.__x-4, 152+2+self.__y, 140+self.__x-4, 160+2+self.__y)
                self.myCanvas.coords(a_bandana3, 145+self.__x-14, 150+2+self.__y, 140+self.__x-4, 148+2+self.__y, 140+self.__x-4, 151+2+self.__y) 
                self.myCanvas.coords(a_vneck, 140+self.__x-4, 150+2+self.__y, 145+self.__x-14, 163+2+self.__y, 125+self.__x+26, 170+2+self.__y, 115+self.__x+46, 160+2+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                self.myCanvas.coords(a_coat, 142+self.__x-8, 145+2+self.__y, 152+self.__x-28, 155+2+self.__y, 85+self.__x+76, 183+2+self.__y, 80+self.__x+104, 183+2+self.__y, 125+self.__x+26, 155+2+self.__y)
                #(12,0) (10,10), (-35,0), (-30,-20), (-5,-5)
                self.__Frame = 0

            self.__looking = "Left"
            self.myCanvas.update()

        def dKey(event): #Move right
            print("'d' key pressed")
            if self.__inAir == True:
                print("IN AIR D")
                self.__x += 1
                return
            elif self.__Frame == 0 and self.__sprint == False and self.__crouch == False: #Moving right without sprinting or crouching FRAME #1
                self.__x += 1 #Arms and legs out self.__x 
                self.myCanvas.coords(a_head, 125+self.__x, 125+self.__y, 150+self.__x, 150+self.__y)
                self.myCanvas.coords(a_name, 138+self.__x, 110+self.__y)
                self.myCanvas.coords(a_torso, 130+self.__x, 150+self.__y, 145+self.__x, 150+self.__y, 145+self.__x, 175+self.__y, 130+self.__x, 175+self.__y)
                self.myCanvas.coords(a_Larm, 115+self.__x, 150+self.__y, 130+self.__x, 165+self.__y)
                self.myCanvas.coords(a_Rarm, 145+self.__x, 150+self.__y, 160+self.__x, 165+self.__y)
                self.myCanvas.coords(a_Rleg, 145+self.__x, 175+self.__y, 160+self.__x, 183+self.__y)
                self.myCanvas.coords(a_Lleg, 115+self.__x, 175+self.__y, 130+self.__x, 183+self.__y)
                self.myCanvas.coords(a_bandana1, 125+self.__x, 140+self.__y, 150+self.__x, 140+self.__y, 150+self.__x, 150+self.__y)
                self.myCanvas.coords(a_bandana2, 125+self.__x, 140+self.__y, 120+self.__x, 142+self.__y, 120+self.__x, 145+self.__y)
                self.myCanvas.coords(a_bandana3, 125+self.__x, 140+self.__y, 120+self.__x, 138+self.__y, 120+self.__x, 141+self.__y)
                self.myCanvas.coords(a_vneck, 130+self.__x, 150+self.__y, 145+self.__x, 155+self.__y, 145+self.__x, 175+self.__y, 130+self.__x, 175+self.__y)
                self.myCanvas.coords(a_coat, 130+self.__x, 145+self.__y, 142+self.__x, 145+self.__y, 135+self.__x, 175+self.__y, 115+self.__x, 177+self.__y, 130+self.__x, 160+self.__y)
                self.__Frame = 1
                
            elif self.__Frame == 1 and self.__sprint == False and self.__crouch == False: #Moving right without sprinting or crouching FRAME #2
                self.__x += 1 #Arms and legs in
                self.myCanvas.coords(a_head, 125+self.__x, 125+3+self.__y, 150+self.__x, 150+3+self.__y)
                self.myCanvas.coords(a_name, 138+self.__x, 110+self.__y)
                self.myCanvas.coords(a_torso, 130+self.__x, 150+3+self.__y, 145+self.__x, 150+3+self.__y, 145+self.__x, 175+3+self.__y, 130+self.__x, 175+3+self.__y)
                self.myCanvas.coords(a_Larm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO
                self.myCanvas.coords(a_Rarm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #Arm hides behind torso
                self.myCanvas.coords(a_Rleg, 145+self.__x-10, 175+self.__y, 160+self.__x-10, 183+self.__y)
                self.myCanvas.coords(a_Lleg, 115+self.__x+10, 175+self.__y, 130+self.__x+10, 183+self.__y)
                self.myCanvas.coords(a_bandana1, 125+self.__x, 140+3+self.__y, 150+self.__x, 140+3+self.__y, 150+self.__x, 150+3+self.__y)
                self.myCanvas.coords(a_bandana2, 125+self.__x, 140+3+self.__y, 120+self.__x, 142+3+self.__y, 120+self.__x, 145+3+self.__y)
                self.myCanvas.coords(a_bandana3, 125+self.__x, 140+3+self.__y, 120+self.__x, 138+3+self.__y, 120+self.__x, 141+3+self.__y)
                self.myCanvas.coords(a_vneck, 130+self.__x, 150+3+self.__y, 145+self.__x, 155+3+self.__y, 145+self.__x, 175+3+self.__y, 130+self.__x, 175+3+self.__y)
                self.myCanvas.coords(a_coat, 130+self.__x, 145+3+self.__y, 142+self.__x, 145+3+self.__y, 135+self.__x, 175+3+self.__y, 115+self.__x, 177+6+self.__y, 130+self.__x, 160+self.__y)
                self.__Frame = 0

            elif self.__Frame == 0 and self.__sprint == True and self.__crouch == False: #Moving right SPRINTING FRAME #1
                self.__x += 1 #Arms and legs out
                self.myCanvas.coords(a_head, 145+self.__x, 135+self.__y, 170+self.__x, 160+self.__y) #(+20, +10) difference from walking
                self.myCanvas.coords(a_name, 138+self.__x, 110+self.__y)
                self.myCanvas.coords(a_torso, 140+self.__x, 150+self.__y, 150+self.__x, 160+self.__y, 125+self.__x, 170+self.__y, 115+self.__x, 160+self.__y) #(10, 0), (5,10), (-20,-5), (-15,-15)
                self.myCanvas.coords(a_Larm, 85+self.__x, 150+self.__y, 100+self.__x, 165+self.__y) #(-30,0)
                self.myCanvas.coords(a_Rarm, 175+self.__x, 150+self.__y, 190+self.__x, 165+self.__y) #(+30,0)
                self.myCanvas.coords(a_Rleg, 150+self.__x, 170+self.__y, 165+self.__x, 178+self.__y) #(+5,-5), (+5,-5)
                self.myCanvas.coords(a_Lleg, 110+self.__x, 170+self.__y, 125+self.__x, 178+self.__y) #(-5,-5), (-5,-5)
                self.myCanvas.coords(a_bandana1, 145+self.__x, 150+self.__y, 170+self.__x, 150+self.__y, 170+self.__x, 160+self.__y) #(+20,10) for all bandana
                self.myCanvas.coords(a_bandana2, 145+self.__x, 150+self.__y, 140+self.__x, 152+self.__y, 140+self.__x, 160+self.__y)
                self.myCanvas.coords(a_bandana3, 145+self.__x, 150+self.__y, 140+self.__x, 148+self.__y, 140+self.__x, 151+self.__y) 
                self.myCanvas.coords(a_vneck, 140+self.__x, 150+self.__y, 145+self.__x, 163+self.__y, 125+self.__x, 170+self.__y, 115+self.__x, 160+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                self.myCanvas.coords(a_coat, 142+self.__x, 145+self.__y, 152+self.__x, 155+self.__y, 100+self.__x, 175+self.__y, 85+self.__x, 157+self.__y, 125+self.__x, 155+self.__y)
                self.__x += 5
                #(12,0) (10,10), (-35,0), (-30,-20), (-5,-5)
                self.__Frame = 1
                
            elif self.__Frame == 1 and self.__sprint == True and self.__crouch == False: #Moving right SPRINTING FRAME #2
                self.__x += 1 #Arms and legs in
                self.myCanvas.coords(a_head, 145+self.__x, 135+5+self.__y, 170+self.__x, 160+5+self.__y) #(+20, +10) difference from walking
                self.myCanvas.coords(a_name, 138+self.__x, 110+self.__y)
                self.myCanvas.coords(a_torso, 140+self.__x, 150+5+self.__y, 150+self.__x, 160+5+self.__y, 125+self.__x, 170+5+self.__y, 115+self.__x, 160+5+self.__y) #(20, 10), (5,10)
                self.myCanvas.coords(a_Larm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                self.myCanvas.coords(a_Rarm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #Arm hides behind torso (+30,0)
                self.myCanvas.coords(a_Rleg, 145+self.__x-10, 175+self.__y, 160+self.__x-10, 183+self.__y)
                self.myCanvas.coords(a_Lleg, 115+self.__x+10, 175+self.__y, 130+self.__x+10, 183+self.__y)
                self.myCanvas.coords(a_bandana1, 145+self.__x, 150+5+self.__y, 170+self.__x, 150+5+self.__y, 170+self.__x, 160+5+self.__y) #(+20,10) for all bandana
                self.myCanvas.coords(a_bandana2, 145+self.__x, 150+5+self.__y, 140+self.__x, 152+5+self.__y, 140+self.__x, 155+5+self.__y)
                self.myCanvas.coords(a_bandana3, 145+self.__x, 150+5+self.__y, 140+self.__x, 148+5+self.__y, 140+self.__x, 151+5+self.__y)
                self.myCanvas.coords(a_vneck, 140+self.__x, 150+5+self.__y, 145+self.__x, 163+5+self.__y, 125+self.__x, 170+5+self.__y, 115+self.__x, 160+5+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                self.myCanvas.coords(a_coat, 142+self.__x, 145+5+self.__y, 152+self.__x, 155+5+self.__y, 100+self.__x, 175+10+self.__y, 85+self.__x, 157+10+self.__y, 125+self.__x, 155+5+self.__y)
                #(12,0) (10,10), (-35,0), (-30,-20), (-5,-5)
                self.__x += 5
                self.__Frame = 0

            elif self.__Frame == 0 and self.__sprint == False and self.__crouch == True: #Moving right CROUCHING FRAMe #1
                self.myCanvas.coords(a_head, 145+self.__x, 135+self.__y, 170+self.__x, 160+self.__y) #(+20, +10) difference from walking
                self.myCanvas.coords(a_name, 138+self.__x, 110+self.__y)
                self.myCanvas.coords(a_torso, 140+self.__x, 150+self.__y, 150+self.__x, 160+self.__y, 125+self.__x, 170+self.__y, 115+self.__x, 160+self.__y) #(10, 0), (5,10), (-20,-5), (-15,-15)
                self.myCanvas.coords(a_Larm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                self.myCanvas.coords(a_Rarm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #Arm hides behind torso (+30,0)
                self.myCanvas.coords(a_Rleg, 145+self.__x-5, 175+self.__y, 160+self.__x-5, 183+self.__y) #(+5,-5), (+5,-5)
                self.myCanvas.coords(a_Lleg, 115+self.__x+5, 175+self.__y, 130+self.__x+5, 183+self.__y) #(-5,-5), (-5,-5)
                self.myCanvas.coords(a_bandana1, 145+self.__x, 150+self.__y, 170+self.__x, 150+self.__y, 170+self.__x, 160+self.__y) #(+20,10) for all bandana
                self.myCanvas.coords(a_bandana2, 145+self.__x, 150+self.__y, 140+self.__x, 152+self.__y, 140+self.__x, 160+self.__y)
                self.myCanvas.coords(a_bandana3, 145+self.__x, 150+self.__y, 140+self.__x, 148+self.__y, 140+self.__x, 151+self.__y) 
                self.myCanvas.coords(a_vneck, 140+self.__x, 150+self.__y, 145+self.__x, 163+self.__y, 125+self.__x, 170+self.__y, 115+self.__x, 160+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                self.myCanvas.coords(a_coat, 142+self.__x, 145+self.__y, 152+self.__x, 155+self.__y, 115+self.__x, 183+self.__y, 92+self.__x, 183+self.__y, 125+self.__x, 155+self.__y)
                self.__Frame = 1
                
            elif self.__Frame == 1 and self.__sprint == False and self.__crouch == True: #Moving right CROUCHING FRAMe #2
                self.__x += 0.5 #Arms and legs in
                self.myCanvas.coords(a_head, 145+self.__x, 135+2+self.__y, 170+self.__x, 160+2+self.__y) #(+20, +10) difference from walking
                self.myCanvas.coords(a_name, 138+self.__x, 110+self.__y)
                self.myCanvas.coords(a_torso, 140+self.__x, 150+2+self.__y, 150+self.__x, 160+2+self.__y, 125+self.__x, 170+2+self.__y, 115+self.__x, 160+2+self.__y) #(20, 10), (5,10)
                self.myCanvas.coords(a_Larm, 130+self.__x+10, 160+2+self.__y, 145+self.__x+10, 175+2+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                self.myCanvas.coords(a_Rarm, 130+self.__x+10, 160+2+self.__y, 145+self.__x+10, 175+2+self.__y) #Arm hides behind torso (+30,0)
                self.myCanvas.coords(a_Rleg, 145+self.__x-10, 175+self.__y, 160+self.__x-10, 183+self.__y)
                self.myCanvas.coords(a_Lleg, 115+self.__x+10, 175+self.__y, 130+self.__x+10, 183+self.__y)
                self.myCanvas.coords(a_bandana1, 145+self.__x, 150+2+self.__y, 170+self.__x, 150+2+self.__y, 170+self.__x, 160+2+self.__y) #(+20,10) for all bandana
                self.myCanvas.coords(a_bandana2, 145+self.__x, 150+2+self.__y, 140+self.__x, 152+2+self.__y, 140+self.__x, 155+2+self.__y)
                self.myCanvas.coords(a_bandana3, 145+self.__x, 150+2+self.__y, 140+self.__x, 148+2+self.__y, 140+self.__x, 151+2+self.__y)
                self.myCanvas.coords(a_vneck, 140+self.__x, 150+2+self.__y, 145+self.__x, 163+2+self.__y, 125+self.__x, 170+2+self.__y, 115+self.__x, 160+2+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                self.myCanvas.coords(a_coat, 142+self.__x, 145+2+self.__y, 152+self.__x, 155+2+self.__y, 115+self.__x, 183+2+self.__y, 92+self.__x, 183+2+self.__y, 125+self.__x, 155+2+self.__y)
                self.__Frame = 0

            self.__looking = "Right"
            self.myCanvas.update()


        def shiftKey(event): #Sprint/Walk toggle
            print("'Shift' key pressed")
            if self.__sprint == True and self.__crouch == False:
                self.__sprint = False
            elif self.__sprint == False and self.__crouch == False:
                self.__sprint = True
            else:
                print("Cannot toggle sprint! Must be out of crouch!")

        def ctrlKey(event): #crouch
            print("'Control' key pressed")
            if self.__crouch == True and self.__sprint == False:
                self.__crouch = False
            elif self.__crouch == False and self.__sprint == False:
                self.__crouch = True
            else:
                print("Cannot toggle crouch! Must be out of sprint!")
            
        def randomRects(num): #FOR BACKGROUND
            for i in range(0,num):
                x1=random.randrange(1000)
                y1=random.randrange(1000)
                x2=x1+random.randrange(1000)
                y2=y1+random.randrange(1000)
                self.myCanvas.create_rectangle(x1,y1,x2,y2,outline="black")

        self.master.title("Harbinger - Alpha 1.6: Jumping and Dropping Update") #Titles the window "Harbinger"

        self.myCanvas = Canvas(width=1500, height=1000, bg="SkyBlue1") #Background with window size. bg= "SkyBlue1"
        self.myCanvas.grid() #Display it

        #randomRects(300) #BACKGROUND UNCOMMENT THIS OUT IF YOU WANT TO USE.
        
        a_description = self.myCanvas.create_text(0, 0, text="""Press 'd' or 'a' to move. Hold 'd' or 'a' to walk. \nPress Shift to change from walking to running. Vise-vera."""
                                                  """ \nPress Ctrl to toggle crouching."""
                                                  """ \nActions are displayed on the interpreter."""
                                                  """ \nPress 'w' to jump. Press 's' to drop down."""
                                                  """ \nNext update will include special ablities (spacebar) or smoother animations.""",
                                                  width=1000, fill="black", anchor="nw", font=("Fixedsys", 16))#Top left corner of screen text
        #Creating ground1
        a_ground1 = self.myCanvas.create_rectangle(0,183,1500,190, outline="black",fill="green")

        #Creating ground2
        a_ground1 = self.myCanvas.create_rectangle(0,273,1500,280, outline="black",fill="green")
        
        #Creating the model of player 1 w/ label above it's head
        #Character is walking to the right of the screen
        #Name of the character
        a_name = self.myCanvas.create_text(138, 110, text="Jefferson Starship", width=1000, fill="green", anchor="center", font=("Fixedsys", 16))

        #Creates the head of character
        a_head = self.myCanvas.create_oval(125, 125, 150, 150, fill="white")

        #HIS RIGHT ARM ANIMATIONS NEEDS TO BE BEHIND TORSO BC IT WOULD SHOW
        a_Rarm = self.myCanvas.create_oval(130, 160, 145, 175, fill="white")
        
        #Torso
        a_torso = self.myCanvas.create_polygon(130, 150, 145, 150, 145, 175, 130, 175, fill="white", outline="black")

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
        self.__b_leftClick = self.myCanvas.bind("<Button-1>", leftClick) #bind.("<BUTTON_NAME>", function_call) #Functions way above
        self.__b_scroll = self.myCanvas.bind("<Button-2>", scroll)
        self.__b_rightClick = self.myCanvas.bind("<Button-3>", rightClick)
        self.__b_a = self.myCanvas.bind("<a>", aKey)
        self.__b_d = self.myCanvas.bind("<d>", dKey)
        self.__b_s = self.myCanvas.bind("<s>", sKey)
        self.__b_w = self.myCanvas.bind("<w>", wKey)
        self.__b_q = self.myCanvas.bind("<q>", qKey)
        self.__b_e = self.myCanvas.bind("<e>", eKey)
        self.__b_shiftR = self.myCanvas.bind("<Shift_R>", shiftKey)
        self.__b_shiftL = self.myCanvas.bind("<Shift_L>", shiftKey)
        self.__b_ctrlL = self.myCanvas.bind("<Control_L>", ctrlKey)
        self.__b_ctrlR = self.myCanvas.bind("<Control_R>", ctrlKey)
        self.__b_space = self.myCanvas.bind("<space>", spaceKey)
        self.myCanvas.focus_set() #Tells Python to use keyboard so left and right arrow keys work now

        #IDK HOW TO CREATE A BUTTON IN THE MAIN WINDOW WILL DO LATER
        #button1=Button(main_frame,text="Click Me")
        #button1.bind("<Button-1>",printName)
        #button1.pack()
        
main_frame = MainFrame()
main_frame.mainloop()

