# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 13:34:53 2019

@author: mathe
"""

from pyknow import *


class cpfNegativado(Fact):
    """Se cpf estiver negativado"""
    cpf = Field(str, mandatory=True)


class praticaEsportesRadicais(Fact):
    """Requisitante pratica esportes radicais"""
    esportesRadicais = Field(bool, mandatory=True, default=False)


class pilotoDeCorrida(Fact):
    """Requisitante é piloto de corrida?"""
    pilotoCorrida = Field(bool, mandatory=True, default=False)


class usaDrogas(Fact):
    """Usuario de drogas?"""
    drogas = Field(bool, mandatory=True, default=False)


class possuiDoencasGraves(Fact):
    """Possui doenças graves?"""
    doencasGraves = Field(bool, mandatory=True, default=False)


class acompanhamentoMedico(Fact):
    """Faz acompanhamento medico?"""
    acompanhamento = Field(bool, mandatory=True, default=True)


class recebeuIndenizacaoPorInvalidez(Fact):
    """Recebeu indenização por invalidez?"""
    indenizacao = Field(bool, mandatory=True, default=False)


class fumante(Fact):
    """Fumante?"""
    fuma = Field(bool, mandatory=True, default=False)


class ingereBebidaDeAlcool(Fact):
    """Ingere bebida de alcool?"""
    bebe = Field(bool, mandatory=True, default=False)


class cepPerigoso(Fact):
    """Mora em região perigosa?"""
    cep = Field(bool, mandatory=True, default=False)


class atividadeProfissionalABordoDeAeronaves(Fact):
    """Realiza atividade profissional a bordo de aeronaves?"""
    aeronaves = Field(bool, mandatory=True, default=False)


class idade(Fact):
    """Idade do requisitante?"""
    idade = Field(int, mandatory=True)


class nivelDiabetes(Fact):
    """Nivel de diabetes?"""
    diabetes = Field(float, mandatory=True)


class tipoDeProfissao(Fact):
    """Tipo de Profissão?"""
    profissao = Field(str, mandatory=True)


class nivelPressao(Fact):
    """Pressão alta, normal ou baixa?"""
    pressao = Field(str, mandatory=True)


class sedentario(Fact):
    """Requisitante é sedentário?"""
    sedentario_ = Field(bool, mandatory=True)


class bomPagador(Fact):
    """Requisitante é bom pagador?"""
    pagador = Field(bool, mandatory=True, default=True)


class possuiFilhos(Fact):
    """Requisitante possui filhos?"""
    possuiFilhos_ = Field(bool, mandatory=True)


class quantidadeDeFilhos(Fact):
    """Quantos filhos?"""
    quantosFilhos = Field(int, mandatory=True)


class casadoSolteiro(Fact):
    """Casado ou solteiro?"""
    casado = Field(bool, mandatory=True)


class frequenciaDeViagens(Fact):
    """Frequencia de Viagens por ano"""
    viagens = Field(int, mandatory=True)


class doencaNeurologica(Fact):
    """Possui doença neurologica?"""
    neuro = Field(bool, mandatory=True)


class possuiCarro(Fact):
    """Possui carro?"""
    carro = Field(bool, mandatory=True)


class clienteAceitar(Fact):
    """Cliente aceitou?"""
    aceitar = Field(bool, mandatory=True)


class possuiABSouAirbag(Fact):
    """Possui ABS ou Airbag?"""
    abs_ou_air = Field(bool, mandatory=True, default=True)


class francesOuChines(Fact):
    """Carro frances ou chines?"""
    frances_ou_chines = Field(bool, mandatory=True)


class alemaoOuJapones(Fact):
    """Carro ou alemao ou japones?"""
    alemao_ou_japones = Field(bool, mandatory=True)


class seguroContraTerceiros(Fact):
    """Segura contra terceiros?"""
    contraTerceiros = Field(bool, mandatory=True)


class franquiaReduzida(Fact):
    """Franquia reduzida?"""
    franquia_reduzida = Field(bool, mandatory=True)


class coberturaRoubo(Fact):
    """Cobertura contra roubo?"""
    roubo = Field(bool, mandatory=True)


class coberturaIncendio(Fact):
    """Cobertura contra Incendio?"""
    incendio = Field(bool, mandatory=True)


class idadeDoCarro(Fact):
    """Idade do carro?"""
    idadeCarro = Field(int, mandatory=True)


class umCondutor(Fact):
    """É mais de um condutor?"""
    um_condutor = Field(bool, mandatory=True)


class carroFicaDentroGaragem(Fact):
    """Carro fica abrigado dentro de uma garagem fechada?"""
    garagem = Field(bool, mandatory=True)


class carroReserva(Fact):
    """Deseja carro reserva?"""
    carro_reserva = Field(bool, mandatory=True)


class coberturaAcidentesPessoaisPassageiros(Fact):
    """Deseja cobertura de acidentes pessoais de passageiros?"""
    acidentesPessoais = Field(bool, mandatory=True)


class condutorJaTeveAcidenteCarro(Fact):
    """Condutor já teve acidentes de carro?"""
    condutorAcidente = Field(bool, mandatory=True)


class indenizacaoMaiorFipe(Fact):
    """Deseja indenização maior que a Fipe?"""
    indenizacaoFipe = Field(bool, mandatory=True)


class sexo(Fact):
    """Masculino ou feminino?"""
    sexo_ = Field(int, mandatory=True)


class veiculoPossuiRastreador(Fact):
    """Possui rastreador?"""
    possuiRastreador = Field(bool, mandatory=True)


class indiceDeRoubo(Fact):
    """Qual o indice de roubo?"""
    indice_roubo = Field(float, mandatory=True)


class utilizaVeiculoParaViagens(Fact):
    """Utiliza o veiculo para viagens?"""
    veiculo_viagens = Field(bool, mandatory=True)


class cobertura(Fact):
    """Cobertura básica, completa ou premium?"""
    cobertura_ = Field(int, mandatory=True, default=2)


class possuirDivida(Fact):
    """Possui divida?"""
    divida = Field(bool, mandatory=True)


class cirurgiaAltoRisco(Fact):
    """Já fez cirurgia de alto risco?"""
    cirurgia = Field(bool, mandatory=True)


class possuiMarcapasso(Fact):
    """Possui marcapasso?"""
    marcapasso = Field(bool, mandatory=True)


class possuiProblemaCardiaco(Fact):
    """Possui problema cardiaco?"""
    problemaCardiaco = Field(bool, mandatory=True)


class possuiHistoricoCancerNaFamilia(Fact):
    """Possui historico de cancer na familia?"""
    cancerNaFamilia = Field(bool, mandatory=True)


class tipoSanguineo(Fact):
    """Qual tipo sanguineo?"""
    sangue = Field(str, mandatory=True)


class celiaco(Fact):
    """É celiaco?"""
    celiaco_ = Field(bool, mandatory=True)


class hipolactasia(Fact):
    """Tem hipolactasia?"""
    hipolactasia_ = Field(bool, mandatory=True)


class doencaTerminal(Fact):
    """Possui doença terminal?"""
    terminal = Field(bool, mandatory=True)


class doencaAutoImune(Fact):
    """Possui doença auto imune?"""
    autoImune = Field(bool, mandatory=True)


class tomouVacinaPolio(Fact):
    """Tomou vacina da polio?"""
    vacinaPolio = Field(bool, mandatory=True, default=True)


class tomouVacinaMeningite(Fact):
    """Tomou vacina meningite?"""
    vacinaMeningite = Field(bool, mandatory=True, default=True)


class viagemPaisesAfrica(Fact):
    """Já viajou ou vai viajar para paises da africa?"""
    viagemAfrica = Field(bool, mandatory=True)


class viagemPaisesEmGuerra(Fact):
    """Já viajou ou vai viajar para paises em guerra?"""
    viagemGuerra = Field(bool, mandatory=True)


class desempregado(Fact):
    """Está desempregado?"""
    desempregado_ = Field(bool, mandatory=True)


class praticaEsportesTiro(Fact):
    """Pratica esportes de tiro?"""
    esportesTiro = Field(bool, mandatory=True)


class sedentario(Fact):
    """Sedentário?"""
    sedentario_ = Field(bool, mandatory=True)


class possuiCasaPropria(Fact):
    """Possui casa propria?"""
    casaProria = Field(bool, mandatory=True)


class localizadaAreaRiscoNatural(Fact):
    """Localizada em area de risco natural?"""
    areaRiscoNatural = Field(bool, mandatory=True)


class imovelEmConstrucao(Fact):
    """Imovel em construção?"""
    emConstrucao = Field(bool, mandatory=True, default=False)


class possuiSistemaDeMonitoramento(Fact):
    """Possui sistema de monitoramento?"""
    sistemaMonitoramento = Field(bool, mandatory=True)


class imovelTombado(Fact):
    """Imovel é tombado pelo patrimonio historico?"""
    tombado = Field(bool, mandatory=True)


class destinadoParaMoradiaColetiva(Fact):
    """Imovel destinado para moradia coletiva ou republica?"""
    moradiaColetiva = Field(bool, mandatory=True)


class tipoDeMoradia(Fact):
    """Apartamento ou casa?"""
    moradia = Field(int, mandatory=True)


class imovelUtilizaMateriaisCombustiveis(Fact):
    """Imovel utiliza materiais combustiveis?"""
    utilizaMateriaisCombustiveis = Field(bool, mandatory=True)


class numeroAparelhosEletronicos(Fact):
    """Numero de aparelhos eletronicos em casa?"""
    numeroAparelhosEletronicos_ = Field(int, mandatory=True)


class valorDosBens(Fact):
    """Valor dos bens?"""
    valor_Dos_Bens = Field(int, mandatory=True)


class possuiCofre(Fact):
    """Possui cofre?"""
    cofre = Field(bool, mandatory=True)


class desejaServicosEmergenciais(Fact):
    """Deseja contratar serviços emergenciais?"""
    servicosEmergenciais = Field(bool, mandatory=True)


class imovelJaHouveSinistro(Fact):
    """Imovel já houve sinistro?"""
    jaHouveSinistro = Field(bool, mandatory=True)


class jaRealizouAlgumTransplante(Fact):
    """Já realizou algum transplante?"""
    transplante = Field(bool, mandatory=True)


class nivelLDL(Fact):
    """Qual o nivel do LDL?"""
    LDL = Field(int, mandatory=True)


class jaTeveCancer(Fact):
    """Já teve cancer?"""
    cancer_ = Field(bool, mandatory=True)


class jaTeveInfarto(Fact):
    """Já teve infarto?"""
    infarto_ = Field(bool, mandatory=True)


class jaTeveAVC(Fact):
    """Já teve AVC?"""
    AVC = Field(bool, mandatory=True)


class algumaDeficiencia(Fact):
    """Possui alguma deficiencia?"""
    deficiencia = Field(bool, mandatory=True)


class obesidade(Fact):
    """Requisitante é obeso?"""
    obeso = Field(bool, mandatory=True)


class possuiCardiopatiaCongenita(Fact):
    """Possui cardiopatia congenita?"""
    cardiopatia = Field(bool, mandatory=True)


class possuiArtrose(Fact):
    """Possui artrose?"""
    artrose = Field(bool, mandatory=True)


class utilizaMedicamentoControlado(Fact):
    """Utiliza medicamento controlado?"""
    medicamentoControlado = Field(bool, mandatory=True)


class possuiDoencaSexualmenteTransmissivel(Fact):
    """Possui alguma DST?"""
    dst = Field(bool, mandatory=True)


class possuiHepatiteB(Fact):
    """Possui Hepatite B?"""
    hepatite = Field(bool, mandatory=True)


class gravida(Fact):
    """Mulher está grávida?"""
    gravida_ = Field(bool, mandatory=True)


class possuiPlanoDeSaude(Fact):
    """Possui plano de Saude?"""
    planoDeSaude = Field(bool, mandatory=True)


class SeguroDeVida(KnowledgeEngine):
    insuranceScore = 0

    @Rule(Fact(cpf=True) | Fact(esportesRadicais=True)
          | Fact(pilotoCorrida=True)
          | Fact(drogas=True)
          | Fact(indenizacao=True)
          | Fact(aeronaves=True)
          | Fact(cirurgia=True)
          | Fact(problemaCardiaco=True)
          | Fact(terminal=True)
          | Fact(vacinaMeningite=True)
          | Fact(viagemGuerra=True)
          | Fact(esportesTiro=True)
          | Fact(deficiencia=True))
    def regra001(self):
        self.declare(Fact(seguro_nao_possivel=True))

    @Rule(Fact(doencasGraves=True) & Fact(acompanhamento=True))
    def regra002(self):
        if self.insuranceScore == 0:
            self.insuranceScore = 2
        else:
            self.insuranceScore *= 2

    @Rule(Fact(doencasGraves=True) & Fact(acompanhamento=False))
    def regra003(self):
        print("Não é possível realizar um seguro para o cliente")

    @Rule(Fact(fuma=True)
          | Fact(bebe=True)
          | Fact(cep=True)
          | Fact(sedentario_=True)
          | Fact(pagador=True)
          | Fact(cancerNaFamilia=True)
          | Fact(vacinaPolio=True)
          | Fact(viagemAfrica=True)
          | Fact(desempregado_=True)
          | Fact(sedentario_=True)
          | Fact(obeso=True)
          | Fact(artrose=True)
          | Fact(medicamentoControlado=True)
          | Fact(hepatite=True))
    def regra004(self):
        self.insuranceScore += 1

    @Rule(Fact(idade=P(lambda idade: idade >= 60 and idade < 70)))
    def regra005(self):
        self.insuranceScore += 1

    @Rule(Fact(idade=P(lambda idade: idade >= 70)))
    def regra006(self):
        self.declare(Fact(seguro_nao_possivel=True))

    @Rule(Fact(diabetes=P(lambda diabetes: diabetes < 120)))
    def AumentarValor(self):
        self.insuranceScore += 1

    @Rule(Fact(diabetes=P(lambda diabetes: diabetes > 200)))
    def regra007(self):
        self.declare(Fact(seguro_nao_possivel=True))

    @Rule(Fact(profissao=True))
    def regra008(self):
        self.insuranceScore += 1

    @Rule(Fact(pressao=True) & Fact(acompanhamento=True))
    def regra009(self):
        self.insuranceScore += 1

    @Rule(Fact(pressao=True) & Fact(acompanhamento=False))
    def regra010(self):
        self.declare(Fact(seguro_nao_possivel=True))

    @Rule(Fact(possuiFilhos_=True) & Fact(quantosFilhos=P(lambda possuiFilhos_: possuiFilhos_ > 0)))
    def regra011(self):
        self.insuranceScore += 1

    @Rule(Fact(casado=True))
    def regra011(self):
        self.insuranceScore += 1

    @Rule(Fact(viagens=P(lambda viagens: viagens > 3)))
    def regra012(self):
        self.insuranceScore += 1

    @Rule(Fact(neuro=True) & Fact(acompanhamento=True))
    def regra013(self):
        self.insuranceScore += 1

    @Rule(Fact(neuro=True) & Fact(acompanhamento=False))
    def regra014(self):
        self.declare(Fact(seguro_nao_possivel=True))

    @Rule(Fact(carro=True))
    def regra015(self):
        self.declare(Fact(ofereca_seguro_carro=True))

    @Rule(Fact(carro=True) & Fact(aceitar=True))
    def regra016(self):
        print("Continuar com peguntas sobre o carro")

    @Rule(Fact(idade=P(lambda idade: idade < 25)))
    def regra017(self):
        self.insuranceScore += 1

    @Rule(Fact(abs_ou_air=True))
    def regra018(self):
        self.insuranceScore -= 1

    @Rule(Fact(frances_ou_chines=True)
          | Fact(contraTerceiros=True)
          | Fact(franquia_reduzida=True)
          | Fact(roubo=True)
          | Fact(incendio=True)
          | Fact(garagem=True)
          | Fact(carro_reserva=True)
          | Fact(acidentesPessoais=True)
          | Fact(condutorAcidente=True)
          | Fact(indenizacaoFipe=True)
          | Fact(sexo_=P(lambda sexo_: sexo_ == 1))
          | Fact(veiculo_viagens=True)
          | Fact(cobertura=P(lambda cobertura: cobertura == 3)))
    def regra019(self):
        self.insuranceScore += 1

    @Rule(Fact(alemao_ou_japones=True)
          | Fact(um_condutor=True)
          | Fact(possuiRastreador=True)
          | Fact(cobertura=P(lambda cobertura: cobertura == 1)))
    def regra020(self):
        self.insuranceScore -= 1

    @Rule(Fact(idadeCarro=P(lambda idadeCarro: idadeCarro > 20)))
    def regra021(self):
        self.insuranceScore += 1

    @Rule(Fact(indice_roubo=P(lambda indice_roubo: indice_roubo > 10)))
    def regra022(self):
        self.insuranceScore += 1

    @Rule(Fact(cobertura=P(lambda cobertura: cobertura == 2)))
    def regra023(self):
        self.insuranceScore += 1

    @Rule(Fact(divida=True))
    def regra024(self):
        self.insuranceScore += 1

    @Rule(Fact(cirurgia=True) & Fact(acompanhamento=True))
    def regra024(self):
        self.insuranceScore += 1

    @Rule(Fact(cirurgia=True) & Fact(acompanhamento=True))
    def regra025(self):
        self.declare(Fact(seguro_nao_possivel=True))

    @Rule(Fact(sangue=P(lambda sangue: sangue == 'O+'))
          | Fact(sangue=P(lambda sangue: sangue == 'O-')))
    def regra026(self):
        self.insuranceScore -= 1

    @Rule(Fact(sangue=P(lambda sangue: sangue == 'AB+'))
          | Fact(sangue=P(lambda sangue: sangue == 'AB-')))
    def regra027(self):
        self.insuranceScore += 1

    @Rule(Fact(celiaco_=True) & Fact(acompanhamento=True))
    def regra028(self):
        self.insuranceScore += 1

    @Rule(Fact(celiaco_=True) & Fact(acompanhamento=True))
    def regra029(self):
        self.declare(Fact(seguro_nao_possivel=True))

    @Rule(Fact(hipolactasia_=True) & Fact(acompanhamento=True))
    def regra030(self):
        self.insuranceScore += 1

    @Rule(Fact(hipolactasia_=True) & Fact(acompanhamento=True))
    def regra031(self):
        self.declare(Fact(seguro_nao_possivel=True))

    @Rule(Fact(autoImune=True) & Fact(acompanhamento=True))
    def regra032(self):
        self.insuranceScore += 1

    @Rule(Fact(autoImune=True) & Fact(acompanhamento=True))
    def regra033(self):
        self.declare(Fact(seguro_nao_possivel=True))

    @Rule(Fact(casaPropria=True))
    def regra034(self):
        self.declare(Fact(ofereca_seguro_residencial=True))

    @Rule(Fact(casaPropria=True) & Fact(aceitar=True))
    def regra035(self):
        self.declare(Fact(ofereca_seguro_carro=True))

    @Rule(Fact(cep=True)
          | Fact(tombado=True)
          | Fact(moradiaColetiva=True)
          | Fact(utilizaMateriaisCombustiveis=True)
          | Fact(cofre=True)
          | Fact(servicosEmergenciais=True)
          | Fact(jaHouveSinistro=True))
    def regra036(self):
        self.insuranceScore += 1

    @Rule(Fact(areaRiscoNatural=True))
    def regra037(self):
        self.declare(Fact(seguro_nao_possivel=True))

    @Rule(Fact(emConstrucao=True)
          | Fact(sistemaMonitoramento=True))
    def regra038(self):
        self.insuranceScore -= 1

    @Rule(Fact(moradia=P(lambda moradia: moradia == 'casa')))
    def regra039(self):
        self.insuranceScore += 1

    @Rule(Fact(moradia=P(lambda moradia: moradia == 'apartamento')))
    def regra040(self):
        self.insuranceScore -= 1

    @Rule(Fact(numeroAparelhosEletronicos_=P(lambda numeroAparelhosEletronicos_: numeroAparelhosEletronicos_ > 10)))
    def regra041(self):
        self.insuranceScore += 1

    @Rule(Fact(valor_Dos_Bens=P(lambda valor_Dos_Bens: valor_Dos_Bens > 100000)))
    def regra042(self):
        self.insuranceScore += 1

    @Rule(Fact(transplante=True) & Fact(acompanhamento=True))
    def regra043(self):
        self.insuranceScore += 1

    @Rule(Fact(transplante=True) & Fact(acompanhamento=False))
    def regra044(self):
        self.declare(Fact(seguro_nao_possivel=True))

    @Rule(Fact(LDL=P(lambda LDL: LDL > 200)) & Fact(acompanhamento=True))
    def regra045(self):
        self.insuranceScore += 1

    @Rule(Fact(LDL=P(lambda LDL: LDL > 200)) & Fact(acompanhamento=False))
    def regra046(self):
        self.declare(Fact(seguro_nao_possivel=True))

    @Rule(Fact(cancer_=True) & Fact(acompanhamento=True))
    def regra047(self):
        self.insuranceScore += 1

    @Rule(Fact(cancer_=True) & Fact(acompanhamento=False))
    def regra048(self):
        self.declare(Fact(seguro_nao_possivel=True))

    @Rule(Fact(infarto_=True) & Fact(acompanhamento=True))
    def regra049(self):
        self.insuranceScore += 1

    @Rule(Fact(infarto_=True) & Fact(acompanhamento=False))
    def regra050(self):
        self.declare(Fact(seguro_nao_possivel=True))

    @Rule(Fact(AVC=True) & Fact(acompanhamento=True))
    def regra051(self):
        self.insuranceScore += 1

    @Rule(Fact(AVC=True) & Fact(acompanhamento=False))
    def NegarSeguro(self):
        self.declare(Fact(seguro_nao_possivel=True))

    @Rule(Fact(cardiopatia=True) & Fact(acompanhamento=True))
    def regra052(self):
        self.insuranceScore += 1

    @Rule(Fact(cardiopatia=True) & Fact(acompanhamento=False))
    def regra053(self):
        self.declare(Fact(seguro_nao_possivel=True))

    @Rule(Fact(dst=True) & Fact(acompanhamento=True))
    def regra054(self):
        self.insuranceScore += 1

    @Rule(Fact(dst=True) & Fact(acompanhamento=False))
    def regra055(self):
        self.declare(Fact(seguro_nao_possivel=True))

    @Rule(Fact(sexo_=P(lambda sexo_: sexo_ == 2)) & Fact(gravida_=True))
    def regra056(self):
        self.insuranceScore += 1

    @Rule(Fact(planoDeSaude=True))
    def regra057(self):
        self.insuranceScore -= 1
