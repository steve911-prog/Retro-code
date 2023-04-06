# Pygame шаблон - скелет нового проекта Pygame
import pygame

w = 360   #ширина игрового окна
h = 480  #высота игрового окна
FPS = 30      #частота кадров в секунду
speed = 5
x = 100
y = 100
w_pl = 50
h_pl = 50

#colors

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)




#создаём игру и окно
pygame.init()  #программа которая запускает pygame
pygame.mixer.init() #для звука

#окно программы
#которое создаёться, когда мы задаём его размер в настройках
screen = pygame.display.set_mode((w,h))

#заглавие окна (title)
pygame.display.set_caption("My game")

#строка для проверки, что программа работает
# с заданной частотой кадров
clock = pygame.time.Clock()
#all_sprites = pygame.split.Group()

class Player(pygame.sprite.Sprite):
    pass


#Цикл игры
running = True
while running:
    clock.tick(FPS)

    #Ввод процеса (события)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed 
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed 
    if keys[pygame.K_DOWN]:
        y += speed         
    if x == w- w_pl:
        x -= speed
    elif x == 0:
        x += speed
    elif y == h - h_pl:
        y -= speed
    elif y == 0:
        y += speed
    #Обновление
    #all_sprites.update()
    #all_sprites.draw(screen)
    
    #Визуализация (сборка)
    # Randing
    screen.fill(black) # fill the screen
    pygame.draw.rect(screen, blue, (x,y,w_pl, h_pl))
     
    # another screen
    pygame.display.flip()
    

pygame.quit()
    
