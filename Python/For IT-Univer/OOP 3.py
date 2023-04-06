from tkinter import *

delt = 0 # Переменная отвечающая за цвет
steps = 0 # Переменная отвечающая за шаги (рисование линий)

class Numbers():
    def __init__(self, num):
        self.num = num
        self.delt = 0
        self.steps = 0

    def count(self):
        pass

    # Функция для рисования линии
    def draw(num, step, delta):
        cnvs.create_line((num, 0), (num, step), fill = "#" + \
                         hex(delta // 65)[2:].zfill(3))

# Функция для определения оттенка цета и длины диаграммы
def function(x):
    global delt, steps
    steps += 1
    delt = max(delt, x)
    if x - 1 > 0.5:
        if x % 2 == 0:
            x = x // 2
        else:
            x = x * 3 + 1
        function(x)
        

tk = Tk()

cnvs = Canvas(tk, width = 500,height = 500,\
              background = '#66CDAA')
cnvs.pack()

steps_count = []
delt_count = []

# Цикл для рисования диаграммы по количеству шагов
for i in range(1000):
    function(i)
    steps_count.append(steps)
    delt_count.append(delt - i)
    draw(i, steps, delt)
    delt = 0
    steps = 0
    tk.update()
     
    
tk.mainloop()

