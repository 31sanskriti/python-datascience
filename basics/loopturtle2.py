from turtle import *

speed = (-10)
sides = 6
distance = 120
fillcolor('purple')
begin_fill()



for i in range(sides):
    forward (distance)
    left(360/sides)

end_fill()


mainloop()



