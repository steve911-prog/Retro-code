from tkinter import *
from random import *
list_elem = ['rock','spock','paper','lizard','scissors']
tk = Tk()
tk.geometry('650x650')
shemak = PhotoImage(file = 'schema.png')
lab = Label(tk, image = shemak)
lab.pack()
list_im = []
list_but = []

def click(event):
        global per_num , lab_num
        rand_elem = choice(list_elem)
        index_widget = list_elem.index(event.widget.extra)
        lab_pic.config(image = list_im[list_elem.index(rand_elem)])
        index_rand = list_elem.index(rand_elem)
        print(kompashka,rand_elem)
        if index_widget == index_rand :
                lab_result['text'] =  'Standoff'
                lab_num += 1 
                per_num += 1 
        elif (index_widget + 1) %5 == index_rand or  (index_widget) %5 + 2 == index_widget:
            kompashka['text'] = 'komp :' + str(lab_num )  
            lab_num += 1
            lab_result['text'] =  'Computer is winner'
        else:
          lab_result['text'] = 'you winner'     
          per_num += 1
          person['text'] = 'you :' + str(per_num )
#print(event.widget.config())

for el in list_elem:
        list_im.append(PhotoImage(file = '%s.png' % el))
        list_but.append(Button(tk, image = list_im[-1]))
        list_but[-1].extra = el
list_but[0].place(x = 285, y = 15)
list_but[1].place(x = 95, y = 155)
list_but[2].place(x = 410, y = 390)
list_but[3].place(x = 160, y = 390)
list_but[4].place(x = 480, y = 155)
lab_pic = Label(tk, image = None, bd = 6, bg = 'blue')
lab_pic.place( x = 290, y = 210 )
tk.bind_class('Button','<1>', click) 
lab_num = 0
per_num = 0
kompashka = Label(tk, text = 'komp : '+ str(lab_num ), font =( 'Arial 20'), fg = 'blue' )
kompashka.place (x = 40 , y = 470)
person = Label(tk, text = 'you : ' + str(per_num), font =( 'Arial 20'), fg = 'blue' )
person.place(y = 470, x = 500 )
lab_result = Label(tk, text = 'Who is winner', font = 'Helvetica 18',  )
lab_result.pack()
lab_result.place(x = 250, y = 470)


