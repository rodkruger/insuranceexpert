import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput

kivy.require('1.11.1')


class MainScreen(BoxLayout):
    main_layout = BoxLayout()

    # Common Widgets
    wgt_cpf_negativado = CheckBox()
    wgt_age = TextInput()
    wgt_children = TextInput()
    wgt_marital_status = TextInput()
    wgt_gender = TextInput()
    wgt_unemployed = CheckBox()
    wgt_height = TextInput()
    wgt_weight = TextInput()
    wgt_pregnant = CheckBox()
    wgt_serasa_score = TextInput()
    wgt_profession = TextInput()

    # Widgets for Life Insurance
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
    wgt_diabetes = CheckBox()
    wgt_arterial_hypertension = CheckBox()
    wgt_sports_practice = CheckBox()
    wgt_travels = TextInput(width=100, size_hint=(None, 1))
    wgt_neurological_disease = CheckBox()
    wgt_surgery = CheckBox()
    wgt_pacemaker = CheckBox()
    wgt_auto_immune_disease = CheckBox()
    wgt_heart_disease = CheckBox()
    wgt_cancer = CheckBox()
    wgt_blood_type = Spinner(width=100, size_hint=(None, 1), values=('O', 'A', 'B', 'AB'))
    wgt_celia = CheckBox()
    wgt_lactose_intolerance = CheckBox()
    wgt_terminal_disease = CheckBox()
    wgt_vaccine_polio = CheckBox()
    wgt_vaccine_meningite = CheckBox()
    wgt_vaccine_yellow_fever = CheckBox()
    wgt_africa_travel = CheckBox()
    wgt_war_travel = CheckBox()
    wgt_shoot_practice = CheckBox()
    wgt_transplant = CheckBox()
    wgt_heart_attack = CheckBox()
    wgt_stroke = CheckBox()
    wgt_deficiencies = CheckBox()
    wgt_osteoarthritis = CheckBox()
    wgt_controlled_medication = CheckBox()
    wgt_sexual_disease = CheckBox()
    wgt_hepatitis = CheckBox()
    wgt_health_plan = CheckBox()
    wgt_life_coverage_type = TextInput(width=100, size_hint=(None, 1))
    wgt_heart_congenital = CheckBox()

    # Widgets for Car Insurance
    wgt_brand = Spinner(width=100, size_hint=(None, 1),
                        values=('Toyota', 'Honda', 'Volkswagen', 'Chevrolet', 'Renault', 'Peugeot', 'Citröen', 'Fiat'))
    wgt_model = TextInput(width=100, size_hint=(None, 1))
    wgt_year = TextInput(width=100, size_hint=(None, 1))
    wgt_abs = CheckBox()
    wgt_airbags = CheckBox()
    wgt_third = CheckBox()
    wgt_reduced = CheckBox()
    wgt_theft = CheckBox()
    wgt_fire = CheckBox()
    wgt_drivers = TextInput(width=100, size_hint=(None, 1))
    wgt_garage = CheckBox()
    wgt_professional = CheckBox()
    wgt_backup_car = CheckBox()
    wgt_personal_passenger = CheckBox()
    wgt_accident = CheckBox()
    wgt_extra_fipe = CheckBox()
    wgt_tracker = CheckBox()
    wgt_theft_index = TextInput(width=100, size_hint=(None, 1))
    wgt_for_travel = CheckBox()
    wgt_car_coverage_type = TextInput(width=100, size_hint=(None, 1))
    wgt_combustible_materials = CheckBox()

    # Widgets for Home Insurance
    wgt_dangerous_neighbour = CheckBox()
    wgt_natural_risk = CheckBox()
    wgt_under_construction = CheckBox()
    wgt_has_alarm = CheckBox()
    wgt_historical = CheckBox()
    wgt_shared = CheckBox()
    wgt_residence_type = Spinner(width=100, size_hint=(None, 1),
                                 values=('Apartamento', 'Casa', 'Sobrado'))
    wgt_number_of_electronics = TextInput(width=100, size_hint=(None, 1))
    wgt_value_of_goods = TextInput(width=100, size_hint=(None, 1))
    wgt_has_safe_box = CheckBox()
    wgt_needs_emergencial_services = CheckBox()
    wgt_insurance_claim = CheckBox()
    wgt_home_coverage_type = Spinner(width=100, size_hint=(None, 1),
                                     values=('Básica', 'Normal', 'Premium'))

    # Widgets for Risk Analysis
    wgt_points = TextInput()

    # Buttons
    wgt_btn_show_common = Button(text="Dados básicos", size_hint=(1, .25))
    wgt_btn_show_life = Button(text="Seguro de Vida", size_hint=(1, .25))
    wgt_btn_show_home = Button(text="Seguro Residencial", size_hint=(1, .25))
    wgt_btn_show_car = Button(text="Seguro de Automóvel", size_hint=(1, .25))

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        self.orientation = 'vertical'

        self.add_widget(self.main_layout)

        self.fillCommon()
        self.fillButtons()

    def fillCommon(self):
        common_lyt = GridLayout(cols=2, row_force_default=True, row_default_height=30)
        common_lyt.cols_minimum[0] = 175
        common_lyt.cols_minimum[1] = 200

        common_lyt.add_widget(Label(text='CPF negativado?'))
        common_lyt.add_widget(self.wgt_cpf_negativado)
        common_lyt.add_widget(Label(text='Idade'))
        common_lyt.add_widget(self.wgt_age)
        common_lyt.add_widget(Label(text='Indicador do serasa'))
        common_lyt.add_widget(self.wgt_serasa_score)
        common_lyt.add_widget(Label(text='Número de filhos'))
        common_lyt.add_widget(self.wgt_children)
        common_lyt.add_widget(Label(text='Estado civil'))
        common_lyt.add_widget(self.wgt_marital_status)
        common_lyt.add_widget(Label(text='Está desempregado?'))
        common_lyt.add_widget(self.wgt_unemployed)
        common_lyt.add_widget(Label(text='Altura'))
        common_lyt.add_widget(self.wgt_height)
        common_lyt.add_widget(Label(text='Peso'))
        common_lyt.add_widget(self.wgt_weight)
        common_lyt.add_widget(Label(text='Profissão'))
        common_lyt.add_widget(self.wgt_profession)
        common_lyt.add_widget(Label(text='Está grávida?'))
        common_lyt.add_widget(self.wgt_pregnant)
        common_lyt.add_widget(Label(text='Sexo'))
        common_lyt.add_widget(self.wgt_gender)

        self.main_layout.add_widget(common_lyt)

    def fillButtons(self):
        buttons_lyt = BoxLayout(orientation='horizontal')
        buttons_lyt.add_widget(self.wgt_btn_show_common)
        buttons_lyt.add_widget(self.wgt_btn_show_life)
        buttons_lyt.add_widget(self.wgt_btn_show_home)
        buttons_lyt.add_widget(self.wgt_btn_show_car)

        self.wgt_btn_show_common.bind(on_press=self.on_wgt_btn_show_common_press)
        self.wgt_btn_show_life.bind(on_press=self.on_wgt_btn_show_life_press)
        self.wgt_btn_show_home.bind(on_press=self.on_wgt_btn_show_home_press)
        self.wgt_btn_show_car.bind(on_press=self.on_wgt_btn_show_car_press)

        self.add_widget(buttons_lyt)

    def fillLifeInsurance(self):
        life_insurance_lyt = BoxLayout(orientation='vertical')
        life_insurance_lyt.add_widget(Label(text='Seguro de Vida', size_hint_x=None, width=100))

        life_insurance_rules_lyt = GridLayout(cols=6, row_default_height=30)

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
        life_insurance_rules_lyt.add_widget(Label(text='Portador de diabetes'))
        life_insurance_rules_lyt.add_widget(self.wgt_diabetes)
        life_insurance_rules_lyt.add_widget(Label(text='Possui hipertensão arterial'))
        life_insurance_rules_lyt.add_widget(self.wgt_arterial_hypertension)
        life_insurance_rules_lyt.add_widget(Label(text='Pratica esportes regularmente?'))
        life_insurance_rules_lyt.add_widget(self.wgt_sports_practice)
        life_insurance_rules_lyt.add_widget(Label(text='Número de viagens por ano'))
        life_insurance_rules_lyt.add_widget(self.wgt_travels)
        life_insurance_rules_lyt.add_widget(Label(text='Portador de doença neurológica?'))
        life_insurance_rules_lyt.add_widget(self.wgt_neurological_disease)
        life_insurance_rules_lyt.add_widget(Label(text='Realizou cirurgia de grande porte?'))
        life_insurance_rules_lyt.add_widget(self.wgt_surgery)
        life_insurance_rules_lyt.add_widget(Label(text='Possui marcapasso?'))
        life_insurance_rules_lyt.add_widget(self.wgt_pacemaker)
        life_insurance_rules_lyt.add_widget(Label(text='Portador de doença auto imune?'))
        life_insurance_rules_lyt.add_widget(self.wgt_auto_immune_disease)
        life_insurance_rules_lyt.add_widget(Label(text='Portador de doença cardíaca?'))
        life_insurance_rules_lyt.add_widget(self.wgt_heart_disease)
        life_insurance_rules_lyt.add_widget(Label(text='Portador de câncer?'))
        life_insurance_rules_lyt.add_widget(self.wgt_cancer)
        life_insurance_rules_lyt.add_widget(Label(text='Tipo sanguíneo'))
        life_insurance_rules_lyt.add_widget(self.wgt_blood_type)
        life_insurance_rules_lyt.add_widget(Label(text='Portador de doença celíaca?'))
        life_insurance_rules_lyt.add_widget(self.wgt_celia)
        life_insurance_rules_lyt.add_widget(Label(text='Intolerância à Lactose?'))
        life_insurance_rules_lyt.add_widget(self.wgt_lactose_intolerance)
        life_insurance_rules_lyt.add_widget(Label(text='Portador de alguma toença em estágio terminal?'))
        life_insurance_rules_lyt.add_widget(self.wgt_terminal_disease)
        life_insurance_rules_lyt.add_widget(Label(text='Viaja para a África?'))
        life_insurance_rules_lyt.add_widget(self.wgt_africa_travel)
        life_insurance_rules_lyt.add_widget(Label(text='Viaja para países em guerra?'))
        life_insurance_rules_lyt.add_widget(self.wgt_war_travel)
        life_insurance_rules_lyt.add_widget(Label(text='Pratica esporte de tiros?'))
        life_insurance_rules_lyt.add_widget(self.wgt_shoot_practice)
        life_insurance_rules_lyt.add_widget(Label(text='Já realizou transplantes?'))
        life_insurance_rules_lyt.add_widget(self.wgt_transplant)
        life_insurance_rules_lyt.add_widget(Label(text='Já teve infarte?'))
        life_insurance_rules_lyt.add_widget(self.wgt_heart_attack)
        life_insurance_rules_lyt.add_widget(Label(text='Já teve AVC?'))
        life_insurance_rules_lyt.add_widget(self.wgt_stroke)
        life_insurance_rules_lyt.add_widget(Label(text='Possui alguma deficiência física?'))
        life_insurance_rules_lyt.add_widget(self.wgt_deficiencies)
        life_insurance_rules_lyt.add_widget(Label(text='Cardiopatia congênita?'))
        life_insurance_rules_lyt.add_widget(self.wgt_heart_congenital)
        life_insurance_rules_lyt.add_widget(Label(text='Artrose?'))
        life_insurance_rules_lyt.add_widget(self.wgt_osteoarthritis)
        life_insurance_rules_lyt.add_widget(Label(text='Faz uso de medicamento controlado?'))
        life_insurance_rules_lyt.add_widget(self.wgt_controlled_medication)
        life_insurance_rules_lyt.add_widget(Label(text='É portador de doença sexualmente transmissível incurável?'))
        life_insurance_rules_lyt.add_widget(self.wgt_sexual_disease)
        life_insurance_rules_lyt.add_widget(Label(text='É portador de Hepatite B?'))
        life_insurance_rules_lyt.add_widget(self.wgt_hepatitis)
        life_insurance_rules_lyt.add_widget(Label(text='Possui plano de saúde?'))
        life_insurance_rules_lyt.add_widget(self.wgt_health_plan)
        life_insurance_rules_lyt.add_widget(Label(text='Tipo de Cobertura'))
        life_insurance_rules_lyt.add_widget(self.wgt_life_coverage_type)

        life_insurance_lyt.add_widget(life_insurance_rules_lyt)

        self.main_layout.add_widget(life_insurance_lyt)

    def fillCarInsurance(self):
        car_insurance_lyt = BoxLayout(orientation='vertical')

        car_insurance_lyt.add_widget(Label(text='Seguro de Automóvel', size_hint_x=None, width=100))

        car_insurance_rules_lyt = GridLayout(cols=4, row_default_height=30)

        car_insurance_rules_lyt.add_widget(Label(text='Marca'))
        car_insurance_rules_lyt.add_widget(self.wgt_brand)
        car_insurance_rules_lyt.add_widget(Label(text='Modelo'))
        car_insurance_rules_lyt.add_widget(self.wgt_model)
        car_insurance_rules_lyt.add_widget(Label(text='Possui ABS?'))
        car_insurance_rules_lyt.add_widget(self.wgt_abs)
        car_insurance_rules_lyt.add_widget(Label(text='Possui Airbags?'))
        car_insurance_rules_lyt.add_widget(self.wgt_airbags)
        car_insurance_rules_lyt.add_widget(Label(text='Seguro contra terceiros?'))
        car_insurance_rules_lyt.add_widget(self.wgt_third)
        car_insurance_rules_lyt.add_widget(Label(text='Franquia reduzida?'))
        car_insurance_rules_lyt.add_widget(self.wgt_reduced)
        car_insurance_rules_lyt.add_widget(Label(text='Roubo?'))
        car_insurance_rules_lyt.add_widget(self.wgt_theft)
        car_insurance_rules_lyt.add_widget(Label(text='Incêndio?'))
        car_insurance_rules_lyt.add_widget(self.wgt_fire)
        car_insurance_rules_lyt.add_widget(Label(text='Número de Motoristas'))
        car_insurance_rules_lyt.add_widget(self.wgt_drivers)
        car_insurance_rules_lyt.add_widget(Label(text='Veículo é guardado em garagem fechada ou coberta?'))
        car_insurance_rules_lyt.add_widget(self.wgt_garage)
        car_insurance_rules_lyt.add_widget(Label(text='Veículo é utilizado para fins profissionais?'))
        car_insurance_rules_lyt.add_widget(self.wgt_professional)
        car_insurance_rules_lyt.add_widget(Label(text='Carro reserva?'))
        car_insurance_rules_lyt.add_widget(self.wgt_backup_car)
        car_insurance_rules_lyt.add_widget(Label(text='Acidentes pessoais de passageiros'))
        car_insurance_rules_lyt.add_widget(self.wgt_personal_passenger)
        car_insurance_rules_lyt.add_widget(Label(text='Condutor se acidentou nos últimos 2 anos?'))
        car_insurance_rules_lyt.add_widget(self.wgt_accident)
        car_insurance_rules_lyt.add_widget(Label(text='110% da Fipe?'))
        car_insurance_rules_lyt.add_widget(self.wgt_extra_fipe)
        car_insurance_rules_lyt.add_widget(Label(text='Rastreador?'))
        car_insurance_rules_lyt.add_widget(self.wgt_tracker)
        car_insurance_rules_lyt.add_widget(Label(text='Índice de roubo do veículo'))
        car_insurance_rules_lyt.add_widget(self.wgt_theft_index)
        car_insurance_rules_lyt.add_widget(Label(text='Veículo utilizado para viagens?'))
        car_insurance_rules_lyt.add_widget(self.wgt_for_travel)
        car_insurance_rules_lyt.add_widget(Label(text='Tipo de cobertura'))
        car_insurance_rules_lyt.add_widget(self.wgt_car_coverage_type)
        car_insurance_rules_lyt.add_widget(Label(text='Número de pontos'))
        car_insurance_rules_lyt.add_widget(self.wgt_points)

        car_insurance_lyt.add_widget(car_insurance_rules_lyt)

        self.main_layout.add_widget(car_insurance_lyt)

    def fillHomeInsurance(self):
        home_insurance_lyt = BoxLayout(orientation='vertical')
        home_insurance_lyt.add_widget(Label(text='Seguro Residencial', size_hint_x=None, width=100))

        home_insurance_rules_lyt = GridLayout(cols=4, row_default_height=30)

        home_insurance_rules_lyt.add_widget(Label(text='Habita em região perigosa?'))
        home_insurance_rules_lyt.add_widget(self.wgt_dangerous_neighbour)
        home_insurance_rules_lyt.add_widget(Label(text='Habita em zonas de riscos naturais?'))
        home_insurance_rules_lyt.add_widget(self.wgt_natural_risk)
        home_insurance_rules_lyt.add_widget(Label(text='Imóvel está em construção?'))
        home_insurance_rules_lyt.add_widget(self.wgt_under_construction)
        home_insurance_rules_lyt.add_widget(Label(text='Imóvel possui alarme?'))
        home_insurance_rules_lyt.add_widget(self.wgt_has_alarm)
        home_insurance_rules_lyt.add_widget(Label(text='Imóvel é tombado como patrimônio histórico?'))
        home_insurance_rules_lyt.add_widget(self.wgt_historical)
        home_insurance_rules_lyt.add_widget(Label(text='Imóvel é usado como república ou moradia coletiva?'))
        home_insurance_rules_lyt.add_widget(self.wgt_shared)
        home_insurance_rules_lyt.add_widget(Label(text='Tipo de moradia'))
        home_insurance_rules_lyt.add_widget(self.wgt_residence_type)
        home_insurance_rules_lyt.add_widget(Label(text='Imóvel utiliza materiais combustíveis?'))
        home_insurance_rules_lyt.add_widget(self.wgt_combustible_materials)
        home_insurance_rules_lyt.add_widget(Label(text='Número de eletrônicos'))
        home_insurance_rules_lyt.add_widget(self.wgt_number_of_electronics)
        home_insurance_rules_lyt.add_widget(Label(text='Valor dos bens'))
        home_insurance_rules_lyt.add_widget(self.wgt_value_of_goods)
        home_insurance_rules_lyt.add_widget(Label(text='Possui cofre?'))
        home_insurance_rules_lyt.add_widget(self.wgt_has_safe_box)
        home_insurance_rules_lyt.add_widget(Label(text='Necessita de serviços emergenciais?'))
        home_insurance_rules_lyt.add_widget(self.wgt_needs_emergencial_services)
        home_insurance_rules_lyt.add_widget(Label(text='Já houve sinistro no imóvel?'))
        home_insurance_rules_lyt.add_widget(self.wgt_insurance_claim)
        home_insurance_rules_lyt.add_widget(Label(text='Tipo de cobertura'))
        home_insurance_rules_lyt.add_widget(self.wgt_home_coverage_type)

        home_insurance_lyt.add_widget(home_insurance_rules_lyt)

        self.main_layout.add_widget(home_insurance_lyt)

    def on_wgt_btn_show_common_press(instance, value):
        instance.main_layout.clear_widgets()
        instance.fillCommon()

    def on_wgt_btn_show_life_press(instance, value):
        instance.main_layout.clear_widgets()
        instance.fillLifeInsurance()

    def on_wgt_btn_show_home_press(instance, value):
        instance.main_layout.clear_widgets()
        instance.fillHomeInsurance()

    def on_wgt_btn_show_car_press(instance, value):
        instance.main_layout.clear_widgets()
        instance.fillCarInsurance()


class MyApp(App):

    def build(self):
        self.title = 'Insurance Expert v1.0'

        return MainScreen()


if __name__ == '__main__':
    MyApp().run()
