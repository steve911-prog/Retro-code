from kivy.app import App
from kivy.lang import Builder

kv = Builder.load_file('build.kv')

class MyMainApp(App):
    def build(self):
        
        return kv


MyMainApp.run(1)    
