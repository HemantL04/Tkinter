from Tkinter import *
root= Tk()
canvas = Canvas(root, width = 1000, height = 1000)
canvas.pack()
canvas.create_line(0, 0, 1000, 1000)

import random
def random_rectangle(width, height):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    canvas.create_rectangle(x1, y1, x2, y2)
    
for x in range(0, 100):
	  random_rectangle(400, 400)
	  
root.mainloop()

