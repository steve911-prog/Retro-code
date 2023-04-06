from  random import *
from tkinter import *
#金 - золото по японски
tk = Tk()
tk.title('Py_Math')
tk.geometry('1100x1100')
r1 = randrange(2, 10)
r2 = ['*','/','-','+']
r3 = randrange(2, 10)
instance_rand = str(r1) + str(choice(r2))+ str(r3)
evir = str(eval(instance_rand))


#attempts = 0
def check(event):
        global  evir
        answer = float(entry.get())
        entry.delete(0, END)
        if choice(r2) == '/' and  r3 < r1:
                instance_rand = str(r3) + str(choice(r2))+ str(r1)
        if answer  !=  float(evir):
            result['text'] = 'Answer is incorrect! :('
            result['bg'] = 'red'
        else: 
            result['text'] = 'Excellent'
            result['bg'] = 'green'
            score += 1
        question += 1
        r1 = randrange(2, 10)
        r2 = ['*','/','-','+']
        r3 = randrange(2, 10)
        instance_rand = str(r1) + str(choice(r2))+ str(r3)
        evir = str(eval(instance_rand))        
        lab_instance['text'] = instance_rand
#widgets
lab1 = Label(tk, text = ' Я загадал пример пример. \n Если ты правильно решишь,  \n тебе + 1 балл.\n Вот пример:' ,
             font = 'Adobe 35', fg = 'blue')
lab1.place(x = 240, y = 40 )
entry = Entry(tk, background = 'black', font = 'Arial 13', fg = 'white', width = 30, borderwidth = 15 )
entry.place(x = 418,y =  310)
#inputs = str(input())



#if choice(r2) == '/' and  r3 < r1:
        #instance_rand = str(r3) + str(choice(r2))+ str(r2)
question, score = 0,0

lab_instance = Label(tk, text = instance_rand , font = 'Arial 30')
lab_instance.place(x = 540,y = 250)
result = Label(tk, text = ' ', font = 'Arial 25')
result.place(x= 430,y = 480)
lab = Label(tk, text =  '{}/{}'.format(question, score) , font = 'Arial 20', fg = 'darkgreen')
lab.place(x = 547, y = 365)

btn = Button(tk, text = 'CHECK', font = "Arial 22")
btn.bind('<1>' ,check)
btn.place(x = 505, y = 410)

tk.mainloop()

'''
scroll_y = Scrollbar(tk, orient="vertical", command= hello)
scroll_y.pack(fill='y', side='right)                           
#алгоритм(ы)

answer = int(en.get())
en.delete(0, END)

elif  ValueError ==  " invalid literal for int() with base 10: '' ":
            result['text'] = 'Entry answer and then press "CHECK"'
            result['bg'] = 'red'
'''

   

