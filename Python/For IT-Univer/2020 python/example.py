import pygame as p#

w = 500#
h = 400#
FPS = 30#

speed = 10#
x = 50#
y = 50#
r = 30#

is_jump = False #
jump_count = 10 #

#color
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)

p.init()#

screen = p.display.set_mode((w,h))#
p.display.set_caption("My game")#

clock = p.time.Clock()#

running = True#
while running:#
    clock.tick(FPS)#

    #Ввод процеса (события)
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False
#        elif event.type == p.KEYDOWN:
 #           if event.key == p.K_RIGHT:
  #              x += speed

    key = p.key.get_pressed()#
    if key[p.K_RIGHT] and x < w: # - (r*2):#
        x += speed
    if key[p.K_LEFT] and x > 5:#
        x -= speed
    if not (is_jump):# Извините, я не понял , для чего нам нужна эта перемнная из_джамп
        if key[p.K_UP] and y > r + 5:#
            y -= speed
        if key[p.K_DOWN] and y < h - r -15:#
            y += speed    

        if key[p.K_SPACE]:#
            is_jump = True
    else:
        if jump_count >= -10: #
            if jump_count > 0:
                y += (jump_count ** 2) / 2#
            else:
                y += (jump_count ** 2) / 2
            jump_count -= 1
        else:
            pass
            
    screen.fill(black)#
    p.draw.circle(screen,green, (int(x),int(y)),int(r))#
    p.display.flip()#
p.quit()
            
