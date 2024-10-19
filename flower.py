from turtle import *
import random

title("spiral bunga dengan bintang")
speed(0)
bgcolor("black")
r, g, b = 255, 0, 255

def gambar_bintang():
    penup()
    goto(random.randint(-300, 300), random.randint(-300, 300))
    pendown()
    color("white")
    dot(4)  

for _ in range(50):
    gambar_bintang()
    update()
    delay(10)

penup()
goto(0, 0)
pendown()

for i in range(300):
    colormode(255)
    if i < 255 // 3:
        g += 3
    elif i < 255 * 2 // 3:
        r -= 3
    elif i < 255:
        b += 3
    elif i < 255 * 4 // 3:
        g -= 3
    elif i < 255 * 5 // 3:
        r += 3
    else:
        b -= 3
    
    r = max(0, min(r, 255))
    g = max(0, min(g, 255))
    b = max(0, min(b, 255))
    
    circle(175 - i, 90)
    lt(90)
    circle(175 - i, 90)
    left(18)
    pencolor(r, g, b)