# -*- coding: utf-8 -*-

'''
Criado em 04/2020
@Autor: Paulo https://github.com/alpdias
'''

import requests
from datetime import date
from bs4 import BeautifulSoup

atual = date.today()
mes = atual.month
ano = atual.year

mesAtual = mes
mesAnterior = mes - 1
mesProximo = mes + 1

verificacao = [mesProximo, mesAtual, mesAnterior]

menuNumero = [mesProximo, mesAtual, mesAnterior]

menuTexto = []

if mesProximo == 1:
    mesProximo = 'janeiro'
elif mesProximo == 2:
    mesProximo = 'fevereiro'
elif mesProximo == 3:
    mesProximo = 'marco'
elif mesProximo == 4:
    mesProximo = 'abril'
elif mesProximo == 5:
    mesProximo = 'maio'
elif mesProximo == 6:
    mesProximo = 'junho'
elif mesProximo == 7:
    mesProximo = 'julho'
elif mesProximo == 8:
    mesProximo = 'agosto'
elif mesProximo == 9:
    mesProximo = 'setembro'
elif mesProximo == 10:
    mesProximo = 'outubro'
elif mesProximo == 11:
    mesProximo = 'novembro'
elif mesProximo == 12:
    mesProximo = 'dezembro'
    
menuTexto.append(mesProximo)    

if mesAtual == 1:
    mesAtual = 'janeiro'
elif mesAtual == 2:
    mesAtual = 'fevereiro'
elif mesAtual == 3:
    mesAtual = 'marco'
elif mesAtual == 4:
    mesAtual = 'abril'
elif mesAtual == 5:
    mesAtual = 'maio'
elif mesAtual == 6:
    mesAtual = 'junho'
elif mesAtual == 7:
    mesAtual = 'julho'
elif mesAtual == 8:
    mesAtual = 'agosto'
elif mesAtual == 9:
    mesAtual = 'setembro'
elif mesAtual == 10:
    mesAtual = 'outubro'
elif mesAtual == 11:
    mesAtual = 'novembro'
elif mesAtual == 12:
    mesAtual = 'dezembro'

menuTexto.append(mesAtual)    
    
if mesAnterior == 1:
    mesAnterior = 'janeiro'
elif mesAnterior == 2:
    mesAnterior = 'fevereiro'
elif mesAnterior == 3:
    mesAnterior = 'marco'
elif mesAnterior == 4:
    mesAnterior = 'abril'
elif mesAnterior == 5:
    mesAnterior = 'maio'
elif mesAnterior == 6:
    mesAnterior = 'junho'
elif mesanterior == 7:
    mesAnterior = 'julho'
elif mesanterior == 8:
    mesAnterior = 'agosto'
elif mesAnterior == 9:
    mesAnterior = 'setembro'
elif mesAnterior == 10:
    mesAnterior = 'outubro'
elif mesAnterior == 11:
    mesAnterior = 'novembro'
elif mesAnterior == 12:
    mesAnterior = 'dezembro'
    
menuTexto.append(mesAnterior)

for i, menuTexto in enumerate(menuTexto): 
    print(f'[{menuNumero[0]}] {menuTexto.title()}')
    menuNumero.pop(0)
    
mes = int(input('Mês de referência: '))

if mes in verificacao:

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
        
    url = f'https://receita.economia.gov.br/acesso-rapido/agenda-tributaria/agenda-tributaria-{ano}/agenda-tributaria-{mes}-{ano}/agenda-tributaria-{mes}-{ano}'

    cabeçalho = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

    requisiçao = requests.get(url, headers=cabeçalho)

    soup = BeautifulSoup(requisiçao.text, 'html.parser')

    corpo = soup.find('div', {'id': 'parent-fieldname-text'})

    elementos = corpo.find('ul')

    links =  elementos.findAll('a', href=True)

    dicio = {} 

    for a in links:

        caminho = a['href']
        dia = a.text.strip()
        dicio[dia] = f'{caminho}'

    print(dicio)

else:
    print('Mês de referência inválido!')

    
