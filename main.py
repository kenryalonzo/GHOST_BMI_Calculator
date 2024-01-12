from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.properties import ObjectProperty
from package.session import Session

from screen_manager import MyScreenManager

class ScreenBrowser(MyScreenManager):
    pass

class MainApp(App):
    manage = ObjectProperty()
    def build(self):
        self.manage = ScreenBrowser()
        status = Session.get_session()['status']
        if status:
            self.manage.current = "index"
        return self.manage
    pass


app = MainApp()
app.run()