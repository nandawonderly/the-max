import kivy
import pandas as pd
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.base import Builder
from kivy.uix.popup import Popup

Window.clearcolor = (1,1,1)  # Branco
Window.size = (500,700)

turmas_df = pd.read_excel('dados.xlsx', sheet_name='turmas')
disciplinas_df = pd.read_excel('dados.xlsx', sheet_name='disciplinas')

class HomeScreen(Screen):
    pass

class TurmasScreen(Screen):
    def show_disciplinas(self, turma):
        disciplinas = disciplinas_df[disciplinas_df['ID_Turma'] == turma]['Disciplina'].tolist()
        content = FloatLayout(orientation='vertical')
        
        for disciplina in disciplinas:
            content.add_widget(Label(text=disciplina))
        
        close_button = Button(text='Fechar', size_hint=(1, 0.2))
        content.add_widget(close_button)
        
        popup = Popup(title=f'Disciplinas da Turma {turma}', content=content, size_hint=(0.8, 0.8))
        close_button.bind(on_release=popup.dismiss)
        popup.open()
              
class Nova(Screen):
    pass

class DisciplinasScreen(Screen):
    pass

class ProfessoresScreen(Screen):
    pass

class GradeScreen(Screen):
    pass

class ConfiguracoesScreen(Screen):
    pass

class NotificacoesScreen(Screen):
    pass

class NovaScreen(Screen):
    pass

class MainApp(App):
    def build(self):
        return Builder.load_file('main.kv')
        sm = ScreenManager()
        sm.add_widget(TurmasScreen(name='turmas'))
        return sm

if __name__ == '__main__':
    MainApp().run()