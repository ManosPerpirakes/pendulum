from pygame import *

w = display.set_mode((1500, 750))
display.set_caption('pendulum')
x = 100
y = 300
r1 = rect.Rect(x, y, 30, 30)
close = False
clock = time.Clock()
go_left = False
counter = -25
while close != True:
    if go_left == False:
        counter += 1
    else:
        counter -= 1
    w.fill((255, 255, 255))
    draw.rect(w, (0, 0, 255), r1)
    for i in event.get():
        if i.type == QUIT:
            close = True
    if go_left == False:
        x += 25
    else:
        x -= 25
    y = (-(counter * counter)+650)
    if counter == 25:
        if go_left:
            go_left = False
        else:
            go_left = True
    if counter == -25:
        if go_left:
            go_left = False
        else:
            go_left = True
    r1.x = x
    r1.y = int(y)
    display.update()
    clock.tick(60)