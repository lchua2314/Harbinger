#This game will use animations with the tkinter and time classes.

from tkinter import *
import random
import time
tk = Tk()
tk.title("Harbinger - Alpha 1.7: New Engine Update")
tk.resizable(0,0)
canvas = Canvas(width=1300, height=700, bg="SkyBlue1")
canvas.pack()
tk.update()

class Sword: 
    def __init__(self,canvas):
        self.canvas = canvas

        #I need help creating designs with a crappy sword AND an OP sword. No animating. I'll do that.

        #Crappy sword
        self.s_name1 = canvas.create_text(500, 100, anchor="center", fill="green", text="Sword Name1", font=("Fixedsys", 16)) #The "s_" means sword for short.
        self.s_blade1 = canvas.create_polygon(495, 110, 505, 110, 505, 160, 495, 160, fill="silver", outline="black") #Follow the format of naming please.

        #OP Sword
        self.s_name2 = canvas.create_text(1000, 100, anchor="center", fill="green", text="Sword Name2", font=("Fixedsys", 16)) 
        self.s_blade2 = canvas.create_polygon(995, 110, 1005, 110, 1005, 160, 995, 160, fill="silver", outline="black")

class Background:
    def __init__(self,canvas):
        self.canvas = canvas
        
        self.a_description = canvas.create_text(0, 0, text="""Press 'd' or 'a' to move. Hold 'd' or 'a' to walk. \nPress Shift to change from walking to running. Vise-vera."""
                                                  """ \nPress Ctrl to toggle crouching."""
                                                  """ \nActions are displayed on the interpreter."""
                                                  """ \nPress 'w' to jump. Press 's' to drop down."""
                                                  """ \nNext update will include special ablities (spacebar) or smoother animations.""",
                                                  width=1000, fill="black", anchor="nw", font=("Fixedsys", 16))#Top left corner of screen text
        #Creating ground1
        self.a_ground1 = canvas.create_rectangle(0,183,1500,190, outline="black",fill="green")

        #Creating ground2
        self.a_ground1 = canvas.create_rectangle(0,273,1500,280, outline="black",fill="green")

class Player:
    def __init__(self,canvas):
        self.canvas=canvas
        
        self.__x, self.__y = 0,0 #Only one coordinate now. This coordinate is where the first shape is initialized. Not the graph.
        self.__Frame = 0 #Two frames-0 and 1. They alternate which makes the character move more lively.
        self.__sprint = False 
        self.__crouch = False
        self.__inAir = False #If player is mid-air, do not run the other animations (walking, crouching, sprinting) in the air. Just increment the player where they want to fall.
        self.__looking = "Right" #Need to check what direction character is facing when moving up or down.
        self.__voiceOn = False

        #KEYBINDINGS
        def spaceKey(event): #Special ability: Voice
            print("'spacebar' key pressed")
            #canvas.unbind("<space>", self.__b_space) #Need to create rebind method soon.
            self.__a_VoR1 = canvas.create_arc(125+self.__x, 125+self.__y, 150+self.__x, 150+self.__y,extent=-45, style=ARC)
            self.__a_VoR2 = canvas.create_arc(130+self.__x, 120+self.__y, 155+self.__x, 155+self.__y,extent=-45, style=ARC)
            self.__a_VoR3 = canvas.create_arc(135+self.__x, 115+self.__y, 160+self.__x, 160+self.__y,extent=-45, style=ARC)
            self.__voiceOn = True

        def eKey(event): #Block
            print("'e' key pressed")
        
        def qKey(event): #Switch weapons
            print("'q' key pressed")
            
        def sKey(event): #Drop down
            print("'s' key pressed")
            print("Making inAir equal True")
            self.__inAir = True
            print("Disabling 's' binding") #Makes sure the user does not spam this animation DURING the animation.
            canvas.unbind("<s>", self.__b_s)

            if self.__voiceOn == True:
                canvas.delete(self.__a_VoR1, self.__a_VoR2, self.__a_VoR3)
                self.__voiceOn = False

            if self.__Frame == 0 and self.__sprint == False and self.__crouch == False and self.__looking == "Left": #Moving left without sprint or crouch FRAME #1
                for count in range(90):
                    self.__y += 1
                    canvas.coords(self.a_head, 125+self.__x, 125+self.__y, 150+self.__x, 150+self.__y)
                    canvas.coords(self.a_name, 138+self.__x, 110+self.__y)
                    canvas.coords(self.a_torso, 130+self.__x, 150+self.__y, 145+self.__x, 150+self.__y, 145+self.__x, 175+self.__y, 130+self.__x, 175+self.__y)
                    canvas.coords(self.a_Larm, 115+self.__x, 150+self.__y, 130+self.__x, 165+self.__y)
                    canvas.coords(self.a_Rarm, 145+self.__x, 150+self.__y, 160+self.__x, 165+self.__y)
                    canvas.coords(self.a_Rleg, 145+self.__x, 175+self.__y, 160+self.__x, 183+self.__y)
                    canvas.coords(self.a_Lleg, 115+self.__x, 175+self.__y, 130+self.__x, 183+self.__y)
                    canvas.coords(self.a_bandana1, 125+self.__x+25, 140+self.__y, 150+self.__x-25, 140+self.__y, 150+self.__x-25, 150+self.__y)
                    canvas.coords(self.a_bandana2, 125+self.__x+25, 140+self.__y, 120+self.__x+35, 142+self.__y, 120+self.__x+35, 145+self.__y)
                    canvas.coords(self.a_bandana3, 125+self.__x+25, 140+self.__y, 120+self.__x+35, 138+self.__y, 120+self.__x+35, 141+self.__y)
                    canvas.coords(self.a_vneck, 130+self.__x, 155+self.__y, 145+self.__x, 150+self.__y, 145+self.__x, 175+self.__y, 130+self.__x, 175+self.__y)
                    canvas.coords(self.a_coat, 145+self.__x, 145+self.__y, 133+self.__x, 145+self.__y, 140+self.__x, 175+self.__y, 160+self.__x, 177+self.__y, 145+self.__x, 160+self.__y)
                    canvas.update()
                    self.__Frame = 1
                
            elif self.__Frame == 1 and self.__sprint == False and self.__crouch == False and self.__looking == "Left": #Moving left without sprint or crouch FRAME #2
                for count in range(90):
                    self.__y += 1
                    canvas.coords(self.a_head, 125+self.__x, 125+3+self.__y, 150+self.__x, 150+3+self.__y)
                    canvas.coords(self.a_name, 138+self.__x, 110+self.__y)
                    canvas.coords(self.a_torso, 130+self.__x, 150+3+self.__y, 145+self.__x, 150+3+self.__y, 145+self.__x, 175+3+self.__y, 130+self.__x, 175+3+self.__y)
                    canvas.coords(self.a_Larm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO
                    canvas.coords(self.a_Rarm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #Arm hides behind torso
                    canvas.coords(self.a_Rleg, 145+self.__x-10, 175+self.__y, 160+self.__x-10, 183+self.__y)
                    canvas.coords(self.a_Lleg, 115+self.__x+10, 175+self.__y, 130+self.__x+10, 183+self.__y)
                    canvas.coords(self.a_bandana1, 125+self.__x+25, 140+3+self.__y, 150+self.__x-25, 140+3+self.__y, 150+self.__x-25, 150+3+self.__y)
                    canvas.coords(self.a_bandana2, 125+self.__x+25, 140+3+self.__y, 120+self.__x+35, 142+3+self.__y, 120+self.__x+35, 145+3+self.__y)
                    canvas.coords(self.a_bandana3, 125+self.__x+25, 140+3+self.__y, 120+self.__x+35, 138+3+self.__y, 120+self.__x+35, 141+3+self.__y)
                    canvas.coords(self.a_vneck, 130+self.__x, 155+3+self.__y, 145+self.__x, 150+3+self.__y, 145+self.__x, 175+3+self.__y, 130+self.__x, 175+3+self.__y)
                    canvas.coords(self.a_coat, 145+self.__x, 145+3+self.__y, 133+self.__x, 145+3+self.__y, 140+self.__x, 175+3+self.__y, 160+self.__x, 177+6+self.__y, 145+self.__x, 160+3+self.__y)
                    canvas.update()
                    self.__Frame = 0

            elif self.__Frame == 0 and self.__sprint == True and self.__crouch == False and self.__looking == "Left": #Moving left SPRINTING FRAME #1
                for count in range(90):
                    self.__y += 1
                    canvas.coords(self.a_head, 145+self.__x-40, 135+self.__y, 170+self.__x-40, 160+self.__y) #(+20, +10) difference from walking
                    canvas.coords(self.a_name, 138+self.__x, 110+self.__y)
                    canvas.coords(self.a_torso, 140+self.__x-4, 150+self.__y, 150+self.__x-24, 160+self.__y, 125+self.__x+26, 170+self.__y, 115+self.__x+46, 160+self.__y) #(10, 0), (5,10), (-20,-5), (-15,-15)
                    canvas.coords(self.a_Larm, 85+self.__x+106, 150+self.__y, 100+self.__x+76, 165+self.__y) #(-30,0)
                    canvas.coords(self.a_Rarm, 175+self.__x-74, 150+self.__y, 190+self.__x-104, 165+self.__y) #(+30,0)
                    canvas.coords(self.a_Rleg, 150+self.__x-24, 170+self.__y, 165+self.__x-54, 178+self.__y) #(+5,-5), (+5,-5)
                    canvas.coords(self.a_Lleg, 110+self.__x+56, 170+self.__y, 125+self.__x+26, 178+self.__y) #(-5,-5), (-5,-5)
                    canvas.coords(self.a_bandana1, 145+self.__x-14, 150+self.__y, 170+self.__x-64, 150+self.__y, 170+self.__x-64, 160+self.__y) #(+20,10) for all bandana
                    canvas.coords(self.a_bandana2, 145+self.__x-14, 150+self.__y, 140+self.__x-4, 152+self.__y, 140+self.__x-4, 160+self.__y)
                    canvas.coords(self.a_bandana3, 145+self.__x-14, 150+self.__y, 140+self.__x-4, 148+self.__y, 140+self.__x-4, 151+self.__y) 
                    canvas.coords(self.a_vneck, 140+self.__x-4, 150+self.__y, 145+self.__x-14, 163+self.__y, 125+self.__x+26, 170+self.__y, 115+self.__x+46, 160+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                    canvas.coords(self.a_coat, 142+self.__x-8, 145+self.__y, 152+self.__x-28, 155+self.__y, 100+self.__x+76, 175+self.__y, 85+self.__x+104, 157+self.__y, 125+self.__x+26, 155+self.__y)
                    canvas.update()
                    self.__Frame = 1
                
            elif self.__Frame == 1 and self.__sprint == True and self.__crouch == False and self.__looking == "Left": #Moving left SPRINTING FRAME #2
                for count in range(90):
                    self.__y += 1
                    canvas.coords(self.a_head, 145+self.__x-40, 135+5+self.__y, 170+self.__x-40, 160+5+self.__y) #(+20, +10) difference from walking
                    canvas.coords(self.a_name, 138+self.__x, 110+self.__y)
                    canvas.coords(self.a_torso, 140+self.__x-4, 150+5+self.__y, 150+self.__x-24, 160+5+self.__y, 125+self.__x+26, 170+5+self.__y, 115+self.__x+46, 160+5+self.__y) #(20, 10), (5,10)
                    canvas.coords(self.a_Larm, 130+self.__x+16, 160+self.__y, 145+self.__x-14, 175+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                    canvas.coords(self.a_Rarm, 130+self.__x+16, 160+self.__y, 145+self.__x-14, 175+self.__y) #Arm hides behind torso (+30,0)
                    canvas.coords(self.a_Rleg, 145+self.__x-10, 175+self.__y, 160+self.__x-10, 183+self.__y)
                    canvas.coords(self.a_Lleg, 115+self.__x+10, 175+self.__y, 130+self.__x+10, 183+self.__y)
                    canvas.coords(self.a_bandana1, 145+self.__x-14, 150+5+self.__y, 170+self.__x-64, 150+5+self.__y, 170+self.__x-64, 160+5+self.__y) #(+20,10) for all bandana
                    canvas.coords(self.a_bandana2, 145+self.__x-14, 150+5+self.__y, 140+self.__x-4, 152+5+self.__y, 140+self.__x-4, 160+5+self.__y)
                    canvas.coords(self.a_bandana3, 145+self.__x-14, 150+5+self.__y, 140+self.__x-4, 148+5+self.__y, 140+self.__x-4, 151+5+self.__y) 
                    canvas.coords(self.a_vneck, 140+self.__x-4, 150+5+self.__y, 145+self.__x-14, 163+5+self.__y, 125+self.__x+26, 170+5+self.__y, 115+self.__x+46, 160+5+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                    canvas.coords(self.a_coat, 142+self.__x-8, 145+5+self.__y, 152+self.__x-28, 155+5+self.__y, 100+self.__x+76, 175+10+self.__y, 85+self.__x+104, 157+10+self.__y, 125+self.__x+26, 155+5+self.__y)
                    canvas.update()
                    self.__Frame = 0

            elif self.__Frame == 0 and self.__sprint == False and self.__crouch == True and self.__looking == "Left": #Moving left CROUCHING FRAME #1
                for count in range(90):
                    self.__y += 1
                    canvas.coords(self.a_head, 145+self.__x-40, 135+self.__y, 170+self.__x-40, 160+self.__y) #(+20, +10) difference from walking
                    canvas.coords(self.a_name, 138+self.__x, 110+self.__y)
                    canvas.coords(self.a_torso, 140+self.__x-4, 150+self.__y, 150+self.__x-24, 160+self.__y, 125+self.__x+26, 170+self.__y, 115+self.__x+46, 160+self.__y) #(10, 0), (5,10), (-20,-5), (-15,-15)
                    canvas.coords(self.a_Larm, 130+self.__x+16, 160+self.__y, 145+self.__x-14, 175+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                    canvas.coords(self.a_Rarm, 130+self.__x+16, 160+self.__y, 145+self.__x-14, 175+self.__y) #Arm hides behind torso (+30,0)
                    canvas.coords(self.a_Rleg, 145+self.__x-5, 175+self.__y, 160+self.__x-5, 183+self.__y) #(+5,-5), (+5,-5)
                    canvas.coords(self.a_Lleg, 115+self.__x+5, 175+self.__y, 130+self.__x+5, 183+self.__y) #(-5,-5), (-5,-5)
                    canvas.coords(self.a_bandana1, 145+self.__x-14, 150+self.__y, 170+self.__x-64, 150+self.__y, 170+self.__x-64, 160+self.__y) #(+20,10) for all bandana
                    canvas.coords(self.a_bandana2, 145+self.__x-14, 150+self.__y, 140+self.__x-4, 152+self.__y, 140+self.__x-4, 160+self.__y)
                    canvas.coords(self.a_bandana3, 145+self.__x-14, 150+self.__y, 140+self.__x-4, 148+self.__y, 140+self.__x-4, 151+self.__y) 
                    canvas.coords(self.a_vneck, 140+self.__x-4, 150+self.__y, 145+self.__x-14, 163+self.__y, 125+self.__x+26, 170+self.__y, 115+self.__x+46, 160+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                    canvas.coords(self.a_coat, 142+self.__x-8, 145+self.__y, 152+self.__x-28, 155+self.__y, 85+self.__x+76, 183+self.__y, 80+self.__x+104, 183+self.__y, 125+self.__x+26, 155+self.__y)
                    canvas.update()
                    self.__Frame = 1
                
            elif self.__Frame == 1 and self.__sprint == False and self.__crouch == True and self.__looking == "Left": #Moving left CROUCHING FRAME #2
                for count in range(90):
                    self.__y += 1
                    canvas.coords(self.a_head, 145+self.__x-40, 135+2+self.__y, 170+self.__x-40, 160+2+self.__y) #(+20, +10) difference from walking
                    canvas.coords(self.a_name, 138+self.__x, 110+self.__y)
                    canvas.coords(self.a_torso, 140+self.__x-4, 150+2+self.__y, 150+self.__x-24, 160+2+self.__y, 125+self.__x+26, 170+2+self.__y, 115+self.__x+46, 160+2+self.__y) #(20, 10), (5,10)
                    canvas.coords(self.a_Larm, 130+self.__x-10, 160+2+self.__y, 145+self.__x-10, 175+2+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                    canvas.coords(self.a_Rarm, 130+self.__x-10, 160+2+self.__y, 145+self.__x-10, 175+2+self.__y) #Arm hides behind torso (+30,0)
                    canvas.coords(self.a_Rleg, 145+self.__x-10, 175+self.__y, 160+self.__x-10, 183+self.__y)
                    canvas.coords(self.a_Lleg, 115+self.__x+10, 175+self.__y, 130+self.__x+10, 183+self.__y)
                    canvas.coords(self.a_bandana1, 145+self.__x-14, 150+2+self.__y, 170+self.__x-64, 150+2+self.__y, 170+self.__x-64, 160+2+self.__y) #(+20,10) for all bandana
                    canvas.coords(self.a_bandana2, 145+self.__x-14, 150+2+self.__y, 140+self.__x-4, 152+2+self.__y, 140+self.__x-4, 160+2+self.__y)
                    canvas.coords(self.a_bandana3, 145+self.__x-14, 150+2+self.__y, 140+self.__x-4, 148+2+self.__y, 140+self.__x-4, 151+2+self.__y) 
                    canvas.coords(self.a_vneck, 140+self.__x-4, 150+2+self.__y, 145+self.__x-14, 163+2+self.__y, 125+self.__x+26, 170+2+self.__y, 115+self.__x+46, 160+2+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                    canvas.coords(self.a_coat, 142+self.__x-8, 145+2+self.__y, 152+self.__x-28, 155+2+self.__y, 85+self.__x+76, 183+2+self.__y, 80+self.__x+104, 183+2+self.__y, 125+self.__x+26, 155+2+self.__y)
                    canvas.update()
                    self.__Frame = 0
            #Moving Right
                    
            elif self.__Frame == 0 and self.__sprint == False and self.__crouch == False: #Moving right without sprinting or crouching FRAME #1
                for count in range(90):
                    self.__y += 1 #Arms and legs out self.__x 
                    canvas.coords(self.a_head, 125+self.__x, 125+self.__y, 150+self.__x, 150+self.__y)
                    canvas.coords(self.a_name, 138+self.__x, 110+self.__y)
                    canvas.coords(self.a_torso, 130+self.__x, 150+self.__y, 145+self.__x, 150+self.__y, 145+self.__x, 175+self.__y, 130+self.__x, 175+self.__y)
                    canvas.coords(self.a_Larm, 115+self.__x, 150+self.__y, 130+self.__x, 165+self.__y)
                    canvas.coords(self.a_Rarm, 145+self.__x, 150+self.__y, 160+self.__x, 165+self.__y)
                    canvas.coords(self.a_Rleg, 145+self.__x, 175+self.__y, 160+self.__x, 183+self.__y)
                    canvas.coords(self.a_Lleg, 115+self.__x, 175+self.__y, 130+self.__x, 183+self.__y)
                    canvas.coords(self.a_bandana1, 125+self.__x, 140+self.__y, 150+self.__x, 140+self.__y, 150+self.__x, 150+self.__y)
                    canvas.coords(self.a_bandana2, 125+self.__x, 140+self.__y, 120+self.__x, 142+self.__y, 120+self.__x, 145+self.__y)
                    canvas.coords(self.a_bandana3, 125+self.__x, 140+self.__y, 120+self.__x, 138+self.__y, 120+self.__x, 141+self.__y)
                    canvas.coords(self.a_vneck, 130+self.__x, 150+self.__y, 145+self.__x, 155+self.__y, 145+self.__x, 175+self.__y, 130+self.__x, 175+self.__y)
                    canvas.coords(self.a_coat, 130+self.__x, 145+self.__y, 142+self.__x, 145+self.__y, 135+self.__x, 175+self.__y, 115+self.__x, 177+self.__y, 130+self.__x, 160+self.__y)
                    canvas.update()
                    self.__Frame = 1
                
            elif self.__Frame == 1 and self.__sprint == False and self.__crouch == False: #Moving right without sprinting or crouching FRAME #2
                for count in range(90):
                    self.__y += 1
                    canvas.coords(self.a_head, 125+self.__x, 125+3+self.__y, 150+self.__x, 150+3+self.__y)
                    canvas.coords(self.a_name, 138+self.__x, 110+self.__y)
                    canvas.coords(self.a_torso, 130+self.__x, 150+3+self.__y, 145+self.__x, 150+3+self.__y, 145+self.__x, 175+3+self.__y, 130+self.__x, 175+3+self.__y)
                    canvas.coords(self.a_Larm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO
                    canvas.coords(self.a_Rarm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #Arm hides behind torso
                    canvas.coords(self.a_Rleg, 145+self.__x-10, 175+self.__y, 160+self.__x-10, 183+self.__y)
                    canvas.coords(self.a_Lleg, 115+self.__x+10, 175+self.__y, 130+self.__x+10, 183+self.__y)
                    canvas.coords(self.a_bandana1, 125+self.__x, 140+3+self.__y, 150+self.__x, 140+3+self.__y, 150+self.__x, 150+3+self.__y)
                    canvas.coords(self.a_bandana2, 125+self.__x, 140+3+self.__y, 120+self.__x, 142+3+self.__y, 120+self.__x, 145+3+self.__y)
                    canvas.coords(self.a_bandana3, 125+self.__x, 140+3+self.__y, 120+self.__x, 138+3+self.__y, 120+self.__x, 141+3+self.__y)
                    canvas.coords(self.a_vneck, 130+self.__x, 150+3+self.__y, 145+self.__x, 155+3+self.__y, 145+self.__x, 175+3+self.__y, 130+self.__x, 175+3+self.__y)
                    canvas.coords(self.a_coat, 130+self.__x, 145+3+self.__y, 142+self.__x, 145+3+self.__y, 135+self.__x, 175+3+self.__y, 115+self.__x, 177+6+self.__y, 130+self.__x, 160+self.__y)
                    canvas.update()
                    self.__Frame = 0

            elif self.__Frame == 0 and self.__sprint == True and self.__crouch == False: #Moving right SPRINTING FRAME #1
                for count in range(90):
                    self.__y += 1
                    canvas.coords(self.a_head, 145+self.__x, 135+self.__y, 170+self.__x, 160+self.__y) #(+20, +10) difference from walking
                    canvas.coords(self.a_name, 138+self.__x, 110+self.__y)
                    canvas.coords(self.a_torso, 140+self.__x, 150+self.__y, 150+self.__x, 160+self.__y, 125+self.__x, 170+self.__y, 115+self.__x, 160+self.__y) #(10, 0), (5,10), (-20,-5), (-15,-15)
                    canvas.coords(self.a_Larm, 85+self.__x, 150+self.__y, 100+self.__x, 165+self.__y) #(-30,0)
                    canvas.coords(self.a_Rarm, 175+self.__x, 150+self.__y, 190+self.__x, 165+self.__y) #(+30,0)
                    canvas.coords(self.a_Rleg, 150+self.__x, 170+self.__y, 165+self.__x, 178+self.__y) #(+5,-5), (+5,-5)
                    canvas.coords(self.a_Lleg, 110+self.__x, 170+self.__y, 125+self.__x, 178+self.__y) #(-5,-5), (-5,-5)
                    canvas.coords(self.a_bandana1, 145+self.__x, 150+self.__y, 170+self.__x, 150+self.__y, 170+self.__x, 160+self.__y) #(+20,10) for all bandana
                    canvas.coords(self.a_bandana2, 145+self.__x, 150+self.__y, 140+self.__x, 152+self.__y, 140+self.__x, 160+self.__y)
                    canvas.coords(self.a_bandana3, 145+self.__x, 150+self.__y, 140+self.__x, 148+self.__y, 140+self.__x, 151+self.__y) 
                    canvas.coords(self.a_vneck, 140+self.__x, 150+self.__y, 145+self.__x, 163+self.__y, 125+self.__x, 170+self.__y, 115+self.__x, 160+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                    canvas.coords(self.a_coat, 142+self.__x, 145+self.__y, 152+self.__x, 155+self.__y, 100+self.__x, 175+self.__y, 85+self.__x, 157+self.__y, 125+self.__x, 155+self.__y)
                    canvas.update()
                    self.__Frame = 1
                
            elif self.__Frame == 1 and self.__sprint == True and self.__crouch == False: #Moving right SPRINTING FRAME #2
                for count in range(90):
                    self.__y += 1
                    canvas.coords(self.a_head, 145+self.__x, 135+5+self.__y, 170+self.__x, 160+5+self.__y) #(+20, +10) difference from walking
                    canvas.coords(self.a_name, 138+self.__x, 110+self.__y)
                    canvas.coords(self.a_torso, 140+self.__x, 150+5+self.__y, 150+self.__x, 160+5+self.__y, 125+self.__x, 170+5+self.__y, 115+self.__x, 160+5+self.__y) #(20, 10), (5,10)
                    canvas.coords(self.a_Larm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                    canvas.coords(self.a_Rarm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #Arm hides behind torso (+30,0)
                    canvas.coords(self.a_Rleg, 145+self.__x-10, 175+self.__y, 160+self.__x-10, 183+self.__y)
                    canvas.coords(self.a_Lleg, 115+self.__x+10, 175+self.__y, 130+self.__x+10, 183+self.__y)
                    canvas.coords(self.a_bandana1, 145+self.__x, 150+5+self.__y, 170+self.__x, 150+5+self.__y, 170+self.__x, 160+5+self.__y) #(+20,10) for all bandana
                    canvas.coords(self.a_bandana2, 145+self.__x, 150+5+self.__y, 140+self.__x, 152+5+self.__y, 140+self.__x, 155+5+self.__y)
                    canvas.coords(self.a_bandana3, 145+self.__x, 150+5+self.__y, 140+self.__x, 148+5+self.__y, 140+self.__x, 151+5+self.__y)
                    canvas.coords(self.a_vneck, 140+self.__x, 150+5+self.__y, 145+self.__x, 163+5+self.__y, 125+self.__x, 170+5+self.__y, 115+self.__x, 160+5+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                    canvas.coords(self.a_coat, 142+self.__x, 145+5+self.__y, 152+self.__x, 155+5+self.__y, 100+self.__x, 175+10+self.__y, 85+self.__x, 157+10+self.__y, 125+self.__x, 155+5+self.__y)
                    canvas.update()
                    self.__Frame = 0

            elif self.__Frame == 0 and self.__sprint == False and self.__crouch == True: #Moving right CROUCHING FRAMe #1
                for count in range(90):
                    self.__y += 1
                    canvas.coords(self.a_head, 145+self.__x, 135+self.__y, 170+self.__x, 160+self.__y) #(+20, +10) difference from walking
                    canvas.coords(self.a_name, 138+self.__x, 110+self.__y)
                    canvas.coords(self.a_torso, 140+self.__x, 150+self.__y, 150+self.__x, 160+self.__y, 125+self.__x, 170+self.__y, 115+self.__x, 160+self.__y) #(10, 0), (5,10), (-20,-5), (-15,-15)
                    canvas.coords(self.a_Larm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                    canvas.coords(self.a_Rarm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #Arm hides behind torso (+30,0)
                    canvas.coords(self.a_Rleg, 145+self.__x-5, 175+self.__y, 160+self.__x-5, 183+self.__y) #(+5,-5), (+5,-5)
                    canvas.coords(self.a_Lleg, 115+self.__x+5, 175+self.__y, 130+self.__x+5, 183+self.__y) #(-5,-5), (-5,-5)
                    canvas.coords(self.a_bandana1, 145+self.__x, 150+self.__y, 170+self.__x, 150+self.__y, 170+self.__x, 160+self.__y) #(+20,10) for all bandana
                    canvas.coords(self.a_bandana2, 145+self.__x, 150+self.__y, 140+self.__x, 152+self.__y, 140+self.__x, 160+self.__y)
                    canvas.coords(self.a_bandana3, 145+self.__x, 150+self.__y, 140+self.__x, 148+self.__y, 140+self.__x, 151+self.__y) 
                    canvas.coords(self.a_vneck, 140+self.__x, 150+self.__y, 145+self.__x, 163+self.__y, 125+self.__x, 170+self.__y, 115+self.__x, 160+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                    canvas.coords(self.a_coat, 142+self.__x, 145+self.__y, 152+self.__x, 155+self.__y, 115+self.__x, 183+self.__y, 92+self.__x, 183+self.__y, 125+self.__x, 155+self.__y)
                    canvas.update()
                    self.__Frame = 1
                
            elif self.__Frame == 1 and self.__sprint == False and self.__crouch == True: #Moving right CROUCHING FRAMe #2
                for count in range(90):
                    self.__y += 1
                    canvas.coords(self.a_head, 145+self.__x, 135+2+self.__y, 170+self.__x, 160+2+self.__y) #(+20, +10) difference from walking
                    canvas.coords(self.a_name, 138+self.__x, 110+self.__y)
                    canvas.coords(self.a_torso, 140+self.__x, 150+2+self.__y, 150+self.__x, 160+2+self.__y, 125+self.__x, 170+2+self.__y, 115+self.__x, 160+2+self.__y) #(20, 10), (5,10)
                    canvas.coords(self.a_Larm, 130+self.__x+10, 160+2+self.__y, 145+self.__x+10, 175+2+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                    canvas.coords(self.a_Rarm, 130+self.__x+10, 160+2+self.__y, 145+self.__x+10, 175+2+self.__y) #Arm hides behind torso (+30,0)
                    canvas.coords(self.a_Rleg, 145+self.__x-10, 175+self.__y, 160+self.__x-10, 183+self.__y)
                    canvas.coords(self.a_Lleg, 115+self.__x+10, 175+self.__y, 130+self.__x+10, 183+self.__y)
                    canvas.coords(self.a_bandana1, 145+self.__x, 150+2+self.__y, 170+self.__x, 150+2+self.__y, 170+self.__x, 160+2+self.__y) #(+20,10) for all bandana
                    canvas.coords(self.a_bandana2, 145+self.__x, 150+2+self.__y, 140+self.__x, 152+2+self.__y, 140+self.__x, 155+2+self.__y)
                    canvas.coords(self.a_bandana3, 145+self.__x, 150+2+self.__y, 140+self.__x, 148+2+self.__y, 140+self.__x, 151+2+self.__y)
                    canvas.coords(self.a_vneck, 140+self.__x, 150+2+self.__y, 145+self.__x, 163+2+self.__y, 125+self.__x, 170+2+self.__y, 115+self.__x, 160+2+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                    canvas.coords(self.a_coat, 142+self.__x, 145+2+self.__y, 152+self.__x, 155+2+self.__y, 115+self.__x, 183+2+self.__y, 92+self.__x, 183+2+self.__y, 125+self.__x, 155+2+self.__y)
                    canvas.update()
                    self.__Frame = 0
            
            canvas.after(100, rebindS) #2000 ms = 2 seconds Later will need to redo this part because not all falling is going to be 2 seconds long.
            
        def rebindS(): #Rebinds S (falling should be done and can fall again)
            self.__b_s = canvas.bind("<s>", sKey)
            print("Rebinding 's' and making inAir=False")
            self.__inAir=False
        
        def wKey(event): #Jump
            print("'w' key pressed")
            print("Making inAir equal True")
            self.__inAir = True
            print("Disabling 'w' binding") #Makes sure the user does not spam this animation DURING the animation.
            canvas.unbind("<w>", self.__b_w)

            if self.__voiceOn == True:
                canvas.delete(self.__a_VoR1, self.__a_VoR2, self.__a_VoR3)
                self.__voiceOn = False
            
            if self.__Frame == 0 and self.__sprint == False and self.__crouch == False and self.__looking == "Left": #Moving left without sprint or crouch FRAME #1
                for count in range(90):
                    self.__y -= 1
                    canvas.coords(self.a_head, 125+self.__x, 125+self.__y, 150+self.__x, 150+self.__y)
                    canvas.coords(self.a_name, 138+self.__x, 110+self.__y)
                    canvas.coords(self.a_torso, 130+self.__x, 150+self.__y, 145+self.__x, 150+self.__y, 145+self.__x, 175+self.__y, 130+self.__x, 175+self.__y)
                    canvas.coords(self.a_Larm, 115+self.__x, 150+self.__y, 130+self.__x, 165+self.__y)
                    canvas.coords(self.a_Rarm, 145+self.__x, 150+self.__y, 160+self.__x, 165+self.__y)
                    canvas.coords(self.a_Rleg, 145+self.__x, 175+self.__y, 160+self.__x, 183+self.__y)
                    canvas.coords(self.a_Lleg, 115+self.__x, 175+self.__y, 130+self.__x, 183+self.__y)
                    canvas.coords(self.a_bandana1, 125+self.__x+25, 140+self.__y, 150+self.__x-25, 140+self.__y, 150+self.__x-25, 150+self.__y)
                    canvas.coords(self.a_bandana2, 125+self.__x+25, 140+self.__y, 120+self.__x+35, 142+self.__y, 120+self.__x+35, 145+self.__y)
                    canvas.coords(self.a_bandana3, 125+self.__x+25, 140+self.__y, 120+self.__x+35, 138+self.__y, 120+self.__x+35, 141+self.__y)
                    canvas.coords(self.a_vneck, 130+self.__x, 155+self.__y, 145+self.__x, 150+self.__y, 145+self.__x, 175+self.__y, 130+self.__x, 175+self.__y)
                    canvas.coords(self.a_coat, 145+self.__x, 145+self.__y, 133+self.__x, 145+self.__y, 140+self.__x, 175+self.__y, 160+self.__x, 177+self.__y, 145+self.__x, 160+self.__y)
                    canvas.update()
                    self.__Frame = 1
                
            elif self.__Frame == 1 and self.__sprint == False and self.__crouch == False and self.__looking == "Left": #Moving left without sprint or crouch FRAME #2
                for count in range(90):
                    self.__y -= 1
                    canvas.coords(self.a_head, 125+self.__x, 125+3+self.__y, 150+self.__x, 150+3+self.__y)
                    canvas.coords(self.a_name, 138+self.__x, 110+self.__y)
                    canvas.coords(self.a_torso, 130+self.__x, 150+3+self.__y, 145+self.__x, 150+3+self.__y, 145+self.__x, 175+3+self.__y, 130+self.__x, 175+3+self.__y)
                    canvas.coords(self.a_Larm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO
                    canvas.coords(self.a_Rarm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #Arm hides behind torso
                    canvas.coords(self.a_Rleg, 145+self.__x-10, 175+self.__y, 160+self.__x-10, 183+self.__y)
                    canvas.coords(self.a_Lleg, 115+self.__x+10, 175+self.__y, 130+self.__x+10, 183+self.__y)
                    canvas.coords(self.a_bandana1, 125+self.__x+25, 140+3+self.__y, 150+self.__x-25, 140+3+self.__y, 150+self.__x-25, 150+3+self.__y)
                    canvas.coords(self.a_bandana2, 125+self.__x+25, 140+3+self.__y, 120+self.__x+35, 142+3+self.__y, 120+self.__x+35, 145+3+self.__y)
                    canvas.coords(self.a_bandana3, 125+self.__x+25, 140+3+self.__y, 120+self.__x+35, 138+3+self.__y, 120+self.__x+35, 141+3+self.__y)
                    canvas.coords(self.a_vneck, 130+self.__x, 155+3+self.__y, 145+self.__x, 150+3+self.__y, 145+self.__x, 175+3+self.__y, 130+self.__x, 175+3+self.__y)
                    canvas.coords(self.a_coat, 145+self.__x, 145+3+self.__y, 133+self.__x, 145+3+self.__y, 140+self.__x, 175+3+self.__y, 160+self.__x, 177+6+self.__y, 145+self.__x, 160+3+self.__y)
                    canvas.update()
                    self.__Frame = 0

            elif self.__Frame == 0 and self.__sprint == True and self.__crouch == False and self.__looking == "Left": #Moving left SPRINTING FRAME #1
                for count in range(90):
                    self.__y -= 1
                    canvas.coords(self.a_head, 145+self.__x-40, 135+self.__y, 170+self.__x-40, 160+self.__y) #(+20, +10) difference from walking
                    canvas.coords(self.a_name, 138+self.__x, 110+self.__y)
                    canvas.coords(self.a_torso, 140+self.__x-4, 150+self.__y, 150+self.__x-24, 160+self.__y, 125+self.__x+26, 170+self.__y, 115+self.__x+46, 160+self.__y) #(10, 0), (5,10), (-20,-5), (-15,-15)
                    canvas.coords(self.a_Larm, 85+self.__x+106, 150+self.__y, 100+self.__x+76, 165+self.__y) #(-30,0)
                    canvas.coords(self.a_Rarm, 175+self.__x-74, 150+self.__y, 190+self.__x-104, 165+self.__y) #(+30,0)
                    canvas.coords(self.a_Rleg, 150+self.__x-24, 170+self.__y, 165+self.__x-54, 178+self.__y) #(+5,-5), (+5,-5)
                    canvas.coords(self.a_Lleg, 110+self.__x+56, 170+self.__y, 125+self.__x+26, 178+self.__y) #(-5,-5), (-5,-5)
                    canvas.coords(self.a_bandana1, 145+self.__x-14, 150+self.__y, 170+self.__x-64, 150+self.__y, 170+self.__x-64, 160+self.__y) #(+20,10) for all bandana
                    canvas.coords(self.a_bandana2, 145+self.__x-14, 150+self.__y, 140+self.__x-4, 152+self.__y, 140+self.__x-4, 160+self.__y)
                    canvas.coords(self.a_bandana3, 145+self.__x-14, 150+self.__y, 140+self.__x-4, 148+self.__y, 140+self.__x-4, 151+self.__y) 
                    canvas.coords(self.a_vneck, 140+self.__x-4, 150+self.__y, 145+self.__x-14, 163+self.__y, 125+self.__x+26, 170+self.__y, 115+self.__x+46, 160+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                    canvas.coords(self.a_coat, 142+self.__x-8, 145+self.__y, 152+self.__x-28, 155+self.__y, 100+self.__x+76, 175+self.__y, 85+self.__x+104, 157+self.__y, 125+self.__x+26, 155+self.__y)
                    canvas.update()
                    self.__Frame = 1
                
            elif self.__Frame == 1 and self.__sprint == True and self.__crouch == False and self.__looking == "Left": #Moving left SPRINTING FRAME #2
                for count in range(90):
                    self.__y -= 1
                    canvas.coords(self.a_head, 145+self.__x-40, 135+5+self.__y, 170+self.__x-40, 160+5+self.__y) #(+20, +10) difference from walking
                    canvas.coords(self.a_name, 138+self.__x, 110+self.__y)
                    canvas.coords(self.a_torso, 140+self.__x-4, 150+5+self.__y, 150+self.__x-24, 160+5+self.__y, 125+self.__x+26, 170+5+self.__y, 115+self.__x+46, 160+5+self.__y) #(20, 10), (5,10)
                    canvas.coords(self.a_Larm, 130+self.__x+16, 160+self.__y, 145+self.__x-14, 175+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                    canvas.coords(self.a_Rarm, 130+self.__x+16, 160+self.__y, 145+self.__x-14, 175+self.__y) #Arm hides behind torso (+30,0)
                    canvas.coords(self.a_Rleg, 145+self.__x-10, 175+self.__y, 160+self.__x-10, 183+self.__y)
                    canvas.coords(self.a_Lleg, 115+self.__x+10, 175+self.__y, 130+self.__x+10, 183+self.__y)
                    canvas.coords(self.a_bandana1, 145+self.__x-14, 150+5+self.__y, 170+self.__x-64, 150+5+self.__y, 170+self.__x-64, 160+5+self.__y) #(+20,10) for all bandana
                    canvas.coords(self.a_bandana2, 145+self.__x-14, 150+5+self.__y, 140+self.__x-4, 152+5+self.__y, 140+self.__x-4, 160+5+self.__y)
                    canvas.coords(self.a_bandana3, 145+self.__x-14, 150+5+self.__y, 140+self.__x-4, 148+5+self.__y, 140+self.__x-4, 151+5+self.__y) 
                    canvas.coords(self.a_vneck, 140+self.__x-4, 150+5+self.__y, 145+self.__x-14, 163+5+self.__y, 125+self.__x+26, 170+5+self.__y, 115+self.__x+46, 160+5+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                    canvas.coords(self.a_coat, 142+self.__x-8, 145+5+self.__y, 152+self.__x-28, 155+5+self.__y, 100+self.__x+76, 175+10+self.__y, 85+self.__x+104, 157+10+self.__y, 125+self.__x+26, 155+5+self.__y)
                    canvas.update()
                    self.__Frame = 0

            elif self.__Frame == 0 and self.__sprint == False and self.__crouch == True and self.__looking == "Left": #Moving left CROUCHING FRAME #1
                for count in range(90):
                    self.__y -= 1
                    canvas.coords(self.a_head, 145+self.__x-40, 135+self.__y, 170+self.__x-40, 160+self.__y) #(+20, +10) difference from walking
                    canvas.coords(self.a_name, 138+self.__x, 110+self.__y)
                    canvas.coords(self.a_torso, 140+self.__x-4, 150+self.__y, 150+self.__x-24, 160+self.__y, 125+self.__x+26, 170+self.__y, 115+self.__x+46, 160+self.__y) #(10, 0), (5,10), (-20,-5), (-15,-15)
                    canvas.coords(self.a_Larm, 130+self.__x+16, 160+self.__y, 145+self.__x-14, 175+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                    canvas.coords(self.a_Rarm, 130+self.__x+16, 160+self.__y, 145+self.__x-14, 175+self.__y) #Arm hides behind torso (+30,0)
                    canvas.coords(self.a_Rleg, 145+self.__x-5, 175+self.__y, 160+self.__x-5, 183+self.__y) #(+5,-5), (+5,-5)
                    canvas.coords(self.a_Lleg, 115+self.__x+5, 175+self.__y, 130+self.__x+5, 183+self.__y) #(-5,-5), (-5,-5)
                    canvas.coords(self.a_bandana1, 145+self.__x-14, 150+self.__y, 170+self.__x-64, 150+self.__y, 170+self.__x-64, 160+self.__y) #(+20,10) for all bandana
                    canvas.coords(self.a_bandana2, 145+self.__x-14, 150+self.__y, 140+self.__x-4, 152+self.__y, 140+self.__x-4, 160+self.__y)
                    canvas.coords(self.a_bandana3, 145+self.__x-14, 150+self.__y, 140+self.__x-4, 148+self.__y, 140+self.__x-4, 151+self.__y) 
                    canvas.coords(self.a_vneck, 140+self.__x-4, 150+self.__y, 145+self.__x-14, 163+self.__y, 125+self.__x+26, 170+self.__y, 115+self.__x+46, 160+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                    canvas.coords(self.a_coat, 142+self.__x-8, 145+self.__y, 152+self.__x-28, 155+self.__y, 85+self.__x+76, 183+self.__y, 80+self.__x+104, 183+self.__y, 125+self.__x+26, 155+self.__y)
                    canvas.update()
                    self.__Frame = 1
                
            elif self.__Frame == 1 and self.__sprint == False and self.__crouch == True and self.__looking == "Left": #Moving left CROUCHING FRAME #2
                for count in range(90):
                    self.__y -= 1
                    canvas.coords(self.a_head, 145+self.__x-40, 135+2+self.__y, 170+self.__x-40, 160+2+self.__y) #(+20, +10) difference from walking
                    canvas.coords(self.a_name, 138+self.__x, 110+self.__y)
                    canvas.coords(self.a_torso, 140+self.__x-4, 150+2+self.__y, 150+self.__x-24, 160+2+self.__y, 125+self.__x+26, 170+2+self.__y, 115+self.__x+46, 160+2+self.__y) #(20, 10), (5,10)
                    canvas.coords(self.a_Larm, 130+self.__x-10, 160+2+self.__y, 145+self.__x-10, 175+2+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                    canvas.coords(self.a_Rarm, 130+self.__x-10, 160+2+self.__y, 145+self.__x-10, 175+2+self.__y) #Arm hides behind torso (+30,0)
                    canvas.coords(self.a_Rleg, 145+self.__x-10, 175+self.__y, 160+self.__x-10, 183+self.__y)
                    canvas.coords(self.a_Lleg, 115+self.__x+10, 175+self.__y, 130+self.__x+10, 183+self.__y)
                    canvas.coords(self.a_bandana1, 145+self.__x-14, 150+2+self.__y, 170+self.__x-64, 150+2+self.__y, 170+self.__x-64, 160+2+self.__y) #(+20,10) for all bandana
                    canvas.coords(self.a_bandana2, 145+self.__x-14, 150+2+self.__y, 140+self.__x-4, 152+2+self.__y, 140+self.__x-4, 160+2+self.__y)
                    canvas.coords(self.a_bandana3, 145+self.__x-14, 150+2+self.__y, 140+self.__x-4, 148+2+self.__y, 140+self.__x-4, 151+2+self.__y) 
                    canvas.coords(self.a_vneck, 140+self.__x-4, 150+2+self.__y, 145+self.__x-14, 163+2+self.__y, 125+self.__x+26, 170+2+self.__y, 115+self.__x+46, 160+2+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                    canvas.coords(self.a_coat, 142+self.__x-8, 145+2+self.__y, 152+self.__x-28, 155+2+self.__y, 85+self.__x+76, 183+2+self.__y, 80+self.__x+104, 183+2+self.__y, 125+self.__x+26, 155+2+self.__y)
                    canvas.update()
                    self.__Frame = 0
            #Moving Right
                    
            elif self.__Frame == 0 and self.__sprint == False and self.__crouch == False: #Moving right without sprinting or crouching FRAME #1
                for count in range(90):
                    self.__y -= 1 #Arms and legs out self.__x 
                    canvas.coords(self.a_head, 125+self.__x, 125+self.__y, 150+self.__x, 150+self.__y)
                    canvas.coords(self.a_name, 138+self.__x, 110+self.__y)
                    canvas.coords(self.a_torso, 130+self.__x, 150+self.__y, 145+self.__x, 150+self.__y, 145+self.__x, 175+self.__y, 130+self.__x, 175+self.__y)
                    canvas.coords(self.a_Larm, 115+self.__x, 150+self.__y, 130+self.__x, 165+self.__y)
                    canvas.coords(self.a_Rarm, 145+self.__x, 150+self.__y, 160+self.__x, 165+self.__y)
                    canvas.coords(self.a_Rleg, 145+self.__x, 175+self.__y, 160+self.__x, 183+self.__y)
                    canvas.coords(self.a_Lleg, 115+self.__x, 175+self.__y, 130+self.__x, 183+self.__y)
                    canvas.coords(self.a_bandana1, 125+self.__x, 140+self.__y, 150+self.__x, 140+self.__y, 150+self.__x, 150+self.__y)
                    canvas.coords(self.a_bandana2, 125+self.__x, 140+self.__y, 120+self.__x, 142+self.__y, 120+self.__x, 145+self.__y)
                    canvas.coords(self.a_bandana3, 125+self.__x, 140+self.__y, 120+self.__x, 138+self.__y, 120+self.__x, 141+self.__y)
                    canvas.coords(self.a_vneck, 130+self.__x, 150+self.__y, 145+self.__x, 155+self.__y, 145+self.__x, 175+self.__y, 130+self.__x, 175+self.__y)
                    canvas.coords(self.a_coat, 130+self.__x, 145+self.__y, 142+self.__x, 145+self.__y, 135+self.__x, 175+self.__y, 115+self.__x, 177+self.__y, 130+self.__x, 160+self.__y)
                    canvas.update()
                    self.__Frame = 1
                
            elif self.__Frame == 1 and self.__sprint == False and self.__crouch == False: #Moving right without sprinting or crouching FRAME #2
                for count in range(90):
                    self.__y -= 1
                    canvas.coords(self.a_head, 125+self.__x, 125+3+self.__y, 150+self.__x, 150+3+self.__y)
                    canvas.coords(self.a_name, 138+self.__x, 110+self.__y)
                    canvas.coords(self.a_torso, 130+self.__x, 150+3+self.__y, 145+self.__x, 150+3+self.__y, 145+self.__x, 175+3+self.__y, 130+self.__x, 175+3+self.__y)
                    canvas.coords(self.a_Larm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO
                    canvas.coords(self.a_Rarm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #Arm hides behind torso
                    canvas.coords(self.a_Rleg, 145+self.__x-10, 175+self.__y, 160+self.__x-10, 183+self.__y)
                    canvas.coords(self.a_Lleg, 115+self.__x+10, 175+self.__y, 130+self.__x+10, 183+self.__y)
                    canvas.coords(self.a_bandana1, 125+self.__x, 140+3+self.__y, 150+self.__x, 140+3+self.__y, 150+self.__x, 150+3+self.__y)
                    canvas.coords(self.a_bandana2, 125+self.__x, 140+3+self.__y, 120+self.__x, 142+3+self.__y, 120+self.__x, 145+3+self.__y)
                    canvas.coords(self.a_bandana3, 125+self.__x, 140+3+self.__y, 120+self.__x, 138+3+self.__y, 120+self.__x, 141+3+self.__y)
                    canvas.coords(self.a_vneck, 130+self.__x, 150+3+self.__y, 145+self.__x, 155+3+self.__y, 145+self.__x, 175+3+self.__y, 130+self.__x, 175+3+self.__y)
                    canvas.coords(self.a_coat, 130+self.__x, 145+3+self.__y, 142+self.__x, 145+3+self.__y, 135+self.__x, 175+3+self.__y, 115+self.__x, 177+6+self.__y, 130+self.__x, 160+self.__y)
                    canvas.update()
                    self.__Frame = 0

            elif self.__Frame == 0 and self.__sprint == True and self.__crouch == False: #Moving right SPRINTING FRAME #1
                for count in range(90):
                    self.__y -= 1
                    canvas.coords(self.a_head, 145+self.__x, 135+self.__y, 170+self.__x, 160+self.__y) #(+20, +10) difference from walking
                    canvas.coords(self.a_name, 138+self.__x, 110+self.__y)
                    canvas.coords(self.a_torso, 140+self.__x, 150+self.__y, 150+self.__x, 160+self.__y, 125+self.__x, 170+self.__y, 115+self.__x, 160+self.__y) #(10, 0), (5,10), (-20,-5), (-15,-15)
                    canvas.coords(self.a_Larm, 85+self.__x, 150+self.__y, 100+self.__x, 165+self.__y) #(-30,0)
                    canvas.coords(self.a_Rarm, 175+self.__x, 150+self.__y, 190+self.__x, 165+self.__y) #(+30,0)
                    canvas.coords(self.a_Rleg, 150+self.__x, 170+self.__y, 165+self.__x, 178+self.__y) #(+5,-5), (+5,-5)
                    canvas.coords(self.a_Lleg, 110+self.__x, 170+self.__y, 125+self.__x, 178+self.__y) #(-5,-5), (-5,-5)
                    canvas.coords(self.a_bandana1, 145+self.__x, 150+self.__y, 170+self.__x, 150+self.__y, 170+self.__x, 160+self.__y) #(+20,10) for all bandana
                    canvas.coords(self.a_bandana2, 145+self.__x, 150+self.__y, 140+self.__x, 152+self.__y, 140+self.__x, 160+self.__y)
                    canvas.coords(self.a_bandana3, 145+self.__x, 150+self.__y, 140+self.__x, 148+self.__y, 140+self.__x, 151+self.__y) 
                    canvas.coords(self.a_vneck, 140+self.__x, 150+self.__y, 145+self.__x, 163+self.__y, 125+self.__x, 170+self.__y, 115+self.__x, 160+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                    canvas.coords(self.a_coat, 142+self.__x, 145+self.__y, 152+self.__x, 155+self.__y, 100+self.__x, 175+self.__y, 85+self.__x, 157+self.__y, 125+self.__x, 155+self.__y)
                    canvas.update()
                    self.__Frame = 1
                
            elif self.__Frame == 1 and self.__sprint == True and self.__crouch == False: #Moving right SPRINTING FRAME #2
                for count in range(90):
                    self.__y -= 1
                    canvas.coords(self.a_head, 145+self.__x, 135+5+self.__y, 170+self.__x, 160+5+self.__y) #(+20, +10) difference from walking
                    canvas.coords(self.a_name, 138+self.__x, 110+self.__y)
                    canvas.coords(self.a_torso, 140+self.__x, 150+5+self.__y, 150+self.__x, 160+5+self.__y, 125+self.__x, 170+5+self.__y, 115+self.__x, 160+5+self.__y) #(20, 10), (5,10)
                    canvas.coords(self.a_Larm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                    canvas.coords(self.a_Rarm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #Arm hides behind torso (+30,0)
                    canvas.coords(self.a_Rleg, 145+self.__x-10, 175+self.__y, 160+self.__x-10, 183+self.__y)
                    canvas.coords(self.a_Lleg, 115+self.__x+10, 175+self.__y, 130+self.__x+10, 183+self.__y)
                    canvas.coords(self.a_bandana1, 145+self.__x, 150+5+self.__y, 170+self.__x, 150+5+self.__y, 170+self.__x, 160+5+self.__y) #(+20,10) for all bandana
                    canvas.coords(self.a_bandana2, 145+self.__x, 150+5+self.__y, 140+self.__x, 152+5+self.__y, 140+self.__x, 155+5+self.__y)
                    canvas.coords(self.a_bandana3, 145+self.__x, 150+5+self.__y, 140+self.__x, 148+5+self.__y, 140+self.__x, 151+5+self.__y)
                    canvas.coords(self.a_vneck, 140+self.__x, 150+5+self.__y, 145+self.__x, 163+5+self.__y, 125+self.__x, 170+5+self.__y, 115+self.__x, 160+5+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                    canvas.coords(self.a_coat, 142+self.__x, 145+5+self.__y, 152+self.__x, 155+5+self.__y, 100+self.__x, 175+10+self.__y, 85+self.__x, 157+10+self.__y, 125+self.__x, 155+5+self.__y)
                    canvas.update()
                    self.__Frame = 0

            elif self.__Frame == 0 and self.__sprint == False and self.__crouch == True: #Moving right CROUCHING FRAMe #1
                for count in range(90):
                    self.__y -= 1
                    canvas.coords(self.a_head, 145+self.__x, 135+self.__y, 170+self.__x, 160+self.__y) #(+20, +10) difference from walking
                    canvas.coords(self.a_name, 138+self.__x, 110+self.__y)
                    canvas.coords(self.a_torso, 140+self.__x, 150+self.__y, 150+self.__x, 160+self.__y, 125+self.__x, 170+self.__y, 115+self.__x, 160+self.__y) #(10, 0), (5,10), (-20,-5), (-15,-15)
                    canvas.coords(self.a_Larm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                    canvas.coords(self.a_Rarm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #Arm hides behind torso (+30,0)
                    canvas.coords(self.a_Rleg, 145+self.__x-5, 175+self.__y, 160+self.__x-5, 183+self.__y) #(+5,-5), (+5,-5)
                    canvas.coords(self.a_Lleg, 115+self.__x+5, 175+self.__y, 130+self.__x+5, 183+self.__y) #(-5,-5), (-5,-5)
                    canvas.coords(self.a_bandana1, 145+self.__x, 150+self.__y, 170+self.__x, 150+self.__y, 170+self.__x, 160+self.__y) #(+20,10) for all bandana
                    canvas.coords(self.a_bandana2, 145+self.__x, 150+self.__y, 140+self.__x, 152+self.__y, 140+self.__x, 160+self.__y)
                    canvas.coords(self.a_bandana3, 145+self.__x, 150+self.__y, 140+self.__x, 148+self.__y, 140+self.__x, 151+self.__y) 
                    canvas.coords(self.a_vneck, 140+self.__x, 150+self.__y, 145+self.__x, 163+self.__y, 125+self.__x, 170+self.__y, 115+self.__x, 160+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                    canvas.coords(self.a_coat, 142+self.__x, 145+self.__y, 152+self.__x, 155+self.__y, 115+self.__x, 183+self.__y, 92+self.__x, 183+self.__y, 125+self.__x, 155+self.__y)
                    canvas.update()
                    self.__Frame = 1
                
            elif self.__Frame == 1 and self.__sprint == False and self.__crouch == True: #Moving right CROUCHING FRAMe #2
                for count in range(90):
                    self.__y -= 1
                    canvas.coords(self.a_head, 145+self.__x, 135+2+self.__y, 170+self.__x, 160+2+self.__y) #(+20, +10) difference from walking
                    canvas.coords(self.a_name, 138+self.__x, 110+self.__y)
                    canvas.coords(self.a_torso, 140+self.__x, 150+2+self.__y, 150+self.__x, 160+2+self.__y, 125+self.__x, 170+2+self.__y, 115+self.__x, 160+2+self.__y) #(20, 10), (5,10)
                    canvas.coords(self.a_Larm, 130+self.__x+10, 160+2+self.__y, 145+self.__x+10, 175+2+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                    canvas.coords(self.a_Rarm, 130+self.__x+10, 160+2+self.__y, 145+self.__x+10, 175+2+self.__y) #Arm hides behind torso (+30,0)
                    canvas.coords(self.a_Rleg, 145+self.__x-10, 175+self.__y, 160+self.__x-10, 183+self.__y)
                    canvas.coords(self.a_Lleg, 115+self.__x+10, 175+self.__y, 130+self.__x+10, 183+self.__y)
                    canvas.coords(self.a_bandana1, 145+self.__x, 150+2+self.__y, 170+self.__x, 150+2+self.__y, 170+self.__x, 160+2+self.__y) #(+20,10) for all bandana
                    canvas.coords(self.a_bandana2, 145+self.__x, 150+2+self.__y, 140+self.__x, 152+2+self.__y, 140+self.__x, 155+2+self.__y)
                    canvas.coords(self.a_bandana3, 145+self.__x, 150+2+self.__y, 140+self.__x, 148+2+self.__y, 140+self.__x, 151+2+self.__y)
                    canvas.coords(self.a_vneck, 140+self.__x, 150+2+self.__y, 145+self.__x, 163+2+self.__y, 125+self.__x, 170+2+self.__y, 115+self.__x, 160+2+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                    canvas.coords(self.a_coat, 142+self.__x, 145+2+self.__y, 152+self.__x, 155+2+self.__y, 115+self.__x, 183+2+self.__y, 92+self.__x, 183+2+self.__y, 125+self.__x, 155+2+self.__y)
                    canvas.update()
                    self.__Frame = 0
            
            canvas.after(100, rebindW) #2000 ms = 2 seconds Later will need to redo this part because not all falling is going to be 2 seconds long.
            
        def rebindW(): #Rebinds W (falling should be done and can fall again)
            self.__b_w = canvas.bind("<w>", wKey)
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

            if self.__voiceOn == True:
                canvas.delete(self.__a_VoR1, self.__a_VoR2, self.__a_VoR3)
                self.__voiceOn = False
            
            if self.__inAir == True:
                print("IN AIR A")
                return
            elif self.__Frame == 0 and self.__sprint == False and self.__crouch == False: #Moving left without sprint or crouch FRAME #1
                self.__x -= 1 #Arms and leg out
                canvas.coords(self.a_head, 125+self.__x, 125+self.__y, 150+self.__x, 150+self.__y)
                canvas.coords(self.a_name, 138+self.__x, 110+self.__y)
                canvas.coords(self.a_torso, 130+self.__x, 150+self.__y, 145+self.__x, 150+self.__y, 145+self.__x, 175+self.__y, 130+self.__x, 175+self.__y)
                canvas.coords(self.a_Larm, 115+self.__x, 150+self.__y, 130+self.__x, 165+self.__y)
                canvas.coords(self.a_Rarm, 145+self.__x, 150+self.__y, 160+self.__x, 165+self.__y)
                canvas.coords(self.a_Rleg, 145+self.__x, 175+self.__y, 160+self.__x, 183+self.__y)
                canvas.coords(self.a_Lleg, 115+self.__x, 175+self.__y, 130+self.__x, 183+self.__y)
                canvas.coords(self.a_bandana1, 125+self.__x+25, 140+self.__y, 150+self.__x-25, 140+self.__y, 150+self.__x-25, 150+self.__y)
                canvas.coords(self.a_bandana2, 125+self.__x+25, 140+self.__y, 120+self.__x+35, 142+self.__y, 120+self.__x+35, 145+self.__y)
                canvas.coords(self.a_bandana3, 125+self.__x+25, 140+self.__y, 120+self.__x+35, 138+self.__y, 120+self.__x+35, 141+self.__y)
                canvas.coords(self.a_vneck, 130+self.__x, 155+self.__y, 145+self.__x, 150+self.__y, 145+self.__x, 175+self.__y, 130+self.__x, 175+self.__y)
                canvas.coords(self.a_coat, 145+self.__x, 145+self.__y, 133+self.__x, 145+self.__y, 140+self.__x, 175+self.__y, 160+self.__x, 177+self.__y, 145+self.__x, 160+self.__y)
                self.__Frame = 1
                
            elif self.__Frame == 1 and self.__sprint == False and self.__crouch == False: #Moving left without sprint or crouch FRAME #2
                self.__x -= 1 #Arms and legs in
                canvas.coords(self.a_head, 125+self.__x, 125+3+self.__y, 150+self.__x, 150+3+self.__y)
                canvas.coords(self.a_name, 138+self.__x, 110+self.__y)
                canvas.coords(self.a_torso, 130+self.__x, 150+3+self.__y, 145+self.__x, 150+3+self.__y, 145+self.__x, 175+3+self.__y, 130+self.__x, 175+3+self.__y)
                canvas.coords(self.a_Larm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO
                canvas.coords(self.a_Rarm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #Arm hides behind torso
                canvas.coords(self.a_Rleg, 145+self.__x-10, 175+self.__y, 160+self.__x-10, 183+self.__y)
                canvas.coords(self.a_Lleg, 115+self.__x+10, 175+self.__y, 130+self.__x+10, 183+self.__y)
                canvas.coords(self.a_bandana1, 125+self.__x+25, 140+3+self.__y, 150+self.__x-25, 140+3+self.__y, 150+self.__x-25, 150+3+self.__y)
                canvas.coords(self.a_bandana2, 125+self.__x+25, 140+3+self.__y, 120+self.__x+35, 142+3+self.__y, 120+self.__x+35, 145+3+self.__y)
                canvas.coords(self.a_bandana3, 125+self.__x+25, 140+3+self.__y, 120+self.__x+35, 138+3+self.__y, 120+self.__x+35, 141+3+self.__y)
                canvas.coords(self.a_vneck, 130+self.__x, 155+3+self.__y, 145+self.__x, 150+3+self.__y, 145+self.__x, 175+3+self.__y, 130+self.__x, 175+3+self.__y)
                canvas.coords(self.a_coat, 145+self.__x, 145+3+self.__y, 133+self.__x, 145+3+self.__y, 140+self.__x, 175+3+self.__y, 160+self.__x, 177+6+self.__y, 145+self.__x, 160+3+self.__y)
                self.__Frame = 0

            elif self.__Frame == 0 and self.__sprint == True and self.__crouch == False: #Moving left SPRINTING FRAME #1
                self.__x -= 1 #Arms and legs out
                canvas.coords(self.a_head, 145+self.__x-40, 135+self.__y, 170+self.__x-40, 160+self.__y) #(+20, +10) difference from walking
                canvas.coords(self.a_name, 138+self.__x, 110+self.__y)
                canvas.coords(self.a_torso, 140+self.__x-4, 150+self.__y, 150+self.__x-24, 160+self.__y, 125+self.__x+26, 170+self.__y, 115+self.__x+46, 160+self.__y) #(10, 0), (5,10), (-20,-5), (-15,-15)
                canvas.coords(self.a_Larm, 85+self.__x+106, 150+self.__y, 100+self.__x+76, 165+self.__y) #(-30,0)
                canvas.coords(self.a_Rarm, 175+self.__x-74, 150+self.__y, 190+self.__x-104, 165+self.__y) #(+30,0)
                canvas.coords(self.a_Rleg, 150+self.__x-24, 170+self.__y, 165+self.__x-54, 178+self.__y) #(+5,-5), (+5,-5)
                canvas.coords(self.a_Lleg, 110+self.__x+56, 170+self.__y, 125+self.__x+26, 178+self.__y) #(-5,-5), (-5,-5)
                canvas.coords(self.a_bandana1, 145+self.__x-14, 150+self.__y, 170+self.__x-64, 150+self.__y, 170+self.__x-64, 160+self.__y) #(+20,10) for all bandana
                canvas.coords(self.a_bandana2, 145+self.__x-14, 150+self.__y, 140+self.__x-4, 152+self.__y, 140+self.__x-4, 160+self.__y)
                canvas.coords(self.a_bandana3, 145+self.__x-14, 150+self.__y, 140+self.__x-4, 148+self.__y, 140+self.__x-4, 151+self.__y) 
                canvas.coords(self.a_vneck, 140+self.__x-4, 150+self.__y, 145+self.__x-14, 163+self.__y, 125+self.__x+26, 170+self.__y, 115+self.__x+46, 160+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                canvas.coords(self.a_coat, 142+self.__x-8, 145+self.__y, 152+self.__x-28, 155+self.__y, 100+self.__x+76, 175+self.__y, 85+self.__x+104, 157+self.__y, 125+self.__x+26, 155+self.__y)
                self.__x -= 5
                #(12,0) (10,10), (-35,0), (-30,-20), (-5,-5)
                self.__Frame = 1
                
            elif self.__Frame == 1 and self.__sprint == True and self.__crouch == False: #Moving left SPRINTING FRAME #2
                self.__x -= 1 #Arms and legs in
                canvas.coords(self.a_head, 145+self.__x-40, 135+5+self.__y, 170+self.__x-40, 160+5+self.__y) #(+20, +10) difference from walking
                canvas.coords(self.a_name, 138+self.__x, 110+self.__y)
                canvas.coords(self.a_torso, 140+self.__x-4, 150+5+self.__y, 150+self.__x-24, 160+5+self.__y, 125+self.__x+26, 170+5+self.__y, 115+self.__x+46, 160+5+self.__y) #(20, 10), (5,10)
                canvas.coords(self.a_Larm, 130+self.__x+16, 160+self.__y, 145+self.__x-14, 175+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                canvas.coords(self.a_Rarm, 130+self.__x+16, 160+self.__y, 145+self.__x-14, 175+self.__y) #Arm hides behind torso (+30,0)
                canvas.coords(self.a_Rleg, 145+self.__x-10, 175+self.__y, 160+self.__x-10, 183+self.__y)
                canvas.coords(self.a_Lleg, 115+self.__x+10, 175+self.__y, 130+self.__x+10, 183+self.__y)
                canvas.coords(self.a_bandana1, 145+self.__x-14, 150+5+self.__y, 170+self.__x-64, 150+5+self.__y, 170+self.__x-64, 160+5+self.__y) #(+20,10) for all bandana
                canvas.coords(self.a_bandana2, 145+self.__x-14, 150+5+self.__y, 140+self.__x-4, 152+5+self.__y, 140+self.__x-4, 160+5+self.__y)
                canvas.coords(self.a_bandana3, 145+self.__x-14, 150+5+self.__y, 140+self.__x-4, 148+5+self.__y, 140+self.__x-4, 151+5+self.__y) 
                canvas.coords(self.a_vneck, 140+self.__x-4, 150+5+self.__y, 145+self.__x-14, 163+5+self.__y, 125+self.__x+26, 170+5+self.__y, 115+self.__x+46, 160+5+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                canvas.coords(self.a_coat, 142+self.__x-8, 145+5+self.__y, 152+self.__x-28, 155+5+self.__y, 100+self.__x+76, 175+10+self.__y, 85+self.__x+104, 157+10+self.__y, 125+self.__x+26, 155+5+self.__y)
                #(12,0) (10,10), (-35,0), (-30,-20), (-5,-5)
                self.__x -= 5
                self.__Frame = 0

            elif self.__Frame == 0 and self.__sprint == False and self.__crouch == True: #Moving left CROUCHING FRAME #1
                self.__x -= 0.5 #Arms and legs out self.__x 
                canvas.coords(self.a_head, 145+self.__x-40, 135+self.__y, 170+self.__x-40, 160+self.__y) #(+20, +10) difference from walking
                canvas.coords(self.a_name, 138+self.__x, 110+self.__y)
                canvas.coords(self.a_torso, 140+self.__x-4, 150+self.__y, 150+self.__x-24, 160+self.__y, 125+self.__x+26, 170+self.__y, 115+self.__x+46, 160+self.__y) #(10, 0), (5,10), (-20,-5), (-15,-15)
                canvas.coords(self.a_Larm, 130+self.__x+16, 160+self.__y, 145+self.__x-14, 175+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                canvas.coords(self.a_Rarm, 130+self.__x+16, 160+self.__y, 145+self.__x-14, 175+self.__y) #Arm hides behind torso (+30,0)
                canvas.coords(self.a_Rleg, 145+self.__x-5, 175+self.__y, 160+self.__x-5, 183+self.__y) #(+5,-5), (+5,-5)
                canvas.coords(self.a_Lleg, 115+self.__x+5, 175+self.__y, 130+self.__x+5, 183+self.__y) #(-5,-5), (-5,-5)
                canvas.coords(self.a_bandana1, 145+self.__x-14, 150+self.__y, 170+self.__x-64, 150+self.__y, 170+self.__x-64, 160+self.__y) #(+20,10) for all bandana
                canvas.coords(self.a_bandana2, 145+self.__x-14, 150+self.__y, 140+self.__x-4, 152+self.__y, 140+self.__x-4, 160+self.__y)
                canvas.coords(self.a_bandana3, 145+self.__x-14, 150+self.__y, 140+self.__x-4, 148+self.__y, 140+self.__x-4, 151+self.__y) 
                canvas.coords(self.a_vneck, 140+self.__x-4, 150+self.__y, 145+self.__x-14, 163+self.__y, 125+self.__x+26, 170+self.__y, 115+self.__x+46, 160+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                canvas.coords(self.a_coat, 142+self.__x-8, 145+self.__y, 152+self.__x-28, 155+self.__y, 85+self.__x+76, 183+self.__y, 80+self.__x+104, 183+self.__y, 125+self.__x+26, 155+self.__y)
                self.__Frame = 1
                
            elif self.__Frame == 1 and self.__sprint == False and self.__crouch == True: #Moving left CROUCHING FRAME #2
                self.__x -= 0.5 #Arms and legs in
                canvas.coords(self.a_head, 145+self.__x-40, 135+2+self.__y, 170+self.__x-40, 160+2+self.__y) #(+20, +10) difference from walking
                canvas.coords(self.a_name, 138+self.__x, 110+self.__y)
                canvas.coords(self.a_torso, 140+self.__x-4, 150+2+self.__y, 150+self.__x-24, 160+2+self.__y, 125+self.__x+26, 170+2+self.__y, 115+self.__x+46, 160+2+self.__y) #(20, 10), (5,10)
                canvas.coords(self.a_Larm, 130+self.__x-10, 160+2+self.__y, 145+self.__x-10, 175+2+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                canvas.coords(self.a_Rarm, 130+self.__x-10, 160+2+self.__y, 145+self.__x-10, 175+2+self.__y) #Arm hides behind torso (+30,0)
                canvas.coords(self.a_Rleg, 145+self.__x-10, 175+self.__y, 160+self.__x-10, 183+self.__y)
                canvas.coords(self.a_Lleg, 115+self.__x+10, 175+self.__y, 130+self.__x+10, 183+self.__y)
                canvas.coords(self.a_bandana1, 145+self.__x-14, 150+2+self.__y, 170+self.__x-64, 150+2+self.__y, 170+self.__x-64, 160+2+self.__y) #(+20,10) for all bandana
                canvas.coords(self.a_bandana2, 145+self.__x-14, 150+2+self.__y, 140+self.__x-4, 152+2+self.__y, 140+self.__x-4, 160+2+self.__y)
                canvas.coords(self.a_bandana3, 145+self.__x-14, 150+2+self.__y, 140+self.__x-4, 148+2+self.__y, 140+self.__x-4, 151+2+self.__y) 
                canvas.coords(self.a_vneck, 140+self.__x-4, 150+2+self.__y, 145+self.__x-14, 163+2+self.__y, 125+self.__x+26, 170+2+self.__y, 115+self.__x+46, 160+2+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                canvas.coords(self.a_coat, 142+self.__x-8, 145+2+self.__y, 152+self.__x-28, 155+2+self.__y, 85+self.__x+76, 183+2+self.__y, 80+self.__x+104, 183+2+self.__y, 125+self.__x+26, 155+2+self.__y)
                #(12,0) (10,10), (-35,0), (-30,-20), (-5,-5)
                self.__Frame = 0

            self.__looking = "Left"
            canvas.update()

        def dKey(event): #Move right
            print("'d' key pressed")

            if self.__voiceOn == True:
                canvas.delete(self.__a_VoR1, self.__a_VoR2, self.__a_VoR3)
                self.__voiceOn = False
                
            if self.__inAir == True:
                print("IN AIR D")
                self.__x += 1
                return
            elif self.__Frame == 0 and self.__sprint == False and self.__crouch == False: #Moving right without sprinting or crouching FRAME #1
                self.__x += 1 #Arms and legs out self.__x 
                canvas.coords(self.a_head, 125+self.__x, 125+self.__y, 150+self.__x, 150+self.__y)
                canvas.coords(self.a_name, 138+self.__x, 110+self.__y)
                canvas.coords(self.a_torso, 130+self.__x, 150+self.__y, 145+self.__x, 150+self.__y, 145+self.__x, 175+self.__y, 130+self.__x, 175+self.__y)
                canvas.coords(self.a_Larm, 115+self.__x, 150+self.__y, 130+self.__x, 165+self.__y)
                canvas.coords(self.a_Rarm, 145+self.__x, 150+self.__y, 160+self.__x, 165+self.__y)
                canvas.coords(self.a_Rleg, 145+self.__x, 175+self.__y, 160+self.__x, 183+self.__y)
                canvas.coords(self.a_Lleg, 115+self.__x, 175+self.__y, 130+self.__x, 183+self.__y)
                canvas.coords(self.a_bandana1, 125+self.__x, 140+self.__y, 150+self.__x, 140+self.__y, 150+self.__x, 150+self.__y)
                canvas.coords(self.a_bandana2, 125+self.__x, 140+self.__y, 120+self.__x, 142+self.__y, 120+self.__x, 145+self.__y)
                canvas.coords(self.a_bandana3, 125+self.__x, 140+self.__y, 120+self.__x, 138+self.__y, 120+self.__x, 141+self.__y)
                canvas.coords(self.a_vneck, 130+self.__x, 150+self.__y, 145+self.__x, 155+self.__y, 145+self.__x, 175+self.__y, 130+self.__x, 175+self.__y)
                canvas.coords(self.a_coat, 130+self.__x, 145+self.__y, 142+self.__x, 145+self.__y, 135+self.__x, 175+self.__y, 115+self.__x, 177+self.__y, 130+self.__x, 160+self.__y)
                self.__Frame = 1
                
            elif self.__Frame == 1 and self.__sprint == False and self.__crouch == False: #Moving right without sprinting or crouching FRAME #2
                self.__x += 1 #Arms and legs in
                canvas.coords(self.a_head, 125+self.__x, 125+3+self.__y, 150+self.__x, 150+3+self.__y)
                canvas.coords(self.a_name, 138+self.__x, 110+self.__y)
                canvas.coords(self.a_torso, 130+self.__x, 150+3+self.__y, 145+self.__x, 150+3+self.__y, 145+self.__x, 175+3+self.__y, 130+self.__x, 175+3+self.__y)
                canvas.coords(self.a_Larm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO
                canvas.coords(self.a_Rarm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #Arm hides behind torso
                canvas.coords(self.a_Rleg, 145+self.__x-10, 175+self.__y, 160+self.__x-10, 183+self.__y)
                canvas.coords(self.a_Lleg, 115+self.__x+10, 175+self.__y, 130+self.__x+10, 183+self.__y)
                canvas.coords(self.a_bandana1, 125+self.__x, 140+3+self.__y, 150+self.__x, 140+3+self.__y, 150+self.__x, 150+3+self.__y)
                canvas.coords(self.a_bandana2, 125+self.__x, 140+3+self.__y, 120+self.__x, 142+3+self.__y, 120+self.__x, 145+3+self.__y)
                canvas.coords(self.a_bandana3, 125+self.__x, 140+3+self.__y, 120+self.__x, 138+3+self.__y, 120+self.__x, 141+3+self.__y)
                canvas.coords(self.a_vneck, 130+self.__x, 150+3+self.__y, 145+self.__x, 155+3+self.__y, 145+self.__x, 175+3+self.__y, 130+self.__x, 175+3+self.__y)
                canvas.coords(self.a_coat, 130+self.__x, 145+3+self.__y, 142+self.__x, 145+3+self.__y, 135+self.__x, 175+3+self.__y, 115+self.__x, 177+6+self.__y, 130+self.__x, 160+self.__y)
                self.__Frame = 0

            elif self.__Frame == 0 and self.__sprint == True and self.__crouch == False: #Moving right SPRINTING FRAME #1
                self.__x += 1 #Arms and legs out
                canvas.coords(self.a_head, 145+self.__x, 135+self.__y, 170+self.__x, 160+self.__y) #(+20, +10) difference from walking
                canvas.coords(self.a_name, 138+self.__x, 110+self.__y)
                canvas.coords(self.a_torso, 140+self.__x, 150+self.__y, 150+self.__x, 160+self.__y, 125+self.__x, 170+self.__y, 115+self.__x, 160+self.__y) #(10, 0), (5,10), (-20,-5), (-15,-15)
                canvas.coords(self.a_Larm, 85+self.__x, 150+self.__y, 100+self.__x, 165+self.__y) #(-30,0)
                canvas.coords(self.a_Rarm, 175+self.__x, 150+self.__y, 190+self.__x, 165+self.__y) #(+30,0)
                canvas.coords(self.a_Rleg, 150+self.__x, 170+self.__y, 165+self.__x, 178+self.__y) #(+5,-5), (+5,-5)
                canvas.coords(self.a_Lleg, 110+self.__x, 170+self.__y, 125+self.__x, 178+self.__y) #(-5,-5), (-5,-5)
                canvas.coords(self.a_bandana1, 145+self.__x, 150+self.__y, 170+self.__x, 150+self.__y, 170+self.__x, 160+self.__y) #(+20,10) for all bandana
                canvas.coords(self.a_bandana2, 145+self.__x, 150+self.__y, 140+self.__x, 152+self.__y, 140+self.__x, 160+self.__y)
                canvas.coords(self.a_bandana3, 145+self.__x, 150+self.__y, 140+self.__x, 148+self.__y, 140+self.__x, 151+self.__y) 
                canvas.coords(self.a_vneck, 140+self.__x, 150+self.__y, 145+self.__x, 163+self.__y, 125+self.__x, 170+self.__y, 115+self.__x, 160+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                canvas.coords(self.a_coat, 142+self.__x, 145+self.__y, 152+self.__x, 155+self.__y, 100+self.__x, 175+self.__y, 85+self.__x, 157+self.__y, 125+self.__x, 155+self.__y)
                self.__x += 5
                #(12,0) (10,10), (-35,0), (-30,-20), (-5,-5)
                self.__Frame = 1
                
            elif self.__Frame == 1 and self.__sprint == True and self.__crouch == False: #Moving right SPRINTING FRAME #2
                self.__x += 1 #Arms and legs in
                canvas.coords(self.a_head, 145+self.__x, 135+5+self.__y, 170+self.__x, 160+5+self.__y) #(+20, +10) difference from walking
                canvas.coords(self.a_name, 138+self.__x, 110+self.__y)
                canvas.coords(self.a_torso, 140+self.__x, 150+5+self.__y, 150+self.__x, 160+5+self.__y, 125+self.__x, 170+5+self.__y, 115+self.__x, 160+5+self.__y) #(20, 10), (5,10)
                canvas.coords(self.a_Larm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                canvas.coords(self.a_Rarm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #Arm hides behind torso (+30,0)
                canvas.coords(self.a_Rleg, 145+self.__x-10, 175+self.__y, 160+self.__x-10, 183+self.__y)
                canvas.coords(self.a_Lleg, 115+self.__x+10, 175+self.__y, 130+self.__x+10, 183+self.__y)
                canvas.coords(self.a_bandana1, 145+self.__x, 150+5+self.__y, 170+self.__x, 150+5+self.__y, 170+self.__x, 160+5+self.__y) #(+20,10) for all bandana
                canvas.coords(self.a_bandana2, 145+self.__x, 150+5+self.__y, 140+self.__x, 152+5+self.__y, 140+self.__x, 155+5+self.__y)
                canvas.coords(self.a_bandana3, 145+self.__x, 150+5+self.__y, 140+self.__x, 148+5+self.__y, 140+self.__x, 151+5+self.__y)
                canvas.coords(self.a_vneck, 140+self.__x, 150+5+self.__y, 145+self.__x, 163+5+self.__y, 125+self.__x, 170+5+self.__y, 115+self.__x, 160+5+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                canvas.coords(self.a_coat, 142+self.__x, 145+5+self.__y, 152+self.__x, 155+5+self.__y, 100+self.__x, 175+10+self.__y, 85+self.__x, 157+10+self.__y, 125+self.__x, 155+5+self.__y)
                #(12,0) (10,10), (-35,0), (-30,-20), (-5,-5)
                self.__x += 5
                self.__Frame = 0

            elif self.__Frame == 0 and self.__sprint == False and self.__crouch == True: #Moving right CROUCHING FRAMe #1
                canvas.coords(self.a_head, 145+self.__x, 135+self.__y, 170+self.__x, 160+self.__y) #(+20, +10) difference from walking
                canvas.coords(self.a_name, 138+self.__x, 110+self.__y)
                canvas.coords(self.a_torso, 140+self.__x, 150+self.__y, 150+self.__x, 160+self.__y, 125+self.__x, 170+self.__y, 115+self.__x, 160+self.__y) #(10, 0), (5,10), (-20,-5), (-15,-15)
                canvas.coords(self.a_Larm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                canvas.coords(self.a_Rarm, 130+self.__x, 160+self.__y, 145+self.__x, 175+self.__y) #Arm hides behind torso (+30,0)
                canvas.coords(self.a_Rleg, 145+self.__x-5, 175+self.__y, 160+self.__x-5, 183+self.__y) #(+5,-5), (+5,-5)
                canvas.coords(self.a_Lleg, 115+self.__x+5, 175+self.__y, 130+self.__x+5, 183+self.__y) #(-5,-5), (-5,-5)
                canvas.coords(self.a_bandana1, 145+self.__x, 150+self.__y, 170+self.__x, 150+self.__y, 170+self.__x, 160+self.__y) #(+20,10) for all bandana
                canvas.coords(self.a_bandana2, 145+self.__x, 150+self.__y, 140+self.__x, 152+self.__y, 140+self.__x, 160+self.__y)
                canvas.coords(self.a_bandana3, 145+self.__x, 150+self.__y, 140+self.__x, 148+self.__y, 140+self.__x, 151+self.__y) 
                canvas.coords(self.a_vneck, 140+self.__x, 150+self.__y, 145+self.__x, 163+self.__y, 125+self.__x, 170+self.__y, 115+self.__x, 160+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                canvas.coords(self.a_coat, 142+self.__x, 145+self.__y, 152+self.__x, 155+self.__y, 115+self.__x, 183+self.__y, 92+self.__x, 183+self.__y, 125+self.__x, 155+self.__y)
                self.__Frame = 1
                
            elif self.__Frame == 1 and self.__sprint == False and self.__crouch == True: #Moving right CROUCHING FRAMe #2
                self.__x += 0.5 #Arms and legs in
                canvas.coords(self.a_head, 145+self.__x, 135+2+self.__y, 170+self.__x, 160+2+self.__y) #(+20, +10) difference from walking
                canvas.coords(self.a_name, 138+self.__x, 110+self.__y)
                canvas.coords(self.a_torso, 140+self.__x, 150+2+self.__y, 150+self.__x, 160+2+self.__y, 125+self.__x, 170+2+self.__y, 115+self.__x, 160+2+self.__y) #(20, 10), (5,10)
                canvas.coords(self.a_Larm, 130+self.__x+10, 160+2+self.__y, 145+self.__x+10, 175+2+self.__y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
                canvas.coords(self.a_Rarm, 130+self.__x+10, 160+2+self.__y, 145+self.__x+10, 175+2+self.__y) #Arm hides behind torso (+30,0)
                canvas.coords(self.a_Rleg, 145+self.__x-10, 175+self.__y, 160+self.__x-10, 183+self.__y)
                canvas.coords(self.a_Lleg, 115+self.__x+10, 175+self.__y, 130+self.__x+10, 183+self.__y)
                canvas.coords(self.a_bandana1, 145+self.__x, 150+2+self.__y, 170+self.__x, 150+2+self.__y, 170+self.__x, 160+2+self.__y) #(+20,10) for all bandana
                canvas.coords(self.a_bandana2, 145+self.__x, 150+2+self.__y, 140+self.__x, 152+2+self.__y, 140+self.__x, 155+2+self.__y)
                canvas.coords(self.a_bandana3, 145+self.__x, 150+2+self.__y, 140+self.__x, 148+2+self.__y, 140+self.__x, 151+2+self.__y)
                canvas.coords(self.a_vneck, 140+self.__x, 150+2+self.__y, 145+self.__x, 163+2+self.__y, 125+self.__x, 170+2+self.__y, 115+self.__x, 160+2+self.__y) #(10,0), (0,8), (-20,-5), (-15,-15)
                canvas.coords(self.a_coat, 142+self.__x, 145+2+self.__y, 152+self.__x, 155+2+self.__y, 115+self.__x, 183+2+self.__y, 92+self.__x, 183+2+self.__y, 125+self.__x, 155+2+self.__y)
                self.__Frame = 0

            self.__looking = "Right"
            canvas.update()


        def shiftKey(event): #Sprint/Walk toggle
            print("'Shift' key pressed")

            if self.__voiceOn == True:
                canvas.delete(self.__a_VoR1, self.__a_VoR2, self.__a_VoR3)
                self.__voiceOn = False
            
            if self.__sprint == True and self.__crouch == False:
                self.__sprint = False
            elif self.__sprint == False and self.__crouch == False:
                self.__sprint = True
            else:
                print("Cannot toggle sprint! Must be out of crouch!")

        def ctrlKey(event): #crouch
            print("'Control' key pressed")

            if self.__voiceOn == True:
                canvas.delete(self.__a_VoR1, self.__a_VoR2, self.__a_VoR3)
                self.__voiceOn = False
            
            if self.__crouch == True and self.__sprint == False:
                self.__crouch = False
            elif self.__crouch == False and self.__sprint == False:
                self.__crouch = True
            else:
                print("Cannot toggle crouch! Must be out of sprint!")
        
        self.canvas = canvas
        #Creating the model of player 1 w/ label above it's head
        #Character is walking to the right of the screen
        #Name of the character
        self.a_name = canvas.create_text(138, 110, text="Gust", width=1000, fill="green", anchor="center", font=("Fixedsys", 16))

        #Creates the head of character
        self.a_head = canvas.create_oval(125, 125, 150, 150, fill="white")

        #HIS RIGHT ARM ANIMATIONS NEEDS TO BE BEHIND TORSO BC IT WOULD SHOW
        self.a_Rarm = canvas.create_oval(130, 160, 145, 175, fill="white")
        
        #Torso
        self.a_torso = canvas.create_polygon(130, 150, 145, 150, 145, 175, 130, 175, fill="white", outline="black")

        #HIS right leg (FRONT LEG)
        self.a_Rleg = canvas.create_oval(135, 175, 150, 183, fill="saddle brown")

        #HIS left leg (BACK LEG)
        self.a_Lleg = canvas.create_oval(125, 175, 140, 183, fill="saddle brown")

        #Bandana
        self.a_bandana1 = canvas.create_polygon(125, 140, 150, 140, 150, 150, fill="black") #Creates a polyon (triangle). Main part of banadana
        self.a_bandana2 = canvas.create_polygon(125, 140, 120, 142, 120, 145, fill="black") #Knot down
        self.a_bandana3 = canvas.create_polygon(125, 140, 120, 138, 120, 141, fill="black") #Knot up

        #V-neck
        self.a_vneck = canvas.create_polygon(130, 150, 145, 155, 145, 175, 130, 175, fill="dark blue")
        
        #Coat
        self.a_coat = canvas.create_polygon(130, 145, 142, 145, 135, 175, 115, 177, 130, 160, fill="gray14")

        #HIS left arm PLACED HERE BC NEEDED FOR ANIMATION (BACK ARM)
        self.a_Larm = canvas.create_oval(130, 160, 145, 175, fill="white")

        #KEYBINDINGS
        self.__b_leftClick = canvas.bind("<Button-1>", leftClick) #bind.("<BUTTON_NAME>", function_call) #Functions way above
        self.__b_scroll = canvas.bind("<Button-2>", scroll)
        self.__b_rightClick = canvas.bind("<Button-3>", rightClick)
        self.__b_a = canvas.bind("<a>", aKey)
        self.__b_d = canvas.bind("<d>", dKey)
        self.__b_s = canvas.bind("<s>", sKey)
        self.__b_w = canvas.bind("<w>", wKey)
        self.__b_q = canvas.bind("<q>", qKey)
        self.__b_e = canvas.bind("<e>", eKey)
        self.__b_shiftR = canvas.bind("<Shift_R>", shiftKey)
        self.__b_shiftL = canvas.bind("<Shift_L>", shiftKey)
        self.__b_ctrlL = canvas.bind("<Control_L>", ctrlKey)
        self.__b_ctrlR = canvas.bind("<Control_R>", ctrlKey)
        self.__b_space = canvas.bind("<space>", spaceKey)
        canvas.focus_set() #Tells Python to use keyboard so left and right arrow keys work now

        #IDK HOW TO CREATE A BUTTON IN THE MAIN WINDOW WILL DO LATER
        #button1=Button(main_frame,text="Click Me")
        #button1.bind("<Button-1>",printName)
        #button1.pack()

background = Background(canvas)
sword = Sword(canvas)
player = Player(canvas)
tk.mainloop()
