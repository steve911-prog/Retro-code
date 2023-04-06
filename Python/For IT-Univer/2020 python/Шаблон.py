# Pygame шаблон - скелет нового проекта Pygame
import pygame

w = 360   #ширина игрового окна
h = 480  #высота игрового окна
FPS = 30      #частота кадров в секунду

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

#Цикл игры
running = True
while running:
    tick(FPS)

    #Ввод процеса (события)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
            
    #Обновление

    #Визуализация (сборка)
    # Randing
    screen.fill(black) # fill the screen

    # another screen
    pygame.display.flip()
    

pygame.quit()
    
