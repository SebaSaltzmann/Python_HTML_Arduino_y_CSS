from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.label = Label(text="Hola mundo")
        self.add_widget(self.label)
        btn = Button(text="Cambiar texto")
        btn.bind(on_press=self.change_text)
        self.add_widget(btn)

    def change_text(self, instance):
        self.label.text = "Has presionado un botón"

class TestApp(App):
    def build(self):
        return MyBoxLayout()
    
if __name__ == "__main__":
    TestApp().run()