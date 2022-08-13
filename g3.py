import pgzrun 

height = 500 
width = 500

img1 = Actor('character_0018', pos = (200,200))
img2 = Actor('character_0019' , topright = (60,60))
img3 = Actor ('character_0020' , topleft = (70,70))
img4 = Actor ('character_0021' , center = (40,40 ))
img5 = Actor ('character_0022' , pos = (300 ,300))


def draw ():
  screen.fill('white')
  img1.draw()
  img2.draw()
  img3.draw()
  img4.draw()
  img5.draw() 

def update():
    img1.y += 1 
    if img1. y >height :
       img1. y = 0 

def update ():
  img2.x += 5
  if img2.x > height :
    img3.x = 0



pgzrun.go()



