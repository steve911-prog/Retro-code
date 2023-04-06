
# mistakes in fuctions : func()
# RV!!!
#



from math import *

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.config import Config

Config.set('graphics','resizable','0')#Win is changed or no
Config.set('graphics','width','380') #Sizes of your window√
Config.set('graphics','height','520')


Builder.load_string("""

<UsualScreen>:
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            size_hint: (1, .13)
            Button:
                text: 'Usual'
                on_press: root.manager.current = 'usual'
            Button:
                text: 'Engineer'
                on_press: root.manager.current = 'engineer'
        RecycleView:
            id: rv
            key_viewclass: 'view'
            key_size: 'height'
            RecycleBoxLayout:
                default_size: None, dp(40)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'   
                Label:
                    id: label
                    text: ' ' 
        GridLayout:
            cols: 4
            Button:
                id: zerospace
                text:'C'
                on_press:
                    
                    root.zerospace()
            Button:
                id: backspace
                text:'<'
                on_press:
                    
                    root.backspace()
            Button:
                id:fabs
                text:'|x|'
                on_press:
                    
                    root.fabs()
            Button:
                id: func
                text:'()'
                on_press:
                    
                    root.func()
            Button:
                id: seven
                text:'7'
                on_press:
                    app.click = 7
                    root.add_numberseven()
            Button:
                id: eight
                text:'8'
                on_press:
                    
                    root.add_numbereight()    
            Button:
                id: nine
                text:'9'
                on_press:
                    app.click = '9'
                    root.add_numbernine()    
            Button:
                id: moremore
                text:'*'
                on_press:
                    
                    root.add_operationmoremore()
            
            Button:
                id: four
                text:'4'
                on_press:
                    
                    root.add_numberfour()
            Button:
                id: five
                text:'5'
                on_press:
                    
                    root.add_numberfive()
            Button:
                id: six
                text:'6'
                on_press:
                    
                    root.add_numbersix()
            Button:
                id: less
                text:'-'
                on_press:
                    
                    root.add_operationminus()
            Button:
                id: one
                text:'1'
                on_press:

                    root.add_numberone()
            Button:
                id: two
                text:'2'
                on_press:
                    
                    root.add_numbertwo()
            Button:
                id: three
                text:'3'
                on_press:
                    
                    root.add_numberthree()
            Button:
                id: more
                text:'+'
                on_press:
                    
                    root.add_operationplus()
            Button:
                id: lessless
                text:'/'
                on_press:
                    
                    root.add_operationlessless()
            Button:
                id: zero
                text:'0'
                on_press:
                    
                    root.add_operationzero()
            Button:
                id:  calc_result
                text:'='
                on_press:
                    
                    root.calc_result()




          
<EngineerScreen>:
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            orientation: 'horizontal'
            size_hint: (1, .025)
            spacing: 2
            Button:
                text: 'Usual'
                on_press: root.manager.current = 'usual'
            Button:
                text: 'Engineer'
                on_press: root.manager.current = 'engineer'
        Label:
            id: label
            text:' 0'
            color:[0,1,1,1]
            font_size: 32
            halign: 'right'
            size_hint: (1, .23)
            text_size: (365, 78)
        GridLayout:
            cols: 5
            spacing: -1
            size_hint: (1, .28)

            Button:
                id: zerospace
                text:'C'
                on_press:
                    
                    root.zerospace()
            Button:
                id: pi
                text:'pi'
                on_press:
                
                    root.pi()    
            Button:
                id: xtwo
                text:'X²'
                on_press:
                
                    root.xtwo()
            Button:
                id: drob
                text:'1/x'
                on_press:
                    
                    root.drob()
            Button:
                id: backspace
                text:'<'
                on_press:
                    
                    root.backspace()
            Button:
                id: log
                text:'log'
                on_press:
                    
                    root.log()
            Button:
                id: sqrt
                text:'√X'
                on_press:
                
                    root.sqrt()
            Button:
                id: func
                text:'()'
                on_press:
                    
                    root.func()    
            Button:
                id: fabs
                text:'|x|'
                on_press:
                    
                    root.fabs()
            Button:
                id: more
                text:'+'
                on_press:
                    
                    root.add_operationmore()    
            Button:
                id: cos
                text:'cos'
                on_press:
            
                    root.cos()
            Button:
                id: seven
                text:'7'
                on_press:
                
                    root.add_numberseven()
            Button:
                id: eight
                text:'8'
                on_press:
                    
                    root.add_numbereight()
            Button:
                id: nine
                text:'9'
                on_press:
        
                    root.add_numbernine()
            Button:
                id: less
                text:'-'
                on_press:
                
                    root.add_operationminus()
            Button:
                id: sin
                text:'sin'
                on_press:
                    
                    root.sin()    
            Button:
                id: four
                text:'4'
                on_press:
        
                    root.add_numberfour()
            Button:
                id: five
                text:'5'
                on_press:
                    
                    root.add_numberfive()
            Button:
                id: six
                text:'6'
                on_press:
            
                    root.add_numbersix()
            Button:
                id: lessless
                text:'/'
                on_press:
            
                    root.add_operationlessless()
            Button:
                id: tan
                text:'tan'
                on_press:
                    
                    root.add_tan()
            Button:
                id: one
                text:'1'
                on_press:
                
                    root.add_numberone()
            Button:
                id:two
                text:'2'
                on_press:
            
                    root.add_numbertwo()
            Button:
                id:three
                text:'3'
                on_press:
                
                    root.add_numberthree()
            Button:
                id: moremore
                text:'*'
                
                    on_press: root.add_operationmoremore()
            Button:
                id: ceil
                text:'ceil'
                on_press:
                
                    root.ceil()
            Button:
                id: procents
                text:'%'
                on_press:
                
                    root.add_operationprocents()
            Button:
                id: zerotwo
                text:'0'
                on_press:
                    
                    root.add_operationzero()
            Button:
                id: tochka
                text:'.'
                on_press:
            
                    root.add_operationtochka()
            Button:
                id: calc_resulttwo
                text:'='
                on_press:
                    
                    root.calc_result()

""")




class UsualScreen(Screen):
    def __init__(self, **kwargs):
        super(UsualScreen, self).__init__(**kwargs)
        self.formula = ' '

        
        def rv(self):
            #def add_story(self, instance):
                #self.ids.rv.data.append({'viewclass': 'Label', 'text': fd})
                #self.f2.write("\n" + self.lbl.text + '=' + eval(self.lbl.text))
            self.f2 = open('history.txt', 'r', encoding = 'utf - 8')
            self.f3 = open('history.txt', 'a', encoding = 'utf - 8')

            self.file = self.f2.read()

        
            self.lbl = Label(text = self.file)
            self.ids.label = self.lbl
            while True:
                self.ids.rv.data.append({'viewclass':'Button','text':slef.file})


    def c_history(self, instance):
        self.f2.seek(0)
        self.f2.truncate()
        #self.read_file = self.f.read()
        self.f2.close()
        self.f2 = open('history.txt', 'a', encoding = 'utf - 8')
        #self.f3 = open('history.txt', 'w', encoding = 'utf - 8')
        self.read_file = self.f.read()
        self.label.text = self.file
        

    def zerospace(self):
        self.ids.label.text = ' '
        self.formula = ' '
         
    def update_label(self):
        self.ids.label.text = self.formula

    
    def drob(self):
        try:
            self.ids.label.text =  str(float(eval('1/'+ str(eval(self.ids.label.text)))))
            self.formula = self.ids.label.text  
        except  ZeroDivisionError:
            self.formula = '0'
            self.lbl.text = '0'
         
    def sqrt(self):
        try:
            self.ids.label.text =  str(float(eval(self.lbl.text)) ** 0.5)
            self.formula =  self.ids.label.text
        except SyntaxError:
            self.formula = '0'
            self.ids.label.text = '0'
            
    def backspace(self):
        if  len(self.ids.label.text) == 1:
            self.formula = ' '
            self.ids.label.text = ' '
        else:
            self.ids.label.text = self.formula
            self.formula = self.formula[:-1]
   

    def func(self):
        c = '*'
        if type(self.ids.label.text[len(self.ids.label.text) - 1]) == 'int':
            if (self.ids.label.text.count('(') + self.ids.label.text.count(')')) % 2 == 0 :
                self.formula += '('
                self.ids.label.text += '('
        else:    
            if self.ids.label.text == '0':
                self.formula = '('
                self.ids.label.text = '('
            elif (self.ids.label.text.count('(') + self.ids.label.text.count(')')) % 2 == 0 :
                self.formula += '('
                self.ids.label.text += '('
            else:
                self.formula += ')'
                self.ids.label.text += ')'

   
    def log(self):
        if self.formula == '0':
            self.formula = 'log('
        else:
            self.formula += ' log('
            self.update_label()

    def cos(self):
        if self.ids.label.text == '0':
            self.formula = 'cos('
        else:
            self.formula += ' cos('
        self.update_label()
      

    def sin(self):
        if self.ids.label.text == '0':
            self.formula = 'sin('
        else:
            self.formula += ' sin('
        self.update_label()    

    def tan(self):
        if self.ids.label.text == '0':
            self.formula = 'tan('
        else:
            self.formula += ' tan('
        self.update_label()        

    def change_sign(self):
        if self.ids.label.text == '0':
            self.formula = '0'
        elif self.ids.label.text[0] == '-':
            self.formula = self.formula[1:]
        else:
            self.formula = '-' + self.formula
        self.update_label() 

    

    def fabs(self): ############################################################################################################^%U^R%JDYJKR^E&TK%%KJKKYTHGJ^I(&YKYTK&^*
        if self.formula == '0':
            self.formula = 'fabs('
        else:
            self.formula += ' fabs('
        self.update_label()     

    def pi(self):
        if self.formula == '0':
            self.formula = '3.14'
        else:
            self.formula =  self.formula + '3.14'
        self.update_label()

    def ceil(self):
        if self.formula == '0':
            self.formula = 'ceil('
        else:
            self.formula += ' ceil('
        self.update_label()

      
    def xtwo(self):
        if self.ids.label.text == '0':
            self.formula = '0'
            
        else:
            self.formula = str(eval(int(self.formula)**2))
        self.update_label()    
   
    def add_numberone(self):
        text = self.ids.one.text
        #self.ids.label.text = self.formula
        
        if self.formula == '0':
            self.formula = ''
            self.formula += text
            self.ids.label.text +=  text
        else:
            self.formula += text
            self.ids.label.text += text   

    def add_numbertwo(self):
        text = self.ids.two.text
        #self.ids.label.text = self.formula
        
        if self.formula == '0':
            self.formula = ''
            self.formula += text
            self.ids.label.text +=  text
        else:
            self.formula += text
            self.ids.label.text += text

    def add_numberthree(self):
        text = self.ids.three.text
        #self.ids.label.text = self.formula
        
        if self.formula == '0':
            self.formula = ''
            self.formula += text
            self.ids.label.text +=  text
        else:
            self.formula += text
            self.ids.label.text += text         

    def add_numberfour(self):
        text = self.ids.four.text
        #self.ids.label.text = self.formula
        
        if self.formula == '0':
            self.formula = ''
            self.formula += text
            self.ids.label.text +=  text
        else:
            self.formula += text
            self.ids.label.text += text 
    
    def add_numberfive(self):
        text = self.ids.five.text
        #self.ids.label.text = self.formula
        
        if self.formula == '0':
            self.formula = ''
            self.formula += text
            self.ids.label.text +=  text
        else:
            self.formula += text
            self.ids.label.text += text 
    
    def add_numbersix(self):
        text = self.ids.six.text
        #self.ids.label.text = self.formula
        
        if self.formula == '0':
            self.formula = ''
            self.formula += text
            self.ids.label.text +=  text
        else:
            self.formula += text
            self.ids.label.text += text

    def add_numberseven(self):
        text = self.ids.seven.text
        #self.ids.label.text = self.formula
        
        if self.formula == '0':
            self.formula = ''
            self.formula += text
            self.ids.label.text +=  text
        else:
            self.formula += text
            self.ids.label.text += text

    def add_numbereight(self):
        text = self.ids.eight.text
        #self.ids.label.text = self.formula
        
        if self.formula == '0':
            self.formula = ''
            self.formula += text
            self.ids.label.text +=  text
        else:
            self.formula += text
            self.ids.label.text += text

    def add_numbernine(self):
        text = self.ids.nine.text
        #self.ids.label.text = self.formula
        
        if self.formula == '0':
            self.formula = ''
            self.formula += text
            self.ids.label.text +=  text
        else:
            self.formula += text
            self.ids.label.text += text         

            
    def add_operationplus(self):
        text = self.ids.more.text
        self.ids.label.text = self.formula     
        
        if self.ids.label.text[len(self.ids.label.text) - 1] == '*':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 
       
        elif self.ids.label.text[len(self.ids.label.text) - 1] == '/':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        elif self.ids.label.text[len(self.ids.label.text) - 1] == '%':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 
        
        elif self.ids.label.text[len(self.ids.label.text) - 1] == '+':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        elif self.ids.label.text[len(self.ids.label.text) - 1] == '-':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        else:
            self.formula += str(text)
            self.ids.label.text += str(text) 

    def add_operationminus(self):
        text = self.ids.less.text
        self.ids.label.text = self.formula     
        
        if self.ids.label.text[len(self.ids.label.text) - 1] == '*':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        elif self.ids.label.text[len(self.ids.label.text) - 1] == '%':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 
       
        elif self.ids.label.text[len(self.ids.label.text) - 1] == '/':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        elif self.ids.label.text[len(self.ids.label.text) - 1] == '+':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        elif self.ids.label.text[len(self.ids.label.text) - 1] == '-':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        else:
            self.formula += str(text)
            self.ids.label.text += str(text)    


    def add_operationlessless(self):
        text = self.ids.lessless.text
        self.ids.label.text = self.formula     
        
        if self.ids.label.text[len(self.ids.label.text) - 1] == '*':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 
       
        elif self.ids.label.text[len(self.ids.label.text) - 1] == '/':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        elif self.ids.label.text[len(self.ids.label.text) - 1] == '%':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        elif self.ids.label.text[len(self.ids.label.text) - 1] == '+':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        elif self.ids.label.text[len(self.ids.label.text) - 1] == '-':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        else:
            self.formula += str(text)
            self.ids.label.text += str(text) 

    def add_operationmoremore(self):
        text = self.ids.moremore.text
        self.ids.label.text = self.formula     
        
        if self.ids.label.text[len(self.ids.label.text) - 1] == '*':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 
       
        elif self.ids.label.text[len(self.ids.label.text) - 1] == '/':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        elif self.ids.label.text[len(self.ids.label.text) - 1] == '%':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        elif self.ids.label.text[len(self.ids.label.text) - 1] == '+':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        elif self.ids.label.text[len(self.ids.label.text) - 1] == '-':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        else:
            self.formula += str(text)
            self.ids.label.text += str(text) 


    def add_operationzero(self):
        text = self.ids.zero.text
        self.ids.label.text = self.formula     
        
        if self.ids.label.text[len(self.ids.label.text) - 1] == '*':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        elif self.ids.label.text[len(self.ids.label.text) - 1] == '%':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 
       
        elif self.ids.label.text[len(self.ids.label.text) - 1] == '/':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        elif self.ids.label.text[len(self.ids.label.text) - 1] == '+':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        elif self.ids.label.text[len(self.ids.label.text) - 1] == '-':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        else:
            self.formula += str(text)
            self.ids.label.text += str(text) 

    def add_operationprocents(self):
        text = self.ids.procents.text
        self.ids.label.text = self.formula     
        
        if self.ids.label.text[len(self.ids.label.text) - 1] == '*':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        elif self.ids.label.text[len(self.ids.label.text) - 1] == '%':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 
       
        elif self.ids.label.text[len(self.ids.label.text) - 1] == '/':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        elif self.ids.label.text[len(self.ids.label.text) - 1] == '+':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        elif self.ids.label.text[len(self.ids.label.text) - 1] == '-':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        else:
            self.formula += str(text)
            self.ids.label.text += str(text)    
        


    def calc_result(self):
        
        try:
            self.ids.label.text = str(eval(self.ids.label.text))
            formula = str(eval(self.ids.label.text))
            formula = '0'
        except SyntaxError:
            formula = '0'
            self.ids.label.text = '0'
        except TypeError:
            formula = '0'
            self.ids.label.text = '0'

        
#############################################################
   

class EngineerScreen(Screen):
    def __init__(self, **kwargs):
        super(EngineerScreen, self).__init__(**kwargs)
        self.formula = ' '
     
    def zerospace(self):
        self.ids.label.text = ' '
        self.formula = ' '
         
    def update_label(self):
        self.ids.label.text = self.formula

    
    def drob(self):
        try:
            self.ids.label.text =  str(float(eval('1/'+ str(eval(self.ids.label.text)))))
            self.formula = self.ids.label.text  
        except  ZeroDivisionError:
            self.formula = '0'
            self.lbl.text = '0'
         
    def sqrt(self):
        try:
            self.ids.label.text =  str(float(eval(self.lbl.text)) ** 0.5)
            self.formula =  self.ids.label.text
        except SyntaxError:
            self.formula = '0'
            self.ids.label.text = '0'
            
    def backspace(self):
        if  len(self.ids.label.text) == 1:
            self.formula = ' '
            self.ids.label.text = ' '
        else:
            self.ids.label.text = self.formula
            self.formula = self.formula[:-1]
   

    def func(self):
        if self.ids.label.text == '0': # cheicking the number of brackets : if number of the brackets is even, bracket = '(', else: ')'
            self.formula = '('  # 
            self.ids.label.text = '('
        elif (self.ids.label.text.count('(') + self.ids.label.text.count(')')) % 2 == 0 :
            self.formula += '('
            self.ids.label.text += '('
        elif (self.ids.label.text.count('(') + self.ids.label.text.count(')')) % 2 != 0 :
            self.formula += ')'
            self.ids.label.text += ')'

   
    def log(self):
        if self.formula == '0':
            self.formula = 'log('
        else:
            self.formula += ' log('
            self.update_label()

    def cos(self):
        if self.ids.label.text == '0':
            self.formula = 'cos('
        else:
            self.formula += ' cos('
        self.update_label()
      

    def sin(self):
        if self.ids.label.text == '0':
            self.formula = 'sin('
        else:
            self.formula += ' sin('
        self.update_label()    

    def tan(self):
        if self.ids.label.text == '0':
            self.formula = 'tan('
        else:
            self.formula += ' tan('
        self.update_label()        

    def change_sign(self):
        if self.ids.label.text == '0':
            self.formula = '0'
        elif self.ids.label.text[0] == '-':
            self.formula = self.formula[1:]
        else:
            self.formula = '-' + self.formula
        self.update_label() 

    

    def fabs(self): 
        if self.formula == '0':
            self.formula = 'fabs('
        else:
            self.formula += ' fabs('
        self.update_label()     

    def pi(self):
        if self.formula == '0':
            self.formula = '3.14'
        else:
            self.formula =  self.formula + '3.14'
        self.update_label()

    def ceil(self):
        if self.formula == '0':
            self.formula = 'ceil('
        else:
            self.formula += ' ceil('
        self.update_label()

      
    def xtwo(self):
        if self.ids.label.text == '0':
            self.formula = '0'
            
        else:
            self.formula = str(eval(int(self.formula)**2))
        self.update_label()    
   
    def add_numberone(self):
        text = self.ids.one.text
        #self.ids.label.text = self.formula
        
        if self.formula == '0':
            self.formula = ''
            self.formula += text
            self.ids.label.text +=  text
        else:
            self.formula += text
            self.ids.label.text += text   

    def add_numbertwo(self):
        text = self.ids.two.text
        #self.ids.label.text = self.formula
        
        if self.formula == '0':
            self.formula = ''
            self.formula += text
            self.ids.label.text +=  text
        else:
            self.formula += text
            self.ids.label.text += text

    def add_numberthree(self):
        text = self.ids.three.text
        #self.ids.label.text = self.formula
        
        if self.formula == '0':
            self.formula = ''
            self.formula += text
            self.ids.label.text +=  text
        else:
            self.formula += text
            self.ids.label.text += text         

    def add_numberfour(self):
        text = self.ids.four.text
        #self.ids.label.text = self.formula
        
        if self.formula == '0':
            self.formula = ''
            self.formula += text
            self.ids.label.text +=  text
        else:
            self.formula += text
            self.ids.label.text += text 
    
    def add_numberfive(self):
        text = self.ids.five.text
        #self.ids.label.text = self.formula
        
        if self.formula == '0':
            self.formula = ''
            self.formula += text
            self.ids.label.text +=  text
        else:
            self.formula += text
            self.ids.label.text += text 
    
    def add_numbersix(self):
        text = self.ids.six.text
        #self.ids.label.text = self.formula
        
        if self.formula == '0':
            self.formula = ''
            self.formula += text
            self.ids.label.text +=  text
        else:
            self.formula += text
            self.ids.label.text += text

    def add_numberseven(self):
        text = self.ids.seven.text
        #self.ids.label.text = self.formula
        
        if self.formula == '0':
            self.formula = ''
            self.formula += text
            self.ids.label.text +=  text
        else:
            self.formula += text
            self.ids.label.text += text

    def add_numbereight(self):
        text = self.ids.eight.text
        #self.ids.label.text = self.formula
        
        if self.formula == '0':
            self.formula = ''
            self.formula += text
            self.ids.label.text +=  text
        else:
            self.formula += text
            self.ids.label.text += text

    def add_numbernine(self):
        text = self.ids.nine.text
        #self.ids.label.text = self.formula
        
        if self.formula == '0':
            self.formula = ''
            self.formula += text
            self.ids.label.text +=  text
        else:
            self.formula += text
            self.ids.label.text += text         

            
    def add_operationplus(self):
        text = self.ids.more.text
        self.ids.label.text = self.formula     
        
        if self.ids.label.text[len(self.ids.label.text) - 1] == '*':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 
       
        elif self.ids.label.text[len(self.ids.label.text) - 1] == '/':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        elif self.ids.label.text[len(self.ids.label.text) - 1] == '%':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 
        
        elif self.ids.label.text[len(self.ids.label.text) - 1] == '+':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        elif self.ids.label.text[len(self.ids.label.text) - 1] == '-':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        else:
            self.formula += str(text)
            self.ids.label.text += str(text) 

    def add_operationminus(self):
        text = self.ids.less.text
        self.ids.label.text = self.formula     
        
        if self.ids.label.text[len(self.ids.label.text) - 1] == '*':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        elif self.ids.label.text[len(self.ids.label.text) - 1] == '%':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 
       
        elif self.ids.label.text[len(self.ids.label.text) - 1] == '/':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        elif self.ids.label.text[len(self.ids.label.text) - 1] == '+':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        elif self.ids.label.text[len(self.ids.label.text) - 1] == '-':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        else:
            self.formula += str(text)
            self.ids.label.text += str(text)    


    def add_operationlessless(self):
        text = self.ids.lessless.text
        self.ids.label.text = self.formula     
        
        if self.ids.label.text[len(self.ids.label.text) - 1] == '*':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 
       
        elif self.ids.label.text[len(self.ids.label.text) - 1] == '/':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        elif self.ids.label.text[len(self.ids.label.text) - 1] == '%':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        elif self.ids.label.text[len(self.ids.label.text) - 1] == '+':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        elif self.ids.label.text[len(self.ids.label.text) - 1] == '-':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        else:
            self.formula += str(text)
            self.ids.label.text += str(text) 

    def add_operationmoremore(self):
        text = self.ids.moremore.text
        self.ids.label.text = self.formula     
        
        if self.ids.label.text[len(self.ids.label.text) - 1] == '*':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 
       
        elif self.ids.label.text[len(self.ids.label.text) - 1] == '/':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        elif self.ids.label.text[len(self.ids.label.text) - 1] == '%':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        elif self.ids.label.text[len(self.ids.label.text) - 1] == '+':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        elif self.ids.label.text[len(self.ids.label.text) - 1] == '-':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        else:
            self.formula += str(text)
            self.ids.label.text += str(text) 


    def add_operationzero(self):
        text = self.ids.zero.text
        self.ids.label.text = self.formula     
        
        if self.ids.label.text[len(self.ids.label.text) - 1] == '*':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        elif self.ids.label.text[len(self.ids.label.text) - 1] == '%':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 
       
        elif self.ids.label.text[len(self.ids.label.text) - 1] == '/':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        elif self.ids.label.text[len(self.ids.label.text) - 1] == '+':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        elif self.ids.label.text[len(self.ids.label.text) - 1] == '-':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        else:
            self.formula += str(text)
            self.ids.label.text += str(text) 

    def add_operationprocents(self):
        text = self.ids.procents.text
        self.ids.label.text = self.formula     
        
        if self.ids.label.text[len(self.ids.label.text) - 1] == '*':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        elif self.ids.label.text[len(self.ids.label.text) - 1] == '%':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 
       
        elif self.ids.label.text[len(self.ids.label.text) - 1] == '/':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        elif self.ids.label.text[len(self.ids.label.text) - 1] == '+':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 

        elif self.ids.label.text[len(self.ids.label.text) - 1] == '-':
            self.ids.label.text = self.ids.label.text[:-1]
            self.formula = self.ids.label.text
            self.ids.label.text += str(text)
            self.formula = self.ids.label.text 
        else:
            self.formula += str(text)
            self.ids.label.text += str(text)
            

    def calc_result(self):
        
        try:
            self.ids.label.text = str(eval(self.ids.label.text))
            formula = str(eval(self.ids.label.text))
            formula = '0'
        except SyntaxError:
            formula = '0'
            self.ids.label.text = '0'
        except TypeError:
            formula = '0'
            self.ids.label.text = '0'
   



# Create the screen manager
sm = ScreenManager()

sm.add_widget(UsualScreen(name = 'usual'))
sm.add_widget(EngineerScreen(name = 'engineer'))


class TestApp(App):
    

    
    
    def build(self):
        click = ' '
        
        return sm

if __name__ == '__main__':
    TestApp().run()
