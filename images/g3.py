import pgzrun 

height = 500 
width = 500

thumb = Actor('thumb1', pos = (200,200))

def draw ():
    screen.clear()
    thumb.draw()

def update():
    thumb.y += 1 
    if thumb. y >height :
        thumb. y = 0 

pgzrun.go()



