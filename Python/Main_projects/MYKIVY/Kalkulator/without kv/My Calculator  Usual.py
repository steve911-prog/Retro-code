from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen

from math import *

from random import randint

from kivy.uix.widget import Widget

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout



Config.set('graphics','resizable','1')#Win is changed or no
Config.set('graphics','width','380') #Sizes of your window√
Config.set('graphics','height','520')



class CalApp(App):
    def update_label(self):
        self.lbl.text = self.formula

    def zerospace(self,instance):
        self.lbl.text = '0'
        self.formula = '0'

    def drob(self, instance):
        try:
            self.lbl.text =  str(float(eval('1/'+ str(eval(self.lbl.text)))))
            self.formula =   str(float(eval('1/'+ str(eval(self.formula)))))
        except  ZeroDivisionError:
            self.formula = '0'
            self.lbl.text = '0'

    def sqrt(self, instance):
        try:
            self.lbl.text =  str(float(eval(self.lbl.text)) ** 0.5)
            self.formula =  str(float(eval(self.formula)) ** 0.5)
        except SyntaxError:
            self.formula = '0'
            self.lbl.text = '0'
        self.formula = '0'




    def backspace(self, instance):
        if  len(self.lbl.text) == 1:
            self.formula = ' '
            self.lbl.text = ' '
        else:
            self.formula = self.formula[:-1]
            self.lbl.text = self.lbl.text[:-1]
    def func2(self,instance):
        if self.lbl.text == '0':
            self.formula = '('
            self.lbl.text = '('
        elif bool(self.lbl.text.rfind('(')) == True and bool(self.lbl.text.rfind(')')) == True:
            self.formula += '('
            self.lbl.text += '('
        elif bool(self.lbl.text.rfind('(')) == True and bool(self.lbl.text.rfind(')')) == False:
            self.formula += ')'
            self.lbl.text += ')'
        else:
            self.formula += ')'
            self.lbl.text += ')'

    def func(self,instance):
        if self.lbl.text == '0':
            self.formula = '('
            self.lbl.text = '('
        elif (self.lbl.text.count('(') + self.lbl.text.count(')')) % 2 == 0 :
            self.formula += '('
            self.lbl.text += '('
        else:
            self.formula += ')'
            self.lbl.text += ')'

   
    def log(self, instance):
        if self.formula == '0':
            self.formula = 'log('
        else:
            self.formula += ' log('
            self.update_label()
    def cos(self,instance):
        if self.formula == '0':
            self.formula = 'cos('
        else:
            self.formula += ' cos('
        self.update_label()
      

    def sin(self,instance):
        if self.formula == '0':
            self.formula = 'sin('
        else:
            self.formula += ' sin('
        self.update_label()    

    def tan(self,instance):
        if self.formula == '0':
            self.formula = 'tan('
        else:
            self.formula += ' tan('
        self.update_label()        

    def change_sign(self, instance):
        if self.lbl.text == '0':
            self.formula = '0'
            self.lbl.text = '0'
        elif self.lbl.text[0] == '-':
            self.lbl.text = self.lbl.text[1:]
            self.formula = self.formula[1:]
        else:
            self.formula = '-' + self.formula
            self.lbl.text = '-' + self.lbl.text   
    def change_sign(self, instance):
        if self.lbl.text == '0':
            self.formula = '0'
            self.lbl.text = '0'
        elif self.lbl.text[0] == '-':
            self.lbl.text = self.lbl.text[1:]
            self.formula = self.formula[1:]
        else:
            self.formula = '-' + self.formula
            self.lbl.text = '-' + self.lbl.text   
    def fabs(self,instance): ############################################################################################################^%U^R%JDYJKR^E&TK%%KJKKYTHGJ^I(&YKYTK&^*
        if self.formula == '0':
            self.formula = 'fabs('
        else:
            self.formula += ' fabs('
        self.update_label()     
    def pi(self, instance):
        if self.formula == '0':
            self.lbl.text = '3.14'
            self.formula = '3.14'
        else:
            self.lbl.text = self.lbl.text + '3.14'
            self.formula =  self.formula + '3.14'

    def ceil(self,instance):
        if self.formula == '0':
            self.formula = 'ceil('
        else:
            self.formula += ' ceil('
        self.update_label()

      
    def xtwo(self, instance):
        if self.lbl.text == '0':
            self.formula = '0'
            self.update_label()
        else:
            self.formula = str(eval(int(self.formula)**2))
            self.update_label()
   
  
      
    def add_number(self, instance):
        self.lbl.text = self.formula

        if self.formula == '0':
            self.formula = ''
            self.formula += str(instance.text)
            self.lbl.text += str(instance.text)
        else:
            self.formula += str(instance.text)
            self.lbl.text += str(instance.text)
            
    def add_operation(self, instance):
        self.lbl.text = self.formula     
        if str(instance.text).lower() == 'x':
            self.formula += '*'
            self.lbl.text += '*'
        elif str(instance.text).lower() == 'X²':
            self.formula += '**2'
            self.lbl.text += '**2'

        if self.lbl.text[len(self.lbl.text) - 1] == '*':
            self.lbl.text = self.lbl.text[:-1]
            self.formula = self.lbl.text
            self.lbl.text += str(instance.text)
            self.formula = self.lbl.text 
       
        elif self.lbl.text[len(self.lbl.text) - 1] == '/':
            self.lbl.text = self.lbl.text[:-1]
            self.formula = self.lbl.text
            self.lbl.text += str(instance.text)
            self.formula = self.lbl.text 

        elif self.lbl.text[len(self.lbl.text) - 1] == '+':
            self.lbl.text = self.lbl.text[:-1]
            self.formula = self.lbl.text
            self.lbl.text += str(instance.text)
            self.formula = self.lbl.text 

        elif self.lbl.text[len(self.lbl.text) - 1] == '-':
            self.lbl.text = self.lbl.text[:-1]
            self.formula = self.lbl.text
            self.lbl.text += str(instance.text)
            self.formula = self.lbl.text 

        else:
            self.formula += str(instance.text)
            self.lbl.text += str(instance.text) 
      


    def calc_result(self, instance):
        try:
            self.lbl.text = str(eval(self.lbl.text))
            self.formula = str(eval(self.lbl.text))
            self.formula = ' '
        except SyntaxError:
            self.formula = ' '
            self.lbl.text = ' '
        except TypeError:
            self.formula = ' '
            self.lbl.text = ' '  #############################################################
   
    def build(self):
            self.formula = ' '
        
            bl = BoxLayout(orientation = 'vertical')
            gl = GridLayout(cols = 4, spacing = -1, size_hint = (1, .28))

        
            self.lbl = Label(text = ' ',color = [0,1,1,1],font_size = 32, halign = 'right'  ,\
                             size_hint = (1, .23), text_size = (365, 78))
            bl2 = BoxLayout(orientation = 'horizontal', size_hint = (1, .035), spacing = 2)

            bl2.add_widget(Button(text = 'History'))
            bl2.add_widget(Button(text = 'Usual'))
            bl2.add_widget(Button(text = 'Engineer'))
            bl2.add_widget(Widget())

            bl.add_widget(bl2)              
            bl.add_widget(self.lbl)
        

            #gl.add_widget(Button(text = '1/x', on_press = self.drob))
            gl.add_widget(Button(text = 'C', on_press = self.zerospace))
            #gl.add_widget(Button(text = 'X²', on_press = self.xtwo))
            gl.add_widget(Button(text = '<', on_press = self.backspace))    
        
            ###########gl.add_widget(Button(text = '+/-', on_press = self.change_sign))
            gl.add_widget(Button(text = '|x|', on_press = self.fabs))

            gl.add_widget(Button(text = '( )', on_press = self.func))
            ##########gl.add_widget(Button(text = '//', on_press = self.add_operation))
            #gl.add_widget(Button(text = 'pi', on_press = self.pi))
            #gl.add_widget(Button(text = 'ceil', on_press = self.ceil))
        
            gl.add_widget(Button(text = '7', on_press = self.add_number))
            gl.add_widget(Button(text = '8', on_press = self.add_number))
            gl.add_widget(Button(text = '9', on_press = self.add_number))
            gl.add_widget(Button(text = '*', on_press = self.add_operation))

            gl.add_widget(Button(text = '4', on_press = self.add_number))
            gl.add_widget(Button(text = '5', on_press = self.add_number))
            gl.add_widget(Button(text = '6', on_press = self.add_number))
            gl.add_widget(Button(text = '-', on_press = self.add_operation))


            gl.add_widget(Button(text = '1', on_press = self.add_number))
            gl.add_widget(Button(text = '2', on_press = self.add_number))
            gl.add_widget(Button(text = '3', on_press = self.add_number))
            gl.add_widget(Button(text = '+', on_press = self.add_operation))

            gl.add_widget(Button(text = '/', on_press = self.add_operation))
            gl.add_widget(Button(text = '0', on_press = self.add_operation))
            gl.add_widget(Button(text = '.', on_press = self.add_operation))
            gl.add_widget(Button(text = '=', on_press = self.calc_result))

        
            bl.add_widget(gl)   
            return bl    
            
      
      
  
      
       
            
CalApp().run()

#°	
#¹	
#²
