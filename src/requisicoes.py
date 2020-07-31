# -*- coding: utf-8 -*-

'''
Criado em 07/2020
@Autor: Paulo https://github.com/alpdias
'''

# bibliotecas python
import requests
from bs4 import BeautifulSoup

def pegarUrls(mes, ano):
    
    """
    Obtém as url's dos dias da agenda tributária
    :param mes: Mês de referência
    param ano: Ano de referência
    return: Retorna um dicionário com os dias e a url dos dias
    """
    
    url = f'https://receita.economia.gov.br/acesso-rapido/agenda-tributaria/agenda-tributaria-{ano}/agenda-tributaria-{mes}-{ano}/agenda-tributaria-{mes}-{ano}'

    cabecalho = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

    requisicao = requests.get(url, headers=cabecalho)

    soup = BeautifulSoup(requisicao.text, 'html.parser')

    corpo = soup.find('div', {'id': 'parent-fieldname-text'})

    elementos = corpo.find('ul')

    links =  elementos.findAll('a', href=True)

    dicio = {} 

    for a in links:

        caminho = a['href']
        dia = a.text.strip()
        dicio[dia] = f'{caminho}'

    return dicio
    
    
