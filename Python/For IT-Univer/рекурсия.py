from tkinter import *
steps = 0
delt = 0

def func(x):
    global steps, delt
    delt = max(delt,x)
    steps += 1
    if x - 1 > 0.5:
        if x % 2 == 0:
            x = x // 2
        else:
            x = x * 3 + 1
        func(x)

def draw(num,steps,delt):
    canv.create_line((num,0),(num,steps),\
                     fill = "#" + hex(delt // 65)[2:].zfill(3))

root = Tk()

canv = Canvas(root, width = 500, height = 500, bg = "lightblue")
canv.pack()
step_count = []
delta_count = []

for i in range(1000):
    func(i)
    step_count.append(steps)
    delta_count.append(delt - i)
    draw(i,steps,delt)
    delt = 0
    steps = 0
    root.update()

root.mainloop()
