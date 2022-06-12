import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text='Hello world')

#TODO design application
#TODO get weather details
#TODO machine learning
#TODO connect script to application

if __name__ == '__main__':
    MyApp().run()