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
    -> Obtem as url's dos dias da agenda tributaria
    :param mes: Mes de referencia
    param ano: Ano de referencia
    return: Retorna um dicionario com os dias e a url dos dias
    """
    
    url = f'https://receita.economia.gov.br/acesso-rapido/agenda-tributaria/agenda-tributaria-{ano}/agenda-tributaria-{mes}-{ano}/agenda-tributaria-{mes}-{ano}' # url para a requisiçao no site

    cabecalho = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} # cabeçalho para entrar no site simulando um usuario

    requisicao = requests.get(url, headers=cabecalho) # requisiçao

    soup = BeautifulSoup(requisicao.text, 'html.parser') # tratando o html

    corpo = soup.find('div', {'id': 'parent-fieldname-text'}) # procurando uma 'div' dentro do html pelo id

    elementos = corpo.find('ul') # recebendo a lista ('ul') dentro da 'div'

    links =  elementos.findAll('a', href=True) # recebendo os elemento html com os links

    dicio = {} # dicionario para adicionar o conteudo

    for a in links:

        caminho = a['href'] # links
        dia = a.text.strip() # valor dentro da tag 'a'
        dicio[dia] = f'{caminho}' # colocando dentro do dicionario

    return dicio
    
  
def pegarItens(url):
    
    """
    -> Obtem os itens da agenda tributaria a partir de uma url
    :param url: Link de um dia especifico da agenda tributaria
    return: 
    """

    cabecalho = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} # cabeçalho para entrar no site simulando um usuario

    requisicao = requests.get(url, headers=cabecalho) # requisiçao

    soup = BeautifulSoup(requisicao.text, 'html.parser') # tratando o html

