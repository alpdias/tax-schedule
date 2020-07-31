# -*- coding: utf-8 -*-

'''
Criado em 04/2020
@Autor: Paulo https://github.com/alpdias
'''

# bibliotecas importadas
import arte
import requisicoes
import tratamentos

# bibliotecas python
from datetime import date

atual = date.today() # data atual
mes = atual.month # mes atual
ano = atual.year # ano atual

mesAtual = mes 
mesAnterior = mes - 1 # mes anterior ao atual
mesProximo = mes + 1 # proximo mes referente ao atual

verificacaoMes = [mesProximo, mesAtual, mesAnterior] # lista com os meses para verificar entrada escolhida

menuNumero = [mesProximo, mesAtual, mesAnterior] # lista com os meses para criar o menu

menuTexto = [] # lista para receber o nome dos meses
  
menuTexto.append(tratamentos.mesCalendario(mesProximo)) # funçao para receber o nome do mes

menuTexto.append(tratamentos.mesCalendario(mesAtual))    
        
menuTexto.append(tratamentos.mesCalendario(mesAnterior))

print('')
arte.arteNome('Agenda Tributaria', 2) # funçao com arte ASCII
print('')

for i, menuTexto in enumerate(menuTexto):  # loop para criar menu
    print(f'[{menuNumero[0]}] {menuTexto.title()}')
    menuNumero.pop(0)
    
print('')    
mes = int(input('Mês de referência: ')) # entrada do mes escolhido
print('')

if mes in verificacaoMes:
    calendario = requisicoes.pegarUrls(tratamentos.mesCalendario(mes), ano) # funçao para buscar um dicionario contendo a agenda do mes selecionado

else:
    print('Mês de referência inválido!')

listaDia = [] # lista para os dias da agenda
listaLink = [] # lista para os links de cada dia da agenda

for k, v in calendario.items(): # laço para separar dia e o link em listas
    listaDia.append(k) # dias
    listaLink.append(v) # links
