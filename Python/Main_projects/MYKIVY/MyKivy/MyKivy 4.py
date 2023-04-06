from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config

from kivy.uix.widget import Widget
from kivy.graphics import (Ellipse, Rectangle, Line,\
                           Color)

from random import *

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

Config.set('graphics','resizable','1')#Win is changed or no
Config.set('graphics','width','700') #Sizes of your window
Config.set('graphics','height','500')



class PainterWidget(Widget):
    #def __init__(self, **kwargs):
        #super(PainterWidget, self).__init__(**kwargs)
    def  on_touch_down(self, touch):
        with self.canvas:
            Color(random(),random(),random(),1)

            rad = 10
            
            Ellipse(pos = (touch.x - 5, touch.y - 5), size = (rad, rad))
            #Line(points = (100, 100, 151, 200, 201,100),\
            #    close = True, width = 7)
            #self.line = Line(points = (), width = 12,\
            #                joint = 'miter') #cap = 'round' )

            touch.ud['line'] = Line(points = (touch.x , touch.y),\
                                    width = 13)
    def on_touch_move(self, touch):
        touch.ud['line'].points += (touch.x , touch.y)


    #def on_touch_down(self, touch):
    #    self.line.points += (touch.x , touch.y)
class PyDApp(App):
   def build(self):
       parent = Widget()
       self.painter = PainterWidget()
       parent.add_widget(self.painter)

       parent.add_widget(\
           Button(text = 'Clear',\
                  on_press = self.clear_canvas,size = (100, 50)))
       parent.add_widget(Button(text = 'Save',
                             on_press = self.save, size = (100, 50),\
        pos = (100,0)))
               

        

       return parent
   def clear_canvas(self, insatnce):
       self.painter.canvas.clear()

   def save(self, instance):
       self.painter.size = (700, 500) 
       self.painter.export_to_png('image.png')
   
            
PyDApp().run()


































