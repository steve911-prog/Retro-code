#Я закоментировал некоторые строки, потому-что их не было в коспекте , и так вышло 



from tkinter import *
from random import *
from time import sleep


w,h = 500,400


class Ball:
    def __init__(self, canvas, color, size):                                  

        self.size = size
        
        self.canvas = canvas
        
        self.id = canvas.create_oval(100,100,100+size,100 + size , fill = color,\
                                     outline = color)
        self.x = choice([-3, -2, -1, 1, 2, 3])  #скорость по х
        self.y = 3  #скорость по у
        self.canvas_height = self.canvas.winfo_height()  
        self.canvas_width = self.canvas.winfo_width()    

        #pos = self.canvas.coords(self.id)

        #paddle_a_pos = self.canvas.coords(padlet_above.id)
        #paddle_b_pos = self.canvas.coords(padlet_below.id)
        #self.center_posX = pos[0] + (pos[2]- pos[0]) // 2
        #self.center_posY = pos[1] + (pos[3]- pos[1]) // 2

    def touch_up(self, pos, paddle_a_pos, paddle_b_pos):
        if self.y < 0:
            if paddle_a_pos[3] >= pos[1] >= paddle_a_pos[1]:
                if paddle_a_pos[0] <= self.center_posX <= paddle_a_pos[2]:
                    return True
            if paddle_b_pos[3] >= pos[1] >= paddle_b_pos[1]:
                if paddle_b_pos[0] <= self.center_posX <= paddle_b_pos[2]:
                    return True
        return False

    def touch_down(self, pos, paddle_a_pos, paddle_b_pos):
        if self.y > 0:
            if paddle_a_pos[3] >= pos[3] >= paddle_a_pos[1]:
                if paddle_a_pos[0] <= self.center_posX <= paddle_a_pos[2]:
                    return True
            if paddle_b_pos[3] >= pos[3] >= paddle_b_pos[1]:
                if paddle_b_pos[0] <= self.center_posX <= paddle_b_pos[2]:
                    return True
        return False
    def touch_left(self, pos, paddle_a_pos, paddle_b_pos):
        if self.x < 0:
            if 0 <= pos[0] - paddle_a_pos[2] <= 3:
                if paddle_a_pos[1] <= self.center_posY <= paddle_a_pos[3]:
                    return True
            if 0 <= pos[0] - paddle_b_pos[2] <= 3:
                if paddle_b_pos[1] <= self.center_posY <= paddle_b_pos[3]:
                    return True
        return False
   
                   
    def touch_right(self, pos, paddle_a_pos, paddle_b_pos):
        if self.x > 0:
            if 0 <= pos[2] - paddle_a_pos[0] <= 3:
                if paddle_a_pos[1] <= self.center_posY <= paddle_a_pos[3]:
                    return True
            if 0 <= pos[2] - paddle_b_pos[0] <= 3:
                if paddle_b_pos[1] <= self.center_posY <= paddle_b_pos[3]:
                    return True
        return False
        
                      
    

    def motion(self):  
        self.canvas.move(self.id, self.x, self.y) #двигает себя (self.id)
        #считываем текущие координаты экземпляра
        #pos - список из 4 значений [x1, y1, x2, y2](координаты шарика)
        pos = self.canvas.coords(self.id)

        paddle_a_pos = self.canvas.coords(padlet_above.id)
        paddle_b_pos = self.canvas.coords(padlet_below.id)
        self.center_pos_x = pos[0] + (pos[2]- pos[0]) // 2
        self.center_pos_x = pos[1] + (pos[3]- pos[1]) // 2

        #abs - модуль числа 
        if pos[1] <= 0 or self.touch_up(pos, paddle_a_pos, paddle_b_pos):
            self.y = - self.y
            if pos[1] <= 0:
                lab_up['text'] = str(int(lab_up['text']) + 1)
        elif pos[3] >= self.canvas_height or self.touch_down(pos, paddle_a_pos, paddle_b_pos):
            self.y = - self.y
            if pos[3] >= self.canvas_height:
                lab_down['text'] = str(int(lab_down['text']) + 1)
            
     
        elif pos[2] >= self.canvas_width or self.touch_right(pos, paddle_a_pos, paddle_b_pos):
            self.x = - self.x

        elif pos[0] <= 0 or self.touch_left(pos, paddle_a_pos, paddle_b_pos):
            self.x = - self.x
            

    #def move(self):
        #self.x or self.y - 1 or self.x or self.y - 1
        
class Paddlet:
    def __init__(self, canvas, where, color, key_left, key_right): # TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
        self.canvas = canvas
        self.x = 0
        self.canvas_height = self.canvas.winfo_height()  
        self.canvas_width = self.canvas.winfo_width()    
        #pp = 4 if where == 'below' else 1
        #pos = [self.canvas.winfo_width() // 2 - 50,
         #      self.canvas.winfo_height()  // 5 * pp - 5 ,
          #     self.canvas.winfo_width() // 2 + 50,
           #    self.canvas.winfo_height()  // 5 * pp + 5]

        pos = [201, 315, 301, 325] if where == 'below' else [201, 75, 301, 85]
        print(pos)
        self.id = canvas.create_rectangle(pos, fill = color, outline = color)
        self.key_left = '<' +key_left + '>'
        self.key_right = '<' + key_right + '>'
        print(self.key_left, self.key_right)
        self.canvas.bind_all(self.key_left, self.turn_left)
        self.canvas.bind_all(self.key_right, self.turn_right)

    def turn_left(self, event):
        self.x = -2.5
      
    def turn_right(self, event):
        self.x = 2.5

    def motion(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)

        if pos[0]<= 0:
            self.x  = 0
        if pos[2] >= self.canvas_width:
            self.x = 0


root = Tk()
root.title("Ping-pong") 
root.resizable(0,0)

count_up = 0
count_down = 0


lab_up = Label(root, text = '0', font = 'Arial 20')
lab_up.pack(side = 'top')
#lab_up.place(x = w + 90 , y = 0)

lab_down = Label(root, text = '0', font = 'Arial 20')
lab_down.pack(side = 'bottom')

canv = Canvas(root, width = 500, height = 400, bg = "cyan")
canv.pack()

padlet_below = Paddlet(canv,'below','green', "Left", 'Right')
padlet_above = Paddlet(canv,'above','green', "a", 'd')

root.update() 
ball = Ball(canv,"green", 25)



while True:
    ball.motion()
    padlet_below.motion()
    padlet_above.motion()
    c = 0.01
    sleep(c)    
    root.update()
    c += 0.00000000005

root.mainloop()
