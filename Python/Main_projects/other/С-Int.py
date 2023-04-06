from tkinter import *
tk = Tk()
tk.geometry('410x420')
tk.title('СaInt')
time = 0
attempts = 0
correct = 0
run = True
def start():
      global run
      run = True
      but1['state'] = 'disabled'
      but2['state'] = 'normal'
      tick()
      lab_points['text'] = '0/0'
      lab_taymer['text'] = '0.0'
def reset():
      global run
      run = False
      #global  correct, time, attempts
      lab_points['text'] = '0/0'
      lab_taymer['text'] = '0.0'
      but1['state'] = 'normal'
def tick():
      global time, run
      time += 1
      tt = str(time // 10) + '.' + str(time % 10)
      lab_taymer['text'] = tt
      if run :
            tk.after(100,tick)

      '''def reset():
            tk.after(100, tick)
            break'''
def stop():
      global correct, attempts, tick , run
      run = False
      attempts += 1
      but2['state'] = 'disabled'
      but1['state'] = 'normal'
      
      if time % 10 == 0:
          correct += 1 
      lab_points['text'] = str(correct) + '/' + str(attempts)    
def pas():
      pass

lab_taymer = Label(tk, text = '0.0', font = 'Helvetica 15', width = 6, height = 2)
lab_taymer.pack()
lab_taymer.place(x = 160, y = 25)
lab_points = Label(tk, text = str(correct) +'/' + str(attempts), font = 'Helvetica 15', width = 6, height = 2)
lab_points.pack()
lab_points.place(x = 160, y = 80)
but1 = Button(tk, text = 'Start', command = start ,font = 'Helvetica 15', width = 10, height = 3, bg = 'green')
but1.place(x = 135, y = 140)
but2 = Button(tk, text = 'Stop', command = stop,font = 'Helvetica 15', width = 10, height = 3, bg = 'red')
but2.place(x = 135, y = 230)
but3 = Button(tk, text = 'Reset',font = 'Helvetica 15', command = reset, width = 10, height = 3, bg = 'white')
but3.place(x = 135, y = 318)
# Random elem in list:
#    a = [5,6,7]
#random.chice(a)
#1
'''
c = 10
id(c)
11234490908893

