from kivy.config import Config
Config.set('graphics', 'width', '393')
Config.set('graphics', 'height', '852')

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp


KV = '''
ScreenManager:
    MenuScreen:
    SettingsScreen:

<MenuScreen>:
    name: 'menu'
    MDLabel:
        text: 'Pantalla de inicio'
        halign: 'center'
    MDIconButton:
        icon: "heart-outline"
        style: "tonal"
        theme_bg_color: "Custom"
        md_bg_color: "brown"
        theme_icon_color: "Custom"
        icon_color: "white"
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        on_release:
            root.manager.current = 'settings'
    MDFabButton:
        icon: "pencil-outline"
        style: "large"
        pos_hint: {'center_x': 0.9, 'center_y': 0.9}

<SettingsScreen>:
    name: 'settings'
    MDLabel:
        text: 'Pantalla de configuración'
        halign: 'center'
    MDRaisedButton:
        text: 'Volver al menú'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        on_release:
            root.manager.current = 'menu'
'''

class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

if __name__ == '__main__':
    MyApp().run()
