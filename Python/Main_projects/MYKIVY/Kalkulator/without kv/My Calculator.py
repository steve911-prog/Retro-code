

class EngineerScreen(Screen):
    pass          

class HistoryScreen(Screen):
    def add_story(self, instance):
       
        self.f2.write("\n" + self.lbl.text + '=' + eval(self.lbl.text))

    def c_history(self, instance):
        self.f2.seek(0)
        self.f2.truncate()
        
        self.f2.close()
        self.f2= open('history.txt', 'a', encoding = 'utf - 8')
        
        self.read_file = self.f.read()
        self.lbl.text = self.read_file
    def build(self):
        self.f = open('history.txt', 'r', encoding = 'utf - 8')

        self.f2 = open('history.txt', 'a', encoding = 'utf - 8')
        #self.f3 = open('history.txt', 'w', encoding = 'utf - 8')

        self.read_file = self.f.read()


    
class UsualScreen(Screen):
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
    




screen_manager = ScreenManager() 

screen_manager.add_widget(EngineerScreen(name ="engineer")) 
screen_manager.add_widget(UsualScreen(name ="usual")) 
screen_manager.add_widget(HistoryScreen(name ="history")) 
  


class Main_CalculatorApp(App):
   def build(self):
       return screen_manager
       #screen_manager.current =  'usual'       
            


      
     
            
Main_CalculatorApp().run()


#°	
#¹	
#²
