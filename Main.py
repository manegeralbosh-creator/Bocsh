from kivy.app import App
from kivy.uix.label import Label

class MySimpleApp(App):
    def build(self):
        return Label(text="Hello! This is my first app.")

if __name__ == "__main__":
    MySimpleApp().run()
