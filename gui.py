from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.textinput import TextInput


class MyDumbScreen(BoxLayout):  # Changed to a BoxLayout for simplicity
    pass



class MyApp(App):

    def build(self):
        Window.size = (300, 200)
        self.root =  MyDumbScreen()
        return self.root

    def callback(self, text):
        self.root.ids.textbox.text = "Hi"


if __name__ == '__main__':
    MyApp().run()