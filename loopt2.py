from turtle import *

colors = ['blue','pink', 'purple']
pensize(5)

for i in range(70, 0,-1):
    pencolor(colors[i%3])
    forward(100)
    left(360/6)
    dot(i*10)
    #circle(i*10)

mainloop()