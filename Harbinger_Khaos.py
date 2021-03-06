#This game will use animations with the tkinter and time classes.

from tkinter import *
import random
import time

voiceOn = False #When this is True, Voice class activates.
basic_attack = False #When this is True, basic attack animation activates and locks the player in the animation until it is over.
lavaDamage = False #This becomes true when chracter hovers over the red area on the left side of the screen below him. Coords could be found in Player class draw() method near the bottom.
manaUsed = False #This becomes true when you press spacebar. This switch flips and deletes the mana in the bar. In the Bars class in draw() method, the second if statement will activate.
sprinting = False #After pressing shiftL, this will turn true, when it does the Bars class draw() method will deduct SP from the bar in the third if statement.
moving = False #This is to make sure the player is moving to deduct SP. Player could be stationary AND be in sprint stance so the character should NOT use SP during this time.
outOfSprint = False #When the sprint bar becomes empty, make this true. This kicks the player out of sprint stance.
oneIterate = True #This takes effect in the Player class's draw() method. The very first if statement will kick the player out of sprint stance. This will not be flipped back on until SP is full again.
hitBySpecialOnce = True
hitByBasicAttackOnce = True
pressQ = True
turnOffEnemy3 = False
enemy3Damage = False
gameOver = False

tk = Tk()
tk.title("Harbinger: Khaos - Alpha 3.0.2: Enemy3 Rematch")
canvas = Canvas(width=1300, height=700, bg="gray30")
canvas.pack()
tk.update()



class Enemy2: #the dark guard (lEon cratieosn)
    def __init__(self,canvas):
        self.canvas = canvas
        self.x, self.y = 0,0
        self.x2 = 0 #for continous movement purposes
        self.Frame = 0
        self.counterFrame = 0 #start it at something higher, so doesnt slide for too long at beginning
        self.Looking = "Left"
        
        self.e2_body2 = canvas.create_polygon(892, 232+2, 908, 232+2, 908, 262+2, 892, 262+2, fill="gray13", outline="black")
        self.e2_head2 = canvas.create_oval(887, 206+2, 913, 232+2, fill="gray", outline="black")
        self.e2_eye2 = canvas.create_polygon(888, 219+2, 900, 219+2, 900, 214+2, fill="red")
        self.e2_helmet2 = canvas.create_polygon(884, 221+2, 889, 231+2, 914, 231+2, 916, 221+2, 914, 211+2, 899, 205+2, 884, 213+2, 902, 213+2, 906, 217+2, 902, 221+2,  fill="black", outline="black")
        

        #might need to create another shoulder if the enemy moves.
        
        
        self.e2_spearshaft2 = canvas.create_polygon(879, 217+2, 882, 217+2, 882, 277+2, 879, 277+2, fill="black")
        self.e2_spearhead2 = canvas.create_polygon(875, 217+2, 880, 202+2, 886, 217+2, fill="black")
        self.e2_righthand2 = canvas.create_oval(872, 232+2, 888, 247+2, fill="gray")
        self.e2_shoulder2 = canvas.create_polygon(899, 237+2, 911, 237+2, 911, 249+2, 899, 249+2, fill="black")
        self.e2_shoulderspike2 = canvas.create_polygon(901, 237+2, 905, 227+2, 909, 237+2, fill="gray")
        self.e2_lefthand2 = canvas.create_oval(897, 242+2, 913, 257+2, fill="gray")
        
        self.e2_Lleg2 = canvas.create_oval(886, 263, 901, 273,  fill="black") #+15, +8
        self.e2_Rleg2 = canvas.create_oval(901-2, 263, 916-2, 273,  fill="black") #+15, +8
        self.e2_name2 = canvas.create_text(900, 200, anchor="center", fill="red", text="Dark Guard", font=("Fixedsys", 16))
        self.e2_hitbox = canvas.create_line(892, 231+2, 908, 262+2, fill="red")
        self.e2_righthandhitbox = canvas.coords(self.e2_righthand2)
        
    def draw(self):
        if self.e2_righthandhitbox[0] <= 0:
            self.Looking = "Right"

        if 0 <= self.counterFrame < 100 and self.Looking == "Left": #stops enemy animation if its right 
            self.x -= 1
            
            # for going forward it will be +self.x2, back is -self.x2
            canvas.coords(self.e2_name2, 900+self.x, 200+self.y)
            canvas.coords(self.e2_body2, 892+self.x, 232+2+self.y, 908+self.x, 232+2+self.y, 908+self.x, 262+2+self.y, 892+self.x, 262+2+self.y)
            canvas.coords(self.e2_head2, 887+self.x, 206+2+self.y, 913+self.x, 232+2+self.y)
            canvas.coords(self.e2_eye2, 888+self.x, 219+2+self.y, 900+self.x, 219+2+self.y, 900+self.x, 214+2+self.y)
            canvas.coords(self.e2_helmet2, 884+self.x, 221+2+self.y, 889+self.x, 231+2+self.y, 914+self.x, 231+2+self.y, 916+self.x, 221+2+self.y, 914+self.x, 211+2+self.y, 899+self.x, 205+2+self.y, 884+self.x, 213+2+self.y, 902+self.x, 213+2+self.y, 906+self.x, 217+2+self.y, 902+self.x, 221+2+self.y)
            canvas.coords(self.e2_hitbox, 892+self.x, 231+2, 908+self.x, 262+2)
            if self.Frame == 0: # left go forward, right go back
                self.x2 -= 1
                canvas.coords(self.e2_shoulder2, 899+self.x+self.x2, 237+2+self.y, 911+self.x+self.x2, 237+2+self.y, 911+self.x+self.x2, 249+2+self.y, 899+self.x+self.x2, 249+2+self.y)
                canvas.coords(self.e2_shoulderspike2, 901+self.x+self.x2, 237+2+self.y, 905+self.x+self.x2, 227+2+self.y, 909+self.x+self.x2, 237+2+self.y)
                canvas.coords(self.e2_lefthand2, 897+self.x+self.x2, 242+2+self.y, 913+self.x+self.x2, 257+2+self.y)
                
                canvas.coords(self.e2_spearshaft2, 879+self.x-self.x2, 217+2+self.y, 882+self.x-self.x2, 217+2+self.y, 882+self.x-self.x2, 277+2+self.y, 879+self.x-self.x2, 277+2+self.y)
                canvas.coords(self.e2_spearhead2, 875+self.x-self.x2, 217+2+self.y, 880+self.x-self.x2, 202+2+self.y, 886+self.x-self.x2, 217+2+self.y)
                canvas.coords(self.e2_righthand2, 872+self.x-self.x2, 232+2+self.y, 888+self.x-self.x2, 247+2+self.y)
                
                canvas.coords(self.e2_Lleg2, 886+self.x, 263+self.y, 901+self.x, 273+self.y)
                
                canvas.coords(self.e2_Rleg2, 901-2+self.x, 263+self.y, 916-2+self.x, 273+self.y)
                #print(self.x2, self.Frame, self.counterFrame)
                                
            elif self.Frame == 1:# returning 
                self.x2 += 1
               
                canvas.coords(self.e2_shoulder2, 899+self.x+self.x2, 237+2+self.y, 911+self.x+self.x2, 237+2+self.y, 911+self.x+self.x2, 249+2+self.y, 899+self.x+self.x2, 249+2+self.y)
                canvas.coords(self.e2_shoulderspike2, 901+self.x+self.x2, 237+2+self.y, 905+self.x+self.x2, 227+2+self.y, 909+self.x+self.x2, 237+2+self.y)
                canvas.coords(self.e2_lefthand2, 897+self.x+self.x2, 242+2+self.y, 913+self.x+self.x2, 257+2+self.y)
                
                canvas.coords(self.e2_spearshaft2, 879+self.x-self.x2, 217+2+self.y, 882+self.x-self.x2, 217+2+self.y, 882+self.x-self.x2, 277+2+self.y, 879+self.x-self.x2, 277+2+self.y)
                canvas.coords(self.e2_spearhead2, 875+self.x-self.x2, 217+2+self.y, 880+self.x-self.x2, 202+2+self.y, 886+self.x-self.x2, 217+2+self.y)
                canvas.coords(self.e2_righthand2, 872+self.x-self.x2, 232+2+self.y, 888+self.x-self.x2, 247+2+self.y)
                
                canvas.coords(self.e2_Lleg2, 886+self.x, 263+self.y, 901+self.x, 273+self.y)
                
                canvas.coords(self.e2_Rleg2, 901-2+self.x, 263+self.y, 916-2+self.x, 273+self.y)
                #print(self.x2, self.Frame, self.counterFrame)
                
                
                
            elif self.Frame == 2: # right go forward, left go back
                self.x2 -= 1
                canvas.coords(self.e2_shoulder2, 899+self.x-self.x2, 237+2+self.y, 911+self.x-self.x2, 237+2+self.y, 911+self.x-self.x2, 249+2+self.y, 899+self.x-self.x2, 249+2+self.y)
                canvas.coords(self.e2_shoulderspike2, 901+self.x-self.x2, 237+2+self.y, 905+self.x-self.x2, 227+2+self.y, 909+self.x-self.x2, 237+2+self.y)
                canvas.coords(self.e2_lefthand2, 897+self.x-self.x2, 242+2+self.y, 913+self.x-self.x2, 257+2+self.y)
                
                canvas.coords(self.e2_spearshaft2, 879+self.x+self.x2, 217+2+self.y, 882+self.x+self.x2, 217+2+self.y, 882+self.x+self.x2, 277+2+self.y, 879+self.x+self.x2, 277+2+self.y)
                canvas.coords(self.e2_spearhead2, 875+self.x+self.x2, 217+2+self.y, 880+self.x+self.x2, 202+2+self.y, 886+self.x+self.x2, 217+2+self.y)
                canvas.coords(self.e2_righthand2, 872+self.x+self.x2, 232+2+self.y, 888+self.x+self.x2, 247+2+self.y)
                
                canvas.coords(self.e2_Lleg2, 886+self.x+3, 263+self.y, 901+self.x+3, 273+self.y)
                
                canvas.coords(self.e2_Rleg2, 901-2+self.x-3, 263+self.y, 916-2+self.x-3, 273+self.y)
                #print(self.x2, self.Frame, self.counterFrame)
                

            elif self.Frame == 3: #returning 
                self.x2 += 1
                
                canvas.coords(self.e2_shoulder2, 899+self.x-self.x2, 237+2+self.y, 911+self.x-self.x2, 237+2+self.y, 911+self.x-self.x2, 249+2+self.y, 899+self.x-self.x2, 249+2+self.y)
                canvas.coords(self.e2_shoulderspike2, 901+self.x-self.x2, 237+2+self.y, 905+self.x-self.x2, 227+2+self.y, 909+self.x-self.x2, 237+2+self.y)
                canvas.coords(self.e2_lefthand2, 897+self.x-self.x2, 242+2+self.y, 913+self.x-self.x2, 257+2+self.y)
                
                canvas.coords(self.e2_spearshaft2, 879+self.x+self.x2, 217+2+self.y, 882+self.x+self.x2, 217+2+self.y, 882+self.x+self.x2, 277+2+self.y, 879+self.x+self.x2, 277+2+self.y)
                canvas.coords(self.e2_spearhead2, 875+self.x+self.x2, 217+2+self.y, 880+self.x+self.x2, 202+2+self.y, 886+self.x+self.x2, 217+2+self.y)
                canvas.coords(self.e2_righthand2, 872+self.x+self.x2, 232+2+self.y, 888+self.x+self.x2, 247+2+self.y)
                
                canvas.coords(self.e2_Lleg2, 886+self.x+3, 263+self.y, 901+self.x+3, 273+self.y)
                
                canvas.coords(self.e2_Rleg2, 901-2+self.x-3, 263+self.y, 916-2+self.x-3, 273+self.y)
                #print(self.x2, self.Frame, self.counterFrame)
                

            #self.x2 = 0


                        


        self.e2_righthandhitbox = canvas.coords(self.e2_righthand2) #to stop enemy2 when it hits window border
        
        self.counterFrame += 1 #Add one to counterFrame (Starts at 0)
        #print(self.Frame)
        #print(self.counterFrame)
        #print(self.counterFrame)
        
        if 0 <= self.counterFrame < 25: #Once 25 iterations of draw() in the while loop far far below, change frame to 0
            self.Frame = 0
        elif 25 <= self.counterFrame < 50: #if self.counterFrame > 25: #Once 50 iterations of draw() in the while loop far far below, change frame to 1
            self.Frame = 1
        elif 50 <= self.counterFrame < 75:
            self.Frame = 2
        elif 75 <= self.counterFrame < 100:
            self.Frame = 3
        if self.counterFrame == 100: #Reset the counter after 50 so that the cycle repeats over and over again.
            self.counterFrame = 0
            self.Frame = 0
        





class Enemy1: #Designs by Edward. Eye animation by Leon.
    def __init__(self,canvas):
        self.canvas = canvas
        self.x, self.y = 0, 0 #Tells how far the creature has moved relative to it's original position. With this animation is possible.
        self.yEye = 0 #Tells when the eye should open and close. Only the eye should use these coordinates.
        self.counter = -100 #Counter starts at -100 so there is a delay in which the eye blinks. Without this enemy1 would blink all the time like a drug addict.
        self.counter2 = 0 #This is to tell the eye to move either closing or opening the eye aniamtion.

        #I need help creating an enemy. Could be anything, but I'd prefer something medieval.

        #Law: Made some of these shapes outlined black so it fits in with the rest of the designs.
        self.e1_name = canvas.create_text(750, 70, anchor="center", fill="red", text="Lil Baby Cyclops", font=("Fixedsys", 16))
        #shoulder
        self.e1_neck = canvas.create_polygon(758, 110, 730,120,780,120, fill="saddle brown", outline="black")
        #body
        self.e1_body = canvas.create_polygon(730,120,730,160,780,160,780,120,fill="saddle brown")
        #arms
        self.e1_leftArm = canvas.create_polygon(730,120,710,140,710,160,730,140,fill="tan", outline="black")
        self.e1_rightArm = canvas.create_polygon(780, 120, 800, 140, 800, 160, 780, 140, fill="tan", outline="black")
        #head
        self.e1_head = canvas.create_oval(745, 80, 765, 120, fill="tan", outline="black")
        #pants
        self.e1_pants = canvas.create_polygon(730,160,730,180,780,180,780,160,fill="dim grey", outline="black")
        #hands
        self.e1_leftHand = canvas.create_oval(700,130,720,160,fill="tan", outline="black")
        # feet
        self.e1_leftFoot = canvas.create_oval(780, 165, 780, 175, fill="black", outline="black")     
        #eye
        self.e1_eye = canvas.create_oval(750,90,760,100, fill="white", outline="black")
        self.e1_pupil = canvas.create_oval(754, 93, 757, 97, fill="black")
        #cannon maybe future levels. Don't want to instant kill player in tutorial.
        #self.el_cannon1=canvas.create_oval(600,130,695,180, fill="grey")

    def draw(self):  #MOVE BOI
        if self.counter == 10: #This is for animating the eye. Every time the self.counter reaaches 10, move the eye. self.counter starts at -100 and iterates postively up. 110 iterations of draw will move the eye.
            if 0 <= self.counter2 <= 4: #If self.counter2 reaches 0, 1, 2, 3, or 4, run through here. It will iterate 5 times before going on to elif. Which is when the eye closes.
                self.yEye += 1 #Make self.yEye add 1. Starts at 0. Goes up to 5.
                canvas.coords(self.e1_eye, 750+self.x,90+self.yEye+self.y,760+self.x,100-self.yEye+self.y) #Move Top left coords down by adding self.yEye to it. Move bottom right coords up by subtracting self.yEye from it.
                self.counter = 0 #Reset self.counter to 0. So 10 iterations later, move the eye again.
                self.counter2 += 1 #tracks counter #Move self.counter2 up one starting from 0. Goes from 0 to 4.
                #print("if")
                #print("counter 2:", self.counter2)
            elif 4 < self.counter2 <= 9: #When self.counter2 = 5, 6, 7, 8, 9, run through this elif block. Iterates 5 times. This is when the eye opens.
                self.yEye -= 1 #Starts at 5. Ends at 0.
                canvas.coords(self.e1_eye, 750+self.x,90+self.yEye+self.y,760+self.x,100-self.yEye+self.y) #eye goes up #Eye opens until full height is reached.
                self.counter = 0
                self.counter2 += 1 #Move self.counter2 up one starting from 0. Goes from 5 to 9. Which is 5, 6, 7, 8, 9. 5 iterations.
                #print("first elif")
                #print("counter 2:", self.counter2)

            if self.counter2 == 5: #When eye closes, move the pupil off screen or else the pupil will overlap the closed eye.
                canvas.move(self.e1_pupil, -10000, -10000)

            if self.counter2 == 6: #When eye opens, move the pupil back on screen in original position.
                canvas.move(self.e1_pupil, 10000, 10000)
                
        if self.counter2 == 10: #After a cycle of 5 if "0 <= self.counter2 <= 4:" and then 5 "elif 4 < self.counter2 <= 9:", reset the variables so the cycle repeats.
            #print("first else")
            self.counter2 = 0
            self.yEye = 0
            self.counter = -100 #self.counter starts at -100 so that there is a time in which enemy1's eye does not blink. 110 iterations later, the eye should start closing again.
        self.counter += 1 #self.counter goes from -100 to 110 then to 0-10 10 times then repeat the cycle.

class Enemy3: #Third enemy design. I'm planning on making this one (design, animation, health, hitboxes), however anyone can ask for edits or anything. Incomplete.
    def __init__(self,canvas, voice, player):
        self.canvas = canvas
        self.voice = voice
        self.player = player

        #Variables
        self.Frame = 0 #0, 1
        self.x, self.y = 0,0
        self.counterFrame = 0
        self.Looking = "Left"
        self.bodyBob = 0
        self.canvas_width = self.canvas.winfo_width()
        self.hpLoss = 0
        self.isDead = False
        self.deleteOnce = True
        self.xDeathHead, self.yDeathHead = 0, 0
        self.yDeathHeadInAir = True
        self.xDeathRibCage, self.yDeathRibCage = 0, 0
        self.xDeathLHand, self.yDeathLHand = 0, 0
        self.xDeathRHand, self.yDeathRHand = 0, 0
        self.deathAnimation = True
        self.deleteEnemy3Complete = True
        self.deleteEnemy3Counter = 0
        self.inAttackRange = False
        self.xAttackArm, self.yAttackArm, self.yAttackArmCounter = 0, 0, 0
        self.xAttackHead, self.yAttackHead, self.xAttackHeadCounter = 0, 0, 0
        self.xAttackTorso, self.yAttackTorso, self.xAttackTorsoCounter = 0, 0, 0
        self.hitPlayerOnce = False

        #Name Above Head, health bar, and all head shapes
        self.e3_name = canvas.create_text(790, 290, anchor="center", fill="red", text="Level 0 Skeleton", font=("Fixedsys", 16))
        self.e3_hp = canvas.create_rectangle(740, 297, 840, 302, fill="red2")
        self.e3_head = canvas.create_oval(777, 305, 802, 330, fill="SlateGray1")
        self.e3_headBlank = canvas.create_rectangle(785, 322, 802, 330, fill="gray30", outline="")
        self.e3_headBlankLine = canvas.create_line(785, 322, 802, 322)
        self.e3_spine = canvas.create_rectangle(787, 322, 795, 330, fill="SlateGray1", outline="black")
        self.e3_spineLine = canvas.create_line(787, 324, 795, 328)
        self.e3_teeth = canvas.create_rectangle(777, 322, 785, 330, fill="SlateGray1", outline="black")
        self.e3_teethDown1 = canvas.create_line(780, 322, 780, 330)
        self.e3_teethDown2 = canvas.create_line(783, 322, 783, 330)
        self.e3_teethCross = canvas.create_line(777, 326, 785, 326)
        self.e3_nose = canvas.create_oval(778, 318, 779, 319, fill="black")
        self.e3_eye = canvas.create_oval(780, 312, 785, 319, fill="cyan")
        self.e3_eye2 = canvas.create_oval(788, 314, 789, 319, fill="black")

        #All torso shapes.
        self.e3_torso = canvas.create_polygon(782, 330, 797, 330, 797, 355, 782, 355, fill="SlateGray1", outline="black")
        self.e3_ribMidDown = canvas.create_line(784, 330, 784, 345)
        self.e3_ribHighestCross = canvas.create_line(782, 333, 784, 333)
        self.e3_ribHighest = canvas.create_polygon(786, 333, 795, 332, 786, 334, fill="black", outline="black")
        self.e3_ribMiddleCross = canvas.create_line(782, 336, 784, 336)
        self.e3_ribMiddle = canvas.create_polygon(786, 336, 795, 335, 786, 337, fill="black", outline="black")
        self.e3_ribThirdCross = canvas.create_line(782, 339, 784, 339)
        self.e3_ribThird = canvas.create_polygon(786, 339, 795, 338, 786, 340, fill="black", outline="black")
        self.e3_ribFourthCross = canvas.create_line(782, 342, 784, 342)
        self.e3_ribFourth = canvas.create_polygon(786, 342, 795, 341, 786, 343, fill="black", outline="black")
        self.e3_ribLowest = canvas.create_line(782, 345, 789, 345)
        self.e3_ribLowest1 = canvas.create_line(789, 344, 794, 344)
        self.e3_ribLowest2 = canvas.create_line(794, 343, 796, 343)
        self.e3_ribLowest3 = canvas.create_line(796, 342, 797, 342)
        self.e3_torsoBlank = canvas.create_polygon(782, 346, 787, 346, 787, 351, 782, 351, fill="gray30", outline="")
        self.e3_spine2VerticalLine = canvas.create_line(787, 346, 787, 350)
        self.e3_torsoBlank2 = canvas.create_polygon(796, 343, 798, 343, 798, 348, 796, 348, fill="gray30", outline="")
        self.e3_spine2VerticalLine1 = canvas.create_line(796, 342, 796, 350)
        self.e3_sprin2DiagonalLine = canvas.create_line(788, 346, 796, 348)
        self.e3_hipLine = canvas.create_line(782, 350, 792, 350)
        self.e3_hipLine2 = canvas.create_line(792, 349, 797, 349)
        self.e3_hipHole = canvas.create_oval(792, 352, 795, 355, fill="black")
        
        #Arms
        self.e3_Larm = canvas.create_oval(767, 330, 782, 345, fill="SlateGray1", outline="black")
        self.e3_Lfinger = canvas.create_line(768, 333, 775, 333)
        self.e3_Lfinger2 = canvas.create_line(767, 336, 776, 336)
        self.e3_Lfinger3 = canvas.create_line(767, 339, 776, 339)
        self.e3_Lfinger4 = canvas.create_line(768, 342, 774, 342)
        self.e3_LfingerDown = canvas.create_line(775, 333, 775, 339)
        self.e3_LfingerDown1 = canvas.create_line(774, 339, 774, 342)
        self.e3_Rarm = canvas.create_oval(797, 330, 812, 345, fill="SlateGray1", outline="black")

        #Legs and hitbox
        self.e3_Rleg = canvas.create_oval(797, 355, 812, 363, fill="SlateGray1", outline="black")
        self.e3_RtoeLine = canvas.create_line(797, 360, 802, 360)
        self.e3_RtoeLine1 = canvas.create_line(797, 358, 802, 358)
        self.e3_RtoeLine2 = canvas.create_line(797, 356, 802, 356)
        self.e3_Lleg = canvas.create_oval(767, 355, 782, 363, fill="SlateGray1", outline="black")
        self.e3_LtoeLine = canvas.create_line(767, 360, 772, 360)
        self.e3_LtoeLine1 = canvas.create_line(767, 358, 772, 358)
        self.e3_LtoeLine2 = canvas.create_line(767, 356, 772, 356)
        self.e3_hitbox = canvas.create_line(802, 305, 777, 363)
        canvas.itemconfigure(self.e3_hitbox, state='hidden') #hides shape.

    def draw(self):
        self.hitboxCoords = canvas.coords(self.e3_hitbox)

        if self.hitboxCoords[2] <= 0 and self.inAttackRange == False: #If Enemy3 hits the left or right border, turn it around.
            self.Looking = "Right"
        elif self.hitboxCoords[2] >= self.canvas_width and self.inAttackRange == False:
            self.Looking = "Left"
            
        #If not in attack range yet and in the range to hit, change to self.inAttackRange = True. This changes all animations to attacking.
        if self.hpLoss < 50 and self.inAttackRange == False and -10 <= self.player.hitbox[3] - self.hitboxCoords[3] <= 10 and ((self.player.hitbox[2] < self.hitboxCoords[0] and 1 <= self.hitboxCoords[0] - self.player.hitbox[2] <= 50) or (self.player.hitbox[2] > self.hitboxCoords[2] and 1 <= self.player.hitbox[2] - self.hitboxCoords[2] <= 50) or (self.player.hitbox[0] > self.hitboxCoords[2] and 1 <= self.player.hitbox[0] - self.hitboxCoords[2] <= 50) or (self.player.hitbox[0] < self.hitboxCoords[0] and 1 <=  self.hitboxCoords[0] - self.player.hitbox[0] <= 50)):
            self.inAttackRange = True
            #print("self.inAttackRange == True")

        #else: #At end of attack animation, make it False
            #self.inAttackRange = False
        #elif self.inAttackRange == False and self.player.hitbox[3] == 363 and self.Looking == "Right" and (self.player.hitbox[2] < self.hitboxCoords[0] and 1 <= self.hitboxCoords[0] - self.player.hitbox[2] <= 10) or (self.player.hitbox[2] > self.hitboxCoords[2] and 1 <= self.player.hitbox[2] - self.hitboxCoords[2] <= 10):
            #self.inAttackRange = True
            #print("self.inAttackRange == True 2")

        if self.player.hitbox[3] != self.hitboxCoords[3]: #self.counterFrame == 99 and 
            if self.player.hitbox[3] - self.hitboxCoords[3] < 0 and self.hitboxCoords[3] > 0:
                self.y -= 1
                #print("First if")
            elif self.player.hitbox[3] - self.hitboxCoords[3] > 0 and self.hitboxCoords[3] < 700:
                self.y += 1
                #print("Second if")

        if self.Looking == "Left" and self.counterFrame == 99 and self.player.hitbox[2] > self.hitboxCoords[2] and self.inAttackRange == False: #If player lands behind Emeny3, turn around.
            self.Looking = "Right"
        elif self.Looking == "Right" and self.counterFrame == 99 and self.player.hitbox[2] < self.hitboxCoords[0] and self.inAttackRange == False: #self.player.hitbox[3] == 363 and
            self.Looking = "Left"

        if 0 <= self.counterFrame <= 100 and self.Looking == "Left" and self.hpLoss < 50 and self.isDead == False and self.inAttackRange == False:
            self.x -= 10
            
            if self.Frame == 0 and self.counterFrame <= 50:
                self.bodyBob = 5
            elif self.Frame == 1 and self.counterFrame > 50:
                self.bodyBob = 0
            
            #Nameplate and Head
            canvas.coords(self.e3_name, 790+self.x, 290+self.y+self.bodyBob)
            canvas.coords(self.e3_hp, 740+self.x+self.hpLoss, 297+self.y+self.bodyBob, 840+self.x-self.hpLoss, 302+self.y+self.bodyBob)
            canvas.coords(self.e3_head, 777+self.x, 305+self.y+self.bodyBob, 802+self.x, 330+self.y+self.bodyBob)
            canvas.coords(self.e3_headBlank, 785+self.x, 322+self.y+self.bodyBob, 802+self.x, 330+self.y+self.bodyBob)
            canvas.coords(self.e3_headBlankLine, 785+self.x, 322+self.y+self.bodyBob, 802+self.x, 322+self.y+self.bodyBob)
            canvas.coords(self.e3_spine, 787+self.x, 322+self.y+self.bodyBob, 795+self.x, 330+self.y+self.bodyBob)
            canvas.coords(self.e3_spineLine, 787+self.x, 324+self.y+self.bodyBob, 795+self.x, 328+self.y+self.bodyBob)
            canvas.coords(self.e3_teeth, 777+self.x, 322+self.y+self.bodyBob, 785+self.x, 330+self.y+self.bodyBob)
            canvas.coords(self.e3_teethDown1, 780+self.x, 322+self.y+self.bodyBob, 780+self.x, 330+self.y+self.bodyBob)
            canvas.coords(self.e3_teethDown2, 783+self.x, 322+self.y+self.bodyBob, 783+self.x, 330+self.y+self.bodyBob)
            canvas.coords(self.e3_teethCross, 777+self.x, 326+self.y+self.bodyBob, 785+self.x, 326+self.y+self.bodyBob)
            canvas.coords(self.e3_nose, 778+self.x, 318+self.y+self.bodyBob, 779+self.x, 319+self.y+self.bodyBob)
            canvas.coords(self.e3_eye, 780+self.x, 312+self.y+self.bodyBob, 785+self.x, 319+self.y+self.bodyBob)
            canvas.coords(self.e3_eye2, 788+self.x, 314+self.y+self.bodyBob, 789+self.x, 319+self.y+self.bodyBob)
            #Torso
            canvas.coords(self.e3_torso, 782+self.x, 330+self.y+self.bodyBob, 797+self.x, 330+self.y+self.bodyBob, 797+self.x, 355+self.y+self.bodyBob, 782+self.x, 355+self.y+self.bodyBob)
            canvas.coords(self.e3_ribMidDown, 784+self.x, 330+self.y+self.bodyBob, 784+self.x, 345+self.y+self.bodyBob)
            canvas.coords(self.e3_ribHighestCross, 782+self.x, 333+self.y+self.bodyBob, 784+self.x, 333+self.y+self.bodyBob)
            canvas.coords(self.e3_ribHighest, 786+self.x, 333+self.y+self.bodyBob, 795+self.x, 332+self.y+self.bodyBob, 786+self.x, 334+self.y+self.bodyBob)
            canvas.coords(self.e3_ribMiddleCross, 782+self.x, 336+self.y+self.bodyBob, 784+self.x, 336+self.y+self.bodyBob)
            canvas.coords(self.e3_ribMiddle, 786+self.x, 336+self.y+self.bodyBob, 795+self.x, 335+self.y+self.bodyBob, 786+self.x, 337+self.y+self.bodyBob)
            canvas.coords(self.e3_ribThirdCross, 782+self.x, 339+self.y+self.bodyBob, 784+self.x, 339+self.y+self.bodyBob)
            canvas.coords(self.e3_ribThird, 786+self.x, 339+self.y+self.bodyBob, 795+self.x, 338+self.y+self.bodyBob, 786+self.x, 340+self.y+self.bodyBob)
            canvas.coords(self.e3_ribFourthCross, 782+self.x, 342+self.y+self.bodyBob, 784+self.x, 342+self.y+self.bodyBob)
            canvas.coords(self.e3_ribFourth, 786+self.x, 342+self.y+self.bodyBob, 795+self.x, 341+self.y+self.bodyBob, 786+self.x, 343+self.y+self.bodyBob)
            canvas.coords(self.e3_ribLowest, 782+self.x, 345+self.y+self.bodyBob, 789+self.x, 345+self.y+self.bodyBob)
            canvas.coords(self.e3_ribLowest1, 789+self.x, 344+self.y+self.bodyBob, 794+self.x, 344+self.y+self.bodyBob)
            canvas.coords(self.e3_ribLowest2, 794+self.x, 343+self.y+self.bodyBob, 796+self.x, 343+self.y+self.bodyBob)
            canvas.coords(self.e3_ribLowest3, 796+self.x, 342+self.y+self.bodyBob, 797+self.x, 342+self.y+self.bodyBob)
            canvas.coords(self.e3_torsoBlank, 782+self.x, 346+self.y+self.bodyBob, 787+self.x, 346+self.y+self.bodyBob, 787+self.x, 351+self.y+self.bodyBob, 782+self.x, 351+self.y+self.bodyBob)
            canvas.coords(self.e3_spine2VerticalLine, 787+self.x, 346+self.y+self.bodyBob, 787+self.x, 350+self.y+self.bodyBob)
            canvas.coords(self.e3_torsoBlank2, 796+self.x, 343+self.y+self.bodyBob, 798+self.x, 343+self.y+self.bodyBob, 798+self.x, 348+self.y+self.bodyBob, 796+self.x, 348+self.y+self.bodyBob)
            canvas.coords(self.e3_spine2VerticalLine1, 796+self.x, 342+self.y+self.bodyBob, 796+self.x, 350+self.y+self.bodyBob)
            canvas.coords(self.e3_sprin2DiagonalLine, 788+self.x, 346+self.y+self.bodyBob, 796+self.x, 348+self.y+self.bodyBob)
            canvas.coords(self.e3_hipLine, 782+self.x, 350+self.y+self.bodyBob, 792+self.x, 350+self.y+self.bodyBob)
            canvas.coords(self.e3_hipLine2, 792+self.x, 349+self.y+self.bodyBob, 797+self.x, 349+self.y+self.bodyBob)
            canvas.coords(self.e3_hipHole, 792+self.x, 352+self.y+self.bodyBob, 795+self.x, 355+self.y+self.bodyBob)
            if self.Frame == 0: #Arms and legs in AND moving
                #Arms
                canvas.coords(self.e3_Larm, 767+self.x+15, 330+self.y+10, 782+self.x+15, 345+self.y+10)
                canvas.coords(self.e3_Lfinger, 768+self.x+15, 333+self.y+10, 775+self.x+15, 333+self.y+10)
                canvas.coords(self.e3_Lfinger2, 767+self.x+15, 336+self.y+10, 776+self.x+15, 336+self.y+10)
                canvas.coords(self.e3_Lfinger3, 767+self.x+15, 339+self.y+10, 776+self.x+15, 339+self.y+10)
                canvas.coords(self.e3_Lfinger4, 768+self.x+15, 342+self.y+10, 774+self.x+15, 342+self.y+10)
                canvas.coords(self.e3_LfingerDown, 775+self.x+15, 333+self.y+10, 775+self.x+15, 339+self.y+10)
                canvas.coords(self.e3_LfingerDown1, 774+self.x+15, 339+self.y+10, 774+self.x+15, 342+self.y+10)
                canvas.coords(self.e3_Rarm, 797+self.x-15, 330+self.y+10, 812+self.x-15, 345+self.y+10)
                #Legs and hitbox
                canvas.coords(self.e3_Rleg, 797+self.x-10, 355+self.y, 812+self.x-10, 363+self.y)
                canvas.coords(self.e3_RtoeLine, 797+self.x-10, 360+self.y, 802+self.x-10, 360+self.y)
                canvas.coords(self.e3_RtoeLine1, 797+self.x-10, 358+self.y, 802+self.x-10, 358+self.y)
                canvas.coords(self.e3_RtoeLine2, 797+self.x-10, 356+self.y, 802+self.x-10, 356+self.y)
                canvas.coords(self.e3_Lleg, 767+self.x+10, 355+self.y, 782+self.x+10, 363+self.y)
                canvas.coords(self.e3_LtoeLine, 767+self.x+10, 360+self.y, 772+self.x+10, 360+self.y)
                canvas.coords(self.e3_LtoeLine1, 767+self.x+10, 358+self.y, 772+self.x+10, 358+self.y)
                canvas.coords(self.e3_LtoeLine2, 767+self.x+10, 356+self.y, 772+self.x+10, 356+self.y)
                canvas.coords(self.e3_hitbox, 802+self.x, 305+self.y, 777+self.x, 363+self.y)
            elif self.Frame == 1: #Arms and legs out AND NOT moving
                #Arms
                canvas.coords(self.e3_Larm, 767+self.x, 330+self.y, 782+self.x, 345+self.y)
                canvas.coords(self.e3_Lfinger, 768+self.x, 333+self.y, 775+self.x, 333+self.y)
                canvas.coords(self.e3_Lfinger2, 767+self.x, 336+self.y, 776+self.x, 336+self.y)
                canvas.coords(self.e3_Lfinger3, 767+self.x, 339+self.y, 776+self.x, 339+self.y)
                canvas.coords(self.e3_Lfinger4, 768+self.x, 342+self.y, 774+self.x, 342+self.y)
                canvas.coords(self.e3_LfingerDown, 775+self.x, 333+self.y, 775+self.x, 339+self.y)
                canvas.coords(self.e3_LfingerDown1, 774+self.x, 339+self.y, 774+self.x, 342+self.y)
                canvas.coords(self.e3_Rarm, 797+self.x, 330+self.y, 812+self.x, 345+self.y)
                #Legs and hitbox
                canvas.coords(self.e3_Rleg, 797+self.x, 355+self.y, 812+self.x, 363+self.y)
                canvas.coords(self.e3_RtoeLine, 797+self.x, 360+self.y, 802+self.x, 360+self.y)
                canvas.coords(self.e3_RtoeLine1, 797+self.x, 358+self.y, 802+self.x, 358+self.y)
                canvas.coords(self.e3_RtoeLine2, 797+self.x, 356+self.y, 802+self.x, 356+self.y)
                canvas.coords(self.e3_Lleg, 767+self.x, 355+self.y, 782+self.x, 363+self.y)
                canvas.coords(self.e3_LtoeLine, 767+self.x, 360+self.y, 772+self.x, 360+self.y)
                canvas.coords(self.e3_LtoeLine1, 767+self.x, 358+self.y, 772+self.x, 358+self.y)
                canvas.coords(self.e3_LtoeLine2, 767+self.x, 356+self.y, 772+self.x, 356+self.y)
                canvas.coords(self.e3_hitbox, 802+self.x, 305+self.y, 777+self.x, 363+self.y)
                
        elif 0 <= self.counterFrame <= 100 and self.Looking == "Right" and self.hpLoss < 50 and self.isDead == False and self.inAttackRange == False: #Enemy3 has to be mirrored and turned facing and moving right
            self.x += 10
            
            if self.Frame == 0 and self.counterFrame <= 50:
                self.bodyBob = 5
            elif self.Frame == 1 and self.counterFrame > 50:
                self.bodyBob = 0
            
            #Nameplate and Head
            canvas.coords(self.e3_name, 790+self.x, 290+self.y+self.bodyBob)
            canvas.coords(self.e3_hp, 740+self.x+self.hpLoss, 297+self.y+self.bodyBob, 840+self.x-self.hpLoss, 302+self.y+self.bodyBob)
            canvas.coords(self.e3_head, 777+self.x+26, 305+self.y+self.bodyBob, 802+self.x-24, 330+self.y+self.bodyBob)
            canvas.coords(self.e3_headBlank, 785+self.x+10, 322+self.y+self.bodyBob, 802+self.x-24, 330+self.y+self.bodyBob)
            canvas.coords(self.e3_headBlankLine, 785+self.x+10, 322+self.y+self.bodyBob, 802+self.x-24, 322+self.y+self.bodyBob)
            canvas.coords(self.e3_spine, 787+self.x+6, 322+self.y+self.bodyBob, 795+self.x-10, 330+self.y+self.bodyBob)
            canvas.coords(self.e3_spineLine, 787+self.x+6, 324+self.y+self.bodyBob, 795+self.x-10, 328+self.y+self.bodyBob)
            canvas.coords(self.e3_teeth, 777+self.x+26, 322+self.y+self.bodyBob, 785+self.x+10, 330+self.y+self.bodyBob)
            canvas.coords(self.e3_teethDown1, 780+self.x+20, 322+self.y+self.bodyBob, 780+self.x+20, 330+self.y+self.bodyBob)
            canvas.coords(self.e3_teethDown2, 783+self.x+14, 322+self.y+self.bodyBob, 783+self.x+14, 330+self.y+self.bodyBob)
            canvas.coords(self.e3_teethCross, 777+self.x+26, 326+self.y+self.bodyBob, 785+self.x+10, 326+self.y+self.bodyBob)
            canvas.coords(self.e3_nose, 778+self.x+24, 318+self.y+self.bodyBob, 779+self.x+22, 319+self.y+self.bodyBob)
            canvas.coords(self.e3_eye, 780+self.x+20, 312+self.y+self.bodyBob, 785+self.x+10, 319+self.y+self.bodyBob)
            canvas.coords(self.e3_eye2, 788+self.x+4, 314+self.y+self.bodyBob, 789+self.x+2, 319+self.y+self.bodyBob)
            #Torso
            canvas.coords(self.e3_torso, 782+self.x+16, 330+self.y+self.bodyBob, 797+self.x-14, 330+self.y+self.bodyBob, 797+self.x-14, 355+self.y+self.bodyBob, 782+self.x+16, 355+self.y+self.bodyBob)
            canvas.coords(self.e3_ribMidDown, 784+self.x+12, 330+self.y+self.bodyBob, 784+self.x+12, 345+self.y+self.bodyBob)
            canvas.coords(self.e3_ribHighestCross, 782+self.x+16, 333+self.y+self.bodyBob, 784+self.x+12, 333+self.y+self.bodyBob)
            canvas.coords(self.e3_ribHighest, 786+self.x+8, 333+self.y+self.bodyBob, 795+self.x-10, 332+self.y+self.bodyBob, 786+self.x+8, 334+self.y+self.bodyBob)
            canvas.coords(self.e3_ribMiddleCross, 782+self.x+16, 336+self.y+self.bodyBob, 784+self.x+12, 336+self.y+self.bodyBob)
            canvas.coords(self.e3_ribMiddle, 786+self.x+8, 336+self.y+self.bodyBob, 795+self.x-10, 335+self.y+self.bodyBob, 786+self.x+8, 337+self.y+self.bodyBob)
            canvas.coords(self.e3_ribThirdCross, 782+self.x+16, 339+self.y+self.bodyBob, 784+self.x+12, 339+self.y+self.bodyBob)
            canvas.coords(self.e3_ribThird, 786+self.x+8, 339+self.y+self.bodyBob, 795+self.x-10, 338+self.y+self.bodyBob, 786+self.x+8, 340+self.y+self.bodyBob)
            canvas.coords(self.e3_ribFourthCross, 782+self.x+16, 342+self.y+self.bodyBob, 784+self.x+12, 342+self.y+self.bodyBob)
            canvas.coords(self.e3_ribFourth, 786+self.x+8, 342+self.y+self.bodyBob, 795+self.x-10, 341+self.y+self.bodyBob, 786+self.x+8, 343+self.y+self.bodyBob)
            canvas.coords(self.e3_ribLowest, 782+self.x+16, 345+self.y+self.bodyBob, 789+self.x+2, 345+self.y+self.bodyBob)
            canvas.coords(self.e3_ribLowest1, 789+self.x+2, 344+self.y+self.bodyBob, 794+self.x-8, 344+self.y+self.bodyBob)
            canvas.coords(self.e3_ribLowest2, 794+self.x-8, 343+self.y+self.bodyBob, 796+self.x-12, 343+self.y+self.bodyBob)
            canvas.coords(self.e3_ribLowest3, 796+self.x-12, 342+self.y+self.bodyBob, 797+self.x-14, 342+self.y+self.bodyBob)
            canvas.coords(self.e3_torsoBlank, 782+self.x+16+1, 346+self.y+self.bodyBob, 787+self.x+6, 346+self.y+self.bodyBob, 787+self.x+6, 351+self.y+self.bodyBob, 782+self.x+16+1, 351+self.y+self.bodyBob)
            canvas.coords(self.e3_spine2VerticalLine, 787+self.x+6, 346+self.y+self.bodyBob, 787+self.x+6, 350+self.y+self.bodyBob)
            canvas.coords(self.e3_torsoBlank2, 796+self.x-12, 343+self.y+self.bodyBob, 798+self.x-16, 343+self.y+self.bodyBob, 798+self.x-16, 348+self.y+self.bodyBob, 796+self.x-12, 348+self.y+self.bodyBob)
            canvas.coords(self.e3_spine2VerticalLine1, 796+self.x-12, 342+self.y+self.bodyBob, 796+self.x-12, 350+self.y+self.bodyBob)
            canvas.coords(self.e3_sprin2DiagonalLine, 788+self.x+4, 346+self.y+self.bodyBob, 796+self.x-12, 348+self.y+self.bodyBob)
            canvas.coords(self.e3_hipLine, 782+self.x+16, 350+self.y+self.bodyBob, 792+self.x-4, 350+self.y+self.bodyBob)
            canvas.coords(self.e3_hipLine2, 792+self.x-4, 349+self.y+self.bodyBob, 797+self.x-14, 349+self.y+self.bodyBob)
            canvas.coords(self.e3_hipHole, 792+self.x-4, 352+self.y+self.bodyBob, 795+self.x-10, 355+self.y+self.bodyBob)
            if self.Frame == 0: #Arms and legs in AND moving
                #Arms
                canvas.coords(self.e3_Larm, 767+self.x+15, 330+self.y+10, 782+self.x+15, 345+self.y+10)
                canvas.coords(self.e3_Lfinger, 768+self.x+15, 333+self.y+10, 775+self.x+15, 333+self.y+10)
                canvas.coords(self.e3_Lfinger2, 767+self.x+15, 336+self.y+10, 776+self.x+15, 336+self.y+10)
                canvas.coords(self.e3_Lfinger3, 767+self.x+15, 339+self.y+10, 776+self.x+15, 339+self.y+10)
                canvas.coords(self.e3_Lfinger4, 768+self.x+15, 342+self.y+10, 774+self.x+15, 342+self.y+10)
                canvas.coords(self.e3_LfingerDown, 775+self.x+15, 333+self.y+10, 775+self.x+15, 339+self.y+10)
                canvas.coords(self.e3_LfingerDown1, 774+self.x+15, 339+self.y+10, 774+self.x+15, 342+self.y+10)
                canvas.coords(self.e3_Rarm, 797+self.x-15, 330+self.y+10, 812+self.x-15, 345+self.y+10)
                #Legs and hitbox
                canvas.coords(self.e3_Rleg, 797+self.x+10-14, 355+self.y, 812+self.x+10-44, 363+self.y)
                canvas.coords(self.e3_RtoeLine, 797+self.x+10-14, 360+self.y, 802+self.x+10-24, 360+self.y)
                canvas.coords(self.e3_RtoeLine1, 797+self.x+10-14, 358+self.y, 802+self.x+10-24, 358+self.y)
                canvas.coords(self.e3_RtoeLine2, 797+self.x+10-14, 356+self.y, 802+self.x+10-24, 356+self.y)
                canvas.coords(self.e3_Lleg, 767+self.x-10+46, 355+self.y, 782+self.x-10+16, 363+self.y)
                canvas.coords(self.e3_LtoeLine, 767+self.x-10+46, 360+self.y, 772+self.x+-10+36, 360+self.y)
                canvas.coords(self.e3_LtoeLine1, 767+self.x-10+46, 358+self.y, 772+self.x-10+36, 358+self.y)
                canvas.coords(self.e3_LtoeLine2, 767+self.x-10+46, 356+self.y, 772+self.x-10+36, 356+self.y)
                canvas.coords(self.e3_hitbox, 802+self.x, 305+self.y, 777+self.x, 363+self.y)
            elif self.Frame == 1: #Arms and legs out AND NOT moving
                #Arms
                canvas.coords(self.e3_Larm, 767+self.x+46, 330+self.y, 782+self.x+16, 345+self.y)
                canvas.coords(self.e3_Lfinger, 768+self.x+44, 333+self.y, 775+self.x+30, 333+self.y)
                canvas.coords(self.e3_Lfinger2, 767+self.x+46, 336+self.y, 776+self.x+28, 336+self.y)
                canvas.coords(self.e3_Lfinger3, 767+self.x+46, 339+self.y, 776+self.x+28, 339+self.y)
                canvas.coords(self.e3_Lfinger4, 768+self.x+44, 342+self.y, 774+self.x+32, 342+self.y)
                canvas.coords(self.e3_LfingerDown, 775+self.x+30, 333+self.y, 775+self.x+30, 339+self.y)
                canvas.coords(self.e3_LfingerDown1, 774+self.x+32, 339+self.y, 774+self.x+32, 342+self.y)
                canvas.coords(self.e3_Rarm, 797+self.x-14, 330+self.y, 812+self.x-44, 345+self.y)
                #Legs and hitbox
                canvas.coords(self.e3_Rleg, 797+self.x-14, 355+self.y, 812+self.x-44, 363+self.y)
                canvas.coords(self.e3_RtoeLine, 797+self.x-14, 360+self.y, 802+self.x-24, 360+self.y)
                canvas.coords(self.e3_RtoeLine1, 797+self.x-14, 358+self.y, 802+self.x-24, 358+self.y)
                canvas.coords(self.e3_RtoeLine2, 797+self.x-14, 356+self.y, 802+self.x-24, 356+self.y)
                canvas.coords(self.e3_Lleg, 767+self.x+46, 355+self.y, 782+self.x+16, 363+self.y)
                canvas.coords(self.e3_LtoeLine, 767+self.x+46, 360+self.y, 772+self.x+36, 360+self.y)
                canvas.coords(self.e3_LtoeLine1, 767+self.x+46, 358+self.y, 772+self.x+36, 358+self.y)
                canvas.coords(self.e3_LtoeLine2, 767+self.x+46, 356+self.y, 772+self.x+36, 356+self.y)
                canvas.coords(self.e3_hitbox, 802+self.x, 305+self.y, 777+self.x, 363+self.y)
        elif self.hpLoss <= 50 and self.isDead == False and self.inAttackRange == False: #and self.inAttackRange == False:
            canvas.coords(self.e3_hp, 740+self.x+self.hpLoss, 297+self.y+self.bodyBob, 840+self.x-self.hpLoss, 302+self.y+self.bodyBob)

                #elif 0 <= self.counterFrame <= 50 and self.Looking == "Left" and self.hpLoss < 50 and self.isDead == False and self.inAttackRange == True:
        elif self.Looking == "Left" and self.hpLoss < 50 and self.isDead == False and self.inAttackRange == True:
            
            canvas.coords(self.e3_hp, 740+self.x+self.xDeathHead +self.hpLoss, 297+self.y+self.yDeathHead, 840+self.x+self.xDeathHead -self.hpLoss, 302+self.y+self.yDeathHead)

            #Head AND LEGS because it only has to iterate once, just leave it here.
            if self.xAttackHeadCounter <= 40:
                if 0 <= self.xAttackHeadCounter < 10: #Head moves back; Enemy3 preps for a swing attack
                    self.xAttackHead += 0.5*5
                    
                    
                    #canvas.coords(self.e3_Rarm, 797+self.x, 330+self.y, 812+self.x, 345+self.y)
            
                    #Legs and hitbox
                    canvas.coords(self.e3_Rleg, 797+self.x, 355+self.y, 812+self.x, 363+self.y)
                    canvas.coords(self.e3_RtoeLine, 797+self.x, 360+self.y, 802+self.x, 360+self.y)
                    canvas.coords(self.e3_RtoeLine1, 797+self.x, 358+self.y, 802+self.x, 358+self.y)
                    canvas.coords(self.e3_RtoeLine2, 797+self.x, 356+self.y, 802+self.x, 356+self.y)
                    canvas.coords(self.e3_Lleg, 767+self.x, 355+self.y, 782+self.x, 363+self.y)
                    canvas.coords(self.e3_LtoeLine, 767+self.x, 360+self.y, 772+self.x, 360+self.y)
                    canvas.coords(self.e3_LtoeLine1, 767+self.x, 358+self.y, 772+self.x, 358+self.y)
                    canvas.coords(self.e3_LtoeLine2, 767+self.x, 356+self.y, 772+self.x, 356+self.y)
                    #canvas.coords(self.e3_hitbox, 802+self.x, 305+self.y, 777+self.x, 363+self.y)
                    
                    #print("First if")
                #elif 5 <= self.xAttackHeadCounter < 20: #Head is stationary
                    #pass
                    #print("Second if")
                elif 25 <= self.xAttackHeadCounter < 35: #Head jerks forward during the swing attack
                    self.xAttackHead -= 1*5
                    
                    #print("Third if")
                elif 35 <= self.xAttackHeadCounter < 40: #Move head back into original position
                    self.xAttackHead += 0.5*5
                    
                    #print("Fourth if")
                        
                #canvas.coords(self.e3_name, 790+self.x+self.xAttackHead+self.x+self.xAttackHeadAttackHead , 290+self.y+self.yAttackHead+self.y+self.yAttackHeadAttackHead)
                #canvas.coords(self.e3_hp, 740+self.x+self.xAttackHead+self.x+self.xAttackHeadAttackHead +self.hpLoss, 297+self.y+self.yAttackHead+self.y+self.yAttackHeadAttackHead, 840+self.x+self.xAttackHead+self.x+self.xAttackHeadAttackHead -self.hpLoss, 302+self.y+self.yAttackHead+self.y+self.yAttackHeadAttackHead)
                canvas.coords(self.e3_head, 777+self.x+self.xAttackHead , 305+self.y+self.yAttackHead, 802+self.x+self.xAttackHead , 330+self.y+self.yAttackHead )
                canvas.coords(self.e3_headBlank, 785+self.x+self.xAttackHead , 322+self.y+self.yAttackHead , 802+self.x+self.xAttackHead , 330+self.y+self.yAttackHead )
                canvas.coords(self.e3_headBlankLine, 785+self.x+self.xAttackHead , 322+self.y+self.yAttackHead , 802+self.x+self.xAttackHead , 322+self.y+self.yAttackHead )
                canvas.coords(self.e3_spine, 787+self.x+self.xAttackHead , 322+self.y+self.yAttackHead , 795+self.x+self.xAttackHead , 330+self.y+self.yAttackHead )
                canvas.coords(self.e3_spineLine, 787+self.x+self.xAttackHead , 324+self.y+self.yAttackHead , 795+self.x+self.xAttackHead , 328+self.y+self.yAttackHead )
                canvas.coords(self.e3_teeth, 777+self.x+self.xAttackHead , 322+self.y+self.yAttackHead , 785+self.x+self.xAttackHead , 330+self.y+self.yAttackHead )
                canvas.coords(self.e3_teethDown1, 780+self.x+self.xAttackHead , 322+self.y+self.yAttackHead , 780+self.x+self.xAttackHead , 330+self.y+self.yAttackHead )
                canvas.coords(self.e3_teethDown2, 783+self.x+self.xAttackHead , 322+self.y+self.yAttackHead , 783+self.x+self.xAttackHead , 330+self.y+self.yAttackHead )
                canvas.coords(self.e3_teethCross, 777+self.x+self.xAttackHead , 326+self.y+self.yAttackHead , 785+self.x+self.xAttackHead , 326+self.y+self.yAttackHead )
                canvas.coords(self.e3_nose, 778+self.x+self.xAttackHead , 318+self.y+self.yAttackHead , 779+self.x+self.xAttackHead , 319+self.y+self.yAttackHead )
                canvas.coords(self.e3_eye, 780+self.x+self.xAttackHead , 312+self.y+self.yAttackHead , 785+self.x+self.xAttackHead , 319+self.y+self.yAttackHead )
                canvas.coords(self.e3_eye2, 788+self.x+self.xAttackHead , 314+self.y+self.yAttackHead , 789+self.x+self.xAttackHead , 319+self.y+self.yAttackHead )
            
            if self.yAttackArmCounter <= 40: #NOTICE THAT IT COUNTS THE Y
                if 0 <= self.yAttackArmCounter < 10: #Arms go behind ribcage.
                    #if 0 <= self.xAttackArmCounter < 5:
                    self.xAttackArm += 2*5
                    
                    #print("First if")
                #elif 5 <= self.yAttackArmCounter < 20: #Arms are stationary, getting ready to shove the player.
                   # pass
                    #print("Second if")
                elif 25 <= self.yAttackArmCounter < 35: #Arms jerk forward in a shoving motion.
                    #if 5 <= self.yAttackArmCounter < 10:
                    self.xAttackArm -= 5*5
                    
                    self.hitboxLarm = canvas.coords(self.e3_Larm)
                    global enemy3Damage
                    if self.hitPlayerOnce  == False and ( self.player.hitbox[1] <= self.hitboxLarm[1] <= self.player.hitbox[3] or self.player.hitbox[1] <= self.hitboxLarm[3] <= self.player.hitbox[3] ) and (self.player.hitbox[0] <= self.hitboxLarm[0] <= self.player.hitbox[2] or self.player.hitbox[2] <= self.hitboxLarm[2] <= self.player.hitbox[0]) and enemy3Damage == False: 
                        enemy3Damage = True
                        self.hitPlayerOnce = True
                        print("Gatekeeper of the 592th Hell, Diesect: HA! HA! HA! ONE LESS TO WORRY ABOUT! HA! HA! HA!")
                    #print("Third if")
                elif 35 <= self.yAttackArmCounter < 40: #Arms move back into original position.
                    #if 10 <= self.yAttackArmCounter < 15:
                    self.xAttackArm += 2*5
                    
                    #print("Fourth if")

                #Arms
                canvas.coords(self.e3_Larm, 767+self.x+15+self.xAttackArm, 330+self.y+self.yAttackArm-7, 782+self.x+15+self.xAttackArm, 345+self.y+self.yAttackArm-7)
                canvas.coords(self.e3_Lfinger, 768+self.x+15+self.xAttackArm, 333+self.y+self.yAttackArm-7, 775+self.x+15+self.xAttackArm, 333+self.y+self.yAttackArm-7)
                canvas.coords(self.e3_Lfinger2, 767+self.x+15+self.xAttackArm, 336+self.y+self.yAttackArm-7, 776+self.x+15+self.xAttackArm, 336+self.y+self.yAttackArm-7)
                canvas.coords(self.e3_Lfinger3, 767+self.x+15+self.xAttackArm, 339+self.y+self.yAttackArm-7, 776+self.x+15+self.xAttackArm, 339+self.y+self.yAttackArm-7)
                canvas.coords(self.e3_Lfinger4, 768+self.x+15+self.xAttackArm, 342+self.y+self.yAttackArm-7, 774+self.x+15+self.xAttackArm, 342+self.y+self.yAttackArm-7)
                canvas.coords(self.e3_LfingerDown, 775+self.x+15+self.xAttackArm, 333+self.y+self.yAttackArm-7, 775+self.x+15+self.xAttackArm, 339+self.y+self.yAttackArm-7)
                canvas.coords(self.e3_LfingerDown1, 774+self.x+15+self.xAttackArm, 339+self.y+self.yAttackArm-7, 774+self.x+15+self.xAttackArm, 342+self.y+self.yAttackArm-7)
                canvas.coords(self.e3_Rarm, 767+self.x+15+self.xAttackArm, 330+self.y+self.yAttackArm-5, 782+self.x+15+self.xAttackArm, 345+self.y+self.yAttackArm-5)

            if self.xAttackTorsoCounter <= 40:
                if 0 <= self.xAttackTorsoCounter < 10: #Torso moves back BUT less than it's head.
                    #if 0 <= self.xAttackTorsoCounter < 5:
                    self.xAttackTorso += 0.25*5
                    
                    #print("First if")
                #elif 10 <= self.xAttackTorsoCounter < 40: #Torso is stationary
                    #pass
                    #print("Second if")
                elif 25 <= self.xAttackTorsoCounter < 35: #Torso jerks forward during the swing attack
                    #if 5 <= self.xAttackTorsoCounter < 10:
                    self.xAttackTorso -= 0.5*5
                    
                    #print("Third if")
                elif 35 <= self.xAttackTorsoCounter < 40: #Move torso back into original position
                    #if 10 <= self.xAttackTorsoCounter < 15:
                    self.xAttackTorso += 0.25*5
                    
                    #print("Fourth if")

                canvas.coords(self.e3_torso, 782+self.x+self.xAttackTorso, 330+self.y+self.yAttackTorso, 797+self.x+self.xAttackTorso, 330+self.y+self.yAttackTorso, 797+self.x+self.xAttackTorso, 355+self.y+self.yAttackTorso, 782+self.x+self.xAttackTorso, 355+self.y+self.yAttackTorso)
                canvas.coords(self.e3_ribMidDown, 784+self.x+self.xAttackTorso, 330+self.y+self.yAttackTorso, 784+self.x+self.xAttackTorso, 345+self.y+self.yAttackTorso)
                canvas.coords(self.e3_ribHighestCross, 782+self.x+self.xAttackTorso, 333+self.y+self.yAttackTorso, 784+self.x+self.xAttackTorso, 333+self.y+self.yAttackTorso)
                canvas.coords(self.e3_ribHighest, 786+self.x+self.xAttackTorso, 333+self.y+self.yAttackTorso, 795+self.x+self.xAttackTorso, 332+self.y+self.yAttackTorso, 786+self.x+self.xAttackTorso, 334+self.y+self.yAttackTorso)
                canvas.coords(self.e3_ribMiddleCross, 782+self.x+self.xAttackTorso, 336+self.y+self.yAttackTorso, 784+self.x+self.xAttackTorso, 336+self.y+self.yAttackTorso)
                canvas.coords(self.e3_ribMiddle, 786+self.x+self.xAttackTorso, 336+self.y+self.yAttackTorso, 795+self.x+self.xAttackTorso, 335+self.y+self.yAttackTorso, 786+self.x+self.xAttackTorso, 337+self.y+self.yAttackTorso)
                canvas.coords(self.e3_ribThirdCross, 782+self.x+self.xAttackTorso, 339+self.y+self.yAttackTorso, 784+self.x+self.xAttackTorso, 339+self.y+self.yAttackTorso)
                canvas.coords(self.e3_ribThird, 786+self.x+self.xAttackTorso, 339+self.y+self.yAttackTorso, 795+self.x+self.xAttackTorso, 338+self.y+self.yAttackTorso, 786+self.x+self.xAttackTorso, 340+self.y+self.yAttackTorso)
                canvas.coords(self.e3_ribFourthCross, 782+self.x+self.xAttackTorso, 342+self.y+self.yAttackTorso, 784+self.x+self.xAttackTorso, 342+self.y+self.yAttackTorso)
                canvas.coords(self.e3_ribFourth, 786+self.x+self.xAttackTorso, 342+self.y+self.yAttackTorso, 795+self.x+self.xAttackTorso, 341+self.y+self.yAttackTorso, 786+self.x+self.xAttackTorso, 343+self.y+self.yAttackTorso)
                canvas.coords(self.e3_ribLowest, 782+self.x+self.xAttackTorso, 345+self.y+self.yAttackTorso, 789+self.x+self.xAttackTorso, 345+self.y+self.yAttackTorso)
                canvas.coords(self.e3_ribLowest1, 789+self.x+self.xAttackTorso, 344+self.y+self.yAttackTorso, 794+self.x+self.xAttackTorso, 344+self.y+self.yAttackTorso)
                canvas.coords(self.e3_ribLowest2, 794+self.x+self.xAttackTorso, 343+self.y+self.yAttackTorso, 796+self.x+self.xAttackTorso, 343+self.y+self.yAttackTorso)
                canvas.coords(self.e3_ribLowest3, 796+self.x+self.xAttackTorso, 342+self.y+self.yAttackTorso, 797+self.x+self.xAttackTorso, 342+self.y+self.yAttackTorso)
                canvas.coords(self.e3_torsoBlank, 782+self.x+self.xAttackTorso, 346+self.y+self.yAttackTorso, 787+self.x+self.xAttackTorso, 346+self.y+self.yAttackTorso, 787+self.x+self.xAttackTorso, 351+self.y+self.yAttackTorso, 782+self.x+self.xAttackTorso, 351+self.y+self.yAttackTorso)
                canvas.coords(self.e3_spine2VerticalLine, 787+self.x+self.xAttackTorso, 346+self.y+self.yAttackTorso, 787+self.x+self.xAttackTorso, 350+self.y+self.yAttackTorso)
                canvas.coords(self.e3_torsoBlank2, 796+self.x+self.xAttackTorso, 343+self.y+self.yAttackTorso, 798+self.x+self.xAttackTorso, 343+self.y+self.yAttackTorso, 798+self.x+self.xAttackTorso, 348+self.y+self.yAttackTorso, 796+self.x+self.xAttackTorso, 348+self.y+self.yAttackTorso)
                canvas.coords(self.e3_spine2VerticalLine1, 796+self.x+self.xAttackTorso, 342+self.y+self.yAttackTorso, 796+self.x+self.xAttackTorso, 350+self.y+self.yAttackTorso)
                canvas.coords(self.e3_sprin2DiagonalLine, 788+self.x+self.xAttackTorso, 346+self.y+self.yAttackTorso, 796+self.x+self.xAttackTorso, 348+self.y+self.yAttackTorso)
                canvas.coords(self.e3_hipLine, 782+self.x+self.xAttackTorso, 350+self.y+self.yAttackTorso, 792+self.x+self.xAttackTorso, 350+self.y+self.yAttackTorso)
                canvas.coords(self.e3_hipLine2, 792+self.x+self.xAttackTorso, 349+self.y+self.yAttackTorso, 797+self.x+self.xAttackTorso, 349+self.y+self.yAttackTorso)
                canvas.coords(self.e3_hipHole, 792+self.x+self.xAttackTorso, 352+self.y+self.yAttackTorso, 795+self.x+self.xAttackTorso, 355+self.y+self.yAttackTorso)

                if self.xAttackTorsoCounter == 40: #When self.xAttackTorsoCounter == 45, reset all variables.
                    self.xAttackTorso, self.yAttackTorso, self.xAttackTorsoCounter = 0, 0, 0
                    #print("Torso attack, done")
                    #if self.yAttackArmCounter == 55: #When self.yAttackArmCounter == 55, reset all variables.
                    self.xAttackArm, self.yAttackArm, self.yAttackArmCounter = 0, 0, 0
                    #print("Arm attack, done")
                    self.hitPlayerOnce = False
                    self.inAttackRange = False
                    #print("Attack, Done")
                    #if self.xAttackHeadCounter == 55: #When self.xAttackHeadCounter == 45, reset all variables.
                    self.xAttackHead, self.yAttackHead, self.xAttackHeadCounter = 0, 0, 0
                    #print("Head attack, Done")
            self.xAttackHeadCounter += 1
            self.yAttackArmCounter += 1
            self.xAttackTorsoCounter += 1

        elif self.Looking == "Right" and self.hpLoss < 50 and self.isDead == False and self.inAttackRange == True:
            
            canvas.coords(self.e3_hp, 740+self.x+self.xDeathHead +self.hpLoss, 297+self.y+self.yDeathHead, 840+self.x+self.xDeathHead -self.hpLoss, 302+self.y+self.yDeathHead)

            #Head AND LEGS because it only has to iterate once, just leave it here.
            if self.xAttackHeadCounter <= 40:
                if 0 <= self.xAttackHeadCounter < 10: #Head moves back; Enemy3 preps for a swing attack
                    self.xAttackHead -= 0.5*5
                    
                    
                    #canvas.coords(self.e3_Rarm, 797+self.x, 330+self.y, 812+self.x, 345+self.y)
            
                    #Legs and hitbox
                    canvas.coords(self.e3_Rleg, 797+self.x-14, 355+self.y, 812+self.x-44, 363+self.y)
                    canvas.coords(self.e3_RtoeLine, 797+self.x-14, 360+self.y, 802+self.x-24, 360+self.y)
                    canvas.coords(self.e3_RtoeLine1, 797+self.x-14, 358+self.y, 802+self.x-24, 358+self.y)
                    canvas.coords(self.e3_RtoeLine2, 797+self.x-14, 356+self.y, 802+self.x-24, 356+self.y)
                    canvas.coords(self.e3_Lleg, 767+self.x+46, 355+self.y, 782+self.x+16, 363+self.y)
                    canvas.coords(self.e3_LtoeLine, 767+self.x+46, 360+self.y, 772+self.x+36, 360+self.y)
                    canvas.coords(self.e3_LtoeLine1, 767+self.x+46, 358+self.y, 772+self.x+36, 358+self.y)
                    canvas.coords(self.e3_LtoeLine2, 767+self.x+46, 356+self.y, 772+self.x+36, 356+self.y)
                    canvas.coords(self.e3_hitbox, 802+self.x, 305+self.y, 777+self.x, 363+self.y)
                    
                    #print("First if")
                #elif 10 <= self.xAttackHeadCounter < 40: #Head is stationary
                    #pass
                    #print("Second if")
                elif 25 <= self.xAttackHeadCounter < 35: #Head jerks forward during the swing attack
                    self.xAttackHead += 1*5
                    
                    #print("Third if")
                elif 35 <= self.xAttackHeadCounter < 40: #Move head back into original position
                    self.xAttackHead -= 0.5*5
                    
                    #print("Fourth if")
                        
                #canvas.coords(self.e3_name, 790+self.x+self.xAttackHead+self.x+self.xAttackHeadAttackHead , 290+self.y+self.yAttackHead+self.y+self.yAttackHeadAttackHead)
                #canvas.coords(self.e3_hp, 740+self.x+self.xAttackHead+self.x+self.xAttackHeadAttackHead +self.hpLoss, 297+self.y+self.yAttackHead+self.y+self.yAttackHeadAttackHead, 840+self.x+self.xAttackHead+self.x+self.xAttackHeadAttackHead -self.hpLoss, 302+self.y+self.yAttackHead+self.y+self.yAttackHeadAttackHead)
                canvas.coords(self.e3_head, 777+self.x+self.xAttackHead+26, 305+self.y+self.yAttackHead, 802+self.x+self.xAttackHead-24, 330+self.y+self.yAttackHead)
                canvas.coords(self.e3_headBlank, 785+self.x+self.xAttackHead+10, 322+self.y+self.yAttackHead, 802+self.x+self.xAttackHead-24, 330+self.y+self.yAttackHead)
                canvas.coords(self.e3_headBlankLine, 785+self.x+self.xAttackHead+10, 322+self.y+self.yAttackHead, 802+self.x+self.xAttackHead-24, 322+self.y+self.yAttackHead)
                canvas.coords(self.e3_spine, 787+self.x+self.xAttackHead+6, 322+self.y+self.yAttackHead, 795+self.x+self.xAttackHead-10, 330+self.y+self.yAttackHead)
                canvas.coords(self.e3_spineLine, 787+self.x+self.xAttackHead+6, 324+self.y+self.yAttackHead, 795+self.x+self.xAttackHead-10, 328+self.y+self.yAttackHead)
                canvas.coords(self.e3_teeth, 777+self.x+self.xAttackHead+26, 322+self.y+self.yAttackHead, 785+self.x+self.xAttackHead+10, 330+self.y+self.yAttackHead)
                canvas.coords(self.e3_teethDown1, 780+self.x+self.xAttackHead+20, 322+self.y+self.yAttackHead, 780+self.x+self.xAttackHead+20, 330+self.y+self.yAttackHead)
                canvas.coords(self.e3_teethDown2, 783+self.x+self.xAttackHead+14, 322+self.y+self.yAttackHead, 783+self.x+self.xAttackHead+14, 330+self.y+self.yAttackHead)
                canvas.coords(self.e3_teethCross, 777+self.x+self.xAttackHead+26, 326+self.y+self.yAttackHead, 785+self.x+self.xAttackHead+10, 326+self.y+self.yAttackHead)
                canvas.coords(self.e3_nose, 778+self.x+self.xAttackHead+24, 318+self.y+self.yAttackHead, 779+self.x+self.xAttackHead+22, 319+self.y+self.yAttackHead)
                canvas.coords(self.e3_eye, 780+self.x+self.xAttackHead+20, 312+self.y+self.yAttackHead, 785+self.x+self.xAttackHead+10, 319+self.y+self.yAttackHead)
                canvas.coords(self.e3_eye2, 788+self.x+self.xAttackHead+4, 314+self.y+self.yAttackHead, 789+self.x+self.xAttackHead+2, 319+self.y+self.yAttackHead)
            
            if self.yAttackArmCounter <= 40: #NOTICE THAT IT COUNTS THE Y
                if 0 <= self.yAttackArmCounter < 10: #Arms move behind ribcage.
                    #if 0 <= self.xAttackArmCounter < 5:
                    self.xAttackArm -= 2*5
                    
                    #print("First if")
                #elif 10 <= self.yAttackArmCounter < 40: #Arms pause getting ready for attack.
                    #pass
                    #print("Second if")
                elif 25 <= self.yAttackArmCounter < 35: #Arms move forward in a shoving motion.
                    #if 5 <= self.yAttackArmCounter < 10:
                    self.xAttackArm += 5*5
                    self.hitboxLarm = canvas.coords(self.e3_Larm)
                    if self.hitPlayerOnce  == False and ( self.player.hitbox[1] <= self.hitboxLarm[1] <= self.player.hitbox[3] or self.player.hitbox[1] <= self.hitboxLarm[3] <= self.player.hitbox[3] ) and (self.player.hitbox[0] <= self.hitboxLarm[0] <= self.player.hitbox[2] or self.player.hitbox[2] <= self.hitboxLarm[2] <= self.player.hitbox[0]) and enemy3Damage == False: 
                        enemy3Damage = True
                        self.hitPlayerOnce = True
                        print("Gatekeeper of the 592th Hell, Diesect: HA! HA! HA! ONE LESS TO WORRY ABOUT! HA! HA! HA!")
                    
                    #print("Third if")
                elif 35 <= self.yAttackArmCounter < 40: #Move arms back into original position
                    #if 10 <= self.yAttackArmCounter < 15:
                    self.xAttackArm -= 2*5
                    
                    #print("Fourth if")

                #Arms
                canvas.coords(self.e3_Larm, 767+self.x+15+self.xAttackArm, 330+self.y+self.yAttackArm-7, 782+self.x+15+self.xAttackArm, 345+self.y+self.yAttackArm-7)
                canvas.coords(self.e3_Lfinger, 768+self.x+15+self.xAttackArm, 333+self.y+self.yAttackArm-7, 775+self.x+15+self.xAttackArm, 333+self.y+self.yAttackArm-7)
                canvas.coords(self.e3_Lfinger2, 767+self.x+15+self.xAttackArm, 336+self.y+self.yAttackArm-7, 776+self.x+15+self.xAttackArm, 336+self.y+self.yAttackArm-7)
                canvas.coords(self.e3_Lfinger3, 767+self.x+15+self.xAttackArm, 339+self.y+self.yAttackArm-7, 776+self.x+15+self.xAttackArm, 339+self.y+self.yAttackArm-7)
                canvas.coords(self.e3_Lfinger4, 768+self.x+15+self.xAttackArm, 342+self.y+self.yAttackArm-7, 774+self.x+15+self.xAttackArm, 342+self.y+self.yAttackArm-7)
                canvas.coords(self.e3_LfingerDown, 775+self.x+15+self.xAttackArm, 333+self.y+self.yAttackArm-7, 775+self.x+15+self.xAttackArm, 339+self.y+self.yAttackArm-7)
                canvas.coords(self.e3_LfingerDown1, 774+self.x+15+self.xAttackArm, 339+self.y+self.yAttackArm-7, 774+self.x+15+self.xAttackArm, 342+self.y+self.yAttackArm-7)
                canvas.coords(self.e3_Rarm, 767+self.x+15+self.xAttackArm, 330+self.y+self.yAttackArm-5, 782+self.x+15+self.xAttackArm, 345+self.y+self.yAttackArm-5)

            if self.xAttackTorsoCounter <= 40:
                if 0 <= self.xAttackTorsoCounter < 10: #Torso moves back BUT less than it's head.
                    #if 0 <= self.xAttackTorsoCounter < 5:
                    self.xAttackTorso -= 0.25*5
                    
                    #print("First if")
                #elif 10 <= self.xAttackTorsoCounter < 40: #Torso is stationary
                    #pass
                    #print("Second if")
                elif 25 <= self.xAttackTorsoCounter < 35: #Torso jerks forward during the swing attack
                    #if 5 <= self.xAttackTorsoCounter < 10:
                    self.xAttackTorso += 0.5*5
                    
                    #print("Third if")
                elif 35 <= self.xAttackTorsoCounter < 40: #Move torso back into original position
                    #if 10 <= self.xAttackTorsoCounter < 15:
                    self.xAttackTorso -= 0.25*5
                    
                    #print("Fourth if")

                canvas.coords(self.e3_torso, 782+self.x+self.xAttackTorso+16, 330+self.y+self.yAttackTorso, 797+self.x+self.xAttackTorso-14, 330+self.y+self.yAttackTorso, 797+self.x+self.xAttackTorso-14, 355+self.y+self.yAttackTorso, 782+self.x+self.xAttackTorso+16, 355+self.y+self.yAttackTorso)
                canvas.coords(self.e3_ribMidDown, 784+self.x+self.xAttackTorso+12, 330+self.y+self.yAttackTorso, 784+self.x+self.xAttackTorso+12, 345+self.y+self.yAttackTorso)
                canvas.coords(self.e3_ribHighestCross, 782+self.x+self.xAttackTorso+16, 333+self.y+self.yAttackTorso, 784+self.x+self.xAttackTorso+12, 333+self.y+self.yAttackTorso)
                canvas.coords(self.e3_ribHighest, 786+self.x+self.xAttackTorso+8, 333+self.y+self.yAttackTorso, 795+self.x+self.xAttackTorso-10, 332+self.y+self.yAttackTorso, 786+self.x+self.xAttackTorso+8, 334+self.y+self.yAttackTorso)
                canvas.coords(self.e3_ribMiddleCross, 782+self.x+self.xAttackTorso+16, 336+self.y+self.yAttackTorso, 784+self.x+self.xAttackTorso+12, 336+self.y+self.yAttackTorso)
                canvas.coords(self.e3_ribMiddle, 786+self.x+self.xAttackTorso+8, 336+self.y+self.yAttackTorso, 795+self.x+self.xAttackTorso-10, 335+self.y+self.yAttackTorso, 786+self.x+self.xAttackTorso+8, 337+self.y+self.yAttackTorso)
                canvas.coords(self.e3_ribThirdCross, 782+self.x+self.xAttackTorso+16, 339+self.y+self.yAttackTorso, 784+self.x+self.xAttackTorso+12, 339+self.y+self.yAttackTorso)
                canvas.coords(self.e3_ribThird, 786+self.x+self.xAttackTorso+8, 339+self.y+self.yAttackTorso, 795+self.x+self.xAttackTorso-10, 338+self.y+self.yAttackTorso, 786+self.x+self.xAttackTorso+8, 340+self.y+self.yAttackTorso)
                canvas.coords(self.e3_ribFourthCross, 782+self.x+self.xAttackTorso+16, 342+self.y+self.yAttackTorso, 784+self.x+self.xAttackTorso+12, 342+self.y+self.yAttackTorso)
                canvas.coords(self.e3_ribFourth, 786+self.x+self.xAttackTorso+8, 342+self.y+self.yAttackTorso, 795+self.x+self.xAttackTorso-10, 341+self.y+self.yAttackTorso, 786+self.x+self.xAttackTorso+8, 343+self.y+self.yAttackTorso)
                canvas.coords(self.e3_ribLowest, 782+self.x+self.xAttackTorso+16, 345+self.y+self.yAttackTorso, 789+self.x+self.xAttackTorso+2, 345+self.y+self.yAttackTorso)
                canvas.coords(self.e3_ribLowest1, 789+self.x+self.xAttackTorso+2, 344+self.y+self.yAttackTorso, 794+self.x+self.xAttackTorso-8, 344+self.y+self.yAttackTorso)
                canvas.coords(self.e3_ribLowest2, 794+self.x+self.xAttackTorso-8, 343+self.y+self.yAttackTorso, 796+self.x+self.xAttackTorso-12, 343+self.y+self.yAttackTorso)
                canvas.coords(self.e3_ribLowest3, 796+self.x+self.xAttackTorso-12, 342+self.y+self.yAttackTorso, 797+self.x+self.xAttackTorso-14, 342+self.y+self.yAttackTorso)
                canvas.coords(self.e3_torsoBlank, 782+self.x+self.xAttackTorso+16+1, 346+self.y+self.yAttackTorso, 787+self.x+self.xAttackTorso+6, 346+self.y+self.yAttackTorso, 787+self.x+self.xAttackTorso+6, 351+self.y+self.yAttackTorso, 782+self.x+self.xAttackTorso+16+1, 351+self.y+self.yAttackTorso)
                canvas.coords(self.e3_spine2VerticalLine, 787+self.x+self.xAttackTorso+6, 346+self.y+self.yAttackTorso, 787+self.x+self.xAttackTorso+6, 350+self.y+self.yAttackTorso)
                canvas.coords(self.e3_torsoBlank2, 796+self.x+self.xAttackTorso-12, 343+self.y+self.yAttackTorso, 798+self.x+self.xAttackTorso-16, 343+self.y+self.yAttackTorso, 798+self.x+self.xAttackTorso-16, 348+self.y+self.yAttackTorso, 796+self.x+self.xAttackTorso-12, 348+self.y+self.yAttackTorso)
                canvas.coords(self.e3_spine2VerticalLine1, 796+self.x+self.xAttackTorso-12, 342+self.y+self.yAttackTorso, 796+self.x+self.xAttackTorso-12, 350+self.y+self.yAttackTorso)
                canvas.coords(self.e3_sprin2DiagonalLine, 788+self.x+self.xAttackTorso+4, 346+self.y+self.yAttackTorso, 796+self.x+self.xAttackTorso-12, 348+self.y+self.yAttackTorso)
                canvas.coords(self.e3_hipLine, 782+self.x+self.xAttackTorso+16, 350+self.y+self.yAttackTorso, 792+self.x+self.xAttackTorso-4, 350+self.y+self.yAttackTorso)
                canvas.coords(self.e3_hipLine2, 792+self.x+self.xAttackTorso-4, 349+self.y+self.yAttackTorso, 797+self.x+self.xAttackTorso-14, 349+self.y+self.yAttackTorso)
                canvas.coords(self.e3_hipHole, 792+self.x+self.xAttackTorso-4, 352+self.y+self.yAttackTorso, 795+self.x+self.xAttackTorso-10, 355+self.y+self.yAttackTorso)

                if self.xAttackTorsoCounter == 40: #When self.xAttackTorsoCounter == 45, reset all variables.
                    self.xAttackTorso, self.yAttackTorso, self.xAttackTorsoCounter = 0, 0, 0
                    #print("Torso attack, done")
                    #if self.yAttackArmCounter == 55: #When self.yAttackArmCounter == 55, reset all variables.
                    self.xAttackArm, self.yAttackArm, self.yAttackArmCounter = 0, 0, 0
                    #print("Arm attack, done")
                    self.hitPlayerOnce = False
                    self.inAttackRange = False
                    #print("Attack, Done")
                    #if self.xAttackHeadCounter == 55: #When self.xAttackHeadCounter == 45, reset all variables.
                    self.xAttackHead, self.yAttackHead, self.xAttackHeadCounter = 0, 0, 0
                    #print("Head attack, Done")
            self.xAttackHeadCounter += 1
            self.yAttackArmCounter += 1
            self.xAttackTorsoCounter += 1                    
        
        elif self.deleteOnce == True: #and self.inAttackRange == False:
            #print("Death aniamtion")
            canvas.delete(self.e3_hp)
            canvas.delete(self.e3_name)
            self.deleteOnce = False
        elif self.deleteOnce == False and self.Looking == "Left" and self.deathAnimation == True: 
            #print("self.deleteOnce == False and self.Looking == Left")
            #Move head x: 100 y: +10 then -363 is the floor coordinates. So y:-373
            if self.yDeathHead <= 31:
                #if self.xDeathHead <= 100: #Always reaches 31 because of above if statement
                self.xDeathHead -= 4
                if self.yDeathHeadInAir == True:
                    self.yDeathHead += 2
                    if self.yDeathHead == -10:
                        self.yDeathHeadInAir = False
                elif self.yDeathHeadInAir == False:
                    self.yDeathHead += 2
                    
                canvas.coords(self.e3_name, 790+self.x+self.xDeathHead , 290+self.y+self.yDeathHead)
                canvas.coords(self.e3_hp, 740+self.x+self.xDeathHead +self.hpLoss, 297+self.y+self.yDeathHead, 840+self.x+self.xDeathHead -self.hpLoss, 302+self.y+self.yDeathHead)
                canvas.coords(self.e3_head, 777+self.x+self.xDeathHead , 305+self.y+self.yDeathHead, 802+self.x+self.xDeathHead , 330+self.y+self.yDeathHead )
                canvas.coords(self.e3_headBlank, 785+self.x+self.xDeathHead , 322+self.y+self.yDeathHead , 802+self.x+self.xDeathHead , 330+self.y+self.yDeathHead )
                canvas.coords(self.e3_headBlankLine, 785+self.x+self.xDeathHead , 322+self.y+self.yDeathHead , 802+self.x+self.xDeathHead , 322+self.y+self.yDeathHead )
                canvas.coords(self.e3_spine, 787+self.x+self.xDeathHead , 322+self.y+self.yDeathHead , 795+self.x+self.xDeathHead , 330+self.y+self.yDeathHead )
                canvas.coords(self.e3_spineLine, 787+self.x+self.xDeathHead , 324+self.y+self.yDeathHead , 795+self.x+self.xDeathHead , 328+self.y+self.yDeathHead )
                canvas.coords(self.e3_teeth, 777+self.x+self.xDeathHead , 322+self.y+self.yDeathHead , 785+self.x+self.xDeathHead , 330+self.y+self.yDeathHead )
                canvas.coords(self.e3_teethDown1, 780+self.x+self.xDeathHead , 322+self.y+self.yDeathHead , 780+self.x+self.xDeathHead , 330+self.y+self.yDeathHead )
                canvas.coords(self.e3_teethDown2, 783+self.x+self.xDeathHead , 322+self.y+self.yDeathHead , 783+self.x+self.xDeathHead , 330+self.y+self.yDeathHead )
                canvas.coords(self.e3_teethCross, 777+self.x+self.xDeathHead , 326+self.y+self.yDeathHead , 785+self.x+self.xDeathHead , 326+self.y+self.yDeathHead )
                canvas.coords(self.e3_nose, 778+self.x+self.xDeathHead , 318+self.y+self.yDeathHead , 779+self.x+self.xDeathHead , 319+self.y+self.yDeathHead )
                canvas.coords(self.e3_eye, 780+self.x+self.xDeathHead , 312+self.y+self.yDeathHead , 785+self.x+self.xDeathHead , 319+self.y+self.yDeathHead )
                canvas.coords(self.e3_eye2, 788+self.x+self.xDeathHead , 314+self.y+self.yDeathHead , 789+self.x+self.xDeathHead , 319+self.y+self.yDeathHead )

                if self.yDeathHead == 32:
                    self.deathAnimation = False

            #Move torso to the left/opposite from where the head is falling.
            if self.yDeathRibCage <= 8:
                #if self.xDeathRibCage <= 100: #Always reaches 31 because of above if statement
                self.xDeathRibCage += 1.5
                self.yDeathRibCage += 1
                
                canvas.coords(self.e3_torso, 782+self.x+self.xDeathRibCage, 330+self.y+self.yDeathRibCage, 797+self.x+self.xDeathRibCage, 330+self.y+self.yDeathRibCage, 797+self.x+self.xDeathRibCage, 355+self.y+self.yDeathRibCage, 782+self.x+self.xDeathRibCage, 355+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_ribMidDown, 784+self.x+self.xDeathRibCage, 330+self.y+self.yDeathRibCage, 784+self.x+self.xDeathRibCage, 345+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_ribHighestCross, 782+self.x+self.xDeathRibCage, 333+self.y+self.yDeathRibCage, 784+self.x+self.xDeathRibCage, 333+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_ribHighest, 786+self.x+self.xDeathRibCage, 333+self.y+self.yDeathRibCage, 795+self.x+self.xDeathRibCage, 332+self.y+self.yDeathRibCage, 786+self.x+self.xDeathRibCage, 334+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_ribMiddleCross, 782+self.x+self.xDeathRibCage, 336+self.y+self.yDeathRibCage, 784+self.x+self.xDeathRibCage, 336+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_ribMiddle, 786+self.x+self.xDeathRibCage, 336+self.y+self.yDeathRibCage, 795+self.x+self.xDeathRibCage, 335+self.y+self.yDeathRibCage, 786+self.x+self.xDeathRibCage, 337+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_ribThirdCross, 782+self.x+self.xDeathRibCage, 339+self.y+self.yDeathRibCage, 784+self.x+self.xDeathRibCage, 339+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_ribThird, 786+self.x+self.xDeathRibCage, 339+self.y+self.yDeathRibCage, 795+self.x+self.xDeathRibCage, 338+self.y+self.yDeathRibCage, 786+self.x+self.xDeathRibCage, 340+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_ribFourthCross, 782+self.x+self.xDeathRibCage, 342+self.y+self.yDeathRibCage, 784+self.x+self.xDeathRibCage, 342+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_ribFourth, 786+self.x+self.xDeathRibCage, 342+self.y+self.yDeathRibCage, 795+self.x+self.xDeathRibCage, 341+self.y+self.yDeathRibCage, 786+self.x+self.xDeathRibCage, 343+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_ribLowest, 782+self.x+self.xDeathRibCage, 345+self.y+self.yDeathRibCage, 789+self.x+self.xDeathRibCage, 345+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_ribLowest1, 789+self.x+self.xDeathRibCage, 344+self.y+self.yDeathRibCage, 794+self.x+self.xDeathRibCage, 344+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_ribLowest2, 794+self.x+self.xDeathRibCage, 343+self.y+self.yDeathRibCage, 796+self.x+self.xDeathRibCage, 343+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_ribLowest3, 796+self.x+self.xDeathRibCage, 342+self.y+self.yDeathRibCage, 797+self.x+self.xDeathRibCage, 342+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_torsoBlank, 782+self.x+self.xDeathRibCage, 346+self.y+self.yDeathRibCage, 787+self.x+self.xDeathRibCage, 346+self.y+self.yDeathRibCage, 787+self.x+self.xDeathRibCage, 351+self.y+self.yDeathRibCage, 782+self.x+self.xDeathRibCage, 351+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_spine2VerticalLine, 787+self.x+self.xDeathRibCage, 346+self.y+self.yDeathRibCage, 787+self.x+self.xDeathRibCage, 350+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_torsoBlank2, 796+self.x+self.xDeathRibCage, 343+self.y+self.yDeathRibCage, 798+self.x+self.xDeathRibCage, 343+self.y+self.yDeathRibCage, 798+self.x+self.xDeathRibCage, 348+self.y+self.yDeathRibCage, 796+self.x+self.xDeathRibCage, 348+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_spine2VerticalLine1, 796+self.x+self.xDeathRibCage, 342+self.y+self.yDeathRibCage, 796+self.x+self.xDeathRibCage, 350+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_sprin2DiagonalLine, 788+self.x+self.xDeathRibCage, 346+self.y+self.yDeathRibCage, 796+self.x+self.xDeathRibCage, 348+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_hipLine, 782+self.x+self.xDeathRibCage, 350+self.y+self.yDeathRibCage, 792+self.x+self.xDeathRibCage, 350+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_hipLine2, 792+self.x+self.xDeathRibCage, 349+self.y+self.yDeathRibCage, 797+self.x+self.xDeathRibCage, 349+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_hipHole, 792+self.x+self.xDeathRibCage, 352+self.y+self.yDeathRibCage, 795+self.x+self.xDeathRibCage, 355+self.y+self.yDeathRibCage)

            #Left hand death animation
            if self.yDeathLHand <= 20:
                #if self.xDeathLHand <= 100: #Always reaches 31 because of above if statement
                self.xDeathLHand -= 1
                self.yDeathLHand += 1
                canvas.coords(self.e3_Larm, 767+self.x+self.xDeathLHand, 330+self.y+self.yDeathLHand, 782+self.x+self.xDeathLHand, 345+self.y+self.yDeathLHand)
                canvas.coords(self.e3_Lfinger, 768+self.x+self.xDeathLHand, 333+self.y+self.yDeathLHand, 775+self.x+self.xDeathLHand, 333+self.y+self.yDeathLHand)
                canvas.coords(self.e3_Lfinger2, 767+self.x+self.xDeathLHand, 336+self.y+self.yDeathLHand, 776+self.x+self.xDeathLHand, 336+self.y+self.yDeathLHand)
                canvas.coords(self.e3_Lfinger3, 767+self.x+self.xDeathLHand, 339+self.y+self.yDeathLHand, 776+self.x+self.xDeathLHand, 339+self.y+self.yDeathLHand)
                canvas.coords(self.e3_Lfinger4, 768+self.x+self.xDeathLHand, 342+self.y+self.yDeathLHand, 774+self.x+self.xDeathLHand, 342+self.y+self.yDeathLHand)
                canvas.coords(self.e3_LfingerDown, 775+self.x+self.xDeathLHand, 333+self.y+self.yDeathLHand, 775+self.x+self.xDeathLHand, 339+self.y+self.yDeathLHand)
                canvas.coords(self.e3_LfingerDown1, 774+self.x+self.xDeathLHand, 339+self.y+self.yDeathLHand, 774+self.x+self.xDeathLHand, 342+self.y+self.yDeathLHand)
                
            #Right hand death animation
            if self.yDeathRHand <= 20:
                #if self.xDeathRHand <= 100: #Always reaches 31 because of above if statement
                self.xDeathRHand += 0.5
                self.yDeathRHand += 1
                canvas.coords(self.e3_Rarm, 797+self.x+self.xDeathRHand, 330+self.y+self.yDeathRHand, 812+self.x+self.xDeathRHand, 345+self.y+self.yDeathRHand)
            
        elif self.deleteOnce == False and self.Looking == "Right" and self.deathAnimation == True:
            #print("self.deleteOnce == False and self.Looking == Right")
            #Move head x: 100 y: +10 then -363 is the floor coordinates. So y:-373
            if self.yDeathHead <= 31:
                #if self.xDeathHead >= -100: #Always reaches -31 because of above if statement
                self.xDeathHead += 2
                if self.yDeathHeadInAir == True:
                    self.yDeathHead -= 2
                    if self.yDeathHead == -10:
                        self.yDeathHeadInAir = False
                elif self.yDeathHeadInAir == False:
                    self.yDeathHead += 2

                canvas.coords(self.e3_name, 790+self.x+self.xDeathHead , 290+self.y+self.yDeathHead )
                canvas.coords(self.e3_hp, 740+self.x+self.xDeathHead +self.hpLoss, 297+self.y+self.yDeathHead , 840+self.x+self.xDeathHead -self.hpLoss, 302+self.y+self.yDeathHead )
                canvas.coords(self.e3_head, 777+self.x+self.xDeathHead +26, 305+self.y+self.yDeathHead , 802+self.x+self.xDeathHead -24, 330+self.y+self.yDeathHead )
                canvas.coords(self.e3_headBlank, 785+self.x+self.xDeathHead +10, 322+self.y+self.yDeathHead , 802+self.x+self.xDeathHead -24, 330+self.y+self.yDeathHead )
                canvas.coords(self.e3_headBlankLine, 785+self.x+self.xDeathHead +10, 322+self.y+self.yDeathHead , 802+self.x+self.xDeathHead -24, 322+self.y+self.yDeathHead )
                canvas.coords(self.e3_spine, 787+self.x+self.xDeathHead +6, 322+self.y+self.yDeathHead , 795+self.x+self.xDeathHead -10, 330+self.y+self.yDeathHead )
                canvas.coords(self.e3_spineLine, 787+self.x+self.xDeathHead +6, 324+self.y+self.yDeathHead , 795+self.x+self.xDeathHead -10, 328+self.y+self.yDeathHead )
                canvas.coords(self.e3_teeth, 777+self.x+self.xDeathHead +26, 322+self.y+self.yDeathHead , 785+self.x+self.xDeathHead +10, 330+self.y+self.yDeathHead )
                canvas.coords(self.e3_teethDown1, 780+self.x+self.xDeathHead +20, 322+self.y+self.yDeathHead , 780+self.x+self.xDeathHead +20, 330+self.y+self.yDeathHead )
                canvas.coords(self.e3_teethDown2, 783+self.x+self.xDeathHead +14, 322+self.y+self.yDeathHead , 783+self.x+self.xDeathHead +14, 330+self.y+self.yDeathHead )
                canvas.coords(self.e3_teethCross, 777+self.x+self.xDeathHead +26, 326+self.y+self.yDeathHead , 785+self.x+self.xDeathHead +10, 326+self.y+self.yDeathHead )
                canvas.coords(self.e3_nose, 778+self.x+self.xDeathHead +24, 318+self.y+self.yDeathHead , 779+self.x+self.xDeathHead +22, 319+self.y+self.yDeathHead )
                canvas.coords(self.e3_eye, 780+self.x+self.xDeathHead +20, 312+self.y+self.yDeathHead , 785+self.x+self.xDeathHead +10, 319+self.y+self.yDeathHead )
                canvas.coords(self.e3_eye2, 788+self.x+self.xDeathHead +4, 314+self.y+self.yDeathHead , 789+self.x+self.xDeathHead +2, 319+self.y+self.yDeathHead )

                if self.yDeathHead == 32:
                    self.deathAnimation = False

            #Move torso to the left/opposite from where the head is falling.
            if self.yDeathRibCage <= 8:
                #if self.xDeathRibCage <= 100: #Always reaches 31 because of above if statement
                self.xDeathRibCage -= 1.5
                self.yDeathRibCage += 1

                canvas.coords(self.e3_torso, 782+self.x+self.xDeathRibCage+16, 330+self.y+self.yDeathRibCage, 797+self.x+self.xDeathRibCage-14, 330+self.y+self.yDeathRibCage, 797+self.x+self.xDeathRibCage-14, 355+self.y+self.yDeathRibCage, 782+self.x+self.xDeathRibCage+16, 355+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_ribMidDown, 784+self.x+self.xDeathRibCage+12, 330+self.y+self.yDeathRibCage, 784+self.x+self.xDeathRibCage+12, 345+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_ribHighestCross, 782+self.x+self.xDeathRibCage+16, 333+self.y+self.yDeathRibCage, 784+self.x+self.xDeathRibCage+12, 333+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_ribHighest, 786+self.x+self.xDeathRibCage+8, 333+self.y+self.yDeathRibCage, 795+self.x+self.xDeathRibCage-10, 332+self.y+self.yDeathRibCage, 786+self.x+self.xDeathRibCage+8, 334+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_ribMiddleCross, 782+self.x+self.xDeathRibCage+16, 336+self.y+self.yDeathRibCage, 784+self.x+self.xDeathRibCage+12, 336+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_ribMiddle, 786+self.x+self.xDeathRibCage+8, 336+self.y+self.yDeathRibCage, 795+self.x+self.xDeathRibCage-10, 335+self.y+self.yDeathRibCage, 786+self.x+self.xDeathRibCage+8, 337+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_ribThirdCross, 782+self.x+self.xDeathRibCage+16, 339+self.y+self.yDeathRibCage, 784+self.x+self.xDeathRibCage+12, 339+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_ribThird, 786+self.x+self.xDeathRibCage+8, 339+self.y+self.yDeathRibCage, 795+self.x+self.xDeathRibCage-10, 338+self.y+self.yDeathRibCage, 786+self.x+self.xDeathRibCage+8, 340+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_ribFourthCross, 782+self.x+self.xDeathRibCage+16, 342+self.y+self.yDeathRibCage, 784+self.x+self.xDeathRibCage+12, 342+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_ribFourth, 786+self.x+self.xDeathRibCage+8, 342+self.y+self.yDeathRibCage, 795+self.x+self.xDeathRibCage-10, 341+self.y+self.yDeathRibCage, 786+self.x+self.xDeathRibCage+8, 343+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_ribLowest, 782+self.x+self.xDeathRibCage+16, 345+self.y+self.yDeathRibCage, 789+self.x+self.xDeathRibCage+2, 345+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_ribLowest1, 789+self.x+self.xDeathRibCage+2, 344+self.y+self.yDeathRibCage, 794+self.x+self.xDeathRibCage-8, 344+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_ribLowest2, 794+self.x+self.xDeathRibCage-8, 343+self.y+self.yDeathRibCage, 796+self.x+self.xDeathRibCage-12, 343+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_ribLowest3, 796+self.x+self.xDeathRibCage-12, 342+self.y+self.yDeathRibCage, 797+self.x+self.xDeathRibCage-14, 342+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_torsoBlank, 782+self.x+self.xDeathRibCage+16+1, 346+self.y+self.yDeathRibCage, 787+self.x+self.xDeathRibCage+6, 346+self.y+self.yDeathRibCage, 787+self.x+self.xDeathRibCage+6, 351+self.y+self.yDeathRibCage, 782+self.x+self.xDeathRibCage+16+1, 351+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_spine2VerticalLine, 787+self.x+self.xDeathRibCage+6, 346+self.y+self.yDeathRibCage, 787+self.x+self.xDeathRibCage+6, 350+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_torsoBlank2, 796+self.x+self.xDeathRibCage-12, 343+self.y+self.yDeathRibCage, 798+self.x+self.xDeathRibCage-16, 343+self.y+self.yDeathRibCage, 798+self.x+self.xDeathRibCage-16, 348+self.y+self.yDeathRibCage, 796+self.x+self.xDeathRibCage-12, 348+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_spine2VerticalLine1, 796+self.x+self.xDeathRibCage-12, 342+self.y+self.yDeathRibCage, 796+self.x+self.xDeathRibCage-12, 350+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_sprin2DiagonalLine, 788+self.x+self.xDeathRibCage+4, 346+self.y+self.yDeathRibCage, 796+self.x+self.xDeathRibCage-12, 348+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_hipLine, 782+self.x+self.xDeathRibCage+16, 350+self.y+self.yDeathRibCage, 792+self.x+self.xDeathRibCage-4, 350+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_hipLine2, 792+self.x+self.xDeathRibCage-4, 349+self.y+self.yDeathRibCage, 797+self.x+self.xDeathRibCage-14, 349+self.y+self.yDeathRibCage)
                canvas.coords(self.e3_hipHole, 792+self.x+self.xDeathRibCage-4, 352+self.y+self.yDeathRibCage, 795+self.x+self.xDeathRibCage-10, 355+self.y+self.yDeathRibCage)

            #Left hand death animation
            if self.yDeathLHand <= 20:
                #if self.xDeathLHand <= 100: #Always reaches 31 because of above if statement
                self.xDeathLHand -= 1
                self.yDeathLHand += 1
                
                canvas.coords(self.e3_Larm, 767+self.x+self.xDeathLHand, 330+self.y+self.yDeathLHand, 782+self.x+self.xDeathLHand, 345+self.y+self.yDeathLHand)
                canvas.coords(self.e3_Lfinger, 768+self.x+self.xDeathLHand, 333+self.y+self.yDeathLHand, 775+self.x+self.xDeathLHand, 333+self.y+self.yDeathLHand)
                canvas.coords(self.e3_Lfinger2, 767+self.x+self.xDeathLHand, 336+self.y+self.yDeathLHand, 776+self.x+self.xDeathLHand, 336+self.y+self.yDeathLHand)
                canvas.coords(self.e3_Lfinger3, 767+self.x+self.xDeathLHand, 339+self.y+self.yDeathLHand, 776+self.x+self.xDeathLHand, 339+self.y+self.yDeathLHand)
                canvas.coords(self.e3_Lfinger4, 768+self.x+self.xDeathLHand, 342+self.y+self.yDeathLHand, 774+self.x+self.xDeathLHand, 342+self.y+self.yDeathLHand)
                canvas.coords(self.e3_LfingerDown, 775+self.x+self.xDeathLHand, 333+self.y+self.yDeathLHand, 775+self.x+self.xDeathLHand, 339+self.y+self.yDeathLHand)
                canvas.coords(self.e3_LfingerDown1, 774+self.x+self.xDeathLHand, 339+self.y+self.yDeathLHand, 774+self.x+self.xDeathLHand, 342+self.y+self.yDeathLHand)
                #canvas.coords(self.e3_Rarm, 797+self.x+self.xDeathLHand, 330+self.y+self.yDeathLHand, 812+self.x+self.xDeathLHand, 345+self.y+self.yDeathLHand)

            #Right hand death animation
            if self.yDeathRHand <= 20:
                #if self.xDeathRHand <= 100: #Always reaches 31 because of above if statement
                self.xDeathRHand += 0.5
                self.yDeathRHand += 1
                canvas.coords(self.e3_Rarm, 797+self.x+self.xDeathRHand, 330+self.y+self.yDeathRHand, 812+self.x+self.xDeathRHand, 345+self.y+self.yDeathRHand)

        elif self.deathAnimation == False and self.deleteEnemy3Complete == True:
            self.deleteEnemy3Counter += 1
            if self.deleteEnemy3Counter == 200:
                #print("Deleting head and torso")
                canvas.delete(self.e3_head)
                canvas.delete(self.e3_headBlank)
                canvas.delete(self.e3_headBlankLine)
                canvas.delete(self.e3_spine)
                canvas.delete(self.e3_spineLine)
                canvas.delete(self.e3_teeth)
                canvas.delete(self.e3_teethDown1)
                canvas.delete(self.e3_teethDown2)
                canvas.delete(self.e3_teethCross)
                canvas.delete(self.e3_nose)
                canvas.delete(self.e3_eye)
                canvas.delete(self.e3_eye2)
                #Deleting torso now.
                canvas.delete(self.e3_torso)
                canvas.delete(self.e3_ribMidDown)
                canvas.delete(self.e3_ribHighestCross)
                canvas.delete(self.e3_ribHighest)
                canvas.delete(self.e3_ribMiddleCross)
                canvas.delete(self.e3_ribMiddle)
                canvas.delete(self.e3_ribThirdCross)
                canvas.delete(self.e3_ribThird)
                canvas.delete(self.e3_ribFourthCross)
                canvas.delete(self.e3_ribFourth)
                canvas.delete(self.e3_ribLowest)
                canvas.delete(self.e3_ribLowest1)
                canvas.delete(self.e3_ribLowest2)
                canvas.delete(self.e3_ribLowest3)
                canvas.delete(self.e3_torsoBlank)
                canvas.delete(self.e3_spine2VerticalLine)
                canvas.delete(self.e3_torsoBlank2)
                canvas.delete(self.e3_spine2VerticalLine1)
                canvas.delete(self.e3_sprin2DiagonalLine)
                canvas.delete(self.e3_hipLine)
                canvas.delete(self.e3_hipLine2)
                canvas.delete(self.e3_hipHole)

            elif self.deleteEnemy3Counter == 225:
                #print("Deleting hands")
                canvas.delete(self.e3_Rarm)
                canvas.delete(self.e3_Larm)
                canvas.delete(self.e3_Lfinger)
                canvas.delete(self.e3_Lfinger2)
                canvas.delete(self.e3_Lfinger3)
                canvas.delete(self.e3_Lfinger4)
                canvas.delete(self.e3_LfingerDown)
                canvas.delete(self.e3_LfingerDown1)
            
            elif self.deleteEnemy3Counter == 250:
                #print("Deleting feet")
                canvas.delete(self.e3_Rleg)
                canvas.delete(self.e3_RtoeLine)
                canvas.delete(self.e3_RtoeLine1)
                canvas.delete(self.e3_RtoeLine2)
                canvas.delete(self.e3_Lleg)
                canvas.delete(self.e3_LtoeLine)
                canvas.delete(self.e3_LtoeLine1)
                canvas.delete(self.e3_LtoeLine2)
                #Deleting hitbox
                #canvas.delete(self.e3_hitbox) #Cannot delete hitbox because error will occur since there is no hitbox coordinates below.
                self.deleteEnemy3Complete = False
        else:
            global turnOffEnemy3
            global gameOver
            print("Neurotic: Perhaps I was wrong about you.")
            print("You win.")
            gameOver = True
            turnOffEnemy3 = True
            #print("Stopping Enemy3's draw method")
    
        if self.hpLoss == 50 and self.isDead == False:
            print("Enemy3 has died")
            self.isDead = True

        global hitBySpecialOnce
        if self.isDead == False and self.hpLoss < 50 and self.hitboxCoords[2] <= self.voice.hitbox[4] <= self.hitboxCoords[0] and (self.hitboxCoords[1] <= self.voice.hitbox[1] <= self.hitboxCoords[3] or self.hitboxCoords[1] <= self.voice.hitbox[9] <= self.hitboxCoords[3]) and hitBySpecialOnce == True:
            self.hpLoss += 5
            hitBySpecialOnce = False
            #print(hitBySpecialOnce)
            print("Voice: 1. Hit Enemy3. Did 5 damage.")
        elif self.isDead == False and self.hpLoss < 50 and self.hitboxCoords[2] <= self.voice.hitbox[10] <= self.hitboxCoords[0] and (self.hitboxCoords[1] <= self.voice.hitbox[1] <= self.hitboxCoords[3] or self.hitboxCoords[1] <= self.voice.hitbox[9] <= self.hitboxCoords[3]) and hitBySpecialOnce == True:
            self.hpLoss += 5
            hitBySpecialOnce = False
            #print(hitBySpecialOnce)
            print("Voice: 2. Hit Enemy3. Did 5 damage.")
        elif self.isDead == False and self.hitboxCoords[2] <= self.voice.hitbox[4] <= self.hitboxCoords[0] and (self.hitboxCoords[1] <= self.voice.hitbox[1] <= self.hitboxCoords[3] or self.hitboxCoords[1] <= self.voice.hitbox[9] <= self.hitboxCoords[3]) and hitBySpecialOnce == True:
            print("Voice: 3. Hit Enemy3 when it's dead. (m8)")
            hitBySpecialOnce = False

        #print(self.voice.hitbox[10])

        global hitByBasicAttackOnce
        global basic_attack
        if self.isDead == False and basic_attack == True and self.hpLoss < 50 and (self.hitboxCoords[2] <= self.player.basicAttackHitboxR[2] <= self.hitboxCoords[0] or self.hitboxCoords[2] <= self.player.basicAttackHitboxR[0] <= self.hitboxCoords[0]) and (self.hitboxCoords[1] <= self.player.basicAttackHitboxR[1] <= self.hitboxCoords[3] or self.hitboxCoords[1] <= self.player.basicAttackHitboxR[3] <= self.hitboxCoords[3]) and hitByBasicAttackOnce == True:
            self.hpLoss += 5
            hitByBasicAttackOnce = False
            #print(hitByBasicAttackOnce)
            print("Basic Atack: 1. Hit Enemy3. Did 5 damage.")
        elif self.isDead == False and basic_attack == True and self.hpLoss < 50 and (self.hitboxCoords[2] <= self.player.basicAttackHitboxL[2] <= self.hitboxCoords[0] or self.hitboxCoords[2] <= self.player.basicAttackHitboxL[0] <= self.hitboxCoords[0]) and (self.hitboxCoords[1] <= self.player.basicAttackHitboxL[1] <= self.hitboxCoords[3] or self.hitboxCoords[1] <= self.player.basicAttackHitboxL[3] <= self.hitboxCoords[3]) and hitByBasicAttackOnce == True:
            self.hpLoss += 5
            hitByBasicAttackOnce = False
            #print(hitByBasicAttackOnce)
            print("Basic Atack: 2. Hit Enemy3. Did 5 damage.")
        elif self.isDead == False and basic_attack == True and (self.hitboxCoords[2] <= self.player.basicAttackHitboxR[2] <= self.hitboxCoords[0] or self.hitboxCoords[2] <= self.player.basicAttackHitboxR[0] <= self.hitboxCoords[0]) and (self.hitboxCoords[1] <= self.player.basicAttackHitboxR[1] <= self.hitboxCoords[3] or self.hitboxCoords[1] <= self.player.basicAttackHitboxR[3] <= self.hitboxCoords[3]) and hitByBasicAttackOnce == True:
            print("Basic Atack: 3. Hit Enemy3 when it's dead. (m8)")
            hitByBasicAttackOnce = False

        #print(self.player.basicAttackHitboxR[10])
        #print(self.player.basicAttackHitboxL[10])
                
        self.counterFrame += 1 #Add one to counterFrame (Starts at 0)
        
        if self.Frame == 1 and self.counterFrame == 50: #Once 25 iterations of draw() in the while loop far far below, change frame to 0
            self.Frame = 0
        elif self.Frame == 0 and self.counterFrame == 50: #if self.counterFrame > 25: #Once 50 iterations of draw() in the while loop far far below, change frame to 1
            self.Frame = 1
            
        if self.counterFrame == 100: #Reset the counter after 50 so that the cycle repeats over and over again.
            self.counterFrame = 0
            

class Sword: 
    def __init__(self,canvas):
        self.canvas = canvas
        #All of these variables are used for drawEye(self) method below.
        self.x_eye1, self.y_eye1 = 0,0
        self.x_pupil1, self.y_pupil1 = 0,0
        self.x_eyelid1, self.y_eyelid1 = 0,0
        self.counter = -70
        self.counter2 = 0
        
        #Anymore sword ideas please make "self.s4_"

        #Rusty Sword (Tier 0) #Desgined by Leon
        self.s1_name1 = canvas.create_text(500, 100, anchor="center", fill="green", text="Rusty Sword (Tier 0)", font=("Fixedsys", 16)) #The "s_" means sword for short.
        self.s1_blade1 = canvas.create_polygon(493, 165, 498, 165, 498, 140, 500, 138, 502, 140, 502, 165, 507, 165, 507, 168, 501, 168, 501, 180, 499, 180, 499, 168, 493, 168, fill="gray50", outline="black") #Follow the format of naming please.
        self.s1_handle1 = canvas.create_polygon(493, 165, 507, 165, 507, 168, 501, 168, 501, 180, 499, 180, 499, 168, 493, 168, fill="saddle brown", outline="black")
        self.s1_hilt1 = canvas.create_polygon(493, 165, 507, 165, 507, 168, 493, 168, fill="brown", outline="black")
        self.s1_rust1 = canvas.create_line(500, 139, 501, 140, 501, 165, fill="brown")

        #Porous Sword (Tier Unknown) Designed by Leon
        #An  unusual sword that is riddled with little holes on its surface. Upon closer inspection the holes seem to be.. pulsating?
        self.s2_name2 = canvas.create_text(1000, 100, anchor="center", fill="green", text="Porous Sword (Tier Unknown)", font=("Fixedsys", 16)) 
        self.s2_handle2 = canvas.create_polygon(999, 160, 1001, 160, 1001, 180, 999, 180, fill="brown", outline="black")
        self.s2_blade2a = canvas.create_arc(993, 130, 1007, 210, start = 0, extent = 180, outline ="red", fill = "pink", width = 1)
        self.s2_blade2b = canvas.create_polygon(1000, 170, 1008, 170, 1008, 187, outline="red", fill="pink")
        self.s2_blade2c = canvas.create_polygon(1000, 170, 1007, 170, 1007, 187, fill="pink")
        self.s2_hole1 = canvas.create_oval(999, 135, 1001, 137, outline="red", fill="black")
        self.s2_hole2 = canvas.create_oval(997, 142, 999, 144, outline="red", fill="black")
        self.s2_hole3 = canvas.create_oval(1001, 144, 1003, 146, outline="red", fill="black")
        self.s2_hole4 = canvas.create_oval(996, 150, 998, 152, outline="red", fill="black")
        self.s2_hole5 = canvas.create_oval(1002, 156, 1004, 158, outline="red", fill="black")
        self.s2_hole6 = canvas.create_oval(995, 159, 997, 161, outline="red", fill="black")

        #True Blood
        #A sword forged with the most wicked souls from hell.
        #Obtained by feeding your sword enough to fill it's hunger, making mostly evil decisions, and being controlling towards the blade around half the time.
        #Your actions make you as sinister as the blade itself, but bold enough to challenge the demonic sword.
        #Due to this the blade respects you and sees you worthy as it's user.
        #The blade treats you as an equal and therefore rewards you with it's true form.
        #Abilities:
        #- Summon the damned souls you have executed (major bosses) and they will fight for you.
        #- All swipe attacks have lingering blood.
        #- Increased damage 
        #- Create portals to hell to suck enemies in (or cracks the ground and drops them in)
        #- Feeds sword after kill.
        #- All lethal abilities now deal x3 damage.
        
        #self.s_TBeyelid1 = canvas.create_oval(430, 190, 570, 280, fill="black")
        #self.s_TBeye1 = canvas.create_oval(430, 200, 570, 270, fill="firebrick4") #EYE OPEN
        #self.s_TBpupil1 = canvas.create_oval(488, 222, 513, 248, fill="black")
        self.s3_bgBlood3 = canvas.create_polygon(460, 210, 495, 230, 545, 270, fill="firebrick4")
        #self.s_bgSkelArm1 = canvas.create_polygon(485-25+10, 220-10, fill="white", outline="black")
        #self.s_bgSkelHand1 = canvas.create_oval(485-25, 220-10+10, 485-25+15, 220-10+10+15, fill="white", outline="black")
        #self.s_bloodbgb3 = canvas.create_polygon(485, 220, 520, 240, 525, 250, fill="firebrick4")
        self.s3_name3 = canvas.create_text(500, 200, anchor="center", fill="red", text="True Blood (Tier: Endgame)", font=("Fixedsys", 16)) #The "s_" means sword for short.
        self.s3_blade3 = canvas.create_polygon(500, 208, 506, 230, 506, 255, 500, 255, fill="black", outline="indian red") #Follow the format of naming please. 500
        self.s3_bladeb3 = canvas.create_polygon(494, 255, 494, 230, 500, 208, 500, 255, fill="black", outline="red") #Follow the format of naming please. 500
        self.s3_hilt3 = canvas.create_polygon(489, 255, 511, 255, 511, 258, 489, 258, fill="grey1", outline="black")
        self.s3_hiltb3 = canvas.create_polygon(491, 255, 509, 255, 509, 258, 491, 258, fill="red2", outline="black")
        self.s3_handle3 = canvas.create_polygon(503, 270, 497, 270, 497, 258, 503, 258, fill="black", outline="black")
        self.s3_sash3 = canvas.create_polygon(503, 260, 497, 260, 497, 258, 503, 258, fill="firebrick4", outline="black")
        self.s3_sashb3 = canvas.create_polygon(503, 270, 497, 270, 497, 269, 503, 269, fill="firebrick4", outline="black")
        self.s3_bottomOfSword = canvas.create_oval(495, 270, 505, 275, fill="red") #EYE OPEN
        self.s3_blackMiddle = canvas.create_oval(500, 256, 500, 257, fill="black")

        #Conscience of the Blade
        self.s_eyelid1 = canvas.create_oval(1155, -130, 1295, -40, fill="black")
        #self.s_eye1 = canvas.create_oval(1155, 20-140, 1295, 90-140, fill="white") #EYE OPEN
        self.s_eye1 = canvas.create_oval(1155, -85, 1295, -85, fill="white") #Eye closed
        self.s_pupil1 = canvas.create_oval(1213, -98, 1238, -72, fill="black")
        
    def drawEye(self): #Animates the big eye in the top right of the screen. self.counter (which is a counter) starts at -70 and ends at 246 when it resets.
        if -70 <= self.counter < 0: #Move closed eye into screen
            if self.counter == -1:
                canvas.move(self.s_eye1, 0, 140)
                canvas.move(self.s_pupil1, 0, 140)
            self.counter += 1
            canvas.move(self.s_eyelid1, 0, 2)
            #print("if 0")
            #self.y_eyelid1 += 2 
            #canvas.coords(self.s_eyelid1, 1155, 10+self.y_eyelid1, 1295, 100+self.y_eyelid1)
        elif 0 <= self.counter <= 25: #Opens eye
            self.y_eye1 += 1 #25
            self.counter += 1
            canvas.coords(self.s_eye1, 1155, 55-self.y_eye1, 1295, 55+self.y_eye1)
            #print("First if")
        elif 25 < self.counter <= 85: #Eye blinks once and remains open
            self.y_eye1 -= 1 #-65+25 = -40
            self.counter += 1
            canvas.coords(self.s_eye1, 1155, 55-self.y_eye1, 1295, 55+self.y_eye1)
            #print("Second if")
        elif 86 <= self.counter <= 100 and self.counter2 == 1: #Pupil moves down
            self.x_pupil1 += 2
            self.y_pupil1 += 1
            self.counter += 1
            canvas.coords(self.s_pupil1, 1213-self.x_pupil1, 42+self.y_pupil1, 1238-self.x_pupil1, 68+self.y_pupil1)
            #print("Third if")
        elif 100 < self.counter <= 124 and self.counter2 == 1: #Pupil rests for a few seconds
            self.counter += 1
        elif 124 < self.counter <= 140 and self.counter2 == 1: #Pupil moves back to middle
            #print("Fourth if")
            self.x_pupil1 -= 2
            self.y_pupil1 -= 1
            self.counter += 1
            canvas.coords(self.s_pupil1, 1213-self.x_pupil1, 42+self.y_pupil1, 1238-self.x_pupil1, 68+self.y_pupil1)
        elif 140 <= self.counter <= 174: #Eye closes
            self.y_eye1 += 1
            self.counter += 1
            canvas.coords(self.s_eye1, 1155, 55-self.y_eye1, 1295, 55+self.y_eye1)
            #print("5 if")
        elif self.counter == 175: #Move pupil and the white in the eye out so only the eyelid is visible
            #print("6 if")
            self.counter += 1
            canvas.move(self.s_eye1, -100000, -100000)
            canvas.move(self.s_pupil1, -100000, -100000)
        elif 176 <= self.counter < 246: #Shift eye upwards out of screen
            #print("7 if")
            self.counter += 1
            canvas.move(self.s_eyelid1, 0, -2)
        elif self.counter == 246: #Resets all eye movement and such.
            self.s_eyelid1 = canvas.create_oval(1155, 10, 1295, 100, fill="black")
            self.s_eye1 = canvas.create_oval(1155, 55, 1295, 55, fill="white") #Eye closed
            self.s_pupil1 = canvas.create_oval(1213, 42, 1238, 68, fill="black")
            canvas.move(self.s_eyelid1, 0, -140)
            canvas.move(self.s_eye1, 0, -140)
            canvas.move(self.s_pupil1, 0, -140)
        
            self.x_eye1, self.y_eye1 = 0,0
            self.x_pupil1, self.y_pupil1 = 0,0
            self.x_eyelid1, self.y_eyelid1 = 0,0
            self.counter = -70
            self.counter2 = 0
            
        if self.counter2 <= 1:
            self.counter2 += 1
        else:               
            self.counter2 = 0

class Bars:
    def __init__(self,canvas):
        self.canvas = canvas

        #Stats that change/Variables
        self.healthLoss = 0
        self.counterFrameLava = 0
        self.manaLoss = 0
        self.sprintLoss = 0
        self.counterFrameSprint = 0 #For first if statement regarding sprint in this class's draw(self) method.
        self.counterFrameSprint2 = -100 #second ^
        self.counterFrameSprint3 = 0 #third ^
        self.getOutOfStatement = True #Used for 

        #Model for the bars in the bottom right hand corner of window.
        self.h_sprintBorder = canvas.create_rectangle(1037, 667, 1228, 689, fill="black", outline="black")
        self.h_sprintGrey = canvas.create_rectangle(1039, 669, 1228, 687, fill="grey50")
        self.h_sprint = canvas.create_rectangle(1039, 669, 1228, 687, fill="green")      
        self.h_sprintName = canvas.create_text(1151, 678, text="SP", fill="black", anchor="center", font=("Fixedsys", 16))       
        self.h_bg = canvas.create_oval(1130, 525, 1295, 690,fill="black", outline="black")       
        self.h_hpFill = canvas.create_line(1273, 608, 1291, 608, fill="red2") 
        self.h_hpGrey = canvas.create_arc(1143, 538, 1282, 677, width=18, start=0, extent=359, style=ARC, outline="grey")     
        self.h_hp = canvas.create_arc(1143, 538, 1282, 677, width=18, start=0, extent=359, style=ARC, outline="red2")
        self.h_mpGrey = canvas.create_arc(1165, 560, 1260, 655, width=18, start=0, extent=359, style=ARC, outline="grey")
        self.h_mp = canvas.create_arc(1165, 560, 1260, 655, width=18, start=0, extent=359, style=ARC, outline="blue")
        self.h_bg2 = canvas.create_arc(1193, 588, 1232, 627, width=26, start=0, extent=359, style=ARC, outline="SteelBlue3")
        self.h_hand1 = canvas.create_oval(1180, 575, 1220, 615,fill="white", outline="black")
        self.h_hand2 = canvas.create_oval(1205, 600, 1245, 640,fill="white", outline="black")
        self.h_weaponName = canvas.create_text(1215, 610, text="Fists", fill="black", anchor="center", font=("Fixedsys", 16))
        self.h_hpName = canvas.create_text(1195, 540, text="HP", fill="black", anchor="center", font=("Fixedsys", 16))
        self.h_mpName = canvas.create_text(1205, 560, text="MP", fill="black", anchor="center", font=("Fixedsys", 16))
        self.h_playerClassName = canvas.create_text(1215, 515, text="[Dis-Connor-ed]", fill="green", anchor="center", font=("Fixedsys", 16))
        self.h_mpAbilityName = canvas.create_text(1215, 655, text="Voice", fill="black", anchor="center", font=("Fixedsys", 16))

    def draw(self):         #When mana is unused, regenerate? #When not hurt, heal? #These are undone.

        global enemy3Damage
        if enemy3Damage == True:
            if self.healthLoss >= -358:
                self.healthLoss -= 10
                canvas.delete(self.h_hp)
                self.h_hp = canvas.create_arc(1143, 538, 1282, 677, width=18, start=0, extent=359+self.healthLoss, style=ARC, outline="red2")
                #print("Decrease hp now from Enemy3 attack)")
                self.h_hpName = canvas.create_text(1195, 540, text="HP", fill="black", anchor="center", font=("Fixedsys", 16))
            elif self.healthLoss <= -359: #if self.counterFrameLava > 25: #Once 50 iterations of draw() in the while loop far far below, change frame to 1
                #print("YOU ARE DEAD caused from Enemy3 attack")
                canvas.delete(self.h_hpFill)
                canvas.delete(self.h_hp)
            #enemy3Damage = False

        #WHEN IN LAVA, GET DAMAGED
        global lavaDamage
        if lavaDamage == True:
            #print("HOT LAVA BOI")
            if self.healthLoss >= -354: #Once 25 iterations of draw() in the while loop far far below, change frame to 0
                self.healthLoss -= 5
                canvas.delete(self.h_hp)
                self.h_hp = canvas.create_arc(1143, 538, 1282, 677, width=18, start=0, extent=359+self.healthLoss, style=ARC, outline="red2")
                #print("Decrease hp now (25 counterFrameLava)")
                self.h_hpName = canvas.create_text(1195, 540, text="HP", fill="black", anchor="center", font=("Fixedsys", 16))
            elif self.healthLoss <= -355: #if self.counterFrameLava > 25: #Once 50 iterations of draw() in the while loop far far below, change frame to 1
                #print("YOU ARE DEAD")
                self.healthLoss -= 300
                canvas.delete(self.h_hpFill)
                canvas.delete(self.h_hp)
                lavaDamage = False
                print("Killed by the red floor.")

            #self.counterFrameLava += 1 #Add one to counterFrame (Starts at 0)
            
            #if self.counterFrameLava == 50: #Reset the counter after 50 so that the cycle repeats over and over again.
                #self.counterFrameLava = 0

        #When mana is used, decrease mana bar
        global manaUsed
        global voiceOn
        if manaUsed == True:
            if voiceOn == True and self.manaLoss >= -349:
                self.manaLoss -= 50
                #print("self.manaLoss:", self.manaLoss)
                canvas.delete(self.h_mp)
                self.h_mp = canvas.create_arc(1165, 560, 1260, 655, width=18, start=0, extent=359+self.manaLoss, style=ARC, outline="blue")
            #else: #Unreachable code because the player.spacebar bind method will not make manaUsed to True ever if out of mana.
                #print("YOU GOT NO MANA!")
                #pass
            self.h_mpName = canvas.create_text(1205, 560, text="MP", fill="black", anchor="center", font=("Fixedsys", 16))
            self.h_mpAbilityName = canvas.create_text(1215, 655, text="Voice", fill="black", anchor="center", font=("Fixedsys", 16))
            manaUsed = False

        #Update sprint bar when sprinting.
        global sprinting
        global moving
        global outOfSprint
        if sprinting == True:
            self.getOutOfStatement = False
            if self.sprintLoss >= -149 and self.counterFrameSprint == 25 and moving == True:
                self.sprintLoss -= 10
                #print("self.sprintLoss:", self.sprintLoss)  #self.sprintLoss: -120 is when change
                canvas.coords(self.h_sprint, 1039-self.sprintLoss, 669, 1228, 687)
                moving = False
            elif self.counterFrameSprint == 25 and moving == True: 
                #print("Out of SP! You must wait until sprint bar is full before sprinting again.")
                moving = False
                outOfSprint = True
                sprinting = False

            self.counterFrameSprint += 1 #Add one to counterFrame (Starts at 0)
            
            if self.counterFrameSprint == 50: #Reset the counter after 50 so that the cycle repeats over and over again.
                self.counterFrameSprint = 0

        if sprinting == False and outOfSprint == False and self.getOutOfStatement == False:
            if self.counterFrameSprint2 >= -100 and self.counterFrameSprint2 < 0:
                #print("Might cause lag") #Doesn't
                pass
            elif self.sprintLoss < 0 and self.counterFrameSprint2 == 25:
                self.sprintLoss += 10
                #print("2. Regenerating sprint... self.sprintLoss:", self.sprintLoss)
                canvas.coords(self.h_sprint, 1039-self.sprintLoss, 669, 1228, 687)
                #moving = False
            elif self.counterFrameSprint2 == 25: 
                #print("2. FULLY RENEGERATED SPRINT!")
                #moving = False
                outOfSprint = False
                #oneIterate = True
                self.counterFrameSprint2 = -100
                self.getOutOfStatement = True

            self.counterFrameSprint2 += 1 #Add one to counterFrame (Starts at 0)
            
            if self.counterFrameSprint2 == 50: #Reset the counter after 50 so that the cycle repeats over and over again.
                self.counterFrameSprint2 = 0

        #AFter running out of sprint, start regenerating SP.
        global oneIterate
        if outOfSprint == True:
            if self.sprintLoss < 0 and self.counterFrameSprint3 == 25:
                self.sprintLoss += 10
                #print("3. Regenerating sprint... self.sprintLoss:", self.sprintLoss)
                canvas.coords(self.h_sprint, 1039-self.sprintLoss, 669, 1228, 687)
                #moving = False
            elif self.counterFrameSprint3 == 25: 
                #print("3. Sprint replenished! You may sprint now.")
                #moving = False
                outOfSprint = False
                oneIterate = True

            self.counterFrameSprint3 += 1 #Add one to counterFrame (Starts at 0)
            
            if self.counterFrameSprint3 == 50: #Reset the counter after 50 so that the cycle repeats over and over again.
                self.counterFrameSprint3 = 0

        global gameOver
        if self.healthLoss <= -359:
            gameOver = True
            canvas.delete(self.h_hpFill)
            canvas.delete(self.h_hp)
            print("GAME OVER")
            print("Just give up.")
            
class PhotoTest: #Testing to see if we can print images onto the program
    def __init__(self,canvas):
        #canvas = tkinter.Canvas(master)
        #canvas.grid(row = 0, column = 0)
        #photoTest = tkinter.PhotoImage(file = './test.gif')
        #canvas.create_image(0,0, image=photoTest, anchor=center)
        pass

class Nathaniel2010: #Refernce to Heavy Rain's AVI 
    def __init__(self,canvas):
        self.canvas = canvas
        #self.n_glove = canvas.create_polyon(fill="black")
        #self.n_glasses = canvas.create_polygon(fill="black")

class Background:
    def __init__(self,canvas):
        self.canvas = canvas
        self.a_description = canvas.create_text(0, 550, text="""Update Alpha 3.0.1: Enemies of the East\n"""
                                                """Kill it.""",
                                                  #"""\nThe line is the hitbox and it is facing the wrong way but I'm too lazy to mirror it and it should be fine."""
                                                #""" Enemy3 should move across the screen, stop, and turn around when it reaches the window border. This is done with the hitbox line."""
                                                #"""\nMight change basic attacks while sprinting and/or crouching to have a different animation."""
                                                #""" Pressing Q now pauses/unpauses the Big Eye animation."""
                                                  #""" Voice rework. Voice and basic attacks can now damage hp bar of Enemy3. Has death animation now and deletes shapes and ends it's draw method.""",
                                                  width=1000, fill="black", anchor="nw", font=("Fixedsys", 16))#Top left corner of screen text
        self.a_description2 = canvas.create_text(0, 0, text="""WASD to move around. Press left Shift to toggle sprint. Press left Control to toggle crouch.\n"""
                                                                 """Spacebar is the special ability that has a cooldown. Only Voice Attack is avaliable. Did I mention you can left click?""",
                                                 width=1000, fill="black", anchor="nw", font=("Fixedsys", 16))#Top left corner of screen text)
        #Creating ground1
        self.a_ground1 = canvas.create_rectangle(0,183,1500,190, outline="black",fill="green")

        #Creating ground2
        self.a_ground2 = canvas.create_rectangle(0,273,1500,280, outline="black",fill="green")

        #Creating lava pool. Can damage player now.
        self.a_lava1 = canvas.create_rectangle(0,273,100,280, outline="black",fill="red")

        #Creating ground3
        self.a_ground3 = canvas.create_rectangle(0,363,1500,370, outline="black",fill="brown")

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

        canvas.move(self.voice1, -10000, -10000)
        canvas.move(self.voice2, -10000, -10000)
        canvas.move(self.voice3, -10000, -10000)

        self.hitbox = canvas.coords(self.voice1)
        self.hitboxEnd = canvas.coords(self.voice3)

        #Mirroring the above over y-axis. Needed for player looking left.
        #125-150 = 25/2 = 12.5- > 13 + 125 = 138
        #self.voice1 = canvas.create_polygon(137+2, 130, 146-16, 136, 147-18, 142, 146-16, 149, 137+2, 155, 143-10, 149, 144-12, 142, 143-10, 136, fill="grey", outline="black")
        #self.voice2 = canvas.create_polygon(130+16, 135, 139-2, 140, 140-4, 142, 139-2, 146, 130+16, 150, 137+2, 144, 137+2, 142, 137+2, 141, fill="grey", outline="black") #(-7, -5 or +5) (+3, 0) (-3,0
        #self.voice3 = canvas.create_polygon(129+18, 140, 131+14, 142, 129+18, 146, 128+20, 144, 130+16, 142, 128+20, 141, fill="grey", outline="black") #(-9, 0)

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
            
            if self.vLooking == "Left": #self.counter == 10:
                #self.counter = 0
                self.x -= 20
                canvas.move(self.voice1, -10, 0)
                canvas.move(self.voice2, -10, 0)
                canvas.move(self.voice3, -10, 0)
                canvas.update() #1
                self.hitbox = canvas.coords(self.voice1)
                self.hitboxEnd = canvas.coords(self.voice3)
                if self.x == -2000: #-520
                    self.x = 0
                    voiceOn = False
                    self.vLooking = ""
                    canvas.move(self.voice1, -1000000, -1000000)
                    canvas.move(self.voice2, -1000000, -1000000)
                    canvas.move(self.voice3, -1000000, -1000000)
                    print("Special Ready.")
                    
            elif self.vLooking == "Right": #self.counter == 10:
                #self.counter = 0
                self.x += 20
                canvas.move(self.voice1, 10, 0)
                canvas.move(self.voice2, 10, 0)
                canvas.move(self.voice3, 10, 0)
                canvas.update() #1
                self.hitbox = canvas.coords(self.voice1)
                self.hitboxEnd = canvas.coords(self.voice3)
                if self.x == 2000: #520
                    self.x = 0
                    voiceOn = False
                    self.vLooking = ""
                    canvas.move(self.voice1, -1000000, -1000000)
                    canvas.move(self.voice2, -1000000, -1000000)
                    canvas.move(self.voice3, -1000000, -1000000)
                    print("Special Ready.")
                    

class Player:
    def __init__(self,canvas, background, bars):
        self.canvas = canvas
        self.background = background
        self.bars = bars
        
        self.x, self.y = 0,0 #Only one coordinate now. This coordinate is where the first shape is __init__ialized. Not the graph.
        self.Frame = 0 #Two frames-0 and 1. They alternate which makes the character move more lively.
        self.sprint = False #Pressing 'Shift' will make it True. In draw() method, will check condition.
        self.crouch = False #Pressing 'Ctrl' will make it True. In draw() method, will check condition.
        self.inAir = False #Unused. But might make the character be able to move left and right while in air later.
        self.looking = "Right" #Need to check what direction character is facing when moving up or down. 
        self.counter = 3 #Without this, the character will slide
        self.counterFrame = 0 #Changes frames Look at the bottom of the draw() method for more details.
        self.notMoving = True #Makes sure the char doesnt slide. This is because at the very end of the code, draw() is constantly being called in the while loop so if there is no sentinel to stop it from moving, the char would slide across the screen.
        self.dropping = False #Pressing 's' will make it True. In draw() method, will check condition.
        self.jumping = False #Pressing 'w' will make it True. In draw() method, will check condition.
        self.inAirCounter = 0 #Check the bottom of draw(). This allows the program to counter how many iterations I want to be in air.
        self.basic_attack_counter = 0
        self.moveFists = 0
        self.forward = True
        #self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.pastBorderLeft = False
        self.pastBorderRight = False
        self.pastBorderUp = False
        self.pastBorderDown = False
        self.pastBorderRightKeepAnimation = False
        
        #Creating the model of player 1 w/ label above it's head
        #Character is walking to the right of the screen
        #Name of the character
        self.a_name = canvas.create_text(138, 110, text="Blademaster of the Thousand Years War, Guy", width=1000, fill="green", anchor="center", font=("Fixedsys", 16))

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

        #Hitbox
        self.a_hitbox = canvas.create_line(150, 125, 125, 183)
        canvas.itemconfigure(self.a_hitbox, state='hidden')
        self.hitbox = canvas.coords(self.a_hitbox)

        #Basic attack hitbox
        self.basicAttackHitboxR = canvas.coords(self.a_Rarm)
        self.basicAttackHitboxL = canvas.coords(self.a_Larm)

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
        global oneIterate
        if outOfSprint == True and oneIterate == True:
            self.sprint = False
            self.counter = 9
            oneIterate = False
            
        if self.counter == 10:
            self.notMoving = True
            pass
        else:
            self.counter += 1

        #JUMP RIGHT WHILE ON RIGHT BORDER

        if self.notMoving == True and self.dropping == False and self.jumping == False: #If character is not moving, do nothing
            pass

        elif self.Frame == 0 and self.sprint == False and self.crouch == False and self.dropping == False and self.jumping == True and self.pastBorderRightKeepAnimation == True: #Moving right without sprinting or crouching FRAME #1
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
            canvas.coords(self.a_hitbox, 150+self.x, 125+self.y, 125+self.x, 183+self.y)
               
        elif self.Frame == 1 and self.sprint == False and self.crouch == False and self.dropping == False and self.jumping == True and self.pastBorderRightKeepAnimation == True: #Moving right without sprinting or crouching FRAME #2
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
            canvas.coords(self.a_hitbox, 150+self.x, 125+self.y, 125+self.x, 183+self.y)

        elif self.Frame == 0 and self.sprint == True and self.crouch == False and self.dropping == False and self.jumping == True and self.pastBorderRightKeepAnimation == True: #Moving right SPRINTING FRAME #1
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
            canvas.coords(self.a_hitbox, 170+self.x, 135+self.y, 125+self.x, 183+self.y)
                
        elif self.Frame == 1 and self.sprint == True and self.crouch == False and self.dropping == False and self.jumping == True and self.pastBorderRightKeepAnimation == True: #Moving right SPRINTING FRAME #2
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
            canvas.coords(self.a_hitbox, 170+self.x, 135+self.y, 125+self.x, 183+self.y)

        elif self.Frame == 0 and self.sprint == False and self.crouch == True and self.dropping == False and self.jumping == True and self.pastBorderRightKeepAnimation == True: #Moving right CROUCHING FRAMe #1
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
            canvas.coords(self.a_hitbox, 170+self.x, 135+self.y, 125+self.x, 183+self.y)
                
        elif self.Frame == 1 and self.sprint == False and self.crouch == True and self.dropping == False and self.jumping == True and self.pastBorderRightKeepAnimation == True: #Moving right CROUCHING FRAMe #2
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
            canvas.coords(self.a_hitbox, 170+self.x, 135+self.y, 125+self.x, 183+self.y)

        #Moving Right DROPPING       
        elif self.Frame == 0 and self.sprint == False and self.crouch == False and self.dropping == True and self.pastBorderRightKeepAnimation == True: #Moving right without sprinting or crouching FRAME #1
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
            canvas.coords(self.a_hitbox, 150+self.x, 125+self.y, 125+self.x, 183+self.y)
               
        elif self.Frame == 1 and self.sprint == False and self.crouch == False and self.dropping == True and self.pastBorderRightKeepAnimation == True: #Moving right without sprinting or crouching FRAME #2
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
            canvas.coords(self.a_hitbox, 150+self.x, 125+self.y, 125+self.x, 183+self.y)
            
        elif self.Frame == 0 and self.sprint == True and self.crouch == False and self.dropping == True and self.pastBorderRightKeepAnimation == True: #Moving right SPRINTING FRAME #1
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
            canvas.coords(self.a_hitbox, 170+self.x, 135+self.y, 125+self.x, 183+self.y)
            
        elif self.Frame == 1 and self.sprint == True and self.crouch == False and self.dropping == True and self.pastBorderRightKeepAnimation == True: #Moving right SPRINTING FRAME #2
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
            canvas.coords(self.a_hitbox, 170+self.x, 135+self.y, 125+self.x, 183+self.y)

        elif self.Frame == 0 and self.sprint == False and self.crouch == True and self.dropping == True and self.pastBorderRightKeepAnimation == True: #Moving right CROUCHING FRAMe #1
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
            canvas.coords(self.a_hitbox, 170+self.x, 135+self.y, 125+self.x, 183+self.y)
              
        elif self.Frame == 1 and self.sprint == False and self.crouch == True and self.dropping == True and self.pastBorderRightKeepAnimation == True: #Moving right CROUCHING FRAMe #2
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
            canvas.coords(self.a_hitbox, 170+self.x, 135+self.y, 125+self.x, 183+self.y)


        #IF CHARACTER IS ON THE RIGHT BORDER HAVE THE KEEP MOVING ANIMATION BUT DO NOT MOVE THE CHARACTER TO THE RIGHT ANYMORE
        elif self.Frame == 0 and self.sprint == False and self.crouch == False and self.looking == "Right" and self.pastBorderRightKeepAnimation == True: #Moving right without sprinting or crouching FRAME #1
            #self.x += 1 #Arms and legs out self.x 
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
            canvas.coords(self.a_hitbox, 150+self.x, 125+self.y, 125+self.x, 183+self.y)
                
        elif self.Frame == 1 and self.sprint == False and self.crouch == False and self.looking == "Right" and self.pastBorderRightKeepAnimation == True: #Moving right without sprinting or crouching FRAME #2
            #self.x += 1 #Arms and legs in
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
            canvas.coords(self.a_hitbox, 150+self.x, 125+self.y, 125+self.x, 183+self.y)

        elif self.Frame == 0 and self.sprint == True and self.crouch == False and self.looking == "Right" and self.pastBorderRightKeepAnimation == True: #Moving right SPRINTING FRAME #1
            #self.x += 1 #Arms and legs out
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
            canvas.coords(self.a_hitbox, 170+self.x, 135+self.y, 125+self.x, 183+self.y)
            #self.x += 3
            #(12,0) (10,10), (-35,0), (-30,-20), (-5,-5)
                
        elif self.Frame == 1 and self.sprint == True and self.crouch == False and self.looking == "Right" and self.pastBorderRightKeepAnimation == True: #Moving right SPRINTING FRAME #2
            #self.x += 1 #Arms and legs in
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
            canvas.coords(self.a_hitbox, 170+self.x, 135+self.y, 125+self.x, 183+self.y)
            #(12,0) (10,10), (-35,0), (-30,-20), (-5,-5)
            #self.x += 3

        elif self.Frame == 0 and self.sprint == False and self.crouch == True and self.looking == "Right" and self.pastBorderRightKeepAnimation == True: #Moving right CROUCHING FRAMe #1
            #self.x += 0.5 #Arms and legs in
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
            canvas.coords(self.a_hitbox, 170+self.x, 135+self.y, 125+self.x, 183+self.y)
                
        elif self.Frame == 1 and self.sprint == False and self.crouch == True and self.looking == "Right" and self.pastBorderRightKeepAnimation == True: #Moving right CROUCHING FRAMe #2
            #self.x += 0.5 #Arms and legs in
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
            canvas.coords(self.a_hitbox, 170+self.x, 135+self.y, 125+self.x, 183+self.y)

        
        
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
            canvas.coords(self.a_hitbox, 125+self.x, 125+self.y, 150+self.x, 183+self.y)

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
            canvas.coords(self.a_hitbox, 125+self.x, 125+self.y, 150+self.x, 183+self.y)

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
            canvas.coords(self.a_hitbox, 145+self.x-40, 135+self.y, 150+self.x, 183+self.y)

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
            canvas.coords(self.a_hitbox, 145+self.x-40, 135+self.y, 150+self.x, 183+self.y)

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
            canvas.coords(self.a_hitbox, 145+self.x-40, 135+self.y, 150+self.x, 183+self.y)
            
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
            canvas.coords(self.a_hitbox, 145+self.x-40, 135+self.y, 150+self.x, 183+self.y)

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
            canvas.coords(self.a_hitbox, 150+self.x, 125+self.y, 125+self.x, 183+self.y)
               
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
            canvas.coords(self.a_hitbox, 150+self.x, 125+self.y, 125+self.x, 183+self.y)

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
            canvas.coords(self.a_hitbox, 170+self.x, 135+self.y, 125+self.x, 183+self.y)
                
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
            canvas.coords(self.a_hitbox, 170+self.x, 135+self.y, 125+self.x, 183+self.y)

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
            canvas.coords(self.a_hitbox, 170+self.x, 135+self.y, 125+self.x, 183+self.y)
                
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
            canvas.coords(self.a_hitbox, 170+self.x, 135+self.y, 125+self.x, 183+self.y)

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
            canvas.coords(self.a_hitbox, 125+self.x, 125+self.y, 150+self.x, 183+self.y)
  
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
            canvas.coords(self.a_hitbox, 125+self.x, 125+self.y, 150+self.x, 183+self.y)

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
            canvas.coords(self.a_hitbox, 145+self.x-40, 135+self.y, 150+self.x, 183+self.y)
                
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
            canvas.coords(self.a_hitbox, 145+self.x-40, 135+self.y, 150+self.x, 183+self.y)

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
            canvas.coords(self.a_hitbox, 145+self.x-40, 135+self.y, 150+self.x, 183+self.y)
                
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
            canvas.coords(self.a_hitbox, 145+self.x-40, 135+self.y, 150+self.x, 183+self.y)
            
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
            canvas.coords(self.a_hitbox, 150+self.x, 125+self.y, 125+self.x, 183+self.y)
               
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
            canvas.coords(self.a_hitbox, 150+self.x, 125+self.y, 125+self.x, 183+self.y)
            
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
            canvas.coords(self.a_hitbox, 170+self.x, 135+self.y, 125+self.x, 183+self.y)
            
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
            canvas.coords(self.a_hitbox, 170+self.x, 135+self.y, 125+self.x, 183+self.y)

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
            canvas.coords(self.a_hitbox, 170+self.x, 135+self.y, 125+self.x, 183+self.y)
              
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
            canvas.coords(self.a_hitbox, 170+self.x, 135+self.y, 125+self.x, 183+self.y)

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
            canvas.coords(self.a_hitbox, 125+self.x, 125+self.y, 150+self.x, 183+self.y)
                
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
            canvas.coords(self.a_hitbox, 125+self.x, 125+self.y, 150+self.x, 183+self.y)

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
            canvas.coords(self.a_hitbox, 145+self.x-40, 135+self.y, 150+self.x, 183+self.y)
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
            canvas.coords(self.a_hitbox, 145+self.x-40, 135+self.y, 150+self.x, 183+self.y)
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
            canvas.coords(self.a_hitbox, 145+self.x-40, 135+self.y, 150+self.x, 183+self.y)
                
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
            canvas.coords(self.a_hitbox, 145+self.x-40, 135+self.y, 150+self.x, 183+self.y)
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
            canvas.coords(self.a_hitbox, 150+self.x, 125+self.y, 125+self.x, 183+self.y)
                
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
            canvas.coords(self.a_hitbox, 150+self.x, 125+self.y, 125+self.x, 183+self.y)

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
            canvas.coords(self.a_hitbox, 170+self.x, 135+self.y, 125+self.x, 183+self.y)
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
            canvas.coords(self.a_hitbox, 170+self.x, 135+self.y, 125+self.x, 183+self.y)
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
            canvas.coords(self.a_hitbox, 170+self.x, 135+self.y, 125+self.x, 183+self.y)
                
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
            canvas.coords(self.a_hitbox, 170+self.x, 135+self.y, 125+self.x, 183+self.y)

        #Checks if hitbox was hit.
        self.hitbox = canvas.coords(self.a_hitbox) #Saves the coordinates of self.a_hitbox
        #print(self.hitbox) #Prints coordinates of the hitbox.
        #print(self.canvas_height)
        #print(self.canvas_width)

        if self.hitbox[3] <= 93: #Makes sure the position of character doesn't pass height
            self.pastBorderUp = True
            self.notMoving = True
            #print("pastBorderUp is True!")
        else:
            self.pastBorderUp = False
            self.notMoving = False

        if self.hitbox[3] >= 633: #Makes sure the position of character doesn't pass bottom of window [156.0, 575.0, 131.0, 633.0]
            self.pastBorderDown = True
            self.notMoving = True
            #print("pastBorderDown is True!")
        else:
            self.pastBorderDown = False
            self.notMoving = False

        if self.hitbox[0]<=0: #Makes sure the position of character doesn't pass left of window
            self.pastBorderLeft = True
            self.notMoving = True
            #print("pastBorderLeft is True!")
        else:
            self.pastBorderLeft = False
            self.notMoving = False

        if self.hitbox[0]>=self.canvas_width: #Makes sure the position of character doesn't pass right ENOUGH
            self.pastBorderRightKeepAnimation = True
            #self.pastBorderRight = True
            #self.notMoving = True
            #print("pastBorderRight is True!")
        else:
            self.pastBorderRightKeepAnimation = False
            #self.pastBorderRight = False
            #self.notMoving = False

        self.hitboxLegRight = canvas.coords(self.a_Rleg)
        self.hitboxLegLeft = canvas.coords(self.a_Lleg)
        self.hitLava = canvas.coords(self.background.a_lava1)
        #print("LAVA:", self.hitLava) #LAVA: [0.0, 273.0, 100.0, 280.0]
        #print("RIGHT:",self.hitboxLegRight)
        #print("LEFT:",self.hitboxLegLeft)
        #LAVA:
        #RIGHT: [115.0, 265.0, 130.0, 273.0]
        #LEFT: [85.0, 265.0, 100.0, 273.0]
        #0,273,100,280, Lava coords

        #LEFT: [61.0, 260.0, 76.0, 268.0] when sprinting with the frame legs out. Lava doesn't affect character if feet are not touching.
        #RIGHT: [80.0, 260.0, 95.0, 268.0]

        #Feet might be switched when in sprint stance
        if (self.hitboxLegLeft[0] <= self.hitLava[2] or self.hitboxLegRight[0] <= self.hitLava[2]) and self.hitboxLegLeft[3] <= self.hitLava[1] and self.hitboxLegRight[1] >= 260: #100, 100, 273, 260.0
            global lavaDamage
            #print("first if")
            lavaDamage = True
        #else:
            #print("second if")
            #lavaDamage = False


        #if self.hitbox[2] and self.hitbox[3]:
            

        #if self.hit_paddle(self.hitbox) == True: #Hitbox stuff
        #    self.y=-3

        self.counterFrame += 1 #Add one to counterFrame (Starts at 0)
        
        if self.counterFrame <= 25: #Once 25 iterations of draw() in the while loop far far below, change frame to 0
            self.Frame = 0
        else: #if self.counterFrame > 25: #Once 50 iterations of draw() in the while loop far far below, change frame to 1
            self.Frame = 1
            
        if self.counterFrame == 50: #Reset the counter after 50 so that the cycle repeats over and over again.
            self.counterFrame = 0

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
        if self.pastBorderLeft == False:
            self.looking = "Left"
            self.counter = 0
            self.notMoving = False
            global moving
            moving = True
        
    def dKey(self,evt):
        self.looking = "Right"
        self.counter = 0
        self.notMoving = False
        global moving
        moving = True
        
    def spaceKey(self, evt): #Special ability: Voice
        #canvas.unbind("<space>", self.b_space)
        global voiceOn
        global manaUsed
        global hitBySpecialOnce
        if voiceOn == True:
            print("Special on cooldown!")
        elif self.bars.manaLoss < -349:
            print("OUT OF MANA! Mana is at 10. 50 needed to cast Voice!")
        else:
            print("Special activated. Used 50 mana. Maximum mana storage is 360.")
            manaUsed = True
            voiceOn = True
            hitBySpecialOnce = True
        #canvas.after(100, self.rebindSpace) #MOVED TO BOTTOM OF VOICE.DRAW()
        
    def rebindSpace(self):
        global voiceOn
        self.b_space = canvas.bind("<space>", self.spaceKey)

    def eKey(self, evt): #Action Key
        print("'e' key pressed")
        

    def qKey(self, evt): #Switch weapons
        #print("'q' key pressed")
        print("Pressed Q: Pause swordEye.draw() animation")
        global pressQ
        if pressQ == True:
            pressQ = False
        else:
            pressQ = True
        
    def sKey(self, evt): #Drop down
        if self.pastBorderDown == False:
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
        if self.pastBorderUp == False:
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
            pass
            #print("basic_attack = False CANNOT ENTER THIS PLACE USUALLY")
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
            canvas.coords(self.a_hitbox, 125+self.x, 125+self.y, 150+self.x, 183+self.y)
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
            canvas.coords(self.a_hitbox, 125+self.x, 125+self.y, 150+self.x, 183+self.y)
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
            canvas.coords(self.a_hitbox, 125+self.x, 125+self.y, 150+self.x, 183+self.y)
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
            canvas.coords(self.a_hitbox, 125+self.x, 125+self.y, 150+self.x, 183+self.y)
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
            canvas.coords(self.a_hitbox, 150+self.x, 125+self.y, 125+self.x, 183+self.y)

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
            canvas.coords(self.a_hitbox, 150+self.x, 125+self.y, 125+self.x, 183+self.y)

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
            canvas.coords(self.a_hitbox, 150+self.x, 125+self.y, 125+self.x, 183+self.y)

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
            canvas.coords(self.a_hitbox, 150+self.x, 125+self.y, 125+self.x, 183+self.y)

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
            #print("Basic attack animation done")
            basic_attack = False

        self.basicAttackHitboxR = canvas.coords(self.a_Rarm)
        self.basicAttackHitboxL = canvas.coords(self.a_Larm)
            
    def leftClick(self, evt): #Basic attack - Punching
        #1 frame - Legs in. Still need facing still need to check if sprinting or crouching. Need to check looking.
        global basic_attack
        global hitByBasicAttackOnce
        #print("Left Click")
        if basic_attack == False:
            basic_attack = True
            hitByBasicAttackOnce = True
            canvas.unbind("<Button-1>", self.b_leftClick)
            canvas.unbind("<Button-2>", self.b_scroll)
            canvas.unbind("<Button-3>", self.b_rightClick)
            canvas.unbind("<a>", self.b_a)
            canvas.unbind("<d>", self.b_d)
            canvas.unbind("<s>", self.b_s)
            canvas.unbind("<w>", self.b_w)
            canvas.unbind("<q>", self.b_q)
            canvas.unbind("<e>", self.b_e)
            #print("Initialing basic attack")
        else:
            #print("Basic attack still in animation!")
            pass

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
        global sprinting
        global outOfSprint
        if self.sprint == True and self.crouch == False and outOfSprint == False:
            self.sprint = False
            sprinting = False
            self.counter = 9 #This line and the next allows one frame of the player.draw() method to change the stance of the character. The character moves a bit due to 1 draw() frame but it is almost unoticeable.
            self.notMoving = False
        elif self.sprint == False and self.crouch == False and outOfSprint == False:
            self.sprint = True
            sprinting = True
            self.counter = 9
            self.notMoving = False
        elif outOfSprint == False: #If you are crouching, pressing shift will change that to sprinting
            #print("Toggling sprint to True and making crouch False")
            self.sprint = True
            sprinting = True
            self.crouch = False
            self.counter = 9
            self.notMoving = False
        else:
            print("YOU CANNOT SPRINT BECAUSE outOfSprint == True")

    def ctrlKey(self, evt): #crouch
        global sprinting
        global outOfSprint
        if self.crouch == True and self.sprint == False:
            self.crouch = False
            self.counter = 9
            self.notMoving = False
        elif self.crouch == False and self.sprint == False:
            self.crouch = True
            self.counter = 9
            self.notMoving = False
        elif outOfSprint == False: #If you are sprinting, pressing ctrl will change that to crouching
            #print("Toggling crouch to True and making sprint False")
            self.sprint = False
            sprinting = False
            self.crouch = True
            self.counter = 9
            self.notMoving = False
        #else: #Unreachable code
            #print("YOU CANNOT SPRINT BECAUSE outOfSprint == True")
                
background = Background(canvas)
enemy1 = Enemy1(canvas)
enemy2 = Enemy2(canvas)
sword = Sword(canvas)
#nathaniel2010 = Nathaniel2010(canvas)
#photoTest = PhotoTest(canvas)
bars = Bars(canvas)
player = Player(canvas,background, bars)
voice = Voice(canvas,player)
enemy3 = Enemy3(canvas, voice, player)
canvas.focus_set() #Tells Python to use keyboard so left and right arrow keys work now

while gameOver == False:
    if basic_attack == False:
        player.draw()
        #pass
    else:
        player.drawAttack()
        #pass
    if voiceOn == True:
        voice.draw()
    enemy1.draw()
    enemy2.draw()
    if turnOffEnemy3 == False:
        enemy3.draw()
    bars.draw()
    #sword.draw() #Incomplete
    if pressQ == True:
        sword.drawEye()
    #nathaniel2010.draw() #Incomplete
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
