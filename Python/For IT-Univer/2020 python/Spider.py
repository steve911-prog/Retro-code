from tkinter import *

##from random import choice
##from random import randrange as rr
from random import choice, randrange as rr

class Spider:   #() neobyazatelno
    def __init__(self, x, y = 0): #!!!
        self.image = PhotoImage(file = 'spider2.png').subsample(rr(5, 20), rr(5, 20)) #umenshaet
        self.color = choice(colors)
        self.speed = rr(1,7)
        self.x = x
        self.y = y
        self.start_x = x
        self.start_y = y

        self.line = canva.create_line([self.start_x, self.start_y], [self.x, self.y], fill = self.color)

        self.img = canva.create_image(x, y, image = self.image)

    def move(self):
        self.y += self.speed
        canva.move(self.img, 0, self.speed)    
        canva.coords(self.line,self.start_x, self.start_y, self.x, self.y)
        if self.y >= 500:
            self.y = 10
            self.x = rr(500)
            canva.coords(self.img,self.x, self.y)
            self.start_y = 0
            self.start_x = self.x


#dz
def clear(event):
    global spiders
    canva.delete('all')
    #spiders = []
    spiders.clear()

def new_spider(event):
    spider = Spider(event.x, event.y)
    spiders.append(spider)

def draw():
    for i in spiders:
        i.move()
    canva.after(rr(30, 500), draw)

# Д/З: заполнить список цветов (минимум 10)
colors = ['green','yellow', 'blue', 'brown', 'gray', 'white', 'black', 'purple', 'pink', 'orange','lightblue','red']

root = Tk()
canva = Canvas(width = 500, height = 500, bg = "black")
canva.pack()
spiders = []
canva.bind('<B1-Motion>', new_spider)




    
    

lab = Label(text = "Кликай по экрану", fg = "red")
lab.pack()

but = Button(text = "ОЧИСТИТЬ")
but.pack()
but.bind('<1>', clear)

draw()

root.mainloop()
