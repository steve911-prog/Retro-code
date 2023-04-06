import pygame as pg

width = 500
height = 400
FPS = 30

speed = 5
x = 50
y = 50
r = 30

is_jump = False
jump_count = 10 #чесно говоря, не знаю для чего это переменная, как тлько пойму, смогу обьяснить все остальные команды , с ней связанные

#color RGB
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)

pg.init()
screen = pg.display.set_mode((width,height))
pg.display.set_caption("My game")

clock = pg.time.Clock()

running = True
while running:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
##        elif event.type == pg.KEYDOWN:
##            if event.key == pg.K_RIGHT:
##                x += speed

    keys = pg.key.get_pressed()
    if keys[pg.K_RIGHT] and x < width - r - 5:
        x += speed
    if keys[pg.K_LEFT] and x > r + 5:
        x -= speed

    if not(is_jump):
        if keys[pg.K_UP] and y > r + 5:
            y -= speed
        if keys[pg.K_DOWN] and y < height - r - 15: # проверка мяча что-бы он не заходил за экран
            y += speed

        if keys[pg.K_SPACE]: # условие,  которое проверяет нажатие пробела
            is_jump = True
    else:
        if jump_count >= -10:
            if jump_count > 0:
                y -= (jump_count ** 2) / 2
            else:
                y += (jump_count ** 2) / 2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10
        
    screen.fill(black)
    pg.draw.circle(screen, green, (x,int(y)),r) #айдл выводил ошибку с флоат



    pg.display.flip() # переворчиавние экрана
    

pg.quit()
