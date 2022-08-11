import pgzrun  #library import

height = 500
width = 800

box = Rect((50,50), (100,100))
box2 = Rect((450,50), (100,100))

def draw():
    screen.fill('white')
    screen.draw.rect(box , 'red')
    screen.draw.rect(box2 , 'blue')

def update():
    box.x += 1
    if box.x > width :
        box.x = 0 

    box2.x += -3
    if box.x < 0 :
        box.x = width

    if box2 .colliderect(box):
        print("collision")    
        box.x += 4
    


pgzrun.go()