from tkinter import  *
from random import choice

tk = Tk()
canv = Canvas(width = 500, height = 500, bg = 'white')
canv.pack()

list_color = ['red','darkred','cyan', 'blue','pink','orange','green','brown','yellow','lime','black','lightgreen','lightyellow']
list_br = []
list_eyes = []
list_mouth = []
for i in range(1,17):
    im_br_file = 'br' + str(i) + '.png'
    im_br = PhotoImage(file = im_br_file )
    list_br.append(im_br)
for eyes in range(1,12):
    im_eyes_file = 'eyes' + str(eyes) + '.png'
    im_eyes = PhotoImage(file = im_eyes_file )
    list_eyes.append(im_eyes)
for mouth in range(10,29):
    im_mouth_file = 'mouth' + str(mouth) + '.png'
    im_mouth= PhotoImage(file = im_mouth_file )
    list_mouth.append(im_mouth)
def click_br(event):
    canv.itemconfig(br, image = choice(list_br))
def click_eyes(event):
    canv.itemconfig(eyes, image = choice(list_eyes))
def click_mouth(event):
    canv.itemconfig(mouth, image = choice(list_mouth))  
def click_color(event):
    canv.itemconfig(circle, fill = choice(list_color))  


circle = canv.create_oval(0,0,500,500 ,fill = choice(list_color))
br = canv.create_image(250,90 ,image = choice(list_br))
eyes = canv.create_image(250,200 ,image = choice(list_eyes))
mouth = canv.create_image(250,350 ,image = choice(list_mouth))
canv.tag_bind(br,'<1>',click_br)
canv.tag_bind(eyes,'<1>',click_eyes)
canv.tag_bind(mouth,'<1>',click_mouth)
canv.tag_bind(circle,'<1>',click_color)                       

tk.mainloop()
