from Tkinter import *
import random
import time

class Ball:
	  def __init__(self, canvas, paddle, color):
	  	  self.canvas = canvas
	  	  self.paddle = paddle
	  	  self.id = canvas.create_oval(10, 10, 25, 25, fill = color)
	  	  self.canvas.move(self.id, 245, 100)
	  	  starts = [-3, -2, -1, 1, 2, 3]
	  	  random.shuffle(starts)
	  	  self.x = starts[0]
	  	  self.y = -3
	  	  self.die = 0
	  	  self.canvas_height = self.canvas.winfo_height()
	  	  self.canvas_width = self.canvas.winfo_width()
	  	  self.hit_bottom = False
	  	
	  def hit_paddle(self, pos):
	  	  paddle_pos = self.canvas.coords(self.paddle.id)
	  	  if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
	  	  	  if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
	  	  	  	  return True
	  	  return False
	  	  
	  def draw(self):
	  	  self.canvas.move(self.id, self.x, self.y)
	  	  pos = self.canvas.coords(self.id)
	  	  if pos[1] <= 0:
	  	  	  self.y = 1
	  	  if pos[1] >= self.canvas_height:
	  	  	  self.hit_bottom == True
	  	  	  self.die = 1
	  	  if pos[0] <=0:
	  	  	  self.x = 3
	  	  if pos[2] >= self.canvas_width:
	  	  	  self.x = -3
	  	  if self.hit_paddle(pos) == True:
	  	  	  self.y = -3

class Paddle:
	  def __init__(self, canvas, color):
	  	  self.canvas = canvas
	  	  self.id = canvas.create_rectangle(0, 0, 100, 10, fill = color)
	  	  self.canvas.move(self.id, 200, 300)
	  	  self.x = 0
	  	  self.flag = 0
	  	  self.canvas_width = self.canvas.winfo_width()
	  	  self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
	  	  self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
	  	  self.canvas.bind_all('<ButtonPress-1>', self.start)
	  
	  def draw(self):
	  	  self.canvas.move(self.id, self.x, 0)
	  	  pos = self.canvas.coords(self.id)
	  	  if pos[0] <= 0:
	  	  	  self.x = 0
	  	  if pos[2] >= self.canvas_width:
	  	  	  self.x = 0
	  
	  def start(self, evt):
	  	  self.flag = 1
	  
	  def turn_left(self, evt):
	  	  self.x = -2
	  
	  def turn_right(self, evt):
	  	  self.x = 2

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
a = canvas.create_text(200, 200, text = "Game over", state = 'hidden', fill = 'red', font = ('Times', 15))
tk.update()

paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')

while 1:
	  if ball.hit_bottom == False and paddle.flag == 1:	  	  
	      ball.draw()
	      paddle.draw()	  
	  if ball.die == 1:
	  	  time.sleep(1)
	  	  canvas.itemconfig(a, state = 'normal')
	  tk.update_idletasks()
	  tk.update()
	  time.sleep(0.01)