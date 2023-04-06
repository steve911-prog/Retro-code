from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.codeinput import CodeInput
#from pygments.lexers import HtmlLexer
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter

Config.set('graphics','resizable','1')#Win is changed or no
Config.set('graphics','width','590') #Sizes of your window
Config.set('graphics','height','490')

class MyApp(App):
    def build(self):
        #return CodeInput(lexer = HtmlLexer())
        s = Scatter()
        fl = FloatLayout(size = (300,300))
        s.add_widget(fl)
        fl.add_widget(Button(
                      text = 'Hello, Kivy!',
                      font_size = 34,
                      on_press = self.btn_press,   #Press button
                      background_color = [0,19,83,255],
                      background_normal = '',
                      size_hint = (.5, .25),
                      pos = (150 ,180)))
        
        return s
        
    def btn_press(self, instance):
        instance.text = 'I pressed'

'''
from kivy.core.audio import SoundLoader

sound = SoundLoader.load('sergey-briksa-mir-ne-prost-2014.mp3')
if sound:
    sound.play()

'''














MyApp().run()
