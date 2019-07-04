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
    emConstrução = Field(bool, mandatory=True, default=False)


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
    @Rule(Fact(cpf=True))
    def NegarSeguro(self):
        print("Não é possível realizar um seguro para o cliente")

    @Rule(possuiDoencasGraves(doencasGraves=True) & acompanhamentoMedico(acompanhamento=True))
    def DuplicarValor(self):
        print("Duplicar valor do seguro")


# engine = SeguroDeVida()
# engine.reset()
#
# engine.declare(Fact(cpf=input("CPF está negativado? ")))
# # engine.declare(Fact(esportesRadicais = input("Praticante de esportes radicais? ")))
# # engine.declare(Fact(pilotoCorrida = input("Piloto de Corrida? ")))
# # engine.declare(Fact(drogas = input("Usuário de drogas? ")))
# # engine.declare(Fact(recebeuIndenizacaoPorInvalidez = input("Já recebeu indenização por invalidez? ")))
#
# engine.run()
