from turtle import *
speed (0)
pencolor('red')
bgcolor('black')
fillcolor('pink')
begin_fill()
for i in range (8):
    forward(150)
    left(360/8)

    for i in range (8):
        forward(40)
        left(360/8)
       
        for i in range (8):
          forward(50)
          left(360/8)

end_fill()

mainloop()