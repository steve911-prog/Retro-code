'''class Reptilii():
    pass

class Turtle(Reptilii):
    pass

class Crocodile(Reptilii):
    pass

class Clyvogolvi(Reptilii):
    pass

class Cheshuityati(Reptilii):
    pass

class Yasherittsi(Cheshuityati):
    pass

class Zmei(Cheshuityati):
    pass '''

from tkinter import *

delt = 0
step = 0


class Numbers():
    def __init__(self, num):
        #super(Numbers, )
        self.num = num 
        self.delt = 0
        self.steps = 0




    def count(self):
        pass

    def draw(num, step, delta):
        #cnvs.create_line()
        cnvs.create_line((num, 0),(num ,step), fill = '#' + hex(delt // 5)[2:].zfill(3))
        # hex perevodit 16 richnuyu systemu    


def function(x):
    global delt, step
    

    step += 1
    delt = max(delt, x)

    if  x  -1 > 0.5:
        if x % 2 == 0:
            x = x // 2

        else:
            x = x + 1
        function(x)

tk = Tk()


cnvs = Canvas(tk, width = 500, height = 500,\
              bg = '#55CDDA')
cnvs.pack()



step_count = []

delta_count = []


for i in range(1000):
    function(i)
    step_count.append(step) #255
    delta_count.append(delt - i) # 0
    Numbers.draw(i, step, delt)
    delt = 110
    step = 110
    tk.update()
    



tk.mainloop()
