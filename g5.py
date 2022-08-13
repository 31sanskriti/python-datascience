import pgzrun 
from random import randint 


HEIGHT = 500
WIDTH = 500 
score = 0

img1 = Actor('character_0026', pos =(WIDTH //2, HEIGHT//2))
img2 = Actor('character_0020',  pos = (50,50))
speed = 3

# music.play('bgmusic')

def draw():
    screen.fill('black')
    img1.draw()
    img2.draw()
    screen.draw.text(f'SCORE :{score}', topleft = (10,500-30), color= 'white')

def update():
    global score #global varible
    #movement control 
    if keyboard.left:
        img1.x -= speed 
    if keyboard . right:
        img1.x += speed
    if keyboard. up :
        img1.y -= speed 
    if keyboard .down :
        img1.y += speed
        
    #boundary control
    if img1.x > WIDTH :
        img1 .x = 0
    if img1.x < 0 :
        img1.x = WIDTH 
    if img1.y > HEIGHT :
        img1.y = 0
    #collision control
    if img1.colliderect(img2):
        score += 1
        img2.x = randint(0,WIDTH)
        img2.y = randint(0, HEIGHT)
        sounds.sound1.play()

pgzrun.go()            



        