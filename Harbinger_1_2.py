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
        
        #KEYBINDINGS
        def spaceKey(event): #Special ability
            print("'spacebar' key pressed")

        def eKey(event): #Block
            print("'e' key pressed")
        
        def qKey(event): #Switch weapons
            print("'q' key pressed")
        
        def sKey(event): #Drop down
            print("'s' key pressed")
        
        def wKey(event): #Jump
            print("'w' key pressed")
            
        def leftClick(event): #Basic attack
            print("Left Click")

        def rightClick(event): #Take aim
            print("Right Click")

        def scroll(event): 
            print("Scroll Click")

        def aKey(event): #Move left
            print("'a' key pressed")
            if self.__Frame == 0 and self.__sprint == False and self.__crouch == False: #Moving left without sprint or crouch FRAME #1
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
                self.__x -= 1 #Arms and legs out self.__x 
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
                
            elif self.__Frame == 1 and self.__sprint == False and self.__crouch == True: #Moving left CROUCHING FRAME #2
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
                
            self.myCanvas.update()

        def dKey(event): #Move right
            print("'d' key pressed")
            if self.__Frame == 0 and self.__sprint == False and self.__crouch == False: #Moving right without sprinting or crouching FRAME #1
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
                self.myCanvas.coords(a_Rarm, 130+self.__x, 150+self.__y, 145+self.__x, 175+self.__y) #Arm hides behind torso (+30,0)
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
                
            elif self.__Frame == 1 and self.__sprint == False and self.__crouch == True: #Moving right CROUCHING FRAMe #2
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
                print("CROUCH OFF")
                self.__crouch = False
                print(self.__crouch)
            elif self.__crouch == False and self.__sprint == False:
                print("CROUCH ON")
                self.__crouch = True
                print(self.__crouch)
            else:
                print("Cannot toggle crouch! Must be out of sprint!")
            

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
        self.myCanvas.bind("<Button-1>", leftClick) #bind.("<BUTTON_NAME>", function_call) #Functions way above
        self.myCanvas.bind("<Button-2>", scroll)
        self.myCanvas.bind("<Button-3>", rightClick)
        self.myCanvas.bind("<a>", aKey)
        self.myCanvas.bind("<d>", dKey)
        self.myCanvas.bind("<s>", sKey)
        self.myCanvas.bind("<w>", wKey)
        self.myCanvas.bind("<q>", qKey)
        self.myCanvas.bind("<e>", eKey)
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

