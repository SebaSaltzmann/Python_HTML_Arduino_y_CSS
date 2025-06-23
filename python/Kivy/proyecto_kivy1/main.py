from kivy.config import Config
Config.set('graphics', 'width', '393')
Config.set('graphics', 'height', '852')

from main import KV
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDFloatingActionButton
from kivymd.app import MDApp

class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

if __name__ == '__main__':
    MyApp().run()
