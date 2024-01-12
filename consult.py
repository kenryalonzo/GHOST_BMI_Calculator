from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import StringProperty
from package.Data import Data

from package.session import Session

Builder.load_file("consult.kv")


class ConsultBmi(BoxLayout):
    imc = StringProperty()
    
    def preload_data(self):
        session = Session.get_session()
        self.imc = str(session['sante']['imc'])
        pass
    pass