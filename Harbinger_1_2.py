#This game will use animations with the tkinter and time classes.

from tkinter import *
import random
import time

voiceOn = False #When this is True, Voice class activates.
basic_attack = False #When this is True, basic attack animation activates and locks the player in the animation until it is over.

tk = Tk()
tk.title("Harbinger - Alpha 2.2: HP, MP, and Sprint Bars Update (and a bit of Movement)")
canvas = Canvas(width=1300, height=700, bg="SkyBlue1")
canvas.pack()
tk.update()


class Enemy2:
    def __init__(self,canvas):
        self.canvas = canvas
        #I need help creating an enemy. Could be anything, but I'd prefer something medieval.
        self.e1_name1 = canvas.create_text(790, 70, anchor="center", fill="red", text="Enemy2", font=("Fixedsys", 16))
        #self.e1_body1 = canvas.create_polygon(780,150 fill="red", outline="black")

        def draw(self):
            global voiceOn

class Enemy:
    def __init__(self,canvas):
        self.canvas = canvas

        #I need help creating an enemy. Could be anything, but I'd prefer something medieval.

        self.e1_name1 = canvas.create_text(750, 70, anchor="center", fill="red", text="Enemy1", font=("Fixedsys", 16))
        #shoulder
        self.e1_neck1 = canvas.create_polygon(758, 110, 730,120,780,120, fill="saddle brown")
        #body
        self.el_body1 = canvas.create_polygon(730,120,730,160,780,160,780,120,fill="saddle brown")
        #arms
        self.el_leftArm1 = canvas.create_polygon(730,120,710,140,710,160,730,140,fill="tan")
        self.el_rightArm1 = canvas.create_polygon(780, 120, 800, 140, 800, 160, 780, 140, fill="tan")
        #head
        self.el_head1 = canvas.create_oval(745, 80, 765, 120, fill="tan")
        #pants
        self.el_pants1= canvas.create_polygon(730,160,730,180,780,180,780,160,fill="dim grey")
        #hands
        self.el_leftHand1=canvas.create_oval(700,130,720,160,fill="tan")
        # feet
        self.el_leftFoot1 = canvas.create_oval(780, 165, 780, 175, fill="black")
        #cannon maybe future levels. Don't want to instant kill player in tutorial.
        #self.el_cannon1=canvas.create_oval(600,130,695,180, fill="grey")

        def draw(self):
            global voiceOn

class Sword: 
    def __init__(self,canvas):
        self.canvas = canvas
        #I need help creating designs with a crappy sword AND an OP sword. No animating. I'll do that.

        #Crappy sword
        self.s_name1 = canvas.create_text(500, 100, anchor="center", fill="green", text="Rusty Sword (Tier 0)", font=("Fixedsys", 16)) #The "s_" means sword for short.
        self.s_blade1 = canvas.create_polygon(493, 165, 498, 165, 498, 140, 500, 130, 502, 140, 502, 165, 507, 165, 507, 168, 502, 168, 502, 180, 498, 180, 498, 168, 493, 168, fill="gray50", outline="black") #Follow the format of naming please.

        #OP Sword
        self.s_name2 = canvas.create_text(1000, 100, anchor="center", fill="green", text="Sword Name2", font=("Fixedsys", 16)) 
        self.s_blade2 = canvas.create_polygon(995, 110, 1005, 110, 1005, 160, 995, 160, fill="silver", outline="black")

        #Don't mess with my eye.
        self.s_eyelid1 = canvas.create_oval(1155, 10, 1295, 100, fill="black")
        #self.s_eye1 = canvas.create_oval(1155, 20, 1295, 90, fill="white") #EYE OPEN
        self.s_eye1 = canvas.create_oval(1155, 55, 1295, 55, fill="white") #Eye closed
        self.s_pupil1 = canvas.create_oval(1213, 42, 1238, 68, fill="black")

        canvas.move(self.s_eyelid1, 0, -140)
        canvas.move(self.s_eye1, 0, -140)
        canvas.move(self.s_pupil1, 0, -140)
        
        self.x_eye1, self.y_eye1 = 0,0
        self.x_pupil1, self.y_pupil1 = 0,0
        self.x_eyelid1, self.y_eyelid1 = 0,0
        self.checker = -70
        self.checker2 = 0
        
    def drawEye(self):
        if self.checker >= -70 and self.checker < 0:
            if self.checker == -1:
                canvas.move(self.s_eye1, 0, 140)
                canvas.move(self.s_pupil1, 0, 140)
            self.checker += 1
            canvas.move(self.s_eyelid1, 0, 2)
            #print("if 0")
            #self.y_eyelid1 += 2 
            #canvas.coords(self.s_eyelid1, 1155, 10+self.y_eyelid1, 1295, 100+self.y_eyelid1)
        elif self.checker >= 0 and self.checker <= 25: #Opens eye
            self.y_eye1 += 1 #25
            self.checker += 1
            canvas.coords(self.s_eye1, 1155, 55-self.y_eye1, 1295, 55+self.y_eye1)
            #print("First if")
        elif self.checker > 25 and self.checker <= 85: #Eye blinks once and remains open
            self.y_eye1 -= 1 #-65+25 = -40
            self.checker += 1
            canvas.coords(self.s_eye1, 1155, 55-self.y_eye1, 1295, 55+self.y_eye1)
            #print("Second if")
        elif self.checker >= 86 and self.checker <= 100 and self.checker2 == 1: #Pupil moves down
            self.x_pupil1 += 2
            self.y_pupil1 += 1
            self.checker += 1
            canvas.coords(self.s_pupil1, 1213-self.x_pupil1, 42+self.y_pupil1, 1238-self.x_pupil1, 68+self.y_pupil1)
            #print("Third if")
        elif self.checker > 100 and self.checker <= 124 and self.checker2 == 1: #Pupil rests for a few seconds
            self.checker += 1
        elif self.checker > 124 and self.checker <= 140 and self.checker2 == 1: #Pupil moves back to middle
            #print("Fourth if")
            self.x_pupil1 -= 2
            self.y_pupil1 -= 1
            self.checker += 1
            canvas.coords(self.s_pupil1, 1213-self.x_pupil1, 42+self.y_pupil1, 1238-self.x_pupil1, 68+self.y_pupil1)
        elif self.checker >= 140 and self.checker <= 174: #Eye closes
            self.y_eye1 += 1
            self.checker += 1
            canvas.coords(self.s_eye1, 1155, 55-self.y_eye1, 1295, 55+self.y_eye1)
            #print("5 if")
        elif self.checker == 175: #Move pupil and the white in the eye out so only the eyelid is visible
            #print("6 if")
            self.checker += 1
            canvas.move(self.s_eye1, -100000, -100000)
            canvas.move(self.s_pupil1, -100000, -100000)
        elif self.checker >= 176 and self.checker < 246: #Shift eye upwards out of screen
            #print("7 if")
            self.checker += 1
            canvas.move(self.s_eyelid1, 0, -2)
            
        if self.checker2 <= 1:
            self.checker2 += 1
        else:               
            self.checker2 = 0

class Bars:
    def __init__(self,canvas):
        self.canvas = canvas
        self.h_hp = canvas.create_arc(1130-50, 610-50, 1145+50, 625+50, extent=359, style=ARC, fill="white")
        self.h_mp = canvas.create_arc(130, 160, 145, 175, extent=90, style=ARC, fill="green")

class Nathaniel2010: #Refernce to Heavy Rain's AVI 
    def __init__(self,canvas):
        self.canvas = canvas
        #self.n_glove = canvas.create_polyon(fill="black")
        #self.n_glasses = canvas.create_polygon(fill="black")

class Background:
    def __init__(self,canvas):
        self.canvas = canvas
        self.a_description = canvas.create_text(0, 550, text="""Update Alpha 2.2: Bars and Movement Update\n"""
                                                """Can toggle from sprint to crouching vise versa now. After you press the toggle for both keys, stance now changes."""
                                                  """"""
                                                """\nMight change basic attacks while sprinting and/or crouching to have a different animation."""
                                                """\n"""
                                                  """ \n""",
                                                  width=1000, fill="black", anchor="nw", font=("Fixedsys", 16))#Top left corner of screen text
        self.a_description2 = canvas.create_text(0, 0, text="""WASD to move around. Press left Shift to toggle sprint. Press left Control to toggle crouch.\n"""
                                                                 """Cannot crouch stance while in sprint stance. Vise versa. Click on other window to view details.\n"""
                                                                 """Spacebar is the special ability that has a cooldown. Only Voice Attack is avaliable.""",
                                                 width=1000, fill="black", anchor="nw", font=("Fixedsys", 16))#Top left corner of screen text)
        #Creating ground1
        self.a_ground1 = canvas.create_rectangle(0,183,1500,190, outline="black",fill="green")

        #Creating ground2
        self.a_ground2 = canvas.create_rectangle(0,273,1500,280, outline="black",fill="green")

        #Creating lava pool to test hitboxes when implemented.
        self.a_lava1 = canvas.create_rectangle(0,273,100,280, outline="black",fill="red")

class Voice():
    def __init__(self,canvas,player):
        self.canvas = canvas
        self.player = player

        self.x, self.y = 0,0
        self.vLooking = ""
        self.counter = 0

        #CREATE VOICE DESIGN HERE! I WILL ANIMATE!
        #self.voiceTEST = canvas.create_oval(125+self.player.x, 125+self.player.y, 150+self.player.x, 150+self.player.y)
        self.voice1 = canvas.create_polygon(137, 130, 146, 136, 147, 142, 146, 149, 137, 155, 143, 149, 144, 142, 143, 136, fill="grey", outline="black")
        self.voice2 = canvas.create_polygon(130, 135, 139, 140, 140, 142, 139, 146, 130, 150, 137, 144, 137, 142, 137, 141, fill="grey", outline="black") #(-7, -5 or +5) (+3, 0) (-3,0
        self.voice3 = canvas.create_polygon(129, 140, 131, 142, 129, 146, 128, 144, 130, 142, 128, 141, fill="grey", outline="black") #(-9, 0)

        #Mirroring the above over y-axis. Needed for player looking left.
        #125-150 = 25/2 = 12.5- > 13 + 125 = 138
        #self.voice1 = canvas.create_polygon(137+2, 130, 146-16, 136, 147-18, 142, 146-16, 149, 137+2, 155, 143-10, 149, 144-12, 142, 143-10, 136, fill="grey", outline="black")
        #self.voice2 = canvas.create_polygon(130+16, 135, 139-2, 140, 140-4, 142, 139-2, 146, 130+16, 150, 137+2, 144, 137+2, 142, 137+2, 141, fill="grey", outline="black") #(-7, -5 or +5) (+3, 0) (-3,0
        #self.voice3 = canvas.create_polygon(129+18, 140, 131+14, 142, 129+18, 146, 128+20, 144, 130+16, 142, 128+20, 141, fill="grey", outline="black") #(-9, 0)

        canvas.move(self.voice1, -10000, -10000)
        canvas.move(self.voice2, -10000, -10000)
        canvas.move(self.voice3, -10000, -10000)

    def draw(self):
        global voiceOn
        if voiceOn == True:
            #print("I can hear you")
            #MOVING LEFT NOT IN AIR. INITIALIZED VOICE
            if self.player.Frame == 0 and self.player.sprint == False and self.player.crouch == False and self.player.looking == "Left" and self.vLooking == "": #Moving left without sprint or crouch FRAME #1
                #canvas.coords(self.voice1, 125+self.player.x-20+self.x, 125+self.player.y, 150+self.player.x-20+self.x, 150+self.player.y)
                canvas.coords(self.voice1, 137+2+self.player.x-30, 130+self.player.y, 146-16+self.player.x-30, 136+self.player.y, 147-18+self.player.x-30, 142+self.player.y, 146-16+self.player.x-30, 149+self.player.y, 137+2+self.player.x-30, 155+self.player.y, 143-10+self.player.x-30, 149+self.player.y, 144-12+self.player.x-30, 142+self.player.y, 143-10+self.player.x-30, 136+self.player.y)
                canvas.coords(self.voice2, 130+16+self.player.x-30, 135+self.player.y, 139-2+self.player.x-30, 140+self.player.y, 140-4+self.player.x-30, 142+self.player.y, 139-2+self.player.x-30, 146+self.player.y, 130+16+self.player.x-30, 150+self.player.y, 137+2+self.player.x-30, 144+self.player.y, 137+2+self.player.x-30, 142+self.player.y, 137+2+self.player.x-30, 141+self.player.y)
                canvas.coords(self.voice3, 129+18+self.player.x-30, 140+self.player.y, 131+14+self.player.x-30, 142+self.player.y, 129+18+self.player.x-30, 146+self.player.y, 128+20+self.player.x-30, 144+self.player.y, 130+16+self.player.x-30, 142+self.player.y, 128+20+self.player.x-30, 141+self.player.y)
                self.vLooking = "Left"
                
            elif self.player.Frame == 1 and self.player.sprint == False and self.player.crouch == False and self.player.looking == "Left" and self.vLooking == "": #Moving left without sprint or crouch FRAME #2
                #canvas.coords(self.voice1, 125+self.player.x-20+self.x, 125+3+self.player.y, 150+self.player.x-20+self.x, 150+3+self.player.y)
                canvas.coords(self.voice1, 137+2+self.player.x-30, 130+self.player.y+3, 146-16+self.player.x-30, 136+self.player.y+3, 147-18+self.player.x-30, 142+self.player.y+3, 146-16+self.player.x-30, 149+self.player.y+3, 137+2+self.player.x-30, 155+self.player.y+3, 143-10+self.player.x-30, 149+self.player.y+3, 144-12+self.player.x-30, 142+self.player.y+3, 143-10+self.player.x-30, 136+self.player.y+3)
                canvas.coords(self.voice2, 130+16+self.player.x-30, 135+self.player.y+3, 139-2+self.player.x-30, 140+self.player.y+3, 140-4+self.player.x-30, 142+self.player.y+3, 139-2+self.player.x-30, 146+self.player.y+3, 130+16+self.player.x-30, 150+self.player.y+3, 137+2+self.player.x-30, 144+self.player.y+3, 137+2+self.player.x-30, 142+self.player.y+3, 137+2+self.player.x-30, 141+self.player.y+3)
                canvas.coords(self.voice3, 129+18+self.player.x-30, 140+self.player.y+3, 131+14+self.player.x-30, 142+self.player.y+3, 129+18+self.player.x-30, 146+self.player.y+3, 128+20+self.player.x-30, 144+self.player.y+3, 130+16+self.player.x-30, 142+self.player.y+3, 128+20+self.player.x-30, 141+self.player.y+3)
                self.vLooking = "Left"
            
            elif self.player.Frame == 0 and self.player.sprint == True and self.player.crouch == False and self.player.looking == "Left" and self.vLooking == "": #Moving left SPRINTING FRAME #1
                #canvas.coords(self.voice1, 145+self.player.x-20+self.x-40, 135+self.player.y, 170+self.player.x-20+self.x-40, 160+self.player.y) #(+20, +10) difference from walking
                canvas.coords(self.voice1, 137+2+self.player.x-30-20, 130+self.player.y+10, 146-16+self.player.x-30-20, 136+self.player.y+10, 147-18+self.player.x-30-20, 142+self.player.y+10, 146-16+self.player.x-30-20, 149+self.player.y+10, 137+2+self.player.x-30-20, 155+self.player.y+10, 143-10+self.player.x-30-20, 149+self.player.y+10, 144-12+self.player.x-30-20, 142+self.player.y+10, 143-10+self.player.x-30-20, 136+self.player.y+10)
                canvas.coords(self.voice2, 130+16+self.player.x-30-20, 135+self.player.y+10, 139-2+self.player.x-30-20, 140+self.player.y+10, 140-4+self.player.x-30-20, 142+self.player.y+10, 139-2+self.player.x-30-20, 146+self.player.y+10, 130+16+self.player.x-30-20, 150+self.player.y+10, 137+2+self.player.x-30-20, 144+self.player.y+10, 137+2+self.player.x-30-20, 142+self.player.y+10, 137+2+self.player.x-30-20, 141+self.player.y+10)
                canvas.coords(self.voice3, 129+18+self.player.x-30-20, 140+self.player.y+10, 131+14+self.player.x-30-20, 142+self.player.y+10, 129+18+self.player.x-30-20, 146+self.player.y+10, 128+20+self.player.x-30-20, 144+self.player.y+10, 130+16+self.player.x-30-20, 142+self.player.y+10, 128+20+self.player.x-30-20, 141+self.player.y+10)
                self.vLooking = "Left"
                
            elif self.player.Frame == 1 and self.player.sprint == True and self.player.crouch == False and self.player.looking == "Left" and self.vLooking == "": #Moving left SPRINTING FRAME #2
                #canvas.coords(self.voice1, 145+self.player.x-20+self.x-40, 135+5+self.player.y+10, 170+self.player.x-20+self.x-40, 160+5+self.player.y+10) #(+20, +10) difference from walking
                canvas.coords(self.voice1, 137+2+self.player.x-30-20, 130+self.player.y+10+5, 146-16+self.player.x-30-20, 136+self.player.y+10+5, 147-18+self.player.x-30-20, 142+self.player.y+10+5, 146-16+self.player.x-30-20, 149+self.player.y+10+5, 137+2+self.player.x-30-20, 155+self.player.y+10+5, 143-10+self.player.x-30-20, 149+self.player.y+10+5, 144-12+self.player.x-30-20, 142+self.player.y+10+5, 143-10+self.player.x-30-20, 136+self.player.y+10+5)
                canvas.coords(self.voice2, 130+16+self.player.x-30-20, 135+self.player.y+10+5, 139-2+self.player.x-30-20, 140+self.player.y+10+5, 140-4+self.player.x-30-20, 142+self.player.y+10+5, 139-2+self.player.x-30-20, 146+self.player.y+10+5, 130+16+self.player.x-30-20, 150+self.player.y+10+5, 137+2+self.player.x-30-20, 144+self.player.y+10+5, 137+2+self.player.x-30-20, 142+self.player.y+10+5, 137+2+self.player.x-30-20, 141+self.player.y+10+5)
                canvas.coords(self.voice3, 129+18+self.player.x-30-20, 140+self.player.y+10+5, 131+14+self.player.x-30-20, 142+self.player.y+10+5, 129+18+self.player.x-30-20, 146+self.player.y+10+5, 128+20+self.player.x-30-20, 144+self.player.y+10+5, 130+16+self.player.x-30-20, 142+self.player.y+10+5, 128+20+self.player.x-30-20, 141+self.player.y+10+5)
                self.vLooking = "Left"
                
            elif self.player.Frame == 0 and self.player.sprint == False and self.player.crouch == True and self.player.looking == "Left" and self.vLooking == "": #Moving left CROUCHING FRAME #1
                #canvas.coords(self.voice1, 145+self.player.x-20+self.x-40, 135+self.player.y+10, 170+self.player.x-20+self.x-40, 160+self.player.y+10) #(+20, +10) difference from walking
                canvas.coords(self.voice1, 137+2+self.player.x-30-20, 130+self.player.y+10, 146-16+self.player.x-30-20, 136+self.player.y+10, 147-18+self.player.x-30-20, 142+self.player.y+10, 146-16+self.player.x-30-20, 149+self.player.y+10, 137+2+self.player.x-30-20, 155+self.player.y+10, 143-10+self.player.x-30-20, 149+self.player.y+10, 144-12+self.player.x-30-20, 142+self.player.y+10, 143-10+self.player.x-30-20, 136+self.player.y+10)
                canvas.coords(self.voice2, 130+16+self.player.x-30-20, 135+self.player.y+10, 139-2+self.player.x-30-20, 140+self.player.y+10, 140-4+self.player.x-30-20, 142+self.player.y+10, 139-2+self.player.x-30-20, 146+self.player.y+10, 130+16+self.player.x-30-20, 150+self.player.y+10, 137+2+self.player.x-30-20, 144+self.player.y+10, 137+2+self.player.x-30-20, 142+self.player.y+10, 137+2+self.player.x-30-20, 141+self.player.y+10)
                canvas.coords(self.voice3, 129+18+self.player.x-30-20, 140+self.player.y+10, 131+14+self.player.x-30-20, 142+self.player.y+10, 129+18+self.player.x-30-20, 146+self.player.y+10, 128+20+self.player.x-30-20, 144+self.player.y+10, 130+16+self.player.x-30-20, 142+self.player.y+10, 128+20+self.player.x-30-20, 141+self.player.y+10)
                self.vLooking = "Left"
                
            elif self.player.Frame == 1 and self.player.sprint == False and self.player.crouch == True and self.player.looking == "Left" and self.vLooking == "": #Moving left CROUCHING FRAME #2
                #canvas.coords(self.voice1, 145+self.player.x-20+self.x-40, 135+2+self.player.y+10, 170+self.player.x-20+self.x-40, 160+2+self.player.y+10) #(+20, +10) difference from walking
                canvas.coords(self.voice1, 137+2+self.player.x-30-20, 130+self.player.y+10+2, 146-16+self.player.x-30-20, 136+self.player.y+10+2, 147-18+self.player.x-30-20, 142+self.player.y+10+2, 146-16+self.player.x-30-20, 149+self.player.y+10+2, 137+2+self.player.x-30-20, 155+self.player.y+10+2, 143-10+self.player.x-30-20, 149+self.player.y+10+2, 144-12+self.player.x-30-20, 142+self.player.y+10+2, 143-10+self.player.x-30-20, 136+self.player.y+10+2)
                canvas.coords(self.voice2, 130+16+self.player.x-30-20, 135+self.player.y+10+2, 139-2+self.player.x-30-20, 140+self.player.y+10+2, 140-4+self.player.x-30-20, 142+self.player.y+10+2, 139-2+self.player.x-30-20, 146+self.player.y+10+2, 130+16+self.player.x-30-20, 150+self.player.y+10+2, 137+2+self.player.x-30-20, 144+self.player.y+10+2, 137+2+self.player.x-30-20, 142+self.player.y+10+2, 137+2+self.player.x-30-20, 141+self.player.y+10+2)
                canvas.coords(self.voice3, 129+18+self.player.x-30-20, 140+self.player.y+10+2, 131+14+self.player.x-30-20, 142+self.player.y+10+2, 129+18+self.player.x-30-20, 146+self.player.y+10+2, 128+20+self.player.x-30-20, 144+self.player.y+10+2, 130+16+self.player.x-30-20, 142+self.player.y+10+2, 128+20+self.player.x-30-20, 141+self.player.y+10+2)
                self.vLooking = "Left"

            #MOVING RIGHT NOT IN AIR. INITIALIZED VOICE
            elif self.player.Frame == 0 and self.player.sprint == False and self.player.crouch == False and self.player.looking == "Right" and self.vLooking == "": #Moving right without sprinting or crouching FRAME #1
                #canvas.coords(self.voice1, 125+self.player.x+20+self.x, 125+self.player.y, 150+self.player.x+20+self.x, 150+self.player.y)
                canvas.coords(self.voice1, 137+self.player.x+30, 130+self.player.y, 146+self.player.x+30, 136+self.player.y, 147+self.player.x+30, 142+self.player.y, 146+self.player.x+30, 149+self.player.y, 137+self.player.x+30, 155+self.player.y, 143+self.player.x+30, 149+self.player.y, 144+self.player.x+30, 142+self.player.y, 143+self.player.x+30, 136+self.player.y)
                canvas.coords(self.voice2, 130+self.player.x+30, 135+self.player.y, 139+self.player.x+30, 140+self.player.y, 140+self.player.x+30, 142+self.player.y, 139+self.player.x+30, 146+self.player.y, 130+self.player.x+30, 150+self.player.y, 137+self.player.x+30, 144+self.player.y, 137+self.player.x+30, 142+self.player.y, 137+self.player.x+30, 141+self.player.y)
                canvas.coords(self.voice3, 129+self.player.x+30, 140+self.player.y, 131+self.player.x+30, 142+self.player.y, 129+self.player.x+30, 146+self.player.y, 128+self.player.x+30, 144+self.player.y, 130+self.player.x+30, 142+self.player.y, 128+self.player.x+30, 141+self.player.y)
                self.vLooking = "Right"
                
            elif self.player.Frame == 1 and self.player.sprint == False and self.player.crouch == False and self.player.looking == "Right" and self.vLooking == "": #Moving right without sprinting or crouching FRAME #2
                #canvas.coords(self.voice1, 125+self.player.x+20+self.x, 125+3+self.player.y, 150+self.player.x+20+self.x, 150+3+self.player.y)
                canvas.coords(self.voice1, 137+self.player.x+30, 130+self.player.y+3, 146+self.player.x+30, 136+self.player.y+3, 147+self.player.x+30, 142+self.player.y+3, 146+self.player.x+30, 149+self.player.y+3, 137+self.player.x+30, 155+self.player.y+3, 143+self.player.x+30, 149+self.player.y+3, 144+self.player.x+30, 142+self.player.y+3, 143+self.player.x+30, 136+self.player.y)
                canvas.coords(self.voice2, 130+self.player.x+30, 135+self.player.y+3, 139+self.player.x+30, 140+self.player.y+3, 140+self.player.x+30, 142+self.player.y+3, 139+self.player.x+30, 146+self.player.y+3, 130+self.player.x+30, 150+self.player.y+3, 137+self.player.x+30, 144+self.player.y+3, 137+self.player.x+30, 142+self.player.y+3, 137+self.player.x+30, 141+self.player.y)
                canvas.coords(self.voice3, 129+self.player.x+30, 140+self.player.y+3, 131+self.player.x+30, 142+self.player.y+3, 129+self.player.x+30, 146+self.player.y+3, 128+self.player.x+30, 144+self.player.y+3, 130+self.player.x+30, 142+self.player.y+3, 128+self.player.x+30, 141+self.player.y)
                self.vLooking = "Right"
            
            elif self.player.Frame == 0 and self.player.sprint == True and self.player.crouch == False and self.player.looking == "Right" and self.vLooking == "": #Moving right SPRINTING FRAME #1
                #canvas.coords(self.voice1, 145+self.player.x+20+self.x, 135+self.player.y, 170+self.player.x+20+self.x, 160+self.player.y) #(+20, +10) difference from walking
                canvas.coords(self.voice1, 137+self.player.x+30+20, 130+self.player.y+10, 146+self.player.x+30+20, 136+self.player.y+10, 147+self.player.x+30+20, 142+self.player.y+10, 146+self.player.x+30+20, 149+self.player.y+10, 137+self.player.x+30+20, 155+self.player.y+10, 143+self.player.x+30+20, 149+self.player.y+10, 144+self.player.x+30+20, 142+self.player.y+10, 143+self.player.x+30+20, 136+self.player.y+10)
                canvas.coords(self.voice2, 130+self.player.x+30+20, 135+self.player.y+10, 139+self.player.x+30+20, 140+self.player.y+10, 140+self.player.x+30+20, 142+self.player.y+10, 139+self.player.x+30+20, 146+self.player.y+10, 130+self.player.x+30+20, 150+self.player.y+10, 137+self.player.x+30+20, 144+self.player.y+10, 137+self.player.x+30+20, 142+self.player.y+10, 137+self.player.x+30+20, 141+self.player.y+10)
                canvas.coords(self.voice3, 129+self.player.x+30+20, 140+self.player.y+10, 131+self.player.x+30+20, 142+self.player.y+10, 129+self.player.x+30+20, 146+self.player.y+10, 128+self.player.x+30+20, 144+self.player.y+10, 130+self.player.x+30+20, 142+self.player.y+10, 128+self.player.x+30+20, 141+self.player.y+10)
                self.vLooking = "Right"
                
            elif self.player.Frame == 1 and self.player.sprint == True and self.player.crouch == False and self.player.looking == "Right" and self.vLooking == "": #Moving right SPRINTING FRAME #2
                #canvas.coords(self.voice1, 145+self.player.x+20+self.x, 135+5+self.player.y+10, 170+self.player.x+20+self.x, 160+5+self.player.y+10) #(+20, +10) difference from walking
                canvas.coords(self.voice1, 137+self.player.x+30+20, 130+self.player.y+10+5, 146+self.player.x+30+20, 136+self.player.y+10+5, 147+self.player.x+30+20, 142+self.player.y+10+5, 146+self.player.x+30+20, 149+self.player.y+10+5, 137+self.player.x+30+20, 155+self.player.y+10+5, 143+self.player.x+30+20, 149+self.player.y+10+5, 144+self.player.x+30+20, 142+self.player.y+10+5, 143+self.player.x+30+20, 136+self.player.y+10+5)
                canvas.coords(self.voice2, 130+self.player.x+30+20, 135+self.player.y+10+5, 139+self.player.x+30+20, 140+self.player.y+10+5, 140+self.player.x+30+20, 142+self.player.y+10+5, 139+self.player.x+30+20, 146+self.player.y+10+5, 130+self.player.x+30+20, 150+self.player.y+10+5, 137+self.player.x+30+20, 144+self.player.y+10+5, 137+self.player.x+30+20, 142+self.player.y+10+5, 137+self.player.x+30+20, 141+self.player.y+10+5)
                canvas.coords(self.voice3, 129+self.player.x+30+20, 140+self.player.y+10+5, 131+self.player.x+30+20, 142+self.player.y+10+5, 129+self.player.x+30+20, 146+self.player.y+10+5, 128+self.player.x+30+20, 144+self.player.y+10+5, 130+self.player.x+30+20, 142+self.player.y+10+5, 128+self.player.x+30+20, 141+self.player.y+10+5)
                self.vLooking = "Right"
                
            elif self.player.Frame == 0 and self.player.sprint == False and self.player.crouch == True and self.player.looking == "Right" and self.vLooking == "": #Moving right CROUCHING FRAMe #1
                #canvas.coords(self.voice1, 145+self.player.x+20+self.x, 135+self.player.y+10, 170+self.player.x+20+self.x, 160+self.player.y+10) #(+20, +10) difference from walking
                canvas.coords(self.voice1, 137+self.player.x+30+20, 130+self.player.y+10, 146+self.player.x+30+20, 136+self.player.y+10, 147+self.player.x+30+20, 142+self.player.y+10, 146+self.player.x+30+20, 149+self.player.y+10, 137+self.player.x+30+20, 155+self.player.y+10, 143+self.player.x+30+20, 149+self.player.y+10, 144+self.player.x+30+20, 142+self.player.y+10, 143+self.player.x+30+20, 136+self.player.y+10)
                canvas.coords(self.voice2, 130+self.player.x+30+20, 135+self.player.y+10, 139+self.player.x+30+20, 140+self.player.y+10, 140+self.player.x+30+20, 142+self.player.y+10, 139+self.player.x+30+20, 146+self.player.y+10, 130+self.player.x+30+20, 150+self.player.y+10, 137+self.player.x+30+20, 144+self.player.y+10, 137+self.player.x+30+20, 142+self.player.y+10, 137+self.player.x+30+20, 141+self.player.y+10)
                canvas.coords(self.voice3, 129+self.player.x+30+20, 140+self.player.y+10, 131+self.player.x+30+20, 142+self.player.y+10, 129+self.player.x+30+20, 146+self.player.y+10, 128+self.player.x+30+20, 144+self.player.y+10, 130+self.player.x+30+20, 142+self.player.y+10, 128+self.player.x+30+20, 141+self.player.y+10)
                self.vLooking = "Right"
                
            elif self.player.Frame == 1 and self.player.sprint == False and self.player.crouch == True and self.player.looking == "Right" and self.vLooking == "": #Moving right CROUCHING FRAMe #2
                #canvas.coords(self.voice1, 145+self.player.x+20+self.x, 135+2+self.player.y+10, 170+self.player.x+20+self.x, 160+2+self.player.y+10) #(+20, +10) difference from walking
                canvas.coords(self.voice1, 137+self.player.x+30+20, 130+self.player.y+10+2, 146+self.player.x+30+20, 136+self.player.y+10+2, 147+self.player.x+30+20, 142+self.player.y+10+2, 146+self.player.x+30+20, 149+self.player.y+10+2, 137+self.player.x+30+20, 155+self.player.y+10+2, 143+self.player.x+30+20, 149+self.player.y+10+2, 144+self.player.x+30+20, 142+self.player.y+10+2, 143+self.player.x+30+20, 136+self.player.y+10)
                canvas.coords(self.voice2, 130+self.player.x+30+20, 135+self.player.y+10+2, 139+self.player.x+30+20, 140+self.player.y+10+2, 140+self.player.x+30+20, 142+self.player.y+10+2, 139+self.player.x+30+20, 146+self.player.y+10+2, 130+self.player.x+30+20, 150+self.player.y+10+2, 137+self.player.x+30+20, 144+self.player.y+10+2, 137+self.player.x+30+20, 142+self.player.y+10+2, 137+self.player.x+30+20, 141+self.player.y+10)
                canvas.coords(self.voice3, 129+self.player.x+30+20, 140+self.player.y+10+2, 131+self.player.x+30+20, 142+self.player.y+10+2, 129+self.player.x+30+20, 146+self.player.y+10+2, 128+self.player.x+30+20, 144+self.player.y+10+2, 130+self.player.x+30+20, 142+self.player.y+10+2, 128+self.player.x+30+20, 141+self.player.y+10)
                self.vLooking = "Right"

            self.counter += 1
            
            if self.vLooking == "Left" and self.counter == 10:
                self.counter = 0
                self.x -= 20
                canvas.move(self.voice1, -50, 0)
                canvas.move(self.voice2, -50, 0)
                canvas.move(self.voice3, -50, 0)
                if self.x == -520:
                    self.x = 0
                    voiceOn = False
                    self.vLooking = ""
                    canvas.move(self.voice1, -1000000, -1000000)
                    canvas.move(self.voice2, -1000000, -1000000)
                    canvas.move(self.voice3, -1000000, -1000000)
                    print("Special Ready.")
                    
            elif self.vLooking == "Right" and self.counter == 10:
                self.counter = 0
                self.x += 20
                canvas.move(self.voice1, 50, 0)
                canvas.move(self.voice2, 50, 0)
                canvas.move(self.voice3, 50, 0)
                if self.x == 520:
                    self.x = 0
                    voiceOn = False
                    self.vLooking = ""
                    canvas.move(self.voice1, -1000000, -1000000)
                    canvas.move(self.voice2, -1000000, -1000000)
                    canvas.move(self.voice3, -1000000, -1000000)
                    print("Special Ready.")        

class Player:
    def __init__(self,canvas):
        self.canvas = canvas
        
        self.x, self.y = 0,0 #Only one coordinate now. This coordinate is where the first shape is __init__ialized. Not the graph.
        self.Frame = 0 #Two frames-0 and 1. They alternate which makes the character move more lively.
        self.sprint = False #Pressing 'Shift' will make it True. In draw() method, will check condition.
        self.crouch = False #Pressing 'Ctrl' will make it True. In draw() method, will check condition.
        self.inAir = False #Unused. But might make the character be able to move left and right while in air later.
        self.looking = "Right" #Need to check what direction character is facing when moving up or down. 
        self.checker = 3 #Without this, the character will slide
        self.checkerFrame = 0 #Changes frames Look at the bottom of the draw() method for more details.
        self.notMoving = True #Makes sure the char doesnt slide. This is because at the very end of the code, draw() is constantly being called in the while loop so if there is no sentinel to stop it from moving, the char would slide across the screen.
        self.dropping = False #Pressing 's' will make it True. In draw() method, will check condition.
        self.jumping = False #Pressing 'w' will make it True. In draw() method, will check condition.
        self.inAirCounter = 0 #Check the bottom of draw(). This allows the program to counter how many iterations I want to be in air.
        self.basic_attack_counter = 0
        self.moveFists = 0
        self.forward = True
        
        #Creating the model of player 1 w/ label above it's head
        #Character is walking to the right of the screen
        #Name of the character
        self.a_name = canvas.create_text(138, 110, text="", width=1000, fill="green", anchor="center", font=("Fixedsys", 16))

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

        #IDK HOW TO CREATE A BUTTON IN THE MAIN WINDOW WILL DO LATER
        #button1=Button(main_frame,text="Click Me")
        #button1.bind("<Button-1>",printName)
        #button1.pack()

        #KEYBINDINGS
        self.b_leftClick = canvas.bind("<Button-1>", self.leftClick) #bind.("<BUTTON_NAME>", function_call) #Functions way above
        self.b_scroll = canvas.bind("<Button-2>", self.scroll)
        self.b_rightClick = canvas.bind("<Button-3>", self.rightClick)
        self.b_a = canvas.bind("<a>", self.aKey)
        self.b_d = canvas.bind("<d>", self.dKey)
        self.b_s = canvas.bind("<s>", self.sKey)
        self.b_w = canvas.bind("<w>", self.wKey)
        self.b_q = canvas.bind("<q>", self.qKey)
        self.b_e = canvas.bind("<e>", self.eKey)
        self.b_shiftR = canvas.bind("<Shift_R>", self.shiftKey)
        self.b_shiftL = canvas.bind("<Shift_L>", self.shiftKey)
        self.b_ctrlL = canvas.bind("<Control_L>", self.ctrlKey)
        self.b_ctrlR = canvas.bind("<Control_R>", self.ctrlKey)
        self.b_space = canvas.bind("<space>", self.spaceKey)

    def draw(self): #Check the while loop way down below. This method will constantly update any movement or no movement at all.

        if self.checker == 10:
            self.notMoving = True
            pass
        else:
            self.checker += 1
        
        if self.notMoving == True and self.dropping == False and self.jumping == False: #If character is not moving, do nothing
            pass
        #JUMP LEFT
        elif self.Frame == 0 and self.sprint == False and self.crouch == False and self.looking == "Left" and self.dropping == False and self.jumping == True: #Moving left without sprint or crouch FRAME #1
            self.y -= 3
            canvas.coords(self.a_head, 125+self.x, 125+self.y, 150+self.x, 150+self.y)
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 130+self.x, 150+self.y, 145+self.x, 150+self.y, 145+self.x, 175+self.y, 130+self.x, 175+self.y)
            canvas.coords(self.a_Larm, 115+self.x, 150+self.y, 130+self.x, 165+self.y)
            canvas.coords(self.a_Rarm, 145+self.x, 150+self.y, 160+self.x, 165+self.y)
            canvas.coords(self.a_Rleg, 145+self.x, 175+self.y, 160+self.x, 183+self.y)
            canvas.coords(self.a_Lleg, 115+self.x, 175+self.y, 130+self.x, 183+self.y)
            canvas.coords(self.a_bandana1, 125+self.x+25, 140+self.y, 150+self.x-25, 140+self.y, 150+self.x-25, 150+self.y)
            canvas.coords(self.a_bandana2, 125+self.x+25, 140+self.y, 120+self.x+35, 142+self.y, 120+self.x+35, 145+self.y)
            canvas.coords(self.a_bandana3, 125+self.x+25, 140+self.y, 120+self.x+35, 138+self.y, 120+self.x+35, 141+self.y)
            canvas.coords(self.a_vneck, 130+self.x, 155+self.y, 145+self.x, 150+self.y, 145+self.x, 175+self.y, 130+self.x, 175+self.y)
            canvas.coords(self.a_coat, 145+self.x, 145+self.y, 133+self.x, 145+self.y, 140+self.x, 175+self.y, 160+self.x, 177+self.y, 145+self.x, 160+self.y)

        elif self.Frame == 1 and self.sprint == False and self.crouch == False and self.looking == "Left" and self.dropping == False and self.jumping == True: #Moving left without sprint or crouch FRAME #2
            self.y -= 3
            canvas.coords(self.a_head, 125+self.x, 125+3+self.y, 150+self.x, 150+3+self.y)
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 130+self.x, 150+3+self.y, 145+self.x, 150+3+self.y, 145+self.x, 175+3+self.y, 130+self.x, 175+3+self.y)
            canvas.coords(self.a_Larm, 130+self.x, 160+self.y, 145+self.x, 175+self.y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO
            canvas.coords(self.a_Rarm, 130+self.x, 160+self.y, 145+self.x, 175+self.y) #Arm hides behind torso
            canvas.coords(self.a_Rleg, 145+self.x-10, 175+self.y, 160+self.x-10, 183+self.y)
            canvas.coords(self.a_Lleg, 115+self.x+10, 175+self.y, 130+self.x+10, 183+self.y)
            canvas.coords(self.a_bandana1, 125+self.x+25, 140+3+self.y, 150+self.x-25, 140+3+self.y, 150+self.x-25, 150+3+self.y)
            canvas.coords(self.a_bandana2, 125+self.x+25, 140+3+self.y, 120+self.x+35, 142+3+self.y, 120+self.x+35, 145+3+self.y)
            canvas.coords(self.a_bandana3, 125+self.x+25, 140+3+self.y, 120+self.x+35, 138+3+self.y, 120+self.x+35, 141+3+self.y)
            canvas.coords(self.a_vneck, 130+self.x, 155+3+self.y, 145+self.x, 150+3+self.y, 145+self.x, 175+3+self.y, 130+self.x, 175+3+self.y)
            canvas.coords(self.a_coat, 145+self.x, 145+3+self.y, 133+self.x, 145+3+self.y, 140+self.x, 175+3+self.y, 160+self.x, 177+6+self.y, 145+self.x, 160+3+self.y)

        elif self.Frame == 0 and self.sprint == True and self.crouch == False and self.looking == "Left" and self.dropping == False and self.jumping == True: #Moving left SPRINTING FRAME #1
            self.y -= 3    
            canvas.coords(self.a_head, 145+self.x-40, 135+self.y, 170+self.x-40, 160+self.y) #(+20, +10) difference from walking
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 140+self.x-4, 150+self.y, 150+self.x-24, 160+self.y, 125+self.x+26, 170+self.y, 115+self.x+46, 160+self.y) #(10, 0), (5,10), (-20,-5), (-15,-15)
            canvas.coords(self.a_Larm, 85+self.x+106, 150+self.y, 100+self.x+76, 165+self.y) #(-30,0)
            canvas.coords(self.a_Rarm, 175+self.x-74, 150+self.y, 190+self.x-104, 165+self.y) #(+30,0)
            canvas.coords(self.a_Rleg, 150+self.x-24, 170+self.y, 165+self.x-54, 178+self.y) #(+5,-5), (+5,-5)
            canvas.coords(self.a_Lleg, 110+self.x+56, 170+self.y, 125+self.x+26, 178+self.y) #(-5,-5), (-5,-5)
            canvas.coords(self.a_bandana1, 145+self.x-14, 150+self.y, 170+self.x-64, 150+self.y, 170+self.x-64, 160+self.y) #(+20,10) for all bandana
            canvas.coords(self.a_bandana2, 145+self.x-14, 150+self.y, 140+self.x-4, 152+self.y, 140+self.x-4, 160+self.y)
            canvas.coords(self.a_bandana3, 145+self.x-14, 150+self.y, 140+self.x-4, 148+self.y, 140+self.x-4, 151+self.y)
            canvas.coords(self.a_vneck, 140+self.x-4, 150+self.y, 145+self.x-14, 163+self.y, 125+self.x+26, 170+self.y, 115+self.x+46, 160+self.y) #(10,0), (0,8), (-20,-5), (-15,-15)
            canvas.coords(self.a_coat, 142+self.x-8, 145+self.y, 152+self.x-28, 155+self.y, 100+self.x+76, 175+self.y, 85+self.x+104, 157+self.y, 125+self.x+26, 155+self.y)   

        elif self.Frame == 1 and self.sprint == True and self.crouch == False and self.looking == "Left" and self.dropping == False and self.jumping == True: #Moving left SPRINTING FRAME #2
            self.y -= 3    
            canvas.coords(self.a_head, 145+self.x-40, 135+5+self.y, 170+self.x-40, 160+5+self.y) #(+20, +10) difference from walking
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 140+self.x-4, 150+5+self.y, 150+self.x-24, 160+5+self.y, 125+self.x+26, 170+5+self.y, 115+self.x+46, 160+5+self.y) #(20, 10), (5,10)
            canvas.coords(self.a_Larm, 130+self.x+16, 160+self.y, 145+self.x-14, 175+self.y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
            canvas.coords(self.a_Rarm, 130+self.x+16, 160+self.y, 145+self.x-14, 175+self.y) #Arm hides behind torso (+30,0)
            canvas.coords(self.a_Rleg, 145+self.x-10, 175+self.y, 160+self.x-10, 183+self.y)
            canvas.coords(self.a_Lleg, 115+self.x+10, 175+self.y, 130+self.x+10, 183+self.y)
            canvas.coords(self.a_bandana1, 145+self.x-14, 150+5+self.y, 170+self.x-64, 150+5+self.y, 170+self.x-64, 160+5+self.y) #(+20,10) for all bandana
            canvas.coords(self.a_bandana2, 145+self.x-14, 150+5+self.y, 140+self.x-4, 152+5+self.y, 140+self.x-4, 160+5+self.y)
            canvas.coords(self.a_bandana3, 145+self.x-14, 150+5+self.y, 140+self.x-4, 148+5+self.y, 140+self.x-4, 151+5+self.y)
            canvas.coords(self.a_vneck, 140+self.x-4, 150+5+self.y, 145+self.x-14, 163+5+self.y, 125+self.x+26, 170+5+self.y, 115+self.x+46, 160+5+self.y) #(10,0), (0,8), (-20,-5), (-15,-15)
            canvas.coords(self.a_coat, 142+self.x-8, 145+5+self.y, 152+self.x-28, 155+5+self.y, 100+self.x+76, 175+10+self.y, 85+self.x+104, 157+10+self.y, 125+self.x+26, 155+5+self.y)

        elif self.Frame == 0 and self.sprint == False and self.crouch == True and self.looking == "Left" and self.dropping == False and self.jumping == True: #Moving left CROUCHING FRAME #1
            self.y -= 3
            canvas.coords(self.a_head, 145+self.x-40, 135+self.y, 170+self.x-40, 160+self.y) #(+20, +10) difference from walking
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 140+self.x-4, 150+self.y, 150+self.x-24, 160+self.y, 125+self.x+26, 170+self.y, 115+self.x+46, 160+self.y) #(10, 0), (5,10), (-20,-5), (-15,-15)
            canvas.coords(self.a_Larm, 130+self.x+16, 160+self.y, 145+self.x-14, 175+self.y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
            canvas.coords(self.a_Rarm, 130+self.x+16, 160+self.y, 145+self.x-14, 175+self.y) #Arm hides behind torso (+30,0)
            canvas.coords(self.a_Rleg, 145+self.x-5, 175+self.y, 160+self.x-5, 183+self.y) #(+5,-5), (+5,-5)
            canvas.coords(self.a_Lleg, 115+self.x+5, 175+self.y, 130+self.x+5, 183+self.y) #(-5,-5), (-5,-5)
            canvas.coords(self.a_bandana1, 145+self.x-14, 150+self.y, 170+self.x-64, 150+self.y, 170+self.x-64, 160+self.y) #(+20,10) for all bandana
            canvas.coords(self.a_bandana2, 145+self.x-14, 150+self.y, 140+self.x-4, 152+self.y, 140+self.x-4, 160+self.y)
            canvas.coords(self.a_bandana3, 145+self.x-14, 150+self.y, 140+self.x-4, 148+self.y, 140+self.x-4, 151+self.y)
            canvas.coords(self.a_vneck, 140+self.x-4, 150+self.y, 145+self.x-14, 163+self.y, 125+self.x+26, 170+self.y, 115+self.x+46, 160+self.y) #(10,0), (0,8), (-20,-5), (-15,-15)
            canvas.coords(self.a_coat, 142+self.x-8, 145+self.y, 152+self.x-28, 155+self.y, 85+self.x+76, 183+self.y, 80+self.x+104, 183+self.y, 125+self.x+26, 155+self.y)
            
        elif self.Frame == 1 and self.sprint == False and self.crouch == True and self.looking == "Left" and self.dropping == False and self.jumping == True: #Moving left CROUCHING FRAME #2
            self.y -= 3
            canvas.coords(self.a_head, 145+self.x-40, 135+2+self.y, 170+self.x-40, 160+2+self.y) #(+20, +10) difference from walking
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 140+self.x-4, 150+2+self.y, 150+self.x-24, 160+2+self.y, 125+self.x+26, 170+2+self.y, 115+self.x+46, 160+2+self.y) #(20, 10), (5,10)
            canvas.coords(self.a_Larm, 130+self.x-10, 160+2+self.y, 145+self.x-10, 175+2+self.y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
            canvas.coords(self.a_Rarm, 130+self.x-10, 160+2+self.y, 145+self.x-10, 175+2+self.y) #Arm hides behind torso (+30,0)
            canvas.coords(self.a_Rleg, 145+self.x-10, 175+self.y, 160+self.x-10, 183+self.y)
            canvas.coords(self.a_Lleg, 115+self.x+10, 175+self.y, 130+self.x+10, 183+self.y)
            canvas.coords(self.a_bandana1, 145+self.x-14, 150+2+self.y, 170+self.x-64, 150+2+self.y, 170+self.x-64, 160+2+self.y) #(+20,10) for all bandana
            canvas.coords(self.a_bandana2, 145+self.x-14, 150+2+self.y, 140+self.x-4, 152+2+self.y, 140+self.x-4, 160+2+self.y)
            canvas.coords(self.a_bandana3, 145+self.x-14, 150+2+self.y, 140+self.x-4, 148+2+self.y, 140+self.x-4, 151+2+self.y)
            canvas.coords(self.a_vneck, 140+self.x-4, 150+2+self.y, 145+self.x-14, 163+2+self.y, 125+self.x+26, 170+2+self.y, 115+self.x+46, 160+2+self.y) #(10,0), (0,8), (-20,-5), (-15,-15)
            canvas.coords(self.a_coat, 142+self.x-8, 145+2+self.y, 152+self.x-28, 155+2+self.y, 85+self.x+76, 183+2+self.y, 80+self.x+104, 183+2+self.y, 125+self.x+26, 155+2+self.y)

        #JUMP RIGHT
                    
        elif self.Frame == 0 and self.sprint == False and self.crouch == False and self.dropping == False and self.jumping == True: #Moving right without sprinting or crouching FRAME #1
            self.y -= 3 #Arms and legs out self.x    
            canvas.coords(self.a_head, 125+self.x, 125+self.y, 150+self.x, 150+self.y)
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 130+self.x, 150+self.y, 145+self.x, 150+self.y, 145+self.x, 175+self.y, 130+self.x, 175+self.y)
            canvas.coords(self.a_Larm, 115+self.x, 150+self.y, 130+self.x, 165+self.y)
            canvas.coords(self.a_Rarm, 145+self.x, 150+self.y, 160+self.x, 165+self.y)
            canvas.coords(self.a_Rleg, 145+self.x, 175+self.y, 160+self.x, 183+self.y)
            canvas.coords(self.a_Lleg, 115+self.x, 175+self.y, 130+self.x, 183+self.y)
            canvas.coords(self.a_bandana1, 125+self.x, 140+self.y, 150+self.x, 140+self.y, 150+self.x, 150+self.y)
            canvas.coords(self.a_bandana2, 125+self.x, 140+self.y, 120+self.x, 142+self.y, 120+self.x, 145+self.y)
            canvas.coords(self.a_bandana3, 125+self.x, 140+self.y, 120+self.x, 138+self.y, 120+self.x, 141+self.y)
            canvas.coords(self.a_vneck, 130+self.x, 150+self.y, 145+self.x, 155+self.y, 145+self.x, 175+self.y, 130+self.x, 175+self.y)
            canvas.coords(self.a_coat, 130+self.x, 145+self.y, 142+self.x, 145+self.y, 135+self.x, 175+self.y, 115+self.x, 177+self.y, 130+self.x, 160+self.y)
               
        elif self.Frame == 1 and self.sprint == False and self.crouch == False and self.dropping == False and self.jumping == True: #Moving right without sprinting or crouching FRAME #2
            self.y -= 3    
            canvas.coords(self.a_head, 125+self.x, 125+3+self.y, 150+self.x, 150+3+self.y)
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 130+self.x, 150+3+self.y, 145+self.x, 150+3+self.y, 145+self.x, 175+3+self.y, 130+self.x, 175+3+self.y)
            canvas.coords(self.a_Larm, 130+self.x, 160+self.y, 145+self.x, 175+self.y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO
            canvas.coords(self.a_Rarm, 130+self.x, 160+self.y, 145+self.x, 175+self.y) #Arm hides behind torso
            canvas.coords(self.a_Rleg, 145+self.x-10, 175+self.y, 160+self.x-10, 183+self.y)
            canvas.coords(self.a_Lleg, 115+self.x+10, 175+self.y, 130+self.x+10, 183+self.y)
            canvas.coords(self.a_bandana1, 125+self.x, 140+3+self.y, 150+self.x, 140+3+self.y, 150+self.x, 150+3+self.y)
            canvas.coords(self.a_bandana2, 125+self.x, 140+3+self.y, 120+self.x, 142+3+self.y, 120+self.x, 145+3+self.y)
            canvas.coords(self.a_bandana3, 125+self.x, 140+3+self.y, 120+self.x, 138+3+self.y, 120+self.x, 141+3+self.y)
            canvas.coords(self.a_vneck, 130+self.x, 150+3+self.y, 145+self.x, 155+3+self.y, 145+self.x, 175+3+self.y, 130+self.x, 175+3+self.y)
            canvas.coords(self.a_coat, 130+self.x, 145+3+self.y, 142+self.x, 145+3+self.y, 135+self.x, 175+3+self.y, 115+self.x, 177+6+self.y, 130+self.x, 160+self.y)

        elif self.Frame == 0 and self.sprint == True and self.crouch == False and self.dropping == False and self.jumping == True: #Moving right SPRINTING FRAME #1
            self.y -= 3    
            canvas.coords(self.a_head, 145+self.x, 135+self.y, 170+self.x, 160+self.y) #(+20, +10) difference from walking
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 140+self.x, 150+self.y, 150+self.x, 160+self.y, 125+self.x, 170+self.y, 115+self.x, 160+self.y) #(10, 0), (5,10), (-20,-5), (-15,-15)
            canvas.coords(self.a_Larm, 85+self.x, 150+self.y, 100+self.x, 165+self.y) #(-30,0)
            canvas.coords(self.a_Rarm, 175+self.x, 150+self.y, 190+self.x, 165+self.y) #(+30,0)
            canvas.coords(self.a_Rleg, 150+self.x, 170+self.y, 165+self.x, 178+self.y) #(+5,-5), (+5,-5)
            canvas.coords(self.a_Lleg, 110+self.x, 170+self.y, 125+self.x, 178+self.y) #(-5,-5), (-5,-5)
            canvas.coords(self.a_bandana1, 145+self.x, 150+self.y, 170+self.x, 150+self.y, 170+self.x, 160+self.y) #(+20,10) for all bandana
            canvas.coords(self.a_bandana2, 145+self.x, 150+self.y, 140+self.x, 152+self.y, 140+self.x, 160+self.y)
            canvas.coords(self.a_bandana3, 145+self.x, 150+self.y, 140+self.x, 148+self.y, 140+self.x, 151+self.y)
            canvas.coords(self.a_vneck, 140+self.x, 150+self.y, 145+self.x, 163+self.y, 125+self.x, 170+self.y, 115+self.x, 160+self.y) #(10,0), (0,8), (-20,-5), (-15,-15)
            canvas.coords(self.a_coat, 142+self.x, 145+self.y, 152+self.x, 155+self.y, 100+self.x, 175+self.y, 85+self.x, 157+self.y, 125+self.x, 155+self.y)
                
        elif self.Frame == 1 and self.sprint == True and self.crouch == False and self.dropping == False and self.jumping == True: #Moving right SPRINTING FRAME #2
            self.y -= 3    
            canvas.coords(self.a_head, 145+self.x, 135+5+self.y, 170+self.x, 160+5+self.y) #(+20, +10) difference from walking
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 140+self.x, 150+5+self.y, 150+self.x, 160+5+self.y, 125+self.x, 170+5+self.y, 115+self.x, 160+5+self.y) #(20, 10), (5,10)
            canvas.coords(self.a_Larm, 130+self.x, 160+self.y, 145+self.x, 175+self.y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
            canvas.coords(self.a_Rarm, 130+self.x, 160+self.y, 145+self.x, 175+self.y) #Arm hides behind torso (+30,0)
            canvas.coords(self.a_Rleg, 145+self.x-10, 175+self.y, 160+self.x-10, 183+self.y)
            canvas.coords(self.a_Lleg, 115+self.x+10, 175+self.y, 130+self.x+10, 183+self.y)
            canvas.coords(self.a_bandana1, 145+self.x, 150+5+self.y, 170+self.x, 150+5+self.y, 170+self.x, 160+5+self.y) #(+20,10) for all bandana
            canvas.coords(self.a_bandana2, 145+self.x, 150+5+self.y, 140+self.x, 152+5+self.y, 140+self.x, 155+5+self.y)
            canvas.coords(self.a_bandana3, 145+self.x, 150+5+self.y, 140+self.x, 148+5+self.y, 140+self.x, 151+5+self.y)
            canvas.coords(self.a_vneck, 140+self.x, 150+5+self.y, 145+self.x, 163+5+self.y, 125+self.x, 170+5+self.y, 115+self.x, 160+5+self.y) #(10,0), (0,8), (-20,-5), (-15,-15)
            canvas.coords(self.a_coat, 142+self.x, 145+5+self.y, 152+self.x, 155+5+self.y, 100+self.x, 175+10+self.y, 85+self.x, 157+10+self.y, 125+self.x, 155+5+self.y)

        elif self.Frame == 0 and self.sprint == False and self.crouch == True and self.dropping == False and self.jumping == True: #Moving right CROUCHING FRAMe #1
            self.y -= 3    
            canvas.coords(self.a_head, 145+self.x, 135+self.y, 170+self.x, 160+self.y) #(+20, +10) difference from walking
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 140+self.x, 150+self.y, 150+self.x, 160+self.y, 125+self.x, 170+self.y, 115+self.x, 160+self.y) #(10, 0), (5,10), (-20,-5), (-15,-15)
            canvas.coords(self.a_Larm, 130+self.x, 160+self.y, 145+self.x, 175+self.y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
            canvas.coords(self.a_Rarm, 130+self.x, 160+self.y, 145+self.x, 175+self.y) #Arm hides behind torso (+30,0)
            canvas.coords(self.a_Rleg, 145+self.x-5, 175+self.y, 160+self.x-5, 183+self.y) #(+5,-5), (+5,-5)
            canvas.coords(self.a_Lleg, 115+self.x+5, 175+self.y, 130+self.x+5, 183+self.y) #(-5,-5), (-5,-5)
            canvas.coords(self.a_bandana1, 145+self.x, 150+self.y, 170+self.x, 150+self.y, 170+self.x, 160+self.y) #(+20,10) for all bandana
            canvas.coords(self.a_bandana2, 145+self.x, 150+self.y, 140+self.x, 152+self.y, 140+self.x, 160+self.y)
            canvas.coords(self.a_bandana3, 145+self.x, 150+self.y, 140+self.x, 148+self.y, 140+self.x, 151+self.y)
            canvas.coords(self.a_vneck, 140+self.x, 150+self.y, 145+self.x, 163+self.y, 125+self.x, 170+self.y, 115+self.x, 160+self.y) #(10,0), (0,8), (-20,-5), (-15,-15)
            canvas.coords(self.a_coat, 142+self.x, 145+self.y, 152+self.x, 155+self.y, 115+self.x, 183+self.y, 92+self.x, 183+self.y, 125+self.x, 155+self.y)
                
        elif self.Frame == 1 and self.sprint == False and self.crouch == True and self.dropping == False and self.jumping == True: #Moving right CROUCHING FRAMe #2
            self.y -= 3
            canvas.coords(self.a_head, 145+self.x, 135+2+self.y, 170+self.x, 160+2+self.y) #(+20, +10) difference from walking
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 140+self.x, 150+2+self.y, 150+self.x, 160+2+self.y, 125+self.x, 170+2+self.y, 115+self.x, 160+2+self.y) #(20, 10), (5,10)
            canvas.coords(self.a_Larm, 130+self.x+10, 160+2+self.y, 145+self.x+10, 175+2+self.y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
            canvas.coords(self.a_Rarm, 130+self.x+10, 160+2+self.y, 145+self.x+10, 175+2+self.y) #Arm hides behind torso (+30,0)
            canvas.coords(self.a_Rleg, 145+self.x-10, 175+self.y, 160+self.x-10, 183+self.y)
            canvas.coords(self.a_Lleg, 115+self.x+10, 175+self.y, 130+self.x+10, 183+self.y)
            canvas.coords(self.a_bandana1, 145+self.x, 150+2+self.y, 170+self.x, 150+2+self.y, 170+self.x, 160+2+self.y) #(+20,10) for all bandana
            canvas.coords(self.a_bandana2, 145+self.x, 150+2+self.y, 140+self.x, 152+2+self.y, 140+self.x, 155+2+self.y)
            canvas.coords(self.a_bandana3, 145+self.x, 150+2+self.y, 140+self.x, 148+2+self.y, 140+self.x, 151+2+self.y)
            canvas.coords(self.a_vneck, 140+self.x, 150+2+self.y, 145+self.x, 163+2+self.y, 125+self.x, 170+2+self.y, 115+self.x, 160+2+self.y) #(10,0), (0,8), (-20,-5), (-15,-15)
            canvas.coords(self.a_coat, 142+self.x, 145+2+self.y, 152+self.x, 155+2+self.y, 115+self.x, 183+2+self.y, 92+self.x, 183+2+self.y, 125+self.x, 155+2+self.y)

        #DROPPING LEFT
        elif self.Frame == 0 and self.sprint == False and self.crouch == False and self.looking == "Left" and self.dropping == True: #Moving left without sprint or crouch FRAME #1
            self.y += 3
            canvas.coords(self.a_head, 125+self.x, 125+self.y, 150+self.x, 150+self.y)
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 130+self.x, 150+self.y, 145+self.x, 150+self.y, 145+self.x, 175+self.y, 130+self.x, 175+self.y)
            canvas.coords(self.a_Larm, 115+self.x, 150+self.y, 130+self.x, 165+self.y)
            canvas.coords(self.a_Rarm, 145+self.x, 150+self.y, 160+self.x, 165+self.y)
            canvas.coords(self.a_Rleg, 145+self.x, 175+self.y, 160+self.x, 183+self.y)
            canvas.coords(self.a_Lleg, 115+self.x, 175+self.y, 130+self.x, 183+self.y)
            canvas.coords(self.a_bandana1, 125+self.x+25, 140+self.y, 150+self.x-25, 140+self.y, 150+self.x-25, 150+self.y)
            canvas.coords(self.a_bandana2, 125+self.x+25, 140+self.y, 120+self.x+35, 142+self.y, 120+self.x+35, 145+self.y)
            canvas.coords(self.a_bandana3, 125+self.x+25, 140+self.y, 120+self.x+35, 138+self.y, 120+self.x+35, 141+self.y)
            canvas.coords(self.a_vneck, 130+self.x, 155+self.y, 145+self.x, 150+self.y, 145+self.x, 175+self.y, 130+self.x, 175+self.y)
            canvas.coords(self.a_coat, 145+self.x, 145+self.y, 133+self.x, 145+self.y, 140+self.x, 175+self.y, 160+self.x, 177+self.y, 145+self.x, 160+self.y)
  
        elif self.Frame == 1 and self.sprint == False and self.crouch == False and self.looking == "Left" and self.dropping == True: #Moving left without sprint or crouch FRAME #2
            self.y += 3    
            canvas.coords(self.a_head, 125+self.x, 125+3+self.y, 150+self.x, 150+3+self.y)
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 130+self.x, 150+3+self.y, 145+self.x, 150+3+self.y, 145+self.x, 175+3+self.y, 130+self.x, 175+3+self.y)
            canvas.coords(self.a_Larm, 130+self.x, 160+self.y, 145+self.x, 175+self.y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO
            canvas.coords(self.a_Rarm, 130+self.x, 160+self.y, 145+self.x, 175+self.y) #Arm hides behind torso
            canvas.coords(self.a_Rleg, 145+self.x-10, 175+self.y, 160+self.x-10, 183+self.y)
            canvas.coords(self.a_Lleg, 115+self.x+10, 175+self.y, 130+self.x+10, 183+self.y)
            canvas.coords(self.a_bandana1, 125+self.x+25, 140+3+self.y, 150+self.x-25, 140+3+self.y, 150+self.x-25, 150+3+self.y)
            canvas.coords(self.a_bandana2, 125+self.x+25, 140+3+self.y, 120+self.x+35, 142+3+self.y, 120+self.x+35, 145+3+self.y)
            canvas.coords(self.a_bandana3, 125+self.x+25, 140+3+self.y, 120+self.x+35, 138+3+self.y, 120+self.x+35, 141+3+self.y)
            canvas.coords(self.a_vneck, 130+self.x, 155+3+self.y, 145+self.x, 150+3+self.y, 145+self.x, 175+3+self.y, 130+self.x, 175+3+self.y)
            canvas.coords(self.a_coat, 145+self.x, 145+3+self.y, 133+self.x, 145+3+self.y, 140+self.x, 175+3+self.y, 160+self.x, 177+6+self.y, 145+self.x, 160+3+self.y)

        elif self.Frame == 0 and self.sprint == True and self.crouch == False and self.looking == "Left" and self.dropping == True: #Moving left SPRINTING FRAME #1
            self.y += 3    
            canvas.coords(self.a_head, 145+self.x-40, 135+self.y, 170+self.x-40, 160+self.y) #(+20, +10) difference from walking
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 140+self.x-4, 150+self.y, 150+self.x-24, 160+self.y, 125+self.x+26, 170+self.y, 115+self.x+46, 160+self.y) #(10, 0), (5,10), (-20,-5), (-15,-15)
            canvas.coords(self.a_Larm, 85+self.x+106, 150+self.y, 100+self.x+76, 165+self.y) #(-30,0)
            canvas.coords(self.a_Rarm, 175+self.x-74, 150+self.y, 190+self.x-104, 165+self.y) #(+30,0)
            canvas.coords(self.a_Rleg, 150+self.x-24, 170+self.y, 165+self.x-54, 178+self.y) #(+5,-5), (+5,-5)
            canvas.coords(self.a_Lleg, 110+self.x+56, 170+self.y, 125+self.x+26, 178+self.y) #(-5,-5), (-5,-5)
            canvas.coords(self.a_bandana1, 145+self.x-14, 150+self.y, 170+self.x-64, 150+self.y, 170+self.x-64, 160+self.y) #(+20,10) for all bandana
            canvas.coords(self.a_bandana2, 145+self.x-14, 150+self.y, 140+self.x-4, 152+self.y, 140+self.x-4, 160+self.y)
            canvas.coords(self.a_bandana3, 145+self.x-14, 150+self.y, 140+self.x-4, 148+self.y, 140+self.x-4, 151+self.y) 
            canvas.coords(self.a_vneck, 140+self.x-4, 150+self.y, 145+self.x-14, 163+self.y, 125+self.x+26, 170+self.y, 115+self.x+46, 160+self.y) #(10,0), (0,8), (-20,-5), (-15,-15)
            canvas.coords(self.a_coat, 142+self.x-8, 145+self.y, 152+self.x-28, 155+self.y, 100+self.x+76, 175+self.y, 85+self.x+104, 157+self.y, 125+self.x+26, 155+self.y)
                
        elif self.Frame == 1 and self.sprint == True and self.crouch == False and self.looking == "Left" and self.dropping == True: #Moving left SPRINTING FRAME #2
            self.y += 3    
            canvas.coords(self.a_head, 145+self.x-40, 135+5+self.y, 170+self.x-40, 160+5+self.y) #(+20, +10) difference from walking
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 140+self.x-4, 150+5+self.y, 150+self.x-24, 160+5+self.y, 125+self.x+26, 170+5+self.y, 115+self.x+46, 160+5+self.y) #(20, 10), (5,10)
            canvas.coords(self.a_Larm, 130+self.x+16, 160+self.y, 145+self.x-14, 175+self.y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
            canvas.coords(self.a_Rarm, 130+self.x+16, 160+self.y, 145+self.x-14, 175+self.y) #Arm hides behind torso (+30,0)
            canvas.coords(self.a_Rleg, 145+self.x-10, 175+self.y, 160+self.x-10, 183+self.y)
            canvas.coords(self.a_Lleg, 115+self.x+10, 175+self.y, 130+self.x+10, 183+self.y)
            canvas.coords(self.a_bandana1, 145+self.x-14, 150+5+self.y, 170+self.x-64, 150+5+self.y, 170+self.x-64, 160+5+self.y) #(+20,10) for all bandana
            canvas.coords(self.a_bandana2, 145+self.x-14, 150+5+self.y, 140+self.x-4, 152+5+self.y, 140+self.x-4, 160+5+self.y)
            canvas.coords(self.a_bandana3, 145+self.x-14, 150+5+self.y, 140+self.x-4, 148+5+self.y, 140+self.x-4, 151+5+self.y)
            canvas.coords(self.a_vneck, 140+self.x-4, 150+5+self.y, 145+self.x-14, 163+5+self.y, 125+self.x+26, 170+5+self.y, 115+self.x+46, 160+5+self.y) #(10,0), (0,8), (-20,-5), (-15,-15)
            canvas.coords(self.a_coat, 142+self.x-8, 145+5+self.y, 152+self.x-28, 155+5+self.y, 100+self.x+76, 175+10+self.y, 85+self.x+104, 157+10+self.y, 125+self.x+26, 155+5+self.y)

        elif self.Frame == 0 and self.sprint == False and self.crouch == True and self.looking == "Left" and self.dropping == True: #Moving left CROUCHING FRAME #1
            self.y += 3
            canvas.coords(self.a_head, 145+self.x-40, 135+self.y, 170+self.x-40, 160+self.y) #(+20, +10) difference from walking
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 140+self.x-4, 150+self.y, 150+self.x-24, 160+self.y, 125+self.x+26, 170+self.y, 115+self.x+46, 160+self.y) #(10, 0), (5,10), (-20,-5), (-15,-15)
            canvas.coords(self.a_Larm, 130+self.x+16, 160+self.y, 145+self.x-14, 175+self.y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
            canvas.coords(self.a_Rarm, 130+self.x+16, 160+self.y, 145+self.x-14, 175+self.y) #Arm hides behind torso (+30,0)
            canvas.coords(self.a_Rleg, 145+self.x-5, 175+self.y, 160+self.x-5, 183+self.y) #(+5,-5), (+5,-5)
            canvas.coords(self.a_Lleg, 115+self.x+5, 175+self.y, 130+self.x+5, 183+self.y) #(-5,-5), (-5,-5)
            canvas.coords(self.a_bandana1, 145+self.x-14, 150+self.y, 170+self.x-64, 150+self.y, 170+self.x-64, 160+self.y) #(+20,10) for all bandana
            canvas.coords(self.a_bandana2, 145+self.x-14, 150+self.y, 140+self.x-4, 152+self.y, 140+self.x-4, 160+self.y)
            canvas.coords(self.a_bandana3, 145+self.x-14, 150+self.y, 140+self.x-4, 148+self.y, 140+self.x-4, 151+self.y)
            canvas.coords(self.a_vneck, 140+self.x-4, 150+self.y, 145+self.x-14, 163+self.y, 125+self.x+26, 170+self.y, 115+self.x+46, 160+self.y) #(10,0), (0,8), (-20,-5), (-15,-15)
            canvas.coords(self.a_coat, 142+self.x-8, 145+self.y, 152+self.x-28, 155+self.y, 85+self.x+76, 183+self.y, 80+self.x+104, 183+self.y, 125+self.x+26, 155+self.y)
                
        elif self.Frame == 1 and self.sprint == False and self.crouch == True and self.looking == "Left" and self.dropping == True: #Moving left CROUCHING FRAME #2
            self.y += 3
            canvas.coords(self.a_head, 145+self.x-40, 135+2+self.y, 170+self.x-40, 160+2+self.y) #(+20, +10) difference from walking
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 140+self.x-4, 150+2+self.y, 150+self.x-24, 160+2+self.y, 125+self.x+26, 170+2+self.y, 115+self.x+46, 160+2+self.y) #(20, 10), (5,10)
            canvas.coords(self.a_Larm, 130+self.x-10, 160+2+self.y, 145+self.x-10, 175+2+self.y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
            canvas.coords(self.a_Rarm, 130+self.x-10, 160+2+self.y, 145+self.x-10, 175+2+self.y) #Arm hides behind torso (+30,0)
            canvas.coords(self.a_Rleg, 145+self.x-10, 175+self.y, 160+self.x-10, 183+self.y)
            canvas.coords(self.a_Lleg, 115+self.x+10, 175+self.y, 130+self.x+10, 183+self.y)
            canvas.coords(self.a_bandana1, 145+self.x-14, 150+2+self.y, 170+self.x-64, 150+2+self.y, 170+self.x-64, 160+2+self.y) #(+20,10) for all bandana
            canvas.coords(self.a_bandana2, 145+self.x-14, 150+2+self.y, 140+self.x-4, 152+2+self.y, 140+self.x-4, 160+2+self.y)
            canvas.coords(self.a_bandana3, 145+self.x-14, 150+2+self.y, 140+self.x-4, 148+2+self.y, 140+self.x-4, 151+2+self.y) 
            canvas.coords(self.a_vneck, 140+self.x-4, 150+2+self.y, 145+self.x-14, 163+2+self.y, 125+self.x+26, 170+2+self.y, 115+self.x+46, 160+2+self.y) #(10,0), (0,8), (-20,-5), (-15,-15)
            canvas.coords(self.a_coat, 142+self.x-8, 145+2+self.y, 152+self.x-28, 155+2+self.y, 85+self.x+76, 183+2+self.y, 80+self.x+104, 183+2+self.y, 125+self.x+26, 155+2+self.y)
        #Moving Right DROPPING       
        elif self.Frame == 0 and self.sprint == False and self.crouch == False and self.dropping == True: #Moving right without sprinting or crouching FRAME #1
            self.y += 3 #Arms and legs out self.x    
            canvas.coords(self.a_head, 125+self.x, 125+self.y, 150+self.x, 150+self.y)
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 130+self.x, 150+self.y, 145+self.x, 150+self.y, 145+self.x, 175+self.y, 130+self.x, 175+self.y)
            canvas.coords(self.a_Larm, 115+self.x, 150+self.y, 130+self.x, 165+self.y)
            canvas.coords(self.a_Rarm, 145+self.x, 150+self.y, 160+self.x, 165+self.y)
            canvas.coords(self.a_Rleg, 145+self.x, 175+self.y, 160+self.x, 183+self.y)
            canvas.coords(self.a_Lleg, 115+self.x, 175+self.y, 130+self.x, 183+self.y)
            canvas.coords(self.a_bandana1, 125+self.x, 140+self.y, 150+self.x, 140+self.y, 150+self.x, 150+self.y)
            canvas.coords(self.a_bandana2, 125+self.x, 140+self.y, 120+self.x, 142+self.y, 120+self.x, 145+self.y)
            canvas.coords(self.a_bandana3, 125+self.x, 140+self.y, 120+self.x, 138+self.y, 120+self.x, 141+self.y)
            canvas.coords(self.a_vneck, 130+self.x, 150+self.y, 145+self.x, 155+self.y, 145+self.x, 175+self.y, 130+self.x, 175+self.y)
            canvas.coords(self.a_coat, 130+self.x, 145+self.y, 142+self.x, 145+self.y, 135+self.x, 175+self.y, 115+self.x, 177+self.y, 130+self.x, 160+self.y)
               
        elif self.Frame == 1 and self.sprint == False and self.crouch == False and self.dropping == True: #Moving right without sprinting or crouching FRAME #2
            self.y += 3    
            canvas.coords(self.a_head, 125+self.x, 125+3+self.y, 150+self.x, 150+3+self.y)
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 130+self.x, 150+3+self.y, 145+self.x, 150+3+self.y, 145+self.x, 175+3+self.y, 130+self.x, 175+3+self.y)
            canvas.coords(self.a_Larm, 130+self.x, 160+self.y, 145+self.x, 175+self.y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO
            canvas.coords(self.a_Rarm, 130+self.x, 160+self.y, 145+self.x, 175+self.y) #Arm hides behind torso
            canvas.coords(self.a_Rleg, 145+self.x-10, 175+self.y, 160+self.x-10, 183+self.y)
            canvas.coords(self.a_Lleg, 115+self.x+10, 175+self.y, 130+self.x+10, 183+self.y)
            canvas.coords(self.a_bandana1, 125+self.x, 140+3+self.y, 150+self.x, 140+3+self.y, 150+self.x, 150+3+self.y)
            canvas.coords(self.a_bandana2, 125+self.x, 140+3+self.y, 120+self.x, 142+3+self.y, 120+self.x, 145+3+self.y)
            canvas.coords(self.a_bandana3, 125+self.x, 140+3+self.y, 120+self.x, 138+3+self.y, 120+self.x, 141+3+self.y)
            canvas.coords(self.a_vneck, 130+self.x, 150+3+self.y, 145+self.x, 155+3+self.y, 145+self.x, 175+3+self.y, 130+self.x, 175+3+self.y)
            canvas.coords(self.a_coat, 130+self.x, 145+3+self.y, 142+self.x, 145+3+self.y, 135+self.x, 175+3+self.y, 115+self.x, 177+6+self.y, 130+self.x, 160+self.y)
            
        elif self.Frame == 0 and self.sprint == True and self.crouch == False and self.dropping == True: #Moving right SPRINTING FRAME #1
            self.y += 3    
            canvas.coords(self.a_head, 145+self.x, 135+self.y, 170+self.x, 160+self.y) #(+20, +10) difference from walking
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 140+self.x, 150+self.y, 150+self.x, 160+self.y, 125+self.x, 170+self.y, 115+self.x, 160+self.y) #(10, 0), (5,10), (-20,-5), (-15,-15)
            canvas.coords(self.a_Larm, 85+self.x, 150+self.y, 100+self.x, 165+self.y) #(-30,0)
            canvas.coords(self.a_Rarm, 175+self.x, 150+self.y, 190+self.x, 165+self.y) #(+30,0)
            canvas.coords(self.a_Rleg, 150+self.x, 170+self.y, 165+self.x, 178+self.y) #(+5,-5), (+5,-5)
            canvas.coords(self.a_Lleg, 110+self.x, 170+self.y, 125+self.x, 178+self.y) #(-5,-5), (-5,-5)
            canvas.coords(self.a_bandana1, 145+self.x, 150+self.y, 170+self.x, 150+self.y, 170+self.x, 160+self.y) #(+20,10) for all bandana
            canvas.coords(self.a_bandana2, 145+self.x, 150+self.y, 140+self.x, 152+self.y, 140+self.x, 160+self.y)
            canvas.coords(self.a_bandana3, 145+self.x, 150+self.y, 140+self.x, 148+self.y, 140+self.x, 151+self.y)
            canvas.coords(self.a_vneck, 140+self.x, 150+self.y, 145+self.x, 163+self.y, 125+self.x, 170+self.y, 115+self.x, 160+self.y) #(10,0), (0,8), (-20,-5), (-15,-15)
            canvas.coords(self.a_coat, 142+self.x, 145+self.y, 152+self.x, 155+self.y, 100+self.x, 175+self.y, 85+self.x, 157+self.y, 125+self.x, 155+self.y)             
        elif self.Frame == 1 and self.sprint == True and self.crouch == False and self.dropping == True: #Moving right SPRINTING FRAME #2
            self.y += 3    
            canvas.coords(self.a_head, 145+self.x, 135+5+self.y, 170+self.x, 160+5+self.y) #(+20, +10) difference from walking
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 140+self.x, 150+5+self.y, 150+self.x, 160+5+self.y, 125+self.x, 170+5+self.y, 115+self.x, 160+5+self.y) #(20, 10), (5,10)
            canvas.coords(self.a_Larm, 130+self.x, 160+self.y, 145+self.x, 175+self.y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
            canvas.coords(self.a_Rarm, 130+self.x, 160+self.y, 145+self.x, 175+self.y) #Arm hides behind torso (+30,0)
            canvas.coords(self.a_Rleg, 145+self.x-10, 175+self.y, 160+self.x-10, 183+self.y)
            canvas.coords(self.a_Lleg, 115+self.x+10, 175+self.y, 130+self.x+10, 183+self.y)
            canvas.coords(self.a_bandana1, 145+self.x, 150+5+self.y, 170+self.x, 150+5+self.y, 170+self.x, 160+5+self.y) #(+20,10) for all bandana
            canvas.coords(self.a_bandana2, 145+self.x, 150+5+self.y, 140+self.x, 152+5+self.y, 140+self.x, 155+5+self.y)
            canvas.coords(self.a_bandana3, 145+self.x, 150+5+self.y, 140+self.x, 148+5+self.y, 140+self.x, 151+5+self.y)
            canvas.coords(self.a_vneck, 140+self.x, 150+5+self.y, 145+self.x, 163+5+self.y, 125+self.x, 170+5+self.y, 115+self.x, 160+5+self.y) #(10,0), (0,8), (-20,-5), (-15,-15)
            canvas.coords(self.a_coat, 142+self.x, 145+5+self.y, 152+self.x, 155+5+self.y, 100+self.x, 175+10+self.y, 85+self.x, 157+10+self.y, 125+self.x, 155+5+self.y)

        elif self.Frame == 0 and self.sprint == False and self.crouch == True and self.dropping == True: #Moving right CROUCHING FRAMe #1
            self.y += 3    
            canvas.coords(self.a_head, 145+self.x, 135+self.y, 170+self.x, 160+self.y) #(+20, +10) difference from walking
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 140+self.x, 150+self.y, 150+self.x, 160+self.y, 125+self.x, 170+self.y, 115+self.x, 160+self.y) #(10, 0), (5,10), (-20,-5), (-15,-15)
            canvas.coords(self.a_Larm, 130+self.x, 160+self.y, 145+self.x, 175+self.y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
            canvas.coords(self.a_Rarm, 130+self.x, 160+self.y, 145+self.x, 175+self.y) #Arm hides behind torso (+30,0)
            canvas.coords(self.a_Rleg, 145+self.x-5, 175+self.y, 160+self.x-5, 183+self.y) #(+5,-5), (+5,-5)
            canvas.coords(self.a_Lleg, 115+self.x+5, 175+self.y, 130+self.x+5, 183+self.y) #(-5,-5), (-5,-5)
            canvas.coords(self.a_bandana1, 145+self.x, 150+self.y, 170+self.x, 150+self.y, 170+self.x, 160+self.y) #(+20,10) for all bandana
            canvas.coords(self.a_bandana2, 145+self.x, 150+self.y, 140+self.x, 152+self.y, 140+self.x, 160+self.y)
            canvas.coords(self.a_bandana3, 145+self.x, 150+self.y, 140+self.x, 148+self.y, 140+self.x, 151+self.y)
            canvas.coords(self.a_vneck, 140+self.x, 150+self.y, 145+self.x, 163+self.y, 125+self.x, 170+self.y, 115+self.x, 160+self.y) #(10,0), (0,8), (-20,-5), (-15,-15)
            canvas.coords(self.a_coat, 142+self.x, 145+self.y, 152+self.x, 155+self.y, 115+self.x, 183+self.y, 92+self.x, 183+self.y, 125+self.x, 155+self.y)
              
        elif self.Frame == 1 and self.sprint == False and self.crouch == True and self.dropping == True: #Moving right CROUCHING FRAMe #2
            self.y += 3
            canvas.coords(self.a_head, 145+self.x, 135+2+self.y, 170+self.x, 160+2+self.y) #(+20, +10) difference from walking
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 140+self.x, 150+2+self.y, 150+self.x, 160+2+self.y, 125+self.x, 170+2+self.y, 115+self.x, 160+2+self.y) #(20, 10), (5,10)
            canvas.coords(self.a_Larm, 130+self.x+10, 160+2+self.y, 145+self.x+10, 175+2+self.y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
            canvas.coords(self.a_Rarm, 130+self.x+10, 160+2+self.y, 145+self.x+10, 175+2+self.y) #Arm hides behind torso (+30,0)
            canvas.coords(self.a_Rleg, 145+self.x-10, 175+self.y, 160+self.x-10, 183+self.y)
            canvas.coords(self.a_Lleg, 115+self.x+10, 175+self.y, 130+self.x+10, 183+self.y)
            canvas.coords(self.a_bandana1, 145+self.x, 150+2+self.y, 170+self.x, 150+2+self.y, 170+self.x, 160+2+self.y) #(+20,10) for all bandana
            canvas.coords(self.a_bandana2, 145+self.x, 150+2+self.y, 140+self.x, 152+2+self.y, 140+self.x, 155+2+self.y)
            canvas.coords(self.a_bandana3, 145+self.x, 150+2+self.y, 140+self.x, 148+2+self.y, 140+self.x, 151+2+self.y)
            canvas.coords(self.a_vneck, 140+self.x, 150+2+self.y, 145+self.x, 163+2+self.y, 125+self.x, 170+2+self.y, 115+self.x, 160+2+self.y) #(10,0), (0,8), (-20,-5), (-15,-15)
            canvas.coords(self.a_coat, 142+self.x, 145+2+self.y, 152+self.x, 155+2+self.y, 115+self.x, 183+2+self.y, 92+self.x, 183+2+self.y, 125+self.x, 155+2+self.y)     

        #MOVING LEFT NOT IN AIR
        elif self.Frame == 0 and self.sprint == False and self.crouch == False and self.looking == "Left": #Moving left without sprint or crouch FRAME #1
            self.x -= 1 #Arms and leg out
            canvas.coords(self.a_head, 125+self.x, 125+self.y, 150+self.x, 150+self.y)
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 130+self.x, 150+self.y, 145+self.x, 150+self.y, 145+self.x, 175+self.y, 130+self.x, 175+self.y)
            canvas.coords(self.a_Larm, 115+self.x, 150+self.y, 130+self.x, 165+self.y)
            canvas.coords(self.a_Rarm, 145+self.x, 150+self.y, 160+self.x, 165+self.y)
            canvas.coords(self.a_Rleg, 145+self.x, 175+self.y, 160+self.x, 183+self.y)
            canvas.coords(self.a_Lleg, 115+self.x, 175+self.y, 130+self.x, 183+self.y)
            canvas.coords(self.a_bandana1, 125+self.x+25, 140+self.y, 150+self.x-25, 140+self.y, 150+self.x-25, 150+self.y)
            canvas.coords(self.a_bandana2, 125+self.x+25, 140+self.y, 120+self.x+35, 142+self.y, 120+self.x+35, 145+self.y)
            canvas.coords(self.a_bandana3, 125+self.x+25, 140+self.y, 120+self.x+35, 138+self.y, 120+self.x+35, 141+self.y)
            canvas.coords(self.a_vneck, 130+self.x, 155+self.y, 145+self.x, 150+self.y, 145+self.x, 175+self.y, 130+self.x, 175+self.y)
            canvas.coords(self.a_coat, 145+self.x, 145+self.y, 133+self.x, 145+self.y, 140+self.x, 175+self.y, 160+self.x, 177+self.y, 145+self.x, 160+self.y)
                
        elif self.Frame == 1 and self.sprint == False and self.crouch == False and self.looking == "Left": #Moving left without sprint or crouch FRAME #2
            self.x -= 1 #Arms and legs in
            canvas.coords(self.a_head, 125+self.x, 125+3+self.y, 150+self.x, 150+3+self.y)
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 130+self.x, 150+3+self.y, 145+self.x, 150+3+self.y, 145+self.x, 175+3+self.y, 130+self.x, 175+3+self.y)
            canvas.coords(self.a_Larm, 130+self.x, 160+self.y, 145+self.x, 175+self.y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO
            canvas.coords(self.a_Rarm, 130+self.x, 160+self.y, 145+self.x, 175+self.y) #Arm hides behind torso
            canvas.coords(self.a_Rleg, 145+self.x-10, 175+self.y, 160+self.x-10, 183+self.y)
            canvas.coords(self.a_Lleg, 115+self.x+10, 175+self.y, 130+self.x+10, 183+self.y)
            canvas.coords(self.a_bandana1, 125+self.x+25, 140+3+self.y, 150+self.x-25, 140+3+self.y, 150+self.x-25, 150+3+self.y)
            canvas.coords(self.a_bandana2, 125+self.x+25, 140+3+self.y, 120+self.x+35, 142+3+self.y, 120+self.x+35, 145+3+self.y)
            canvas.coords(self.a_bandana3, 125+self.x+25, 140+3+self.y, 120+self.x+35, 138+3+self.y, 120+self.x+35, 141+3+self.y)
            canvas.coords(self.a_vneck, 130+self.x, 155+3+self.y, 145+self.x, 150+3+self.y, 145+self.x, 175+3+self.y, 130+self.x, 175+3+self.y)
            canvas.coords(self.a_coat, 145+self.x, 145+3+self.y, 133+self.x, 145+3+self.y, 140+self.x, 175+3+self.y, 160+self.x, 177+6+self.y, 145+self.x, 160+3+self.y)

        elif self.Frame == 0 and self.sprint == True and self.crouch == False and self.looking == "Left": #Moving left SPRINTING FRAME #1
            self.x -= 1 #Arms and legs out
            canvas.coords(self.a_head, 145+self.x-40, 135+self.y, 170+self.x-40, 160+self.y) #(+20, +10) difference from walking
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 140+self.x-4, 150+self.y, 150+self.x-24, 160+self.y, 125+self.x+26, 170+self.y, 115+self.x+46, 160+self.y) #(10, 0), (5,10), (-20,-5), (-15,-15)
            canvas.coords(self.a_Larm, 85+self.x+106, 150+self.y, 100+self.x+76, 165+self.y) #(-30,0)
            canvas.coords(self.a_Rarm, 175+self.x-74, 150+self.y, 190+self.x-104, 165+self.y) #(+30,0)
            canvas.coords(self.a_Rleg, 150+self.x-24, 170+self.y, 165+self.x-54, 178+self.y) #(+5,-5), (+5,-5)
            canvas.coords(self.a_Lleg, 110+self.x+56, 170+self.y, 125+self.x+26, 178+self.y) #(-5,-5), (-5,-5)
            canvas.coords(self.a_bandana1, 145+self.x-14, 150+self.y, 170+self.x-64, 150+self.y, 170+self.x-64, 160+self.y) #(+20,10) for all bandana
            canvas.coords(self.a_bandana2, 145+self.x-14, 150+self.y, 140+self.x-4, 152+self.y, 140+self.x-4, 160+self.y)
            canvas.coords(self.a_bandana3, 145+self.x-14, 150+self.y, 140+self.x-4, 148+self.y, 140+self.x-4, 151+self.y)
            canvas.coords(self.a_vneck, 140+self.x-4, 150+self.y, 145+self.x-14, 163+self.y, 125+self.x+26, 170+self.y, 115+self.x+46, 160+self.y) #(10,0), (0,8), (-20,-5), (-15,-15)
            canvas.coords(self.a_coat, 142+self.x-8, 145+self.y, 152+self.x-28, 155+self.y, 100+self.x+76, 175+self.y, 85+self.x+104, 157+self.y, 125+self.x+26, 155+self.y)
            self.x -= 3
            #(12,0) (10,10), (-35,0), (-30,-20), (-5,-5)
                
        elif self.Frame == 1 and self.sprint == True and self.crouch == False and self.looking == "Left": #Moving left SPRINTING FRAME #2
            self.x -= 1 #Arms and legs in
            canvas.coords(self.a_head, 145+self.x-40, 135+5+self.y, 170+self.x-40, 160+5+self.y) #(+20, +10) difference from walking
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 140+self.x-4, 150+5+self.y, 150+self.x-24, 160+5+self.y, 125+self.x+26, 170+5+self.y, 115+self.x+46, 160+5+self.y) #(20, 10), (5,10)
            canvas.coords(self.a_Larm, 130+self.x+16, 160+self.y, 145+self.x-14, 175+self.y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
            canvas.coords(self.a_Rarm, 130+self.x+16, 160+self.y, 145+self.x-14, 175+self.y) #Arm hides behind torso (+30,0)
            canvas.coords(self.a_Rleg, 145+self.x-10, 175+self.y, 160+self.x-10, 183+self.y)
            canvas.coords(self.a_Lleg, 115+self.x+10, 175+self.y, 130+self.x+10, 183+self.y)
            canvas.coords(self.a_bandana1, 145+self.x-14, 150+5+self.y, 170+self.x-64, 150+5+self.y, 170+self.x-64, 160+5+self.y) #(+20,10) for all bandana
            canvas.coords(self.a_bandana2, 145+self.x-14, 150+5+self.y, 140+self.x-4, 152+5+self.y, 140+self.x-4, 160+5+self.y)
            canvas.coords(self.a_bandana3, 145+self.x-14, 150+5+self.y, 140+self.x-4, 148+5+self.y, 140+self.x-4, 151+5+self.y) 
            canvas.coords(self.a_vneck, 140+self.x-4, 150+5+self.y, 145+self.x-14, 163+5+self.y, 125+self.x+26, 170+5+self.y, 115+self.x+46, 160+5+self.y) #(10,0), (0,8), (-20,-5), (-15,-15)
            canvas.coords(self.a_coat, 142+self.x-8, 145+5+self.y, 152+self.x-28, 155+5+self.y, 100+self.x+76, 175+10+self.y, 85+self.x+104, 157+10+self.y, 125+self.x+26, 155+5+self.y)
            #(12,0) (10,10), (-35,0), (-30,-20), (-5,-5)
            self.x -= 3

        elif self.Frame == 0 and self.sprint == False and self.crouch == True and self.looking == "Left": #Moving left CROUCHING FRAME #1
            self.x -= 0.5 #Arms and legs out self.x 
            canvas.coords(self.a_head, 145+self.x-40, 135+self.y, 170+self.x-40, 160+self.y) #(+20, +10) difference from walking
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 140+self.x-4, 150+self.y, 150+self.x-24, 160+self.y, 125+self.x+26, 170+self.y, 115+self.x+46, 160+self.y) #(10, 0), (5,10), (-20,-5), (-15,-15)
            canvas.coords(self.a_Larm, 130+self.x+16, 160+self.y, 145+self.x-14, 175+self.y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
            canvas.coords(self.a_Rarm, 130+self.x+16, 160+self.y, 145+self.x-14, 175+self.y) #Arm hides behind torso (+30,0)
            canvas.coords(self.a_Rleg, 145+self.x-5, 175+self.y, 160+self.x-5, 183+self.y) #(+5,-5), (+5,-5)
            canvas.coords(self.a_Lleg, 115+self.x+5, 175+self.y, 130+self.x+5, 183+self.y) #(-5,-5), (-5,-5)
            canvas.coords(self.a_bandana1, 145+self.x-14, 150+self.y, 170+self.x-64, 150+self.y, 170+self.x-64, 160+self.y) #(+20,10) for all bandana
            canvas.coords(self.a_bandana2, 145+self.x-14, 150+self.y, 140+self.x-4, 152+self.y, 140+self.x-4, 160+self.y)
            canvas.coords(self.a_bandana3, 145+self.x-14, 150+self.y, 140+self.x-4, 148+self.y, 140+self.x-4, 151+self.y)
            canvas.coords(self.a_vneck, 140+self.x-4, 150+self.y, 145+self.x-14, 163+self.y, 125+self.x+26, 170+self.y, 115+self.x+46, 160+self.y) #(10,0), (0,8), (-20,-5), (-15,-15)
            canvas.coords(self.a_coat, 142+self.x-8, 145+self.y, 152+self.x-28, 155+self.y, 85+self.x+76, 183+self.y, 80+self.x+104, 183+self.y, 125+self.x+26, 155+self.y)
                
        elif self.Frame == 1 and self.sprint == False and self.crouch == True and self.looking == "Left": #Moving left CROUCHING FRAME #2
            self.x -= 0.5 #Arms and legs in
            canvas.coords(self.a_head, 145+self.x-40, 135+2+self.y, 170+self.x-40, 160+2+self.y) #(+20, +10) difference from walking
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 140+self.x-4, 150+2+self.y, 150+self.x-24, 160+2+self.y, 125+self.x+26, 170+2+self.y, 115+self.x+46, 160+2+self.y) #(20, 10), (5,10)
            canvas.coords(self.a_Larm, 130+self.x-10, 160+2+self.y, 145+self.x-10, 175+2+self.y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
            canvas.coords(self.a_Rarm, 130+self.x-10, 160+2+self.y, 145+self.x-10, 175+2+self.y) #Arm hides behind torso (+30,0)
            canvas.coords(self.a_Rleg, 145+self.x-10, 175+self.y, 160+self.x-10, 183+self.y)
            canvas.coords(self.a_Lleg, 115+self.x+10, 175+self.y, 130+self.x+10, 183+self.y)
            canvas.coords(self.a_bandana1, 145+self.x-14, 150+2+self.y, 170+self.x-64, 150+2+self.y, 170+self.x-64, 160+2+self.y) #(+20,10) for all bandana
            canvas.coords(self.a_bandana2, 145+self.x-14, 150+2+self.y, 140+self.x-4, 152+2+self.y, 140+self.x-4, 160+2+self.y)
            canvas.coords(self.a_bandana3, 145+self.x-14, 150+2+self.y, 140+self.x-4, 148+2+self.y, 140+self.x-4, 151+2+self.y) 
            canvas.coords(self.a_vneck, 140+self.x-4, 150+2+self.y, 145+self.x-14, 163+2+self.y, 125+self.x+26, 170+2+self.y, 115+self.x+46, 160+2+self.y) #(10,0), (0,8), (-20,-5), (-15,-15)
            canvas.coords(self.a_coat, 142+self.x-8, 145+2+self.y, 152+self.x-28, 155+2+self.y, 85+self.x+76, 183+2+self.y, 80+self.x+104, 183+2+self.y, 125+self.x+26, 155+2+self.y)
            #(12,0) (10,10), (-35,0), (-30,-20), (-5,-5)


        #MOVING RIGHT NOT IN AIR
        elif self.Frame == 0 and self.sprint == False and self.crouch == False and self.looking == "Right": #Moving right without sprinting or crouching FRAME #1
            self.x += 1 #Arms and legs out self.x 
            canvas.coords(self.a_head, 125+self.x, 125+self.y, 150+self.x, 150+self.y)
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 130+self.x, 150+self.y, 145+self.x, 150+self.y, 145+self.x, 175+self.y, 130+self.x, 175+self.y)
            canvas.coords(self.a_Larm, 115+self.x, 150+self.y, 130+self.x, 165+self.y)
            canvas.coords(self.a_Rarm, 145+self.x, 150+self.y, 160+self.x, 165+self.y)
            canvas.coords(self.a_Rleg, 145+self.x, 175+self.y, 160+self.x, 183+self.y)
            canvas.coords(self.a_Lleg, 115+self.x, 175+self.y, 130+self.x, 183+self.y)
            canvas.coords(self.a_bandana1, 125+self.x, 140+self.y, 150+self.x, 140+self.y, 150+self.x, 150+self.y)
            canvas.coords(self.a_bandana2, 125+self.x, 140+self.y, 120+self.x, 142+self.y, 120+self.x, 145+self.y)
            canvas.coords(self.a_bandana3, 125+self.x, 140+self.y, 120+self.x, 138+self.y, 120+self.x, 141+self.y)
            canvas.coords(self.a_vneck, 130+self.x, 150+self.y, 145+self.x, 155+self.y, 145+self.x, 175+self.y, 130+self.x, 175+self.y)
            canvas.coords(self.a_coat, 130+self.x, 145+self.y, 142+self.x, 145+self.y, 135+self.x, 175+self.y, 115+self.x, 177+self.y, 130+self.x, 160+self.y)
                
        elif self.Frame == 1 and self.sprint == False and self.crouch == False and self.looking == "Right": #Moving right without sprinting or crouching FRAME #2
            self.x += 1 #Arms and legs in
            canvas.coords(self.a_head, 125+self.x, 125+3+self.y, 150+self.x, 150+3+self.y)
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 130+self.x, 150+3+self.y, 145+self.x, 150+3+self.y, 145+self.x, 175+3+self.y, 130+self.x, 175+3+self.y)
            canvas.coords(self.a_Larm, 130+self.x, 160+self.y, 145+self.x, 175+self.y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO
            canvas.coords(self.a_Rarm, 130+self.x, 160+self.y, 145+self.x, 175+self.y) #Arm hides behind torso
            canvas.coords(self.a_Rleg, 145+self.x-10, 175+self.y, 160+self.x-10, 183+self.y)
            canvas.coords(self.a_Lleg, 115+self.x+10, 175+self.y, 130+self.x+10, 183+self.y)
            canvas.coords(self.a_bandana1, 125+self.x, 140+3+self.y, 150+self.x, 140+3+self.y, 150+self.x, 150+3+self.y)
            canvas.coords(self.a_bandana2, 125+self.x, 140+3+self.y, 120+self.x, 142+3+self.y, 120+self.x, 145+3+self.y)
            canvas.coords(self.a_bandana3, 125+self.x, 140+3+self.y, 120+self.x, 138+3+self.y, 120+self.x, 141+3+self.y)
            canvas.coords(self.a_vneck, 130+self.x, 150+3+self.y, 145+self.x, 155+3+self.y, 145+self.x, 175+3+self.y, 130+self.x, 175+3+self.y)
            canvas.coords(self.a_coat, 130+self.x, 145+3+self.y, 142+self.x, 145+3+self.y, 135+self.x, 175+3+self.y, 115+self.x, 177+6+self.y, 130+self.x, 160+self.y)

        elif self.Frame == 0 and self.sprint == True and self.crouch == False and self.looking == "Right": #Moving right SPRINTING FRAME #1
            self.x += 1 #Arms and legs out
            canvas.coords(self.a_head, 145+self.x, 135+self.y, 170+self.x, 160+self.y) #(+20, +10) difference from walking
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 140+self.x, 150+self.y, 150+self.x, 160+self.y, 125+self.x, 170+self.y, 115+self.x, 160+self.y) #(10, 0), (5,10), (-20,-5), (-15,-15)
            canvas.coords(self.a_Larm, 85+self.x, 150+self.y, 100+self.x, 165+self.y) #(-30,0)
            canvas.coords(self.a_Rarm, 175+self.x, 150+self.y, 190+self.x, 165+self.y) #(+30,0)
            canvas.coords(self.a_Rleg, 150+self.x, 170+self.y, 165+self.x, 178+self.y) #(+5,-5), (+5,-5)
            canvas.coords(self.a_Lleg, 110+self.x, 170+self.y, 125+self.x, 178+self.y) #(-5,-5), (-5,-5)
            canvas.coords(self.a_bandana1, 145+self.x, 150+self.y, 170+self.x, 150+self.y, 170+self.x, 160+self.y) #(+20,10) for all bandana
            canvas.coords(self.a_bandana2, 145+self.x, 150+self.y, 140+self.x, 152+self.y, 140+self.x, 160+self.y)
            canvas.coords(self.a_bandana3, 145+self.x, 150+self.y, 140+self.x, 148+self.y, 140+self.x, 151+self.y) 
            canvas.coords(self.a_vneck, 140+self.x, 150+self.y, 145+self.x, 163+self.y, 125+self.x, 170+self.y, 115+self.x, 160+self.y) #(10,0), (0,8), (-20,-5), (-15,-15)
            canvas.coords(self.a_coat, 142+self.x, 145+self.y, 152+self.x, 155+self.y, 100+self.x, 175+self.y, 85+self.x, 157+self.y, 125+self.x, 155+self.y)
            self.x += 3
            #(12,0) (10,10), (-35,0), (-30,-20), (-5,-5)
                
        elif self.Frame == 1 and self.sprint == True and self.crouch == False and self.looking == "Right": #Moving right SPRINTING FRAME #2
            self.x += 1 #Arms and legs in
            canvas.coords(self.a_head, 145+self.x, 135+5+self.y, 170+self.x, 160+5+self.y) #(+20, +10) difference from walking
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 140+self.x, 150+5+self.y, 150+self.x, 160+5+self.y, 125+self.x, 170+5+self.y, 115+self.x, 160+5+self.y) #(20, 10), (5,10)
            canvas.coords(self.a_Larm, 130+self.x, 160+self.y, 145+self.x, 175+self.y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
            canvas.coords(self.a_Rarm, 130+self.x, 160+self.y, 145+self.x, 175+self.y) #Arm hides behind torso (+30,0)
            canvas.coords(self.a_Rleg, 145+self.x-10, 175+self.y, 160+self.x-10, 183+self.y)
            canvas.coords(self.a_Lleg, 115+self.x+10, 175+self.y, 130+self.x+10, 183+self.y)
            canvas.coords(self.a_bandana1, 145+self.x, 150+5+self.y, 170+self.x, 150+5+self.y, 170+self.x, 160+5+self.y) #(+20,10) for all bandana
            canvas.coords(self.a_bandana2, 145+self.x, 150+5+self.y, 140+self.x, 152+5+self.y, 140+self.x, 155+5+self.y)
            canvas.coords(self.a_bandana3, 145+self.x, 150+5+self.y, 140+self.x, 148+5+self.y, 140+self.x, 151+5+self.y)
            canvas.coords(self.a_vneck, 140+self.x, 150+5+self.y, 145+self.x, 163+5+self.y, 125+self.x, 170+5+self.y, 115+self.x, 160+5+self.y) #(10,0), (0,8), (-20,-5), (-15,-15)
            canvas.coords(self.a_coat, 142+self.x, 145+5+self.y, 152+self.x, 155+5+self.y, 100+self.x, 175+10+self.y, 85+self.x, 157+10+self.y, 125+self.x, 155+5+self.y)
            #(12,0) (10,10), (-35,0), (-30,-20), (-5,-5)
            self.x += 3

        elif self.Frame == 0 and self.sprint == False and self.crouch == True and self.looking == "Right": #Moving right CROUCHING FRAMe #1
            self.x += 0.5 #Arms and legs in
            canvas.coords(self.a_head, 145+self.x, 135+self.y, 170+self.x, 160+self.y) #(+20, +10) difference from walking
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 140+self.x, 150+self.y, 150+self.x, 160+self.y, 125+self.x, 170+self.y, 115+self.x, 160+self.y) #(10, 0), (5,10), (-20,-5), (-15,-15)
            canvas.coords(self.a_Larm, 130+self.x, 160+self.y, 145+self.x, 175+self.y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
            canvas.coords(self.a_Rarm, 130+self.x, 160+self.y, 145+self.x, 175+self.y) #Arm hides behind torso (+30,0)
            canvas.coords(self.a_Rleg, 145+self.x-5, 175+self.y, 160+self.x-5, 183+self.y) #(+5,-5), (+5,-5)
            canvas.coords(self.a_Lleg, 115+self.x+5, 175+self.y, 130+self.x+5, 183+self.y) #(-5,-5), (-5,-5)
            canvas.coords(self.a_bandana1, 145+self.x, 150+self.y, 170+self.x, 150+self.y, 170+self.x, 160+self.y) #(+20,10) for all bandana
            canvas.coords(self.a_bandana2, 145+self.x, 150+self.y, 140+self.x, 152+self.y, 140+self.x, 160+self.y)
            canvas.coords(self.a_bandana3, 145+self.x, 150+self.y, 140+self.x, 148+self.y, 140+self.x, 151+self.y)
            canvas.coords(self.a_vneck, 140+self.x, 150+self.y, 145+self.x, 163+self.y, 125+self.x, 170+self.y, 115+self.x, 160+self.y) #(10,0), (0,8), (-20,-5), (-15,-15)
            canvas.coords(self.a_coat, 142+self.x, 145+self.y, 152+self.x, 155+self.y, 115+self.x, 183+self.y, 92+self.x, 183+self.y, 125+self.x, 155+self.y)
                
        elif self.Frame == 1 and self.sprint == False and self.crouch == True and self.looking == "Right": #Moving right CROUCHING FRAMe #2
            self.x += 0.5 #Arms and legs in
            canvas.coords(self.a_head, 145+self.x, 135+2+self.y, 170+self.x, 160+2+self.y) #(+20, +10) difference from walking
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 140+self.x, 150+2+self.y, 150+self.x, 160+2+self.y, 125+self.x, 170+2+self.y, 115+self.x, 160+2+self.y) #(20, 10), (5,10)
            canvas.coords(self.a_Larm, 130+self.x+10, 160+2+self.y, 145+self.x+10, 175+2+self.y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
            canvas.coords(self.a_Rarm, 130+self.x+10, 160+2+self.y, 145+self.x+10, 175+2+self.y) #Arm hides behind torso (+30,0)
            canvas.coords(self.a_Rleg, 145+self.x-10, 175+self.y, 160+self.x-10, 183+self.y)
            canvas.coords(self.a_Lleg, 115+self.x+10, 175+self.y, 130+self.x+10, 183+self.y)
            canvas.coords(self.a_bandana1, 145+self.x, 150+2+self.y, 170+self.x, 150+2+self.y, 170+self.x, 160+2+self.y) #(+20,10) for all bandana
            canvas.coords(self.a_bandana2, 145+self.x, 150+2+self.y, 140+self.x, 152+2+self.y, 140+self.x, 155+2+self.y)
            canvas.coords(self.a_bandana3, 145+self.x, 150+2+self.y, 140+self.x, 148+2+self.y, 140+self.x, 151+2+self.y)
            canvas.coords(self.a_vneck, 140+self.x, 150+2+self.y, 145+self.x, 163+2+self.y, 125+self.x, 170+2+self.y, 115+self.x, 160+2+self.y) #(10,0), (0,8), (-20,-5), (-15,-15)
            canvas.coords(self.a_coat, 142+self.x, 145+2+self.y, 152+self.x, 155+2+self.y, 115+self.x, 183+2+self.y, 92+self.x, 183+2+self.y, 125+self.x, 155+2+self.y)


        self.checkerFrame += 1 #Add one to checkerFrame (Starts at 0)
        
        if self.checkerFrame <= 25: #Once 25 iterations of draw() in the while loop far far below, change frame to 0
            self.Frame = 0
        else: #if self.checkerFrame > 25: #Once 50 iterations of draw() in the while loop far far below, change frame to 1
            self.Frame = 1
            
        if self.checkerFrame == 50: #Reset the counter after 50 so that the cycle repeats over and over again.
            self.checkerFrame = 0

        if self.jumping == True:
            self.dropping = False

        if self.dropping == True:
            self.jumping = False

        if self.jumping == True or self.dropping == True:
            self.inAirCounter += 1

        if self.inAirCounter == 30:
            self.jumping = False
            self.dropping = False
            self.inAirCounter = 0
            canvas.after(100, self.rebindS) #2000 ms = 2 seconds Later will need to redo this part because not all falling is going to be 2 seconds long.
            canvas.after(100, self.rebindW) #2000 ms = 2 seconds Later will need to redo this part because not all falling is going to be 2 seconds long.

        canvas.update()
            
    def aKey(self, evt):
        self.looking = "Left"
        self.checker = 0
        self.notMoving = False
        
    def dKey(self,evt):
        self.looking = "Right"
        self.checker = 0
        self.notMoving = False
        
    def spaceKey(self, evt): #Special ability: Voice
        #canvas.unbind("<space>", self.b_space)
        global voiceOn
        if voiceOn == True:
            print("Special on cooldown!")
        else:
            print("Special activated.")
            voiceOn = True
        #canvas.after(100, self.rebindSpace) #MOVED TO BOTTOM OF VOICE.DRAW()
        
    def rebindSpace(self):
        global voiceOn
        self.b_space = canvas.bind("<space>", self.spaceKey)

    def eKey(self, evt): #Action Key
        print("'e' key pressed")
        

    def qKey(self, evt): #Switch weapons
        print("'q' key pressed")

    def sKey(self, evt): #Drop down
        #print("'s' key pressed")
        #print("Making inAir equal True")
        self.inAir = True
        self.dropping = True
        #print("Disabling 's' binding") #Makes sure the user does not spam this animation DURING the animation.
        canvas.unbind("<s>", self.b_s)
        canvas.unbind("<w>", self.b_w)
        #canvas.after(100, self.rebindS) #2000 ms = 2 seconds Later will need to redo this part because not all falling is going to be 2 seconds long.

    def rebindS(self): #Rebinds S (falling should be done and can fall again)
        self.b_s = canvas.bind("<s>", self.sKey)
        #print("Rebinding 's' and making inAir=False")
        self.inAir=False

    def wKey(self, evt): #Jump
        #print("'w' key pressed")
        #print("Making inAir equal True")
        self.inAir = True
        self.jumping = True
        #print("Disabling 'w' binding") #Makes sure the user does not spam this animation DURING the animation.
        canvas.unbind("<w>", self.b_w)
        canvas.unbind("<s>", self.b_s)
        #canvas.after(100, self.rebindW) #2000 ms = 2 seconds Later will need to redo this part because not all falling is going to be 2 seconds long.

    def rebindW(self): #Rebinds W (falling should be done and can fall again)
        self.b_w = canvas.bind("<w>", self.wKey)
        #print("Rebinding 'w' and making inAir=False")
        self.inAir=False

    def rebindleftClick(self):
        self.b_leftClick = canvas.bind("<Button-1>", self.leftClick)
        global basic_attack
        print("Basic attack still in animtion")
        basic_attack = False

    def drawAttack(self):
        global basic_attack
        if basic_attack == False:
            print("basic_attack = False CANNOT ENTER THIS PLACE USUALLY")
        #MOVING LEFT NOT IN AIR - PUNCHING
        
        elif self.Frame == 1  and self.looking == "Left" and self.forward == True: #Moving left without sprint or crouch # and self.crouch == False 
            self.moveFists -= 2
            canvas.coords(self.a_head, 125+self.x, 125+3+self.y, 150+self.x, 150+3+self.y)
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 130+self.x, 150+3+self.y, 145+self.x, 150+3+self.y, 145+self.x, 175+3+self.y, 130+self.x, 175+3+self.y)
            canvas.coords(self.a_Larm, 115+self.x, 150+self.y+2, 130+self.x, 165+self.y+2) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO
            canvas.coords(self.a_Rarm, 115+self.x+self.moveFists, 150+self.y, 130+self.x+self.moveFists, 165+self.y) #Arm hides behind torso
            canvas.coords(self.a_Rleg, 145+self.x-10, 175+self.y, 160+self.x-10, 183+self.y)
            canvas.coords(self.a_Lleg, 115+self.x+10, 175+self.y, 130+self.x+10, 183+self.y)
            canvas.coords(self.a_bandana1, 125+self.x+25, 140+3+self.y, 150+self.x-25, 140+3+self.y, 150+self.x-25, 150+3+self.y)
            canvas.coords(self.a_bandana2, 125+self.x+25, 140+3+self.y, 120+self.x+35, 142+3+self.y, 120+self.x+35, 145+3+self.y)
            canvas.coords(self.a_bandana3, 125+self.x+25, 140+3+self.y, 120+self.x+35, 138+3+self.y, 120+self.x+35, 141+3+self.y)
            canvas.coords(self.a_vneck, 130+self.x, 155+3+self.y, 145+self.x, 150+3+self.y, 145+self.x, 175+3+self.y, 130+self.x, 175+3+self.y)
            canvas.coords(self.a_coat, 145+self.x, 145+3+self.y, 133+self.x, 145+3+self.y, 140+self.x, 175+3+self.y, 160+self.x, 177+6+self.y, 145+self.x, 160+3+self.y)
            canvas.update()

        elif self.Frame == 1  and self.looking == "Left" and self.forward == False: #Moving left without sprint or crouch 
            self.moveFists += 2
            canvas.coords(self.a_head, 125+self.x, 125+3+self.y, 150+self.x, 150+3+self.y)
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 130+self.x, 150+3+self.y, 145+self.x, 150+3+self.y, 145+self.x, 175+3+self.y, 130+self.x, 175+3+self.y)
            canvas.coords(self.a_Larm, 115+self.x, 150+self.y+2, 130+self.x, 165+self.y+2) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO
            canvas.coords(self.a_Rarm, 115+self.x+self.moveFists, 150+self.y, 130+self.x+self.moveFists, 165+self.y) #Arm hides behind torso
            canvas.coords(self.a_Rleg, 145+self.x-10, 175+self.y, 160+self.x-10, 183+self.y)
            canvas.coords(self.a_Lleg, 115+self.x+10, 175+self.y, 130+self.x+10, 183+self.y)
            canvas.coords(self.a_bandana1, 125+self.x+25, 140+3+self.y, 150+self.x-25, 140+3+self.y, 150+self.x-25, 150+3+self.y)
            canvas.coords(self.a_bandana2, 125+self.x+25, 140+3+self.y, 120+self.x+35, 142+3+self.y, 120+self.x+35, 145+3+self.y)
            canvas.coords(self.a_bandana3, 125+self.x+25, 140+3+self.y, 120+self.x+35, 138+3+self.y, 120+self.x+35, 141+3+self.y)
            canvas.coords(self.a_vneck, 130+self.x, 155+3+self.y, 145+self.x, 150+3+self.y, 145+self.x, 175+3+self.y, 130+self.x, 175+3+self.y)
            canvas.coords(self.a_coat, 145+self.x, 145+3+self.y, 133+self.x, 145+3+self.y, 140+self.x, 175+3+self.y, 160+self.x, 177+6+self.y, 145+self.x, 160+3+self.y)
            canvas.update()
        
        elif self.Frame == 0  and self.looking == "Left" and self.forward == True: #Moving left without sprint or crouch 
            self.moveFists -= 2
            canvas.coords(self.a_head, 125+self.x, 125+3+self.y, 150+self.x, 150+3+self.y)
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 130+self.x, 150+3+self.y, 145+self.x, 150+3+self.y, 145+self.x, 175+3+self.y, 130+self.x, 175+3+self.y)
            canvas.coords(self.a_Larm, 115+self.x+self.moveFists, 150+self.y+2, 130+self.x+self.moveFists, 165+self.y+2) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO
            canvas.coords(self.a_Rarm, 115+self.x, 150+self.y, 130+self.x, 165+self.y) #Arm hides behind torso
            canvas.coords(self.a_Rleg, 145+self.x-10, 175+self.y, 160+self.x-10, 183+self.y)
            canvas.coords(self.a_Lleg, 115+self.x+10, 175+self.y, 130+self.x+10, 183+self.y)
            canvas.coords(self.a_bandana1, 125+self.x+25, 140+3+self.y, 150+self.x-25, 140+3+self.y, 150+self.x-25, 150+3+self.y)
            canvas.coords(self.a_bandana2, 125+self.x+25, 140+3+self.y, 120+self.x+35, 142+3+self.y, 120+self.x+35, 145+3+self.y)
            canvas.coords(self.a_bandana3, 125+self.x+25, 140+3+self.y, 120+self.x+35, 138+3+self.y, 120+self.x+35, 141+3+self.y)
            canvas.coords(self.a_vneck, 130+self.x, 155+3+self.y, 145+self.x, 150+3+self.y, 145+self.x, 175+3+self.y, 130+self.x, 175+3+self.y)
            canvas.coords(self.a_coat, 145+self.x, 145+3+self.y, 133+self.x, 145+3+self.y, 140+self.x, 175+3+self.y, 160+self.x, 177+6+self.y, 145+self.x, 160+3+self.y)
            canvas.update()

        elif self.Frame == 0  and self.looking == "Left" and self.forward == False: #Moving left without sprint or crouch 
            self.moveFists += 2
            canvas.coords(self.a_head, 125+self.x, 125+3+self.y, 150+self.x, 150+3+self.y)
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 130+self.x, 150+3+self.y, 145+self.x, 150+3+self.y, 145+self.x, 175+3+self.y, 130+self.x, 175+3+self.y)
            canvas.coords(self.a_Larm, 115+self.x+self.moveFists, 150+self.y+2, 130+self.x+self.moveFists, 165+self.y+2) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO
            canvas.coords(self.a_Rarm, 115+self.x, 150+self.y, 130+self.x, 165+self.y) #Arm hides behind torso
            canvas.coords(self.a_Rleg, 145+self.x-10, 175+self.y, 160+self.x-10, 183+self.y)
            canvas.coords(self.a_Lleg, 115+self.x+10, 175+self.y, 130+self.x+10, 183+self.y)
            canvas.coords(self.a_bandana1, 125+self.x+25, 140+3+self.y, 150+self.x-25, 140+3+self.y, 150+self.x-25, 150+3+self.y)
            canvas.coords(self.a_bandana2, 125+self.x+25, 140+3+self.y, 120+self.x+35, 142+3+self.y, 120+self.x+35, 145+3+self.y)
            canvas.coords(self.a_bandana3, 125+self.x+25, 140+3+self.y, 120+self.x+35, 138+3+self.y, 120+self.x+35, 141+3+self.y)
            canvas.coords(self.a_vneck, 130+self.x, 155+3+self.y, 145+self.x, 150+3+self.y, 145+self.x, 175+3+self.y, 130+self.x, 175+3+self.y)
            canvas.coords(self.a_coat, 145+self.x, 145+3+self.y, 133+self.x, 145+3+self.y, 140+self.x, 175+3+self.y, 160+self.x, 177+6+self.y, 145+self.x, 160+3+self.y)
            canvas.update()
            
        #elif self.Frame == 0 and self.crouch == False and self.looking == "Left" and self.forward == True: #Moving left SPRINTING FRAME #1
            #self.x -= 1 #Arms and legs out
            #canvas.coords(self.a_head, 145+self.x-40, 135+self.y, 170+self.x-40, 160+self.y) #(+20, +10) difference from walking
            #canvas.coords(self.a_name, 138+self.x, 110+self.y)
           # canvas.coords(self.a_torso, 140+self.x-4, 150+self.y, 150+self.x-24, 160+self.y, 125+self.x+26, 170+self.y, 115+self.x+46, 160+self.y) #(10, 0), (5,10), (-20,-5), (-15,-15)
           # canvas.coords(self.a_Larm, 85+self.x+106, 150+self.y, 100+self.x+76, 165+self.y) #(-30,0)
           # canvas.coords(self.a_Rarm, 175+self.x-74, 150+self.y, 190+self.x-104, 165+self.y) #(+30,0)
          #  canvas.coords(self.a_Rleg, 150+self.x-24, 170+self.y, 165+self.x-54, 178+self.y) #(+5,-5), (+5,-5)
            #canvas.coords(self.a_Lleg, 110+self.x+56, 170+self.y, 125+self.x+26, 178+self.y) #(-5,-5), (-5,-5)
            #canvas.coords(self.a_bandana1, 145+self.x-14, 150+self.y, 170+self.x-64, 150+self.y, 170+self.x-64, 160+self.y) #(+20,10) for all bandana
         #   canvas.coords(self.a_bandana2, 145+self.x-14, 150+self.y, 140+self.x-4, 152+self.y, 140+self.x-4, 160+self.y)
           # canvas.coords(self.a_bandana3, 145+self.x-14, 150+self.y, 140+self.x-4, 148+self.y, 140+self.x-4, 151+self.y)
          #  canvas.coords(self.a_vneck, 140+self.x-4, 150+self.y, 145+self.x-14, 163+self.y, 125+self.x+26, 170+self.y, 115+self.x+46, 160+self.y) #(10,0), (0,8), (-20,-5), (-15,-15)
            #canvas.coords(self.a_coat, 142+self.x-8, 145+self.y, 152+self.x-28, 155+self.y, 100+self.x+76, 175+self.y, 85+self.x+104, 157+self.y, 125+self.x+26, 155+self.y)
            #self.x -= 3
            #(12,0) (10,10), (-35,0), (-30,-20), (-5,-5)
                
        #elif self.Frame == 1 and self.crouch == False and self.looking == "Left" and self.forward == True: #Moving left SPRINTING FRAME #2
         #   self.x -= 1 #Arms and legs in
          #  canvas.coords(self.a_head, 145+self.x-40, 135+5+self.y, 170+self.x-40, 160+5+self.y) #(+20, +10) difference from walking
           # canvas.coords(self.a_name, 138+self.x, 110+self.y)
            #canvas.coords(self.a_torso, 140+self.x-4, 150+5+self.y, 150+self.x-24, 160+5+self.y, 125+self.x+26, 170+5+self.y, 115+self.x+46, 160+5+self.y) #(20, 10), (5,10)
            #canvas.coords(self.a_Larm, 130+self.x+16, 160+self.y, 145+self.x-14, 175+self.y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
            #canvas.coords(self.a_Rarm, 130+self.x+16, 160+self.y, 145+self.x-14, 175+self.y) #Arm hides behind torso (+30,0)
            #canvas.coords(self.a_Rleg, 145+self.x-10, 175+self.y, 160+self.x-10, 183+self.y)
            #canvas.coords(self.a_Lleg, 115+self.x+10, 175+self.y, 130+self.x+10, 183+self.y)
            #canvas.coords(self.a_bandana1, 145+self.x-14, 150+5+self.y, 170+self.x-64, 150+5+self.y, 170+self.x-64, 160+5+self.y) #(+20,10) for all bandana
            #canvas.coords(self.a_bandana2, 145+self.x-14, 150+5+self.y, 140+self.x-4, 152+5+self.y, 140+self.x-4, 160+5+self.y)
            #canvas.coords(self.a_bandana3, 145+self.x-14, 150+5+self.y, 140+self.x-4, 148+5+self.y, 140+self.x-4, 151+5+self.y) 
            #canvas.coords(self.a_vneck, 140+self.x-4, 150+5+self.y, 145+self.x-14, 163+5+self.y, 125+self.x+26, 170+5+self.y, 115+self.x+46, 160+5+self.y) #(10,0), (0,8), (-20,-5), (-15,-15)
            #canvas.coords(self.a_coat, 142+self.x-8, 145+5+self.y, 152+self.x-28, 155+5+self.y, 100+self.x+76, 175+10+self.y, 85+self.x+104, 157+10+self.y, 125+self.x+26, 155+5+self.y)
            #(12,0) (10,10), (-35,0), (-30,-20), (-5,-5)
            #self.x -= 3

      #  elif self.Frame == 0 and self.crouch == True and self.looking == "Left" and self.forward == True: #Moving left CROUCHING FRAME #1
            #self.x -= 0.5 #Arms and legs out self.x 
            #canvas.coords(self.a_head, 145+self.x-40, 135+self.y, 170+self.x-40, 160+self.y) #(+20, +10) difference from walking
            #canvas.coords(self.a_name, 138+self.x, 110+self.y)
           # canvas.coords(self.a_torso, 140+self.x-4, 150+self.y, 150+self.x-24, 160+self.y, 125+self.x+26, 170+self.y, 115+self.x+46, 160+self.y) #(10, 0), (5,10), (-20,-5), (-15,-15)
           # canvas.coords(self.a_Larm, 130+self.x+16, 160+self.y, 145+self.x-14, 175+self.y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
           # canvas.coords(self.a_Rarm, 130+self.x+16, 160+self.y, 145+self.x-14, 175+self.y) #Arm hides behind torso (+30,0)
           # canvas.coords(self.a_Rleg, 145+self.x-5, 175+self.y, 160+self.x-5, 183+self.y) #(+5,-5), (+5,-5)
           # canvas.coords(self.a_Lleg, 115+self.x+5, 175+self.y, 130+self.x+5, 183+self.y) #(-5,-5), (-5,-5)
           # canvas.coords(self.a_bandana1, 145+self.x-14, 150+self.y, 170+self.x-64, 150+self.y, 170+self.x-64, 160+self.y) #(+20,10) for all bandana
           # canvas.coords(self.a_bandana2, 145+self.x-14, 150+self.y, 140+self.x-4, 152+self.y, 140+self.x-4, 160+self.y)
           # canvas.coords(self.a_bandana3, 145+self.x-14, 150+self.y, 140+self.x-4, 148+self.y, 140+self.x-4, 151+self.y)
           # canvas.coords(self.a_vneck, 140+self.x-4, 150+self.y, 145+self.x-14, 163+self.y, 125+self.x+26, 170+self.y, 115+self.x+46, 160+self.y) #(10,0), (0,8), (-20,-5), (-15,-15)
           # canvas.coords(self.a_coat, 142+self.x-8, 145+self.y, 152+self.x-28, 155+self.y, 85+self.x+76, 183+self.y, 80+self.x+104, 183+self.y, 125+self.x+26, 155+self.y)
                
        #elif self.Frame == 1 and self.crouch == True and self.looking == "Left" and self.forward == True: #Moving left CROUCHING FRAME #2
           # self.x -= 0.5 #Arms and legs in
            #canvas.coords(self.a_head, 145+self.x-40, 135+2+self.y, 170+self.x-40, 160+2+self.y) #(+20, +10) difference from walking
           # canvas.coords(self.a_name, 138+self.x, 110+self.y)
           # canvas.coords(self.a_torso, 140+self.x-4, 150+2+self.y, 150+self.x-24, 160+2+self.y, 125+self.x+26, 170+2+self.y, 115+self.x+46, 160+2+self.y) #(20, 10), (5,10)
           # canvas.coords(self.a_Larm, 130+self.x-10, 160+2+self.y, 145+self.x-10, 175+2+self.y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
           # canvas.coords(self.a_Rarm, 130+self.x-10, 160+2+self.y, 145+self.x-10, 175+2+self.y) #Arm hides behind torso (+30,0)
           # canvas.coords(self.a_Rleg, 145+self.x-10, 175+self.y, 160+self.x-10, 183+self.y)
           # canvas.coords(self.a_Lleg, 115+self.x+10, 175+self.y, 130+self.x+10, 183+self.y)
          #  canvas.coords(self.a_bandana1, 145+self.x-14, 150+2+self.y, 170+self.x-64, 150+2+self.y, 170+self.x-64, 160+2+self.y) #(+20,10) for all bandana
           # canvas.coords(self.a_bandana2, 145+self.x-14, 150+2+self.y, 140+self.x-4, 152+2+self.y, 140+self.x-4, 160+2+self.y)
           # canvas.coords(self.a_bandana3, 145+self.x-14, 150+2+self.y, 140+self.x-4, 148+2+self.y, 140+self.x-4, 151+2+self.y) 
          #  canvas.coords(self.a_vneck, 140+self.x-4, 150+2+self.y, 145+self.x-14, 163+2+self.y, 125+self.x+26, 170+2+self.y, 115+self.x+46, 160+2+self.y) #(10,0), (0,8), (-20,-5), (-15,-15)
           # canvas.coords(self.a_coat, 142+self.x-8, 145+2+self.y, 152+self.x-28, 155+2+self.y, 85+self.x+76, 183+2+self.y, 80+self.x+104, 183+2+self.y, 125+self.x+26, 155+2+self.y)
            #(12,0) (10,10), (-35,0), (-30,-20), (-5,-5)


        #MOVING RIGHT NOT IN AIR

        elif self.Frame == 0  and self.looking == "Right" and self.forward == True: #Moving right without sprinting or crouching FRAME #2
            self.moveFists += 2
            canvas.coords(self.a_head, 125+self.x, 125+3+self.y, 150+self.x, 150+3+self.y)
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 130+self.x, 150+3+self.y, 145+self.x, 150+3+self.y, 145+self.x, 175+3+self.y, 130+self.x, 175+3+self.y)
            canvas.coords(self.a_Larm, 145+self.x+self.moveFists, 150+self.y+2, 160+self.x+self.moveFists, 165+self.y+2) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO
            canvas.coords(self.a_Rarm, 145+self.x, 150+self.y, 160+self.x, 165+self.y) #Arm hides behind torso
            canvas.coords(self.a_Rleg, 145+self.x-10, 175+self.y, 160+self.x-10, 183+self.y)
            canvas.coords(self.a_Lleg, 115+self.x+10, 175+self.y, 130+self.x+10, 183+self.y)
            canvas.coords(self.a_bandana1, 125+self.x, 140+3+self.y, 150+self.x, 140+3+self.y, 150+self.x, 150+3+self.y)
            canvas.coords(self.a_bandana2, 125+self.x, 140+3+self.y, 120+self.x, 142+3+self.y, 120+self.x, 145+3+self.y)
            canvas.coords(self.a_bandana3, 125+self.x, 140+3+self.y, 120+self.x, 138+3+self.y, 120+self.x, 141+3+self.y)
            canvas.coords(self.a_vneck, 130+self.x, 150+3+self.y, 145+self.x, 155+3+self.y, 145+self.x, 175+3+self.y, 130+self.x, 175+3+self.y)
            canvas.coords(self.a_coat, 130+self.x, 145+3+self.y, 142+self.x, 145+3+self.y, 135+self.x, 175+3+self.y, 115+self.x, 177+6+self.y, 130+self.x, 160+self.y)

        elif self.Frame == 0  and self.looking == "Right" and self.forward == False: #Moving right without sprinting or crouching FRAME #2
            self.moveFists -= 2
            canvas.coords(self.a_head, 125+self.x, 125+3+self.y, 150+self.x, 150+3+self.y)
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 130+self.x, 150+3+self.y, 145+self.x, 150+3+self.y, 145+self.x, 175+3+self.y, 130+self.x, 175+3+self.y)
            canvas.coords(self.a_Larm, 145+self.x+self.moveFists, 150+self.y+2, 160+self.x+self.moveFists, 165+self.y+2) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO
            canvas.coords(self.a_Rarm, 145+self.x, 150+self.y, 160+self.x, 165+self.y) #Arm hides behind torso
            canvas.coords(self.a_Rleg, 145+self.x-10, 175+self.y, 160+self.x-10, 183+self.y)
            canvas.coords(self.a_Lleg, 115+self.x+10, 175+self.y, 130+self.x+10, 183+self.y)
            canvas.coords(self.a_bandana1, 125+self.x, 140+3+self.y, 150+self.x, 140+3+self.y, 150+self.x, 150+3+self.y)
            canvas.coords(self.a_bandana2, 125+self.x, 140+3+self.y, 120+self.x, 142+3+self.y, 120+self.x, 145+3+self.y)
            canvas.coords(self.a_bandana3, 125+self.x, 140+3+self.y, 120+self.x, 138+3+self.y, 120+self.x, 141+3+self.y)
            canvas.coords(self.a_vneck, 130+self.x, 150+3+self.y, 145+self.x, 155+3+self.y, 145+self.x, 175+3+self.y, 130+self.x, 175+3+self.y)
            canvas.coords(self.a_coat, 130+self.x, 145+3+self.y, 142+self.x, 145+3+self.y, 135+self.x, 175+3+self.y, 115+self.x, 177+6+self.y, 130+self.x, 160+self.y)

        elif self.Frame == 1  and self.looking == "Right" and self.forward == True: #Moving right without sprinting or crouching FRAME #2
            self.moveFists += 2
            canvas.coords(self.a_head, 125+self.x, 125+3+self.y, 150+self.x, 150+3+self.y)
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 130+self.x, 150+3+self.y, 145+self.x, 150+3+self.y, 145+self.x, 175+3+self.y, 130+self.x, 175+3+self.y)
            canvas.coords(self.a_Larm, 145+self.x, 150+self.y+2, 160+self.x, 165+self.y+2) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO
            canvas.coords(self.a_Rarm, 145+self.x+self.moveFists, 150+self.y, 160+self.x+self.moveFists, 165+self.y) #Arm hides behind torso
            canvas.coords(self.a_Rleg, 145+self.x-10, 175+self.y, 160+self.x-10, 183+self.y)
            canvas.coords(self.a_Lleg, 115+self.x+10, 175+self.y, 130+self.x+10, 183+self.y)
            canvas.coords(self.a_bandana1, 125+self.x, 140+3+self.y, 150+self.x, 140+3+self.y, 150+self.x, 150+3+self.y)
            canvas.coords(self.a_bandana2, 125+self.x, 140+3+self.y, 120+self.x, 142+3+self.y, 120+self.x, 145+3+self.y)
            canvas.coords(self.a_bandana3, 125+self.x, 140+3+self.y, 120+self.x, 138+3+self.y, 120+self.x, 141+3+self.y)
            canvas.coords(self.a_vneck, 130+self.x, 150+3+self.y, 145+self.x, 155+3+self.y, 145+self.x, 175+3+self.y, 130+self.x, 175+3+self.y)
            canvas.coords(self.a_coat, 130+self.x, 145+3+self.y, 142+self.x, 145+3+self.y, 135+self.x, 175+3+self.y, 115+self.x, 177+6+self.y, 130+self.x, 160+self.y)

        elif self.Frame == 1  and self.looking == "Right" and self.forward == False: #Moving right without sprinting or crouching FRAME #2
            self.moveFists -= 2
            canvas.coords(self.a_head, 125+self.x, 125+3+self.y, 150+self.x, 150+3+self.y)
            canvas.coords(self.a_name, 138+self.x, 110+self.y)
            canvas.coords(self.a_torso, 130+self.x, 150+3+self.y, 145+self.x, 150+3+self.y, 145+self.x, 175+3+self.y, 130+self.x, 175+3+self.y)
            canvas.coords(self.a_Larm, 145+self.x, 150+self.y+2, 160+self.x, 165+self.y+2) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO
            canvas.coords(self.a_Rarm, 145+self.x+self.moveFists, 150+self.y, 160+self.x+self.moveFists, 165+self.y) #Arm hides behind torso
            canvas.coords(self.a_Rleg, 145+self.x-10, 175+self.y, 160+self.x-10, 183+self.y)
            canvas.coords(self.a_Lleg, 115+self.x+10, 175+self.y, 130+self.x+10, 183+self.y)
            canvas.coords(self.a_bandana1, 125+self.x, 140+3+self.y, 150+self.x, 140+3+self.y, 150+self.x, 150+3+self.y)
            canvas.coords(self.a_bandana2, 125+self.x, 140+3+self.y, 120+self.x, 142+3+self.y, 120+self.x, 145+3+self.y)
            canvas.coords(self.a_bandana3, 125+self.x, 140+3+self.y, 120+self.x, 138+3+self.y, 120+self.x, 141+3+self.y)
            canvas.coords(self.a_vneck, 130+self.x, 150+3+self.y, 145+self.x, 155+3+self.y, 145+self.x, 175+3+self.y, 130+self.x, 175+3+self.y)
            canvas.coords(self.a_coat, 130+self.x, 145+3+self.y, 142+self.x, 145+3+self.y, 135+self.x, 175+3+self.y, 115+self.x, 177+6+self.y, 130+self.x, 160+self.y)

        #elif self.Frame == 0 and self.crouch == False and self.looking == "Right" and self.forward == True: #Moving right SPRINTING FRAME #1
            #self.x += 1 #Arms and legs out
            #canvas.coords(self.a_head, 145+self.x, 135+self.y, 170+self.x, 160+self.y) #(+20, +10) difference from walking
            #canvas.coords(self.a_name, 138+self.x, 110+self.y)
            #canvas.coords(self.a_torso, 140+self.x, 150+self.y, 150+self.x, 160+self.y, 125+self.x, 170+self.y, 115+self.x, 160+self.y) #(10, 0), (5,10), (-20,-5), (-15,-15)
            #canvas.coords(self.a_Larm, 85+self.x, 150+self.y, 100+self.x, 165+self.y) #(-30,0)
            #canvas.coords(self.a_Rarm, 175+self.x, 150+self.y, 190+self.x, 165+self.y) #(+30,0)
            #canvas.coords(self.a_Rleg, 150+self.x, 170+self.y, 165+self.x, 178+self.y) #(+5,-5), (+5,-5)
            #canvas.coords(self.a_Lleg, 110+self.x, 170+self.y, 125+self.x, 178+self.y) #(-5,-5), (-5,-5)
            #canvas.coords(self.a_bandana1, 145+self.x, 150+self.y, 170+self.x, 150+self.y, 170+self.x, 160+self.y) #(+20,10) for all bandana
            #canvas.coords(self.a_bandana2, 145+self.x, 150+self.y, 140+self.x, 152+self.y, 140+self.x, 160+self.y)
            #canvas.coords(self.a_bandana3, 145+self.x, 150+self.y, 140+self.x, 148+self.y, 140+self.x, 151+self.y) 
            #canvas.coords(self.a_vneck, 140+self.x, 150+self.y, 145+self.x, 163+self.y, 125+self.x, 170+self.y, 115+self.x, 160+self.y) #(10,0), (0,8), (-20,-5), (-15,-15)
            #canvas.coords(self.a_coat, 142+self.x, 145+self.y, 152+self.x, 155+self.y, 100+self.x, 175+self.y, 85+self.x, 157+self.y, 125+self.x, 155+self.y)
           # self.x += 3
            #(12,0) (10,10), (-35,0), (-30,-20), (-5,-5)
                
        #elif self.Frame == 1 and self.crouch == False and self.looking == "Right" and self.forward == True: #Moving right SPRINTING FRAME #2
            #self.x += 1 #Arms and legs in
            #canvas.coords(self.a_head, 145+self.x, 135+5+self.y, 170+self.x, 160+5+self.y) #(+20, +10) difference from walking
            #canvas.coords(self.a_name, 138+self.x, 110+self.y)
           # canvas.coords(self.a_torso, 140+self.x, 150+5+self.y, 150+self.x, 160+5+self.y, 125+self.x, 170+5+self.y, 115+self.x, 160+5+self.y) #(20, 10), (5,10)
            #canvas.coords(self.a_Larm, 130+self.x, 160+self.y, 145+self.x, 175+self.y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
            #canvas.coords(self.a_Rarm, 130+self.x, 160+self.y, 145+self.x, 175+self.y) #Arm hides behind torso (+30,0)
            #canvas.coords(self.a_Rleg, 145+self.x-10, 175+self.y, 160+self.x-10, 183+self.y)
            #canvas.coords(self.a_Lleg, 115+self.x+10, 175+self.y, 130+self.x+10, 183+self.y)
            #canvas.coords(self.a_bandana1, 145+self.x, 150+5+self.y, 170+self.x, 150+5+self.y, 170+self.x, 160+5+self.y) #(+20,10) for all bandana
            #canvas.coords(self.a_bandana2, 145+self.x, 150+5+self.y, 140+self.x, 152+5+self.y, 140+self.x, 155+5+self.y)
            #canvas.coords(self.a_bandana3, 145+self.x, 150+5+self.y, 140+self.x, 148+5+self.y, 140+self.x, 151+5+self.y)
            #canvas.coords(self.a_vneck, 140+self.x, 150+5+self.y, 145+self.x, 163+5+self.y, 125+self.x, 170+5+self.y, 115+self.x, 160+5+self.y) #(10,0), (0,8), (-20,-5), (-15,-15)
           # canvas.coords(self.a_coat, 142+self.x, 145+5+self.y, 152+self.x, 155+5+self.y, 100+self.x, 175+10+self.y, 85+self.x, 157+10+self.y, 125+self.x, 155+5+self.y)
            #(12,0) (10,10), (-35,0), (-30,-20), (-5,-5)
            #self.x += 3

        #elif self.Frame == 0 and self.crouch == True and self.looking == "Right" and self.forward == True: #Moving right CROUCHING FRAMe #1
            #self.x += 0.5 #Arms and legs in
           # canvas.coords(self.a_head, 145+self.x, 135+self.y, 170+self.x, 160+self.y) #(+20, +10) difference from walking
            #canvas.coords(self.a_name, 138+self.x, 110+self.y)
           # canvas.coords(self.a_torso, 140+self.x, 150+self.y, 150+self.x, 160+self.y, 125+self.x, 170+self.y, 115+self.x, 160+self.y) #(10, 0), (5,10), (-20,-5), (-15,-15)
           # canvas.coords(self.a_Larm, 130+self.x, 160+self.y, 145+self.x, 175+self.y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
          #  canvas.coords(self.a_Rarm, 130+self.x, 160+self.y, 145+self.x, 175+self.y) #Arm hides behind torso (+30,0)
          #  canvas.coords(self.a_Rleg, 145+self.x-5, 175+self.y, 160+self.x-5, 183+self.y) #(+5,-5), (+5,-5)
          #  canvas.coords(self.a_Lleg, 115+self.x+5, 175+self.y, 130+self.x+5, 183+self.y) #(-5,-5), (-5,-5)
          #  canvas.coords(self.a_bandana1, 145+self.x, 150+self.y, 170+self.x, 150+self.y, 170+self.x, 160+self.y) #(+20,10) for all bandana
          #  canvas.coords(self.a_bandana2, 145+self.x, 150+self.y, 140+self.x, 152+self.y, 140+self.x, 160+self.y)
          #  canvas.coords(self.a_bandana3, 145+self.x, 150+self.y, 140+self.x, 148+self.y, 140+self.x, 151+self.y)
          #  canvas.coords(self.a_vneck, 140+self.x, 150+self.y, 145+self.x, 163+self.y, 125+self.x, 170+self.y, 115+self.x, 160+self.y) #(10,0), (0,8), (-20,-5), (-15,-15)
          #  canvas.coords(self.a_coat, 142+self.x, 145+self.y, 152+self.x, 155+self.y, 115+self.x, 183+self.y, 92+self.x, 183+self.y, 125+self.x, 155+self.y)
                
       # elif self.Frame == 1 and self.crouch == True and self.looking == "Right" and self.forward == True: #Moving right CROUCHING FRAMe #2
          #  self.x += 0.5 #Arms and legs in
          #  canvas.coords(self.a_head, 145+self.x, 135+2+self.y, 170+self.x, 160+2+self.y) #(+20, +10) difference from walking
          #  canvas.coords(self.a_name, 138+self.x, 110+self.y)
          #  canvas.coords(self.a_torso, 140+self.x, 150+2+self.y, 150+self.x, 160+2+self.y, 125+self.x, 170+2+self.y, 115+self.x, 160+2+self.y) #(20, 10), (5,10)
          #  canvas.coords(self.a_Larm, 130+self.x+10, 160+2+self.y, 145+self.x+10, 175+2+self.y) #LEft arm here (back arm) THIS ARM IS ABOVE TORSO (-30,0)
         #   canvas.coords(self.a_Rarm, 130+self.x+10, 160+2+self.y, 145+self.x+10, 175+2+self.y) #Arm hides behind torso (+30,0)
         #   canvas.coords(self.a_Rleg, 145+self.x-10, 175+self.y, 160+self.x-10, 183+self.y)
        #    canvas.coords(self.a_Lleg, 115+self.x+10, 175+self.y, 130+self.x+10, 183+self.y)
        #    canvas.coords(self.a_bandana1, 145+self.x, 150+2+self.y, 170+self.x, 150+2+self.y, 170+self.x, 160+2+self.y) #(+20,10) for all bandana
       #     canvas.coords(self.a_bandana2, 145+self.x, 150+2+self.y, 140+self.x, 152+2+self.y, 140+self.x, 155+2+self.y)
        #    canvas.coords(self.a_bandana3, 145+self.x, 150+2+self.y, 140+self.x, 148+2+self.y, 140+self.x, 151+2+self.y)
       #     canvas.coords(self.a_vneck, 140+self.x, 150+2+self.y, 145+self.x, 163+2+self.y, 125+self.x, 170+2+self.y, 115+self.x, 160+2+self.y) #(10,0), (0,8), (-20,-5), (-15,-15)
       #     canvas.coords(self.a_coat, 142+self.x, 145+2+self.y, 152+self.x, 155+2+self.y, 115+self.x, 183+2+self.y, 92+self.x, 183+2+self.y, 125+self.x, 155+2+self.y)

        if self.forward == True and self.basic_attack_counter < 10:
            self.basic_attack_counter += 1
        elif self.forward == True and self.basic_attack_counter == 10:
            self.basic_attack_counter = 0
            self.forward = False
            #self.moveFists = 0
        elif self.forward == False and self.basic_attack_counter < 10:
            self.basic_attack_counter += 1
        elif self.forward == False and self.basic_attack_counter == 10:
            #self.moveFists = 0
            if self.Frame == 0:
                self.Frame = 1
            else:
                self.Frame = 0 
            self.basic_attack_counter = 0
            self.forward = True
            self.b_leftClick = canvas.bind("<Button-1>", self.leftClick) #bind.("<BUTTON_NAME>", function_call) #Functions way above
            self.b_scroll = canvas.bind("<Button-2>", self.scroll)
            self.b_rightClick = canvas.bind("<Button-3>", self.rightClick)
            self.b_a = canvas.bind("<a>", self.aKey)
            self.b_d = canvas.bind("<d>", self.dKey)
            self.b_s = canvas.bind("<s>", self.sKey)
            self.b_w = canvas.bind("<w>", self.wKey)
            self.b_q = canvas.bind("<q>", self.qKey)
            self.b_e = canvas.bind("<e>", self.eKey)
            self.b_shiftR = canvas.bind("<Shift_R>", self.shiftKey)
            self.b_shiftL = canvas.bind("<Shift_L>", self.shiftKey)
            self.b_ctrlL = canvas.bind("<Control_L>", self.ctrlKey)
            self.b_ctrlR = canvas.bind("<Control_R>", self.ctrlKey)
            self.b_space = canvas.bind("<space>", self.spaceKey)
            self.b_leftClick = canvas.bind("<Button-1>", self.leftClick)
            print("Basic attack animation done")
            basic_attack = False
            
    def leftClick(self, evt): #Basic attack - Punching
        #1 frame - Legs in. Still need facing still need to check if sprinting or crouching. Need to check looking.
        global basic_attack
        #print("Left Click")
        if basic_attack == False:
            basic_attack = True
            canvas.unbind("<Button-1>", self.b_leftClick)
            canvas.unbind("<Button-2>", self.b_scroll)
            canvas.unbind("<Button-3>", self.b_rightClick)
            canvas.unbind("<a>", self.b_a)
            canvas.unbind("<d>", self.b_d)
            canvas.unbind("<s>", self.b_s)
            canvas.unbind("<w>", self.b_w)
            canvas.unbind("<q>", self.b_q)
            canvas.unbind("<e>", self.b_e)
            print("Initialing basic attack")
        else:
            print("Basic attack still in animation!")

            #I forgot what was the below.
        #elif basic_attack == True: #Will never reach
         #   print("Basic attack still in aniamtion!")
        #elif basic_attack == True and basic_attack_counter == 30:
         #   basic_attack = False
            #self.b_leftClick = canvas.bind("<Button-1>", self.leftClick)
          #  print("if basic_attack == True and counter == 30")
        #else:
         #   print("Basic attack still in animation!")
          #  basic_attack_counter += 1
        
    def rightClick(self, evt): #Take aim
        print("Right Click")

    def scroll(self, evt): 
        print("Scroll Click")

    def shiftKey(self, evt): #Sprint/Walk toggle
        if self.sprint == True and self.crouch == False:
            self.sprint = False
            self.checker = 9 #This line and the next allows one frame of the player.draw() method to change the stance of the character. The character moves a bit due to 1 draw() frame but it is almost unoticeable.
            self.notMoving = False
        elif self.sprint == False and self.crouch == False:
            self.sprint = True
            self.checker = 9
            self.notMoving = False
        else: #If you are crouching, pressing shift will change that to sprinting
            #print("Toggling sprint to True and making crouch False")
            self.sprint = True
            self.crouch = False
            self.checker = 9
            self.notMoving = False

    def ctrlKey(self, evt): #crouch
        if self.crouch == True and self.sprint == False:
            self.crouch = False
            self.checker = 9
            self.notMoving = False
        elif self.crouch == False and self.sprint == False:
            self.crouch = True
            self.checker = 9
            self.notMoving = False
        else: #If you are sprinting, pressing shift will change that to crouching
            #print("Toggling crouch to True and making sprint False")
            self.sprint = False
            self.crouch = True
            self.checker = 9
            self.notMoving = False
                
background = Background(canvas)
enemy = Enemy(canvas)
sword = Sword(canvas)
#nathaniel2010 = Nathaniel2010(canvas)
bars = Bars(canvas)
player = Player(canvas)
voice = Voice(canvas,player)
canvas.focus_set() #Tells Python to use keyboard so left and right arrow keys work now

while 1:
    if basic_attack == False:
        player.draw()
    else:
        player.drawAttack()
    #bars.draw()
    #sword.draw()
    sword.drawEye()
    #enemy.draw()
    #nathaniel2010.draw()
    voice.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
