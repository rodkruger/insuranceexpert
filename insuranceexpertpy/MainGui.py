from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class MainScreen(GridLayout):
    # Widgets for Life Insurance
    wgt_cpf_negativado = CheckBox()
    wgt_radical_sports = CheckBox()
    wgt_racing_driver = CheckBox()
    wgt_use_drugs = CheckBox()
    wgt_serious_diseases = CheckBox()
    wgt_medical_monitoring = CheckBox()
    wgt_invalidity = CheckBox()
    wgt_smoker = CheckBox()
    wgt_alcohol = CheckBox()
    wgt_dangerous_zone = CheckBox()
    wgt_airline_crew = CheckBox()
    wgt_age = TextInput()
    wgt_diabetes = CheckBox()
    wgt_profession = TextInput()
    wgt_arterial_hypertension = CheckBox()
    wgt_sports_practice = CheckBox()
    wgt_serasa_score = TextInput()
    wgt_children = TextInput()
    wgt_marital_status = TextInput()
    wgt_travels = TextInput()
    wgt_neurological_disease = CheckBox()

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        self.cols = 3
        self.rows = 1

        life_insurance_lyt = BoxLayout(orientation='vertical')
        life_insurance_lyt.add_widget(Label(text='Seguro de Vida', size_hint_x=None, width=100))

        life_insurance_rules_lyt = GridLayout(cols=2)
        life_insurance_rules_lyt.add_widget(Label(text='CPF negativado?'))
        life_insurance_rules_lyt.add_widget(self.wgt_cpf_negativado)
        life_insurance_rules_lyt.add_widget(Label(text='Pratica esportes radicais?'))
        life_insurance_rules_lyt.add_widget(self.wgt_radical_sports)
        life_insurance_rules_lyt.add_widget(Label(text='É piloto de corrida?'))
        life_insurance_rules_lyt.add_widget(self.wgt_racing_driver)
        life_insurance_rules_lyt.add_widget(Label(text='Utiliza ou já utilizou drogas?'))
        life_insurance_rules_lyt.add_widget(self.wgt_use_drugs)
        life_insurance_rules_lyt.add_widget(Label(text='É portador de doenças graves?'))
        life_insurance_rules_lyt.add_widget(self.wgt_serious_diseases)
        life_insurance_rules_lyt.add_widget(Label(text='Realiza acompanhamento médico periódico?'))
        life_insurance_rules_lyt.add_widget(self.wgt_medical_monitoring)
        life_insurance_rules_lyt.add_widget(Label(text='Já recebeu indenização por invalidez?'))
        life_insurance_rules_lyt.add_widget(self.wgt_invalidity)
        life_insurance_rules_lyt.add_widget(Label(text='É fumante?'))
        life_insurance_rules_lyt.add_widget(self.wgt_smoker)
        life_insurance_rules_lyt.add_widget(Label(text='Faz uso freqüente de bebidas alcoólicas?'))
        life_insurance_rules_lyt.add_widget(self.wgt_alcohol)
        life_insurance_rules_lyt.add_widget(Label(text='Habita em regiões perigosas?'))
        life_insurance_rules_lyt.add_widget(self.wgt_dangerous_zone)
        life_insurance_rules_lyt.add_widget(Label(text='Realiza atividades profissionais a bordo de aeronaves?'))
        life_insurance_rules_lyt.add_widget(self.wgt_airline_crew)
        life_insurance_rules_lyt.add_widget(Label(text='Idade'))
        life_insurance_rules_lyt.add_widget(self.wgt_age)
        life_insurance_rules_lyt.add_widget(Label(text='Portador de diabetes'))
        life_insurance_rules_lyt.add_widget(self.wgt_diabetes)
        life_insurance_rules_lyt.add_widget(Label(text='Profession'))
        life_insurance_rules_lyt.add_widget(self.wgt_profession)
        life_insurance_rules_lyt.add_widget(Label(text='Possui hipertensão arterial'))
        life_insurance_rules_lyt.add_widget(self.wgt_arterial_hypertension)
        life_insurance_rules_lyt.add_widget(Label(text='Pratica esportes regularmente?'))
        life_insurance_rules_lyt.add_widget(self.wgt_sports_practice)
        life_insurance_rules_lyt.add_widget(Label(text='Indicador do serasa'))
        life_insurance_rules_lyt.add_widget(self.wgt_serasa_score)
        life_insurance_rules_lyt.add_widget(Label(text='Número de filhos'))
        life_insurance_rules_lyt.add_widget(self.wgt_children)
        life_insurance_rules_lyt.add_widget(Label(text='Estado civil'))
        life_insurance_rules_lyt.add_widget(self.wgt_marital_status)
        life_insurance_rules_lyt.add_widget(Label(text='Número de viagens por ano'))
        life_insurance_rules_lyt.add_widget(self.wgt_travels)
        life_insurance_rules_lyt.add_widget(Label(text='Portador de doença neurológica?'))
        life_insurance_rules_lyt.add_widget(self.wgt_neurological_disease)

        life_insurance_lyt.add_widget(life_insurance_rules_lyt)

        self.add_widget(life_insurance_lyt)

        home_insurance_lyt = BoxLayout(orientation='vertical')
        home_insurance_lyt.add_widget(Label(text='Seguro Residencial', size_hint_x=None, width=100))

        home_insurance_rules_lyt = GridLayout(cols=2)
        home_insurance_rules_lyt.add_widget(Label(text='CPF negativado?'))
        home_insurance_rules_lyt.add_widget(CheckBox())
        home_insurance_rules_lyt.add_widget(Label(text='É homem?'))
        home_insurance_rules_lyt.add_widget(CheckBox())

        home_insurance_lyt.add_widget(home_insurance_rules_lyt)

        self.add_widget(home_insurance_lyt)

        auto_insurance_lyt = BoxLayout(orientation='vertical')
        auto_insurance_lyt.add_widget(Label(text='Seguro de Automóvel', size_hint_x=None, width=100))

        auto_insurance_rules_lyt = GridLayout(cols=2)
        auto_insurance_rules_lyt.add_widget(Label(text='CPF negativado?'))
        auto_insurance_rules_lyt.add_widget(CheckBox())
        auto_insurance_rules_lyt.add_widget(Label(text='É homem?'))
        auto_insurance_rules_lyt.add_widget(CheckBox())

        auto_insurance_lyt.add_widget(auto_insurance_rules_lyt)

        self.add_widget(auto_insurance_lyt)


class MyApp(App):

    def build(self):
        return MainScreen()


if __name__ == '__main__':
    MyApp().run()
