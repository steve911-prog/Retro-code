from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.anchorlayout import AnchorLayout 

class MyApp(App):
    def build(self):
        al =AnchorLayout()

        bl = BoxLayout(orientation = 'vertical', size_hint = [.4, .4])
        bl.add_widget(TextInput())
        bl.add_widget(TextInput())
        bl.add_widget(Button(text = 'X'))
        al.add_widget(bl)
        return al
                


MyApp().run()

