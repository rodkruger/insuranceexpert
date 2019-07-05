import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.modules import inspector
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from pyknow import Fact

from LifeInsurance import SeguroDeVida

kivy.require('1.11.1')


def convertStrToFloat(floatAsStr):
    if not floatAsStr:
        return 0
    else:
        return float(floatAsStr)


def convertStrToInt(intAsStr):
    if not intAsStr:
        return 0
    else:
        return float(intAsStr)


class MainScreen(BoxLayout):
    top_lyt = BoxLayout()
    main_lyt = BoxLayout()
    bottom_lyt = BoxLayout()

    # Common Widgets
    wgt_cpf_negativado = CheckBox(width=200, size_hint=(None, 1))
    wgt_age = TextInput(multiline=False, write_tab=False)
    wgt_children = TextInput(multiline=False, write_tab=False)
    wgt_marital_status = Spinner(width=200, size_hint=(None, 1), values=('Solteiro', 'Casado'))
    wgt_gender = Spinner(width=200, size_hint=(None, 1), values=('Masculino', 'Feminino'))
    wgt_unemployed = CheckBox(width=200, size_hint=(None, 1))
    wgt_height = TextInput(multiline=False, write_tab=False)
    wgt_weight = TextInput(multiline=False, write_tab=False)
    wgt_pregnant = CheckBox(width=200, size_hint=(None, 1))
    wgt_serasa_score = TextInput(multiline=False, write_tab=False)
    wgt_profession = Spinner(width=200, size_hint=(None, 1), values=('Engenheiro', 'Médico', 'Dentista'))

    # Widgets for Life Insurance
    wgt_radical_sports = CheckBox(width=200, size_hint=(None, 1))
    wgt_racing_driver = CheckBox(width=200, size_hint=(None, 1))
    wgt_use_drugs = CheckBox(width=200, size_hint=(None, 1))
    wgt_serious_diseases = CheckBox(width=200, size_hint=(None, 1))
    wgt_medical_monitoring = CheckBox(width=200, size_hint=(None, 1))
    wgt_invalidity = CheckBox(width=200, size_hint=(None, 1))
    wgt_smoker = CheckBox(width=200, size_hint=(None, 1))
    wgt_alcohol = CheckBox(width=200, size_hint=(None, 1))
    wgt_dangerous_zone = CheckBox(width=200, size_hint=(None, 1))
    wgt_airline_crew = CheckBox(width=200, size_hint=(None, 1))
    wgt_diabetes = CheckBox(width=200, size_hint=(None, 1))
    wgt_arterial_hypertension = CheckBox(width=200, size_hint=(None, 1))
    wgt_sports_practice = CheckBox(width=200, size_hint=(None, 1))
    wgt_travels = TextInput(width=200, size_hint=(None, 1), multiline=False, write_tab=False)
    wgt_neurological_disease = CheckBox(width=200, size_hint=(None, 1))
    wgt_surgery = CheckBox(width=200, size_hint=(None, 1))
    wgt_pacemaker = CheckBox(width=200, size_hint=(None, 1))
    wgt_auto_immune_disease = CheckBox(width=200, size_hint=(None, 1))
    wgt_heart_disease = CheckBox(width=200, size_hint=(None, 1))
    wgt_cancer = CheckBox(width=200, size_hint=(None, 1))
    wgt_blood_type = Spinner(width=200, size_hint=(None, 1), values=('O', 'A', 'B', 'AB'))
    wgt_celia = CheckBox(width=200, size_hint=(None, 1))
    wgt_lactose_intolerance = CheckBox(width=200, size_hint=(None, 1))
    wgt_terminal_disease = CheckBox(width=200, size_hint=(None, 1))
    wgt_vaccine_polio = CheckBox(width=200, size_hint=(None, 1))
    wgt_vaccine_meningite = CheckBox(width=200, size_hint=(None, 1))
    wgt_vaccine_yellow_fever = CheckBox(width=200, size_hint=(None, 1))
    wgt_africa_travel = CheckBox(width=200, size_hint=(None, 1))
    wgt_war_travel = CheckBox(width=200, size_hint=(None, 1))
    wgt_shoot_practice = CheckBox(width=200, size_hint=(None, 1))
    wgt_transplant = CheckBox(width=200, size_hint=(None, 1))
    wgt_heart_attack = CheckBox(width=200, size_hint=(None, 1))
    wgt_stroke = CheckBox(width=200, size_hint=(None, 1))
    wgt_deficiencies = CheckBox(width=200, size_hint=(None, 1))
    wgt_osteoarthritis = CheckBox(width=200, size_hint=(None, 1))
    wgt_controlled_medication = CheckBox(width=200, size_hint=(None, 1))
    wgt_sexual_disease = CheckBox(width=200, size_hint=(None, 1))
    wgt_hepatitis = CheckBox(width=200, size_hint=(None, 1))
    wgt_health_plan = CheckBox(width=200, size_hint=(None, 1))
    wgt_life_coverage_type = Spinner(width=200, size_hint=(None, 1), values=('Básica', 'Normal', 'Premium'))
    wgt_heart_congenital = CheckBox(width=200, size_hint=(None, 1))

    # Widgets for Car Insurance
    wgt_brand = Spinner(width=200, size_hint=(None, 1),
                        values=('Toyota', 'Honda', 'Volkswagen', 'Chevrolet', 'Renault', 'Peugeot', 'Citröen', 'Fiat'))
    wgt_model = TextInput(width=200, size_hint=(None, 1))
    wgt_year = TextInput(width=200, size_hint=(None, 1))
    wgt_abs = CheckBox(width=200, size_hint=(None, 1))
    wgt_airbags = CheckBox(width=200, size_hint=(None, 1))
    wgt_third = CheckBox(width=200, size_hint=(None, 1))
    wgt_reduced = CheckBox(width=200, size_hint=(None, 1))
    wgt_theft = CheckBox(width=200, size_hint=(None, 1))
    wgt_fire = CheckBox(width=200, size_hint=(None, 1))
    wgt_drivers = TextInput(width=200, size_hint=(None, 1))
    wgt_garage = CheckBox(width=200, size_hint=(None, 1))
    wgt_professional = CheckBox(width=200, size_hint=(None, 1))
    wgt_backup_car = CheckBox(width=200, size_hint=(None, 1))
    wgt_personal_passenger = CheckBox(width=200, size_hint=(None, 1))
    wgt_accident = CheckBox(width=200, size_hint=(None, 1))
    wgt_extra_fipe = CheckBox(width=200, size_hint=(None, 1))
    wgt_tracker = CheckBox(width=200, size_hint=(None, 1))
    wgt_theft_index = TextInput(width=200, size_hint=(None, 1))
    wgt_for_travel = CheckBox(width=200, size_hint=(None, 1))
    wgt_car_coverage_type = Spinner(width=200, size_hint=(None, 1), values=('Básica', 'Normal', 'Premium'))
    wgt_combustible_materials = CheckBox(width=200, size_hint=(None, 1))

    # Widgets for Home Insurance
    wgt_dangerous_neighbour = CheckBox(width=200, size_hint=(None, 1))
    wgt_natural_risk = CheckBox(width=200, size_hint=(None, 1))
    wgt_under_construction = CheckBox(width=200, size_hint=(None, 1))
    wgt_has_alarm = CheckBox(width=200, size_hint=(None, 1))
    wgt_historical = CheckBox(width=200, size_hint=(None, 1))
    wgt_shared = CheckBox(width=200, size_hint=(None, 1))
    wgt_residence_type = Spinner(width=200, size_hint=(None, 1),
                                 values=('Apartamento', 'Casa', 'Sobrado'))
    wgt_number_of_electronics = TextInput(width=200, size_hint=(None, 1))
    wgt_value_of_goods = TextInput(width=200, size_hint=(None, 1))
    wgt_has_safe_box = CheckBox(width=200, size_hint=(None, 1))
    wgt_needs_emergencial_services = CheckBox(width=200, size_hint=(None, 1))
    wgt_insurance_claim = CheckBox(width=200, size_hint=(None, 1))
    wgt_home_coverage_type = Spinner(width=200, size_hint=(None, 1),
                                     values=('Básica', 'Normal', 'Premium'))

    # Widgets for Risk Analysis
    wgt_points = TextInput()

    # Buttons
    wgt_btn_show_common = Button(text="Dados básicos", size_hint=(1, .25))
    wgt_btn_show_life = Button(text="Seguro de Vida", size_hint=(1, .25))
    wgt_btn_show_home = Button(text="Seguro Residencial", size_hint=(1, .25))
    wgt_btn_show_car = Button(text="Seguro de Automóvel", size_hint=(1, .25))
    wgt_btn_calculate = Button(text="Calcular", size_hint=(1, .25))

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        self.orientation = 'vertical'

        self.add_widget(self.top_lyt)
        self.add_widget(self.main_lyt)
        self.add_widget(self.bottom_lyt)

        self.fillHeader()
        self.fillCommon()
        self.fillButtons()

    def posInputField(self, theLabelText, theInputField, layout):
        aLabel = Label(text=theLabelText, halign="right", valign="middle")
        aLabel.bind(size=aLabel.setter('text_size'))
        layout.add_widget(aLabel)
        layout.add_widget(theInputField)
        return aLabel

    def fillHeader(self):


    def fillCommon(self):
        common_lyt = GridLayout(cols=2, row_force_default=True, row_default_height=30, size_hint=(None, 1), width=400)

        common_lyt.cols_minimum[0] = 200
        common_lyt.cols_minimum[1] = 200

        self.posInputField('Idade: ', self.wgt_age, common_lyt)
        self.posInputField('Indicador do serasa: ', self.wgt_serasa_score, common_lyt)
        self.posInputField('Número de filhos: ', self.wgt_children, common_lyt)
        self.posInputField('Estado civil: ', self.wgt_marital_status, common_lyt)
        self.posInputField('Altura: ', self.wgt_height, common_lyt)
        self.posInputField('Peso: ', self.wgt_weight, common_lyt)
        self.posInputField('Profissão: ', self.wgt_profession, common_lyt)
        self.posInputField('Sexo: ', self.wgt_gender, common_lyt)
        self.posInputField('CPF negativado: ', self.wgt_cpf_negativado, common_lyt)
        self.posInputField('Está desempregado: ', self.wgt_unemployed, common_lyt)
        self.posInputField('Está grávida: ', self.wgt_pregnant, common_lyt)

        self.main_lyt.add_widget(common_lyt)

    def fillButtons(self):
        buttons_lyt = BoxLayout(orientation='horizontal')
        buttons_lyt.add_widget(self.wgt_btn_show_common)
        buttons_lyt.add_widget(self.wgt_btn_show_life)
        buttons_lyt.add_widget(self.wgt_btn_show_home)
        buttons_lyt.add_widget(self.wgt_btn_show_car)
        buttons_lyt.add_widget(self.wgt_btn_calculate)

        self.wgt_btn_show_common.bind(on_press=self.on_wgt_btn_show_common_press)
        self.wgt_btn_show_life.bind(on_press=self.on_wgt_btn_show_life_press)
        self.wgt_btn_show_home.bind(on_press=self.on_wgt_btn_show_home_press)
        self.wgt_btn_show_car.bind(on_press=self.on_wgt_btn_show_car_press)
        self.wgt_btn_calculate.bind(on_press=self.on_wgt_btn_calculate_press)

        self.add_widget(buttons_lyt)

    def fillLifeInsurance(self):
        life_insurance_lyt = BoxLayout(orientation='vertical')

        life_insurance_basics_lyt = GridLayout(cols=2, row_force_default=True, row_default_height=30,
                                               size_hint=(None, 1), width=400)

        life_insurance_basics_lyt.cols_minimum[0] = 200
        life_insurance_basics_lyt.cols_minimum[1] = 200

        self.posInputField('Tipo de Cobertura', self.wgt_life_coverage_type, life_insurance_basics_lyt)
        self.posInputField('Tipo sanguíneo', self.wgt_blood_type, life_insurance_basics_lyt)
        self.posInputField('Número de viagens por ano', self.wgt_travels, life_insurance_basics_lyt)

        life_insurance_lyt.add_widget(life_insurance_basics_lyt)

        life_insurance_rules_lyt = GridLayout(cols=6, row_force_default=True, row_default_height=30)

        self.posInputField('Pratica esportes radicais?', self.wgt_radical_sports, life_insurance_rules_lyt)
        self.posInputField('É piloto de corrida?', self.wgt_racing_driver, life_insurance_rules_lyt)
        self.posInputField('Utiliza ou já utilizou drogas?', self.wgt_use_drugs, life_insurance_rules_lyt)
        self.posInputField('É portador de doenças graves?', self.wgt_serious_diseases, life_insurance_rules_lyt)
        self.posInputField('Realiza acompanhamento médico periódico?', self.wgt_medical_monitoring,
                           life_insurance_rules_lyt)
        self.posInputField('Já recebeu indenização por invalidez?', self.wgt_invalidity, life_insurance_rules_lyt)
        self.posInputField('É fumante?', self.wgt_smoker, life_insurance_rules_lyt)
        self.posInputField('Faz uso freqüente de bebidas alcoólicas?', self.wgt_alcohol, life_insurance_rules_lyt)
        self.posInputField('Habita em regiões perigosas?', self.wgt_dangerous_zone, life_insurance_rules_lyt)
        self.posInputField('Realiza atividades profissionais\na bordo de aeronaves?', self.wgt_airline_crew,
                           life_insurance_rules_lyt)
        self.posInputField('Portador de diabetes', self.wgt_diabetes, life_insurance_rules_lyt)
        self.posInputField('Possui hipertensão arterial', self.wgt_arterial_hypertension, life_insurance_rules_lyt)
        self.posInputField('Pratica esportes regularmente?', self.wgt_sports_practice, life_insurance_rules_lyt)
        self.posInputField('Portador de doença neurológica?', self.wgt_neurological_disease, life_insurance_rules_lyt)
        self.posInputField('Realizou cirurgia de grande porte?', self.wgt_surgery, life_insurance_rules_lyt)
        self.posInputField('Possui marcapasso?', self.wgt_pacemaker, life_insurance_rules_lyt)
        self.posInputField('Portador de doença auto imune?', self.wgt_auto_immune_disease, life_insurance_rules_lyt)
        self.posInputField('Portador de doença cardíaca?', self.wgt_heart_disease, life_insurance_rules_lyt)
        self.posInputField('Portador de câncer?', self.wgt_cancer, life_insurance_rules_lyt)
        self.posInputField('Portador de doença celíaca?', self.wgt_celia, life_insurance_rules_lyt)
        self.posInputField('Intolerância à Lactose?', self.wgt_lactose_intolerance, life_insurance_rules_lyt)
        self.posInputField('Portador de alguma\ndoença em estágio terminal?', self.wgt_terminal_disease,
                           life_insurance_rules_lyt)
        self.posInputField('Viaja para a África?', self.wgt_africa_travel, life_insurance_rules_lyt)
        self.posInputField('Viaja para países em guerra?', self.wgt_war_travel, life_insurance_rules_lyt)
        self.posInputField('Pratica esporte de tiros?', self.wgt_shoot_practice, life_insurance_rules_lyt)
        self.posInputField('Já realizou transplantes?', self.wgt_transplant, life_insurance_rules_lyt)
        self.posInputField('Já teve infarte?', self.wgt_heart_attack, life_insurance_rules_lyt)
        self.posInputField('Já teve AVC?', self.wgt_stroke, life_insurance_rules_lyt)
        self.posInputField('Possui alguma deficiência física?', self.wgt_deficiencies, life_insurance_rules_lyt)
        self.posInputField('Cardiopatia congênita?', self.wgt_heart_congenital, life_insurance_rules_lyt)
        self.posInputField('Artrose?', self.wgt_osteoarthritis, life_insurance_rules_lyt)
        self.posInputField('Faz uso de medicamento controlado?', self.wgt_controlled_medication,
                           life_insurance_rules_lyt)
        self.posInputField('É portador de doença sexualmente\ntransmissível incurável?', self.wgt_sexual_disease,
                           life_insurance_rules_lyt)
        self.posInputField('É portador de Hepatite B?', self.wgt_hepatitis, life_insurance_rules_lyt)
        self.posInputField('Possui plano de saúde?', self.wgt_health_plan, life_insurance_rules_lyt)
        self.posInputField('Tomou vacina de poliomelite?', self.wgt_vaccine_polio, life_insurance_rules_lyt)
        self.posInputField('Tomou vacina de meningite?', self.wgt_vaccine_meningite, life_insurance_rules_lyt)
        self.posInputField('Tomou vacina da febre amarela?', self.wgt_vaccine_yellow_fever, life_insurance_rules_lyt)

        life_insurance_lyt.add_widget(life_insurance_rules_lyt)

        self.main_lyt.add_widget(life_insurance_lyt)

    def fillCarInsurance(self):
        car_insurance_lyt = BoxLayout(orientation='vertical')

        car_insurance_rules_lyt = GridLayout(cols=4, row_default_height=30)

        self.posInputField('Tipo de cobertura: ', self.wgt_car_coverage_type, car_insurance_rules_lyt)
        self.posInputField('Possui ABS? ', self.wgt_abs, car_insurance_rules_lyt)
        self.posInputField('Marca: ', self.wgt_brand, car_insurance_rules_lyt)
        self.posInputField('Possui Airbags? ', self.wgt_airbags, car_insurance_rules_lyt)
        self.posInputField('Modelo: ', self.wgt_model, car_insurance_rules_lyt)
        self.posInputField('Rastreador? ', self.wgt_tracker, car_insurance_rules_lyt)
        self.posInputField('Número de Motoristas: ', self.wgt_drivers, car_insurance_rules_lyt)
        self.posInputField('Carro reserva? ', self.wgt_backup_car, car_insurance_rules_lyt)
        self.posInputField('Índice de roubo do veículo: ', self.wgt_theft_index, car_insurance_rules_lyt)
        self.posInputField('Seguro contra terceiros? ', self.wgt_third, car_insurance_rules_lyt)
        self.posInputField('Franquia reduzida? ', self.wgt_reduced, car_insurance_rules_lyt)
        self.posInputField('Roubo? ', self.wgt_theft, car_insurance_rules_lyt)
        self.posInputField('Incêndio? ', self.wgt_fire, car_insurance_rules_lyt)
        self.posInputField('Veículo é guardado em garagem fechada ou coberta? ', self.wgt_garage,
                           car_insurance_rules_lyt)
        self.posInputField('Veículo é utilizado para fins profissionais? ', self.wgt_professional,
                           car_insurance_rules_lyt)
        self.posInputField('Acidentes pessoais de passageiros ', self.wgt_personal_passenger, car_insurance_rules_lyt)
        self.posInputField('Condutor se acidentou nos últimos 2 anos? ', self.wgt_accident, car_insurance_rules_lyt)
        self.posInputField('110% da Fipe? ', self.wgt_extra_fipe, car_insurance_rules_lyt)
        self.posInputField('Veículo utilizado para viagens? ', self.wgt_for_travel, car_insurance_rules_lyt)

        car_insurance_lyt.add_widget(car_insurance_rules_lyt)

        self.main_lyt.add_widget(car_insurance_lyt)

    def fillHomeInsurance(self):
        home_insurance_lyt = BoxLayout(orientation='vertical')

        home_insurance_rules_lyt = GridLayout(cols=2, row_default_height=30)
        home_insurance_rules_lyt.cols_minimum[0] = 200
        home_insurance_rules_lyt.cols_minimum[1] = 750

        self.posInputField('Tipo de cobertura: ', self.wgt_home_coverage_type, home_insurance_rules_lyt)
        self.posInputField('Tipo de moradia: ', self.wgt_residence_type, home_insurance_rules_lyt)
        self.posInputField('Número de eletrônicos: ', self.wgt_number_of_electronics, home_insurance_rules_lyt)
        self.posInputField('Valor dos bens: ', self.wgt_value_of_goods, home_insurance_rules_lyt)
        self.posInputField('Habita em região perigosa? ', self.wgt_dangerous_neighbour, home_insurance_rules_lyt)
        self.posInputField('Habita em zonas de riscos naturais? ', self.wgt_natural_risk, home_insurance_rules_lyt)
        self.posInputField('Imóvel está em construção? ', self.wgt_under_construction, home_insurance_rules_lyt)
        self.posInputField('Imóvel possui alarme? ', self.wgt_has_alarm, home_insurance_rules_lyt)
        self.posInputField('Imóvel é tombado como patrimônio histórico? ', self.wgt_historical,
                           home_insurance_rules_lyt)
        self.posInputField('Imóvel é usado como república ou moradia coletiva? ', self.wgt_shared,
                           home_insurance_rules_lyt)
        self.posInputField('Imóvel utiliza materiais combustíveis? ', self.wgt_combustible_materials,
                           home_insurance_rules_lyt)
        self.posInputField('Possui cofre? ', self.wgt_has_safe_box, home_insurance_rules_lyt)
        self.posInputField('Necessita de serviços emergenciais? ', self.wgt_needs_emergencial_services,
                           home_insurance_rules_lyt)
        self.posInputField('Já houve sinistro no imóvel? ', self.wgt_insurance_claim,
                           home_insurance_rules_lyt)

        home_insurance_lyt.add_widget(home_insurance_rules_lyt)

        self.main_lyt.add_widget(home_insurance_lyt)

    def on_wgt_btn_show_common_press(instance, value):
        instance.main_lyt.clear_widgets()
        instance.clear_parents()
        instance.fillCommon()

    def on_wgt_btn_show_life_press(instance, value):
        instance.main_lyt.clear_widgets()
        instance.clear_parents()
        instance.fillLifeInsurance()

    def on_wgt_btn_show_home_press(instance, value):
        instance.main_lyt.clear_widgets()
        instance.clear_parents()
        instance.fillHomeInsurance()

    def on_wgt_btn_show_car_press(instance, value):
        instance.main_lyt.clear_widgets()
        instance.clear_parents()
        instance.fillCarInsurance()

    def on_wgt_btn_calculate_press(instance, value):
        engine = SeguroDeVida()
        engine.reset()

        engine.declare(Fact(cpf=instance.wgt_cpf_negativado.active))
        engine.declare(Fact(esportesRadicais=instance.wgt_radical_sports.active))
        engine.declare(Fact(pilotoCorrida=instance.wgt_racing_driver.active))
        engine.declare(Fact(drogas=instance.wgt_use_drugs.active))
        engine.declare(Fact(doencasGraves=instance.wgt_serious_diseases.active))
        engine.declare(Fact(doencasGraves=instance.wgt_serious_diseases.active))
        engine.declare(Fact(acompanhamentoMedico=instance.wgt_medical_monitoring.active))
        engine.declare(Fact(acompanhamento=instance.wgt_medical_monitoring.active))
        engine.declare(Fact(indenizacao=instance.wgt_invalidity.active))
        engine.declare(Fact(fuma=instance.wgt_smoker.active))
        engine.declare(Fact(bebe=instance.wgt_alcohol.active))
        engine.declare(Fact(cep=instance.wgt_dangerous_neighbour.active))
        engine.declare(Fact(aeronaves=instance.wgt_airline_crew.active))
        engine.declare(Fact(idade=convertStrToFloat(instance.wgt_age.text)))
        engine.declare(Fact(diabetes=instance.wgt_diabetes.active))
        engine.declare(Fact(profissao=instance.wgt_profession.text))
        # engine.declare(Fact(pressao=<to_be_defined>))
        engine.declare(Fact(sedentario_=instance.wgt_sports_practice.active))
        # engine.declare(Fact(pagador=<to_be_defined>))
        # engine.declare(Fact(possuiFilhos_=<to_be_defined>))
        engine.declare(Fact(quantosFilhos=convertStrToInt(instance.wgt_children.text)))
        engine.declare(Fact(casado=instance.wgt_marital_status.text))
        engine.declare(Fact(viagens=convertStrToInt(instance.wgt_travels.text)))
        engine.declare(Fact(neuro=instance.wgt_neurological_disease.active))
        engine.declare(Fact(cirurgia=instance.wgt_surgery.active))
        engine.declare(Fact(marcapasso=instance.wgt_pacemaker.active))
        engine.declare(Fact(problemaCardiaco=instance.wgt_heart_disease.active))
        engine.declare(Fact(cancerNaFamilia=instance.wgt_cancer.active))
        engine.declare(Fact(sangue=instance.wgt_blood_type.text))
        engine.declare(Fact(celiaco_=instance.wgt_celia.active))
        engine.declare(Fact(hipolactasia_=instance.wgt_lactose_intolerance.active))
        engine.declare(Fact(terminal=instance.wgt_terminal_disease.active))
        engine.declare(Fact(autoImune=instance.wgt_auto_immune_disease.active))
        engine.declare(Fact(vacinaPolio=instance.wgt_vaccine_polio.active))
        engine.declare(Fact(vacinaMeningite=instance.wgt_vaccine_meningite.active))
        engine.declare(Fact(viagemAfrica=instance.wgt_africa_travel.active))
        engine.declare(Fact(viagemGuerra=instance.wgt_war_travel.active))
        engine.declare(Fact(desempregado_=instance.wgt_unemployed.active))
        engine.declare(Fact(esportesTiro=instance.wgt_shoot_practice.active))
        engine.declare(Fact(transplante=instance.wgt_transplant.active))

        engine.declare(Fact(abs_ou_air=instance.wgt_airbags.active))
        # engine.declare(Fact(frances_ou_chines=instance.wgt_model.text))
        # engine.declare(Fact(alemao_ou_japones=instance.wgt_model.text))
        engine.declare(Fact(contraTerceiros=instance.wgt_third.active))
        engine.declare(Fact(franquia_reduzida=instance.wgt_reduced.active))
        engine.declare(Fact(roubo=instance.wgt_theft.active))
        engine.declare(Fact(incendio=instance.wgt_fire.active))
        engine.declare(Fact(idadeCarro=convertStrToInt(instance.wgt_year.text)))
        # engine.declare(Fact(um_condutor=<to_be_defined>))
        engine.declare(Fact(garagem=instance.wgt_garage.active))
        engine.declare(Fact(carro_reserva=instance.wgt_backup_car.active))
        engine.declare(Fact(acidentesPessoais=instance.wgt_personal_passenger.active))
        engine.declare(Fact(condutorAcidente=instance.wgt_accident.active))
        engine.declare(Fact(indenizacaoFipe=instance.wgt_extra_fipe.active))
        engine.declare(Fact(sexo_=instance.wgt_gender.text))
        engine.declare(Fact(possuiRastreador=instance.wgt_tracker.active))
        # engine.declare(Fact(indice_roubo=<to_be_defined>))
        engine.declare(Fact(veiculo_viagens=instance.wgt_for_travel.active))
        engine.declare(Fact(cobertura_=instance.wgt_car_coverage_type.text))
        # engine.declare(Fact(divida=<to_be_defined>))

        # engine.declare(Fact(casaProria=<to_be_defined>))
        engine.declare(Fact(areaRiscoNatural=instance.wgt_natural_risk.active))
        engine.declare(Fact(emConstrucao=instance.wgt_under_construction.active))
        engine.declare(Fact(sistemaMonitoramento=instance.wgt_medical_monitoring.active))
        engine.declare(Fact(tombado=instance.wgt_historical.active))
        engine.declare(Fact(moradiaColetiva=instance.wgt_shared.active))
        engine.declare(Fact(moradia=convertStrToInt(instance.wgt_residence_type.text)))
        engine.declare(Fact(utilizaMateriaisCombustiveis=instance.wgt_combustible_materials.active))
        engine.declare(Fact(numeroAparelhosEletronicos_=convertStrToInt(instance.wgt_number_of_electronics.text)))
        engine.declare(Fact(valor_Dos_Bens=convertStrToFloat(instance.wgt_value_of_goods.text)))
        engine.declare(Fact(cofre=instance.wgt_has_safe_box.active))
        engine.declare(Fact(servicosEmergenciais=instance.wgt_needs_emergencial_services.active))
        engine.declare(Fact(jaHouveSinistro=instance.wgt_insurance_claim.active))

        # engine.declare(Fact(nivelLDL=<to_be_defined>))
        engine.declare(Fact(cancer_=instance.wgt_cancer.active))
        engine.declare(Fact(infarto_=instance.wgt_heart_attack.active))
        engine.declare(Fact(AVC=instance.wgt_stroke.active))
        engine.declare(Fact(deficiencia=instance.wgt_deficiencies.active))
        # engine.declare(Fact(obeso=<to_be_defined>))
        engine.declare(Fact(cardiopatia=instance.wgt_heart_congenital.active))
        engine.declare(Fact(artrose=instance.wgt_osteoarthritis.active))
        engine.declare(Fact(medicamentoControlado=instance.wgt_controlled_medication.active))
        engine.declare(Fact(dst=instance.wgt_sexual_disease.active))
        engine.declare(Fact(hepatite=instance.wgt_hepatitis.active))
        engine.declare(Fact(gravida_=instance.wgt_pregnant.active))
        engine.declare(Fact(planoDeSaude=instance.wgt_health_plan.active))

        engine.run()

        print(engine.facts)
        print(engine.insuranceScore)

    def clear_parents(self):
        self.wgt_cpf_negativado.parent = None
        self.wgt_age.parent = None
        self.wgt_children.parent = None
        self.wgt_marital_status.parent = None
        self.wgt_gender.parent = None
        self.wgt_unemployed.parent = None
        self.wgt_height.parent = None
        self.wgt_weight.parent = None
        self.wgt_pregnant.parent = None
        self.wgt_serasa_score.parent = None
        self.wgt_profession.parent = None
        self.wgt_radical_sports.parent = None
        self.wgt_racing_driver.parent = None
        self.wgt_use_drugs.parent = None
        self.wgt_serious_diseases.parent = None
        self.wgt_medical_monitoring.parent = None
        self.wgt_invalidity.parent = None
        self.wgt_smoker.parent = None
        self.wgt_alcohol.parent = None
        self.wgt_dangerous_zone.parent = None
        self.wgt_airline_crew.parent = None
        self.wgt_diabetes.parent = None
        self.wgt_arterial_hypertension.parent = None
        self.wgt_sports_practice.parent = None
        self.wgt_travels.parent = None
        self.wgt_neurological_disease.parent = None
        self.wgt_surgery.parent = None
        self.wgt_pacemaker.parent = None
        self.wgt_auto_immune_disease.parent = None
        self.wgt_heart_disease.parent = None
        self.wgt_cancer.parent = None
        self.wgt_blood_type.parent = None
        self.wgt_celia.parent = None
        self.wgt_lactose_intolerance.parent = None
        self.wgt_terminal_disease.parent = None
        self.wgt_vaccine_polio.parent = None
        self.wgt_vaccine_meningite.parent = None
        self.wgt_vaccine_yellow_fever.parent = None
        self.wgt_africa_travel.parent = None
        self.wgt_war_travel.parent = None
        self.wgt_shoot_practice.parent = None
        self.wgt_transplant.parent = None
        self.wgt_heart_attack.parent = None
        self.wgt_stroke.parent = None
        self.wgt_deficiencies.parent = None
        self.wgt_osteoarthritis.parent = None
        self.wgt_controlled_medication.parent = None
        self.wgt_sexual_disease.parent = None
        self.wgt_hepatitis.parent = None
        self.wgt_health_plan.parent = None
        self.wgt_life_coverage_type.parent = None
        self.wgt_heart_congenital.parent = None
        self.wgt_brand.parent = None
        self.wgt_model.parent = None
        self.wgt_year.parent = None
        self.wgt_abs.parent = None
        self.wgt_airbags.parent = None
        self.wgt_third.parent = None
        self.wgt_reduced.parent = None
        self.wgt_theft.parent = None
        self.wgt_fire.parent = None
        self.wgt_drivers.parent = None
        self.wgt_garage.parent = None
        self.wgt_professional.parent = None
        self.wgt_backup_car.parent = None
        self.wgt_personal_passenger.parent = None
        self.wgt_accident.parent = None
        self.wgt_extra_fipe.parent = None
        self.wgt_tracker.parent = None
        self.wgt_theft_index.parent = None
        self.wgt_for_travel.parent = None
        self.wgt_car_coverage_type.parent = None
        self.wgt_combustible_materials.parent = None
        self.wgt_dangerous_neighbour.parent = None
        self.wgt_natural_risk.parent = None
        self.wgt_under_construction.parent = None
        self.wgt_has_alarm.parent = None
        self.wgt_historical.parent = None
        self.wgt_shared.parent = None
        self.wgt_residence_type.parent = None
        self.wgt_number_of_electronics.parent = None
        self.wgt_value_of_goods = TextInput(width=200, size_hint=(None, 1))
        self.wgt_has_safe_box.parent = None
        self.wgt_needs_emergencial_services.parent = None
        self.wgt_insurance_claim.parent = None
        self.wgt_home_coverage_type.parent = None
        self.wgt_points.parent = None
        self.wgt_btn_show_common.parent = None
        self.wgt_btn_show_life.parent = None
        self.wgt_btn_show_home.parent = None
        self.wgt_btn_show_car.parent = None
        self.wgt_btn_calculate.parent = None


class MyApp(App):

    def build(self):
        self.title = 'Insurance Expert v1.0'
        mainScreen = MainScreen()

        inspector.create_inspector(Window, mainScreen)

        return mainScreen


if __name__ == '__main__':
    MyApp().run()
