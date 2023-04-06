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




class Cal_HApp(App):
    def add_story(self, instance):
       
        self.f2.write("\n" + self.lbl.text + '=' + eval(self.lbl.text))

    def c_history(self, instance):
        self.f2.seek(0)
        self.f2.truncate()
        #self.read_file = self.f.read()
        self.f2.close()
        self.f2= open('history.txt', 'a', encoding = 'utf - 8')
        #self.f3 = open('history.txt', 'w', encoding = 'utf - 8')
        self.read_file = self.f.read()
        self.lbl.text = self.read_file

    #words_file = open('words.txt', 'r', encoding = 'utf - 8')
    #list_words = words_file.read().split()
       


    ##### don't
            ### forget
            ######tooooo
                 #############addd
                            ################ RecycleView

        
    def build(self):
            self.formula = ' '
        
            bl = BoxLayout(orientation = 'vertical')
            gl = GridLayout(cols = 3, spacing = -1, size_hint = (1, .05))

            self.f = open('history.txt', 'r', encoding = 'utf - 8')

            self.f2 = open('history.txt', 'a', encoding = 'utf - 8')
            #self.f3 = open('history.txt', 'w', encoding = 'utf - 8')

            self.read_file = self.f.read()
            print(self.read_file)
            self.lbl = Label(text = str(self.read_file) ,color = [0,1,1,1],font_size = 20,\
                             size_hint = (1, .73), text_size = (355, 430))

            bl2 = BoxLayout(orientation = 'horizontal', size_hint = (1, .05), spacing = 2)
   
            bl2.add_widget(Button(text = 'History'))
            bl2.add_widget(Button(text = 'Usual'))
            bl2.add_widget(Button(text = 'Engineer'))
            bl2.add_widget(Widget())

            bl.add_widget(bl2)              
            bl.add_widget(self.lbl)
        
            gl.add_widget(Widget())
            gl.add_widget(Button(text = 'Delete', on_press = self.c_history))
            gl.add_widget(Widget())
            
            
            bl.add_widget(gl)   
            return bl    
            
      
      
  
      
       
            
Cal_HApp().run()

#°	
#¹	
#²
