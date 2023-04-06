from tkinter import*
import random
mimo = 0
root = Tk()
def loadwords():
    words_file = open('words.txt', 'r', encoding = 'utf - 8')
    list_words = words_file.read().split()
    print(list_words)
    return words_file.read().split()[1: ]
def show_word():
    lab['text'] = show
def gallows():
    canv.create_line([50, 520],[50,520], [100,420], [200,520],[100,520],[100,120],[300,120],[300,170],width=17)
def but_event(event):
    let = event.widget['text']
    event.widget.config(state = 'disabled') 
    ind = word.find(let)
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
    while ind != -1:
        show[ind] = let
        ind = word.find(let, ind + 1)

    show_word()   


alf = 'абвгдеёзжиклмнопрстуфхцчшщьыъюя'
list_but=[]
list_words = loadwords()
#word = []
show = []
def choice_words():
    global list_words, word, show
    word = random.choice[list_words]
    show = ['-']*len(word)


root.geometry
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
show_word(
choice_words()
root.mainloop()
