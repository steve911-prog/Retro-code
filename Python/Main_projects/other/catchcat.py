from  tkinter import   *
import random 
tk = Tk()

tk.title('Catchcat')
cat = PhotoImage( file = 'cat.gif') 
cat = cat.subsample(5, 6)
snow = PhotoImage(file =  'Снег5.gif') 
clicks = 0
misses = 0
lab = Label(text = 'Caught {} times, miss {} times'.format(clicks, misses))
lab.grid(columnspan = 3, row = 4)
def click(event):
     global clicks, misses
     misses += 0
     clicks += 1
     lab['text'] = 'Caught {} times, miss {} times'.format(clicks,misses)
def miss(event):
     global misses, clicks
     misses += 1
     clicks += 0 
     lab['text'] = 'Caught {} times, miss {} times'.format(clicks, misses )
def run():
    but_cat.grid(column = random.randrange(3), row =  random.randrange(3))
    but_cat.after(800, run)

for i in range(3):
    for j in range(3):
        but_snow = Button(image = snow)
        but_snow.grid(column = i , row = j)
        but_snow.bind('<1>', miss)

but_cat = Button(image = cat)
but_cat.bind('<1>', click)
but_cat.grid(column = 1, row = 1)
run()




tk.mainloop()
