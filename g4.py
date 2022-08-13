import pgzrun 

HEIGHT = 500
WIDTH = 500 

img1 = Actor('character_0026', topleft =(50,50))
img2 = Actor('character_0024', pos=(300,300))
speed = 3
def draw():
    screen.fill('black')
    img1.draw()
    img2.draw()

def update():
    img1.x +=1
    if img1.x> WIDTH:
        img1.x = 0

    if keyboard.left:
        img2.x-= speed
    if keyboard.right:
        img2.x += speed
    if keyboard.up:
        img2.y -= speed
    if keyboard.down:
        img2.y += speed 
    if img2.colliderect(img1):
        sounds.sound1.play()

pgzrun.go()        
            
    

           