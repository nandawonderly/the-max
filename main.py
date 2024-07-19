import kivy
import pandas as pd
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.base import Builder
from kivy.uix.popup import Popup

Window.clearcolor = (1,1,1)  # Branco
Window.size = (500,700)

dados1 = {
    "Turmas": ["1111", "1112", "1113"]
}

dados2 = {
    "Disciplinas": ["Matemática", "Português", "História"]
}

df1 = pd.DataFrame(dados1)
df2 = pd.DataFrame(dados2)

nome_arquivo = "dados.xlsx"

with pd.ExcelWriter(nome_arquivo) as writer:
    df1.to_excel(writer, sheet_name='turmas', index=False)
    df2.to_excel(writer, sheet_name='disciplinas', index=False)

turmas_df = pd.read_excel('dados.xlsx', sheet_name='turmas')
disciplinas_df = pd.read_excel('dados.xlsx', sheet_name='disciplinas')

class HomeScreen(Screen):
    pass

class GridTurmas(GridLayout):
    def __init__(self, **kwargs):
        super(GridTurmas, self).__init__(**kwargs)
        self.cols = 3
        self.spacing = 10
        self.padding = 10
        self.size_hint = (None, None)
        self.size = (200, 200)

        nome_arquivo = "dados.xlsx"

        self.df = pd.read_excel(nome_arquivo)

        for index, row in self.df.iterrows():
            btn = Button(text=str(row['Turmas']),
                         size_hint=(None, None),
                         size=(100, 40))
            btn.bind(on_press=self.show_info)
            self.add_widget(btn)

    def show_info(self, instance):
        turma = instance.text
        info = self.df[self.df['Turmas'] == turma].iloc[0]

        info_text = f"Turmas: {info['Turmas']}"
        popup = Popup(title='Informações',
                      content=Label (text=info_text),
                      size_hint=(None, None), size=(300, 200))
        popup.open()

class TurmasScreen(Screen):
    pass
              
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