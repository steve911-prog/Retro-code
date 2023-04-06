from tkinter import*
import random
root = Tk()
mimo = 0
alf = 'абвгдеёзжиклмнопрстуфхцчшщьыъюя'
def resturt(event):
    pass
    mimo = 0
    for i in list_but:
        i.config(state = 'normal')
    show_word()     
    canv.create_oval([250,150], [350, 250],width = 10 )
    canv.create_line([300,240],[300,360], width = 13, fill = 'red')
    canv.create_line([300,370],[265,450], width =13, fill = 'red')
    canv.create_line([300,370],[350,450], width =13, fill = 'red')
    canv.create_line([300,310],[265,380], width = 13, fill = 'red')
    canv.create_line([300,310],[350,380], width = 13, fill = 'red')
    canv.create_line([250,200],[350,200], width = 13, fill = 'red') 
        
def loadwords():
    words_file = open('words.txt', 'r', encoding = 'utf - 8')
    list_words =  words_file.read().split()
    #print(list_words)
    return words_file.read().split()[1: ]

list_but=[]
list_words = loadwords()
def show_word():
    lab['text'] = show
def gallows():
    canv.create_line([50, 520],[50,520], [100,420], [200,520],[100,520],[100,120],[300,120],[300,170],width=17)
def but_event(event):
    let = event.widget['text']
    event.widget.config(state = 'disabled') 
    ind = str(list_words).find(lit)
    if ind == -1:
        mimo += 1
        if mimo == 1:
                canv.create_oval([250,150], [350, 250],width = 10 )
        elif mimo == 2:
            canv.create_line([300,240],[300,360], width = 13)
        elif mimo == 3:
            canv.create_line([300,370],[265,450], width =13)
        elif mimo == 4:
            canv.create_line([300,370],[350,450], width =13)
        elif mimo == 5:
            canv.create_line([300,310],[265,380], width = 13)
        elif mimo == 6:
            canv.create_line([300,310],[350,380], width = 13)
        elif mimo == 7:
            canv.create_line([250,200],[350,200], width = 13)

            show = 'Looser! ["_"]'
            for i in  list_but:
                i.config(state = 'disabled')
    while ind != -1:
        show[ind] = let
        ind = word.find(let, ind + 1)
    if ('_' in show):
        show = 'Excellent!'
        for i in  list_but:
            i.config(state = 'disabled')
    show_word()   




#word = []
show = []
def choice_words():
    global list_words, word, show,mimo
    word = random.choice(list_words)
    show = ['-']*len(word)

but_resturt = Button(root, text = 'Resturt')
but_resturt.pack(side = 'bottom')
but_resturt.bind('<1>', resturt)
#root.geometry
canv = Canvas(root,width =  557, height = 530, bg = 'red')
canv.pack()

lab = Label(root,  text = '_')
lab.pack()
for lit in alf :
        list_but.append(Button(root, text = lit))
        list_but[-1].pack(side ='left')
        list_but[-1].bind('<1>', but_event)
loadwords()
gallows()
show_word()
choice_words()
root.mainloop()
