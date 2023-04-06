'''
from tkinter import *
tk = Tk()
tk.title('Title')
tk.geometry('X x Y')

label = Label(tk, text = ' Я загадал пример пример \n из таблицы умножения. \n Если ты правильно решишь,  \n тебе + 1 балл.\n Вот пример:' ,
             font = 'Adobe 26', fg = 'blue')
label.pack()
label.grid(row = 1,column = 1) /' label.place(x = , y = )

entry = Entry(tk, background = 'black', font = 'Arial 14', fg = 'white', width = 20, borderwidth = 10 )
entry.grid(row = 4, column = 1)
entry.pack()

button = Button(tk, text = 'Check')
button.bind('<1>' ,check)
button.grid(row = 1, column = 1) / button.place(x = , y = )

c = Canvas(root, width = 505, height = 101)
c.pack()
c.grid(row = 1, column = 1, rowspon = 1, columnspon = 1 ) / c.place(x = ,y =)




tk.mainloop()
'''


