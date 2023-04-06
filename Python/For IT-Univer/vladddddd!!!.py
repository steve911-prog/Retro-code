from tkinter import *
root = Tk()

def click_but(event):
        but['bg'] = 'lightblue'


but = Button(text = 'ok', bg = 'red' , fg = 'yellow', font = 'Arial 51')
but.pack()
but.bind('<Button - 1>',click_but )

canv = Canvas(width = 500, height = 500, bg = 'white')
canv.pack()

canv.create_rectangle([30,40],[140,140], fill = 'red', outline = 'grey20',width = 3)

canv.create_oval([30,40],[140,140], fill = 'yellow', outline = 'blue',width = 3)


canv.create_polygon([250,25],[50,40],[450,400],[29,10],[76,100], fill = 'yellow', outline = 'blue')
root.mainloop()
