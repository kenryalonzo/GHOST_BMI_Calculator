from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.label import Label

from package.session import Session

Builder.load_file("signup.kv")

class SignUpPage(BoxLayout):
    def check_pseudo(self, widget:Label):
        status = Session.get_session()['status']
        if not status: 
            widget.opacity = 1
    pass