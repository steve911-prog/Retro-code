from tkinter import *
from random import choice

w, h = 500, 400

class Ball:
    #конструктор (функция) инициализации
    #через self. объявляются собственные переменные
    def __init__(self, canvas, color, size):
        self.size = size
        self.canvas = canvas
        #id - имя, по которому  можно будет обращаться к экземляру
        self.id = canvas.create_oval(100,100,100 + size,100 + size,\
                                     fill = color, outline = color)
        self.x = choice([-3, -2, -1, 1, 2, 3])  #скорость по х
        self.y = 3  #скорость по у
        self.canvas_height = self.canvas.winfo_height()  #высота холста
        self.canvas_width = self.canvas.winfo_width()    #ширина холста

class Paddlet:
    def __init__(self, canvas, where, color, key_left, key_right):
        self.canvas = canvas
        self.x = 0
        self.canvas_height = self.canvas.winfo_height()  #высота холста
        self.canvas_width = self.canvas.winfo_width()    #ширина холста
        pp  = 4 if where == "below" else 1
        print(pp)
        pos = [self.canvas.winfo_width() // 2 + 50 * 4 , self.canvas.winfo_height() // 5 * pp + 35,\
               self.canvas.winfo_width() // 2 + 50 * 5 + 50, self.canvas.winfo_height() // 5 * pp + 50]
        print(pos)
        self.id = canvas.create_rectangle(pos, fill = color, outline = color)
        self.key_left = "<" + key_left + ">"
        self.key_right = "<" + key_right + ">"
        self.canvas.bind_all(self.key_left, self.turn_left)
        self.canvas.bind_all(self.key_right, self.turn_right)

        

    def turn_left(self, event):
        self.x = -2
    def turn_right(self, event):
        self.x = 2

    def motion(self):
        self.canvas_move(self.id, self.x, 6)
        #pos = 


root = Tk()
root.title("Ping-pong") #заглавие окна

#счёт верхнего (синего) игрока
lab_up = Label(root, text = "0", fg = "blue", font = "Times 20 bold")
#lab_up.place(x = w / 2, y = 0)   #расположение объекта
#.pack(side = TOP())     #особенности метода pack в расположении
lab_up.pack()

canv = Canvas(root, width = w, height = h, bg = "cyan")
canv.pack()

#счёт нижнего (зелёного) игрока
lab_down = Label(root, text = "0", fg = "green", font = "Times 20 bold")
lab_down.pack()


padlet_below = Paddlet(canv, "below", "green", 'Button-1', 'Button-3')

padlet_up = Paddlet(canv, "up", "red", 'a', 'd')

root.update() #принудительное обновление состояния окна root
#ball - экземпляр класса Ball
ball = Ball(canv,"green",25)
while True:      #бесконечный цикл
    ball.motion()
    time.sleep(0.01)  #задержка во время перезапуска программы
                         #в бесконечном цикле (для корректной работы)
    root.update()
root.mainloop()
