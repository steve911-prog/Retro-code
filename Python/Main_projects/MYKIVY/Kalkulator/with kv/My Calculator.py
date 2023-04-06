'''from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen

from math import *

from random import randint

from kivy.uix.widget import Widget

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout



Config.set('graphics','resizable','0')#Win is changed or no
Config.set('graphics','width','380') #Sizes of your window√
Config.set('graphics','height','520')

#Builder.load_file('build.kv')

Builder.load_string('''
'''<EngineerScreen>:
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            orientation: 'horizontal'
            size_hint: (1, .035)
            spacing: 2
            

            Button:
                text:'C'
                on_press: app.screen_manager.current = 'history'
            Button:
                text:'pi'
                on_press: app.screen_manager.current = 'usual'
            Button:
                text:'X²'
                on_press: app.screen_manager.current = 'engineer'

        Label:
            text:' '
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
                text:'C'
                on_press: self.zerospace
            Button:
                text:'pi'
                on_press: self.pi    
            Button:
                text:'X²'
                on_press: self.xtwo
            Button:
                text:'1/x'
                on_press: self.drob
            Button:
                text:'<'
                on_press: self.backspace
            Button:
                text:'log'
                on_press: self.log
            Button:
                text:'√X'
                on_press: self.sqrt
            Button:
                text:'()'
                on_press: self.func    
            Button:
                text:'|x|'
                on_press: self.fabs
            Button:
                text:'+'
                on_press: self.add_operation    
            Button:
                text:'cos'
                on_press: self.cos
            Button:
                text:'7'
                on_press: self.add_number
            Button:
                text:'8'
                on_press: self.add_number
            Button:
                text:'9'
                on_press: self.add_number
            Button:
                text:'-'
                on_press: self.add_operation
            Button:
                text:'sin'
                on_press: self.add_number    
            Button:
                text:'4'
                on_press: self.add_number
            Button:
                text:'5'
                on_press: self.add_number
            Button:
                text:'6'
                on_press: self.add_number
            Button:
                text:'/'
                on_press: self.add_operation
            Button:
                text:'tan'
                on_press: self.add_number
            Button:
                text:'1'
                on_press: self.add_number
            Button:
                text:'2'
                on_press: self.add_number
            Button:
                text:'3'
                on_press: self.add_number
            Button:
                text:'*'
                on_press: self.add_operation
            Button:
                text:'ceil'
                on_press: self.add_number
            Button:
                text:'%'
                on_press: self.add_operation
            Button:
                text:'0'
                on_press: self.add_operation
            Button:
                text:'.'
                on_press: self.add_operation
            Button:
                text:'='
                on_press: calc_result

<UsualScreen>:
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            Button:
                text:'History'
                on_press: app.screen_manager.current = 'history'
            Button:
                text:'Usual'
                on_press: app.screen_manager.current = 'usual'
            Button:
                text:'Egineer'
                on_press: app.screen_manager.current = 'engineer'
        Label:
            text:' '
            color:[0,1,1,1]
            font_size: 32
            halign: 'right'
            size_hint: (1, .23)
            text_size: (365, 78)    

        GridLayout:
            Button:
                text:'C'
                on_press:self.zerospace
            Button:
                text:'<'
                on_press:self.backspace
            Button:
                text:'|x|'
                on_press:self.fabs
            Button:
                text:'()'
                on_press:self.func
            Button:
                text:'7'
                on_press:self.add_number
            Button:
                text:'8'
                on_press:self.add_number    
            Button:
                text:'9'
                on_press:self.add_number    
            Button:
                text:'*'
                on_press:self.add_operation
            Button:
                text:'4'
                on_press:self.add_number
            Button:
                text:'7'
                on_press:self.add_number
            Button:
                text:'*'
                on_press:self.add_operation
            Button:
                text:'4'
                on_press:self.add_number
            Button:
                text:'5'
                on_press:self.add_number
            Button:
                text:'6'
                on_press:self.add_number
            Button:
                text:'-'
                on_press:self.add_operation
            Button:
                text:'1'
                on_press:self.add_number
            Button:
                text:'2'
                on_press:self.add_number
            Button:
                text:'3'
                on_press:self.add_number
            Button:
                text:'+'
                on_press:self.add_operation
            Button:
                text:'/'
                on_press:self.add_operation
            Button:
                text:'0'
                on_press:self.add_operation
            Button:
                text:'='
                on_press:self.calc_result

<HistoryScreen>:
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            Button:
                text:'History'
                on_press: app.screen_manager.current = 'history'
            Button:
                text:'Usual'
                on_press: app.screen_manager.current = 'usual'
            Button:
                text:'Egineer'
                on_press: app.screen_manager.current = 'engineer'
        Label:
            text: 'history'                        #str(self.read_file)
            color:[0,1,1,1]
            font_size: 20
            size_hint: (1, .73)
            text_size: (355, 430)
        GridLayout:
            cols: 3
            spacing: -1
            size_hint: (1, .05)

            Widget
            Button:
                text: 'Delete'
                on_press: self.c_history
            Widget


                
'''''')

class EngineerScreen(Screen):
    pass          

class HistoryScreen(Screen):
    pass
##    def add_story(self, instance):
##       
##        self.f2.write("\n" + self.lbl.text + '=' + eval(self.lbl.text))
##
##    def c_history(self, instance):
##        self.f2.seek(0)
##        self.f2.truncate()
##        
##        self.f2.close()
##        self.f2= open('history.txt', 'a', encoding = 'utf - 8')
##        
##        self.read_file = self.f.read()
##        self.lbl.text = self.read_file
##    def build(self):
##        self.f = open('history.txt', 'r', encoding = 'utf - 8')
##
##        self.f2 = open('history.txt', 'a', encoding = 'utf - 8')
##        #self.f3 = open('history.txt', 'w', encoding = 'utf - 8')
##
##        self.read_file = self.f.read()


    
class UsualScreen(Screen):
    pass




screen_manager = ScreenManager() 

screen_manager.add_widget(EngineerScreen(name ="engineer")) 
screen_manager.add_widget(UsualScreen(name ="usual")) 
screen_manager.add_widget(HistoryScreen(name ="history")) 

class Main_CalculatorApp(App):
    def build(self):
        return screen_manager

        #self.config

      
       
            
Main_CalculatorApp().run()

#°	
#¹	
#²
'''

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string('''<EngineerScreen>:
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            orientation: 'horizontal'
            size_hint: (1, .035)
            spacing: 2
            

            Button:
                text:'History'
                on_press: app.screen_manager.current = 'history'
            Button:
                text:'Usual'
                on_press: app.screen_manager.current = 'usual'
            Button:
                text:'Engineer'
                on_press: app.screen_manager.current = 'engineer'

        Label:
            text:' '
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
                text:'C'
                on_press: self.zerospace
            Button:
                text:'pi'
                on_press: self.pi    
            Button:
                text:'X²'
                on_press: self.xtwo
            Button:
                text:'1/x'
                on_press: self.drob
            Button:
                text:'<'
                on_press: self.backspace
            Button:
                text:'log'
                on_press: self.log
            Button:
                text:'√X'
                on_press: self.sqrt
            Button:
                text:'()'
                on_press: self.func    
            Button:
                text:'|x|'
                on_press: self.fabs
            Button:
                text:'+'
                on_press: self.add_operation    
            Button:
                text:'cos'
                on_press: self.cos
            Button:
                text:'7'
                on_press: self.add_number
            Button:
                text:'8'
                on_press: self.add_number
            Button:
                text:'9'
                on_press: self.add_number
            Button:
                text:'-'
                on_press: self.add_operation
            Button:
                text:'sin'
                on_press: self.add_number    
            Button:
                text:'4'
                on_press: self.add_number
            Button:
                text:'5'
                on_press: self.add_number
            Button:
                text:'6'
                on_press: self.add_number
            Button:
                text:'/'
                on_press: self.add_operation
            Button:
                text:'tan'
                on_press: self.add_number
            Button:
                text:'1'
                on_press: self.add_number
            Button:
                text:'2'
                on_press: self.add_number
            Button:
                text:'3'
                on_press: self.add_number
            Button:
                text:'*'
                on_press: self.add_operation
            Button:
                text:'ceil'
                on_press: self.add_number
            Button:
                text:'%'
                on_press: self.add_operation
            Button:
                text:'0'
                on_press: self.add_operation
            Button:
                text:'.'
                on_press: self.add_operation
            Button:
                text:'='
                on_press: calc_result

<UsualScreen>:
    BoxLayout:
        orientation: 'vertical'
        
        BoxLayout:
            size_hint: (1, .1)
            Button:
                text:'History'
                on_press: app.screen_manager.current = 'history'
            Button:
                text:'Usual'
                on_press: app.screen_manager.current = 'usual'
            Button:
                text:'Egineer'
                on_press: app.screen_manager.current = 'engineer'
        Label:
            text:' '
            color:[0,1,1,1]
            font_size: 32
            halign: 'right'
            size_hint: (1, .23)
            text_size: (365, 78)    

        GridLayout:
            cols: 5
            Button:
                text:'C'
                on_press:self.zerospace
            Button:
                text:'<'
                on_press:self.backspace
            Button:
                text:'|x|'
                on_press:self.fabs
            Button:
                text:'()'
                on_press:self.func
            Button:
                text:'7'
                on_press:self.add_number
            Button:
                text:'8'
                on_press:self.add_number    
            Button:
                text:'9'
                on_press:self.add_number    
            Button:
                text:'*'
                on_press:self.add_operation
            Button:
                text:'4'
                on_press:self.add_number
            Button:
                text:'7'
                on_press:self.add_number
            Button:
                text:'*'
                on_press:self.add_operation
            Button:
                text:'4'
                on_press:self.add_number
            Button:
                text:'5'
                on_press:self.add_number
            Button:
                text:'6'
                on_press:self.add_number
            Button:
                text:'-'
                on_press:self.add_operation
            Button:
                text:'1'
                on_press:self.add_number
            Button:
                text:'2'
                on_press:self.add_number
            Button:
                text:'3'
                on_press:self.add_number
            Button:
                text:'+'
                on_press:self.add_operation
            Button:
                text:'/'
                on_press:self.add_operation
            Button:
                text:'0'
                on_press:self.add_operation
            Button:
                text:'='
                on_press:self.calc_result

<HistoryScreen>:
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            Button:
                text:'History'
                on_press: root.manager.current = 'history'
            Button:
                text:'Usual'
                on_press: root.manager.current = 'usual'
            Button:
                text:'Egineer'
                on_press: root.manager.current = 'engineer'
        Label:
            text: 'history'                        #str(self.read_file)
            color:[0,1,1,1]
            font_size: 20
            size_hint: (1, .73)
            text_size: (355, 430)
        GridLayout:
            cols: 3
            spacing: -1
            size_hint: (1, .05)

            Widget
            Button:
                text: 'Delete'
                on_press: self.c_history
            Widget''')

# Declare both screens
class EngineerScreen(Screen):
    pass

class UsualScreen(Screen):
    pass

class HistoryScreen(Screen):
    pass

# Create the screen manager
'''sm = ScreenManager()
sm.add_widget(EngineerScreen(name='menu'))
sm.add_widget(UsualScreen(name='settings'))
sm.add_widget(HistoryScreen(name='settings'))'''


   
# Add the screens to the manager and then supply a name 
# that is used to switch screens 


  
# Create the App class 
class CalculatorApp(App): 
    def build(self): 
        screen_manager = ScreenManager()
        screen_manager.add_widget(UsualScreen(name ="usual")) 
        screen_manager.add_widget(EngineerScreen(name ="engineer")) 
        screen_manager.add_widget(HistoryScreen(name ="history")) 
        return screen_manager 
  



if __name__ == '__main__':
    CalculatorApp().run()








