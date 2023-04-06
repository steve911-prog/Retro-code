from tkinter import *
from random import choice
tk = Tk()

cnvs = Canvas(tk, width = 600, height = 600, bg  = '#BDFF41')
cnvs.pack()

w1 = 40
h1 = 15

w2 = w1
h2 = 55

for i in range(1000):
    color_list = ['red', 'white', 'blue', 'green', 'yellow']
    cnvs.create_line(w1, h1, w2, h2, fill = choice(color_list))

    w1 += 10
    w2 = w1

    h2 += 15
