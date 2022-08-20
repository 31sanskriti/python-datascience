from turtle import *
speed (0)
pencolor('red')
bgcolor('black')
fillcolor('pink')
begin_fill()
for i in range (8):
    #penup()
    forward(150)
    left(360/8)
    #pendown()
    

    for i in range (8):
        forward(40)
        left(360/8)
       
        for i in range (8):
          forward(50)
          left(360/8)
          dot (6)
          #write(i)

    

end_fill()

mainloop()