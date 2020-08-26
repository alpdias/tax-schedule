# -*- coding: utf-8 -*-

'''
Criado em 04/2020
@Autor: Paulo https://github.com/alpdias
'''

# bibliotecas importadas
import requisicoes

# bibliotecas python
from datetime import date
from time import sleep
from pyfiglet import Figlet

atual = date.today() # data atual
mes = atual.month # mes atual
ano = atual.year # ano atual

mesAtual = mes 
mesAnterior = mes - 1 # mes anterior ao atual
mesProximo = mes + 1 # proximo mes referente ao atual

verificacaoMes = [mesProximo, mesAtual, mesAnterior] # lista com os meses para verificar entrada escolhida

menuNumero = [mesProximo, mesAtual, mesAnterior] # lista com os meses para criar o menu

menuTexto = [] # lista para receber o nome dos meses

def mesCalendario(mes):
    
    """
    -> Retornar o nome do mes equivalente ao numero
    :param mes: Numero do mes
    :return: Nome do mes
    """
    
    if mes == 1:
        mes = 'janeiro'
    elif mes == 2:
        mes = 'fevereiro'
    elif mes == 3:
        mes = 'marco'
    elif mes == 4:
        mes = 'abril'
    elif mes == 5:
        mes = 'maio'
    elif mes == 6:
        mes = 'junho'
    elif mes == 7:
        mes = 'julho'
    elif mes == 8:
        mes = 'agosto'
    elif mes == 9:
        mes = 'setembro'
    elif mes == 10:
        mes = 'outubro'
    elif mes == 11:
        mes = 'novembro'
    elif mes == 12:
        mes = 'dezembro'

    return mes
  
menuTexto.append(mesCalendario(mesProximo)) # funçao para criar o nome do mes

menuTexto.append(mesCalendario(mesAtual))    
        
menuTexto.append(mesCalendario(mesAnterior))

def arteNome(nome, timeSleep=0):

    """
    -> Cria uma arte ASCII com o nome enviado
    :param nome: Texto para criar a arte
    :para timeSleep: Tempo de espera (opcional)
    :return: Retorna arte ASCII
    """
    
    f = Figlet(font='slant') # recebe a funçao mais a fonte a ser utilizada
    nome = f.renderText(nome) # recebe o texto
    
    print(nome) # mostra o texto em forma de arte ASCII
    sleep(timeSleep)

print('')
arteNome('Agenda Tributaria', 2) # funçao com arte ASCII
print('')

for i, menuTexto in enumerate(menuTexto):  # loop para criar menu
    print(f'[{menuNumero[0]}] {menuTexto.title()}')
    menuNumero.pop(0)
    
print('')    
mes = int(input('Mês de referência: ')) # entrada do mes escolhido
print('')

if mes in verificacaoMes:
    try:
        calendario = requisicoes.itens(mes, ano) # funçao para buscar os itens da agenda tributaria
    except AttributeError:
        print('Mês de referência sem conteúdo!')

else:
    print('Mês de referência inválido!')

