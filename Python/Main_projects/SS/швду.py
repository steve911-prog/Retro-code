from tkinter import *
tk = Tk()
lab = Label()
cnvs = Canvas(tk, width = 600, height = 600)
cnvs.pack()
animal_list = ['monkey','rooster', 'dog','pig','rat','ox','tiger','rabbit','dragon','snake','horse',
               'sheep', ]
color_list = [ 'white', 'white',
              'blue','blue', 'green', 'green','red','red', 'yellow', 'yellow']
list_img = []
entr = Entry(tk, width = 30)
entr.pack()
def check(event):
    cnvs.delete('all')
    year = int(entry.get())
    index_anim = year % 12
    ind_col = year % 10
    cnvs['bg'] = color_list[ind_col]
    cnvs.create_image(250, 250, image = list_img)
    cnvs.create_text(300, 500, text = color_list[ind % el] + animal_list[index_anim], font = 'sans 60')
for el in animal_list:
    list_img.append(PhotoImage(file = '%s.png'  % el))


btn = Button(tk, text = 'Peint year',command = check)
btn.pack()
btn.bind('<1>', check)


tk.mainloop()
#
