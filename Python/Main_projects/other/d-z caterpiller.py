from tkinter import *
root = Tk()
c = Canvas(width=500,height=500,bg='white')
c.pack()
c.create_oval([20,90],[140,190], fill = 'green', outline = 'dark green',width = 3)
c.create_oval([120,140],[240,240], fill = 'green', outline = 'dark green',width = 3)
c.create_oval([220,190],[340,290], fill = 'green', outline = 'dark green',width = 3)
c.create_oval([320,240],[440,340], fill = 'green', outline = 'dark green',width = 3)
c.create_arc([283,310],[350,210],start=0,extent=120,style = ARC,fill = 'dark green',width = 14)
c.create_arc([360,310],[410,210],start=0,extent=120,style = ARC,fill = 'dark green',width = 14)
c.create_oval([350,280],[370,290],fill='black')
c.create_oval([380,280],[400,290],fill='black')
c.create_line([340,300],[420,300],fill='black')
root.mainloop()
