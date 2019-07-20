from tkinter import *
import random
import time

counter = 0 #We use these counter
counter1 = 0

tk = Tk()
tk.title("Pong!")
tk.resizable(0,0) #Cannot resize window because it would mess up the game size.
tk.wm_attributes("-topmost", 1) #
canvas = Canvas(tk, width = 500, height = 400, bd = 0, highlightthickness = 0)
canvas.config(bg = "black") #Background is black
canvas.pack()
tk.update()

canvas.create_line(250,0,250,400,fill = "white")

class Ball:
    def __init__(self,canvas,paddle,paddle1,color):
        self.canvas = canvas
        self.paddle = paddle
        self.paddle1 = paddle1
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,233,200)
        starts = [-3,3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = 500
        self.counter = 0 #I think we don't use these two counters
        self.counter1 = 0

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[0] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                return True
            return False

    def hit_paddle1(self,pos):
        paddle_pos = self.canvas.coords(self.paddle1.id)
        if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[2] >= paddle_pos[0] and pos[2] <= paddle_pos[2]:
                return True
            return False

    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
            self.score(False)
        if pos[2] >= self.canvas_width:
            self.x = -3
            self.score(True)
        if self.hit_paddle(pos) == True:
            self.x = 3
        if self.hit_paddle1(pos) == True:
            self.x = -3

    def score(self,val):
        global counter
        global counter1

        if val == True:
            a = self.canvas.create_text(125, 40, text = counter, font = ("Arial",60),fill = "white")
            canvas.itemconfig(a,fill = "black")
            counter +=1
            a = self.canvas.create_text(125, 40, text = counter, font = ("Arial",60),fill = "white")

        if val == False:
            a = self.canvas.create_text(375, 40, text = counter1, font = ("Arial",60),fill = "white")
            canvas.itemconfig(a,fill = "black")
            counter1 +=1
            a = self.canvas.create_text(375, 40, text = counter1, font = ("Arial",60),fill = "white")
            
class Paddle: #Left paddle
    def __init__(self, canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,150,30,250,fill=color)
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('w',self.turn_left)
        self.canvas.bind_all('s',self.turn_right)

    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= 400:
            self.y = 0
    def turn_left(self,evt):
        self.y = -3

    def turn_right(self,evt):
        self.y = 3

class Paddle1: #Right paddle
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(470,150,500,250, fill=color)
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Up>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Down>',self.turn_right)

    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= 400:
            self.y = 0
            
    def turn_left(self,evt):
        self.y = -3

    def turn_right(self,evt):
        self.y = 3

paddle = Paddle(canvas, "blue")
paddle1 = Paddle1(canvas, "red")
ball = Ball(canvas, paddle, paddle1, "orange")

while 1:
    ball.draw()
    paddle.draw()
    paddle1.draw()

    if counter == 10: #Red player wins at score 10
        ball.x = 0
        ball.y = 0
        paddle.y = 0
        paddle1.y = 0
        canvas.create_text(250,200,text = "Congrats Player Red! You Win!", font = 32, fill = "red")
        canvas.create_text(250,215,text = "Score: " + str(counter) + "- " + str(counter1), font = 32, fill = "red")

    if counter1 == 10: #Blue player wins at score 10
        ball.x = 0
        ball.y = 0
        paddle.y = 0
        paddle1.y = 0
        canvas.create_text(250,200,text = "Congrats Player Blue! You Win!", font = 32, fill = "red")
        canvas.create_text(250,215,text = "Score: " + str(counter) + "- " + str(counter1), font = 32, fill = "red")

    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

    if counter == 10 or counter1 == 10: #If the game ended, makes the shapes still.
        time.sleep(60)
