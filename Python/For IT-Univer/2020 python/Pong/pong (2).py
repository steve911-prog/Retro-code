from tkinter import *
from random import *
from time import sleep
class Ball:
    def __init__(self, canvas, color):                                  
        self.canvas = canvas
        #id - имя, по которому  можно будет обращаться к экземляру
        self.id = canvas.create_oval(100,100,125,125, fill = color,\
                                     outline = color)
        self.x = choice([-3, -2, -1, 1, 2, 3])  #скорость по х
        self.y = 3  #скорость по у
        self.canvas_height = self.canvas.winfo_height()  
        self.canvas_width = self.canvas.winfo_width()    

    def motion(self):  
        self.canvas.move(self.id, self.x, self.y) #двигает себя (self.id)
        #считываем текущие координаты экземпляра
        #pos - список из 4 значений [x1, y1, x2, y2](координаты шарика)
        pos = self.canvas.coords(self.id)
        
        #abs - модуль числа 
        if pos[0] <= 0:
            self.x = abs(self.x)
        if pos[1] <= 0:
            self.y = abs(self.y)
            
     
        if pos[2] >= self.canvas_width:
            self.x = - abs(self.x)

        if pos[3] >= self.canvas_height:
            self.y = - abs(self.y)
            

    def move(self):
        self.x or self.y - 1 or self.x or self.y - 1
        

        

root = Tk()
root.title("Ping-pong") 
canv = Canvas(root, width = 500, height = 400, bg = "cyan")
canv.pack()
root.update() 
ball = Ball(canv,"green")
while True:
    ball.motion()
    c = 0.01
    sleep(c)    
    root.update()
    c += 0.00000000001

root.mainloop()
