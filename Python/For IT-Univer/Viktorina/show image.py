from tkinter import *
from random import *
tk  = Tk()
W = 500
H = 334
color = ['white','blue','yellow','green', 'red','gold','silver','cyan','purple']
def coords(event):
    col = event.x // (W // 3)
    row = event.y // (H // 3)
    question =  row * 3 + col
    for rect in rects:
        canvas.itemconfig(rect, fill = choice(color))
    item = canvas.find_closest(event.x,event.y)
    if canvas.type(item) == 'rectangle':
        canvas.itemconfig(item, fill = 'lightblue')
    en.delete(0, END) 
    en.config(fg = 'black', font = "Arial 20")
        
def compare(event):
    if en.get() == answers[question]:
        canvas.delete(rects[question])
        canvas.delete(text[question])
    
canvas = Canvas(tk, width = W, height = H)
canvas.grid(row = 5, column = 6)
canvas.bind('<1>', coords)
en = Entry(tk)
en.grid(row = 6, column = 6)
en.bind("<Return>", compare)
tasks = ["(2 + 9)* 5",\
         "7 * 8 + 13",\
         "3 * 6",\
         "42 // 6", \
         "12 // 3  \n+ 5",\
         "35 // 7", \
         "32 // 4",\
         "4 ** 3",\
         "64 // 8 * 3"]


answers = ["55","69","18","7","9","5","8","64","24"]


    

bridge = PhotoImage(file = "picsart.png").subsample(2)#загружаем изображение
canvas.create_image((W // 2,H // 2), image = bridge)#выводим изображение на холст
w = W // 3
h = H // 3

rects = []
texts = []

for j in range(3):
    for i in range(3):
        left_topX = w * i
        left_topY = h * j
        right_bottomX = w * i + w
        right_bottomY = h * j + h        
        rect = canvas.create_rectangle(left_topX, left_topY,
                                right_bottomX, right_bottomY,
                                fill = 'white')
        text = canvas.create_text(left_topX + w//2, left_topY + h // 2,
                           text = tasks[j * 3 + i])
        rects.append(rect)
        texts.append(text)        
tk.mainloop()       














'''from tkinter import *
tk  = Tk()
w,h  = 500,334
canvas = Canvas(tk, width = w, height = h)
canvas.grid(row = 5, column = 6)

tasks = ["(2 + 9)* 5",\
         "7 * 8 + 13",\
         "3 * 6",\
         "42 // 6", \
         "12 // 3  \n+ 5",\
         "35 // 7", \
         "32 // 4",\
         "4 ** 3",\
         "64 // 8 * 3"]


answers = ["55","69","18","7","9","5","8","64","24"]





robot = PhotoImage(file = 'robot')
canvas.create_image((w // 2 , h // 2), image = robot)
canvas.create_text(left_topX + W // 6, left_topY + H // 6,/
                         text = tasks[j*3 + i])

tk.mainloop()
'''
