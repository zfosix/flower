from turtle import *

title("reinbow sprial")
speed(0)
bgcolor("black")
r,g,b=255,0,255

for i in range(300):
    colormode(255)
    if i<255//3:
        g+=3
    elif i<255*2//3:
        r-=3
    elif i<255:
        b+=3
    elif i<255*5//3:
        g-=3
    elif i <255*5//3:
        r+=3
    else:
        b-=3
    circle(175-i,90)
    lt(90)
    circle(175-i,90)
    left(18)
    pencolor(r,g,b)                           