from tkinter import *
list_animals = ['monkey', 'rooster', 'dog', 'pig','rat','ox', 'tiger', 'rabbit', 'dragon', 'snake','horse', 'sheep',]
list_colors = ['white',' white','blue', 'blue', 'green', 'green', 'red', 'red', 'yellow', 'yellow',]
list_img=[]


root = Tk()


def check(event):
    canv.delete("all")
    year = int(ent.get())
    ind_anim = year % 12
    ind_col = year % 10
    canv["bg"] = list_colors[ind_col]
    canv.create_image(250, 250, image = list_img[ind_anim])
    canv.create_text(400, 400, text = list_colors[ind_col] +" "+ list_animals[ind_anim], font = 'sans 15')
for el in list_animals:
    list_img.append(PhotoImage(file = "%s.png" % el))





    
canv = Canvas(root, width = 500, height = 500)
canv.pack()

ent = Entry(root, width = 30)
ent.pack()

but = Button(root, text = "Entry the year...")
but.pack()

but.bind("<1>", check)












root.mainloop()
