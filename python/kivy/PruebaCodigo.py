from kivy.config import Config
Config.set('graphics', 'width', '393')
Config.set('graphics', 'height', '852')

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton

KV = '''
MDScreen:
    MDRaisedButton:
        text: "Registrarse"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
    MDRaisedButton:
        text: "Iniciar sesión"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
'''

class MyApp(MDApp):
    def  build(self):
        return Builder.load_string(KV)
    
if __name__ == '__main__':
    MyApp().run()
