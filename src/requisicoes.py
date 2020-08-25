# -*- coding: utf-8 -*-

'''
Criado em 07/2020
@Autor: Paulo https://github.com/alpdias
'''

# bibliotecas python
import requests
from bs4 import BeautifulSoup

# bibliotecas importadas
import tratamentos

def pegarUrls(mes, ano):
    
    """
    -> Obtem as url's dos dias da agenda tributaria
    :param mes: Mes de referencia
    :param ano: Ano de referencia
    return: Retorna um dicionario com os dias e as url's dos eventos
    """
    
    url = f'https://receita.economia.gov.br/acesso-rapido/agenda-tributaria/agenda-tributaria-{ano}/agenda-tributaria-{mes}-{ano}/agenda-tributaria-{mes}-{ano}' # url para a requisiçao no site

    cabecalho = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} # cabeçalho para entrar no site simulando um usuario

    requisicao = requests.get(url, headers=cabecalho) # requisiçao

    soup = BeautifulSoup(requisicao.text, 'html.parser') # tratando o html

    corpo = soup.find('div', {'id': 'parent-fieldname-text'}) # procurando uma 'div' dentro do html pelo id

    elementos = corpo.find('ul') # recebendo a lista 'ul' dentro da 'div'

    links =  elementos.findAll('a', href=True) # recebendo os elemento html com os links

    dicio = {} # dicionario para adicionar o conteudo

    for a in links:

        caminho = a['href'] # links
        dia = a.text.strip() # valor dentro da tag 'a'
        dicio[dia] = f'{caminho}' # colocando dentro do dicionario

    return dicio
    
  
def itens(mes, ano):
    
    """
    -> Obtem os itens da agenda tributaria a partir de uma url
    :param mes: Mes de referencia
    :param ano: Ano de referencia
    return: Retorna dicionarios com os eventos da agenda tributaria
    """

    calendario = pegarUrls(tratamentos.mesCalendario(mes), ano) # funçao para buscar um dicionario contendo a agenda do mes e ano selecionado

    listaDia = [] # lista para os dias da agenda

    for k, v in calendario.items(): # laço para separar os dias em lista
        listaDia.append(k)

    for k, v in calendario.items(): # laço para separar os link's dos eventos da agenda

        url = v # link's de cada dia da agenda

        cabecalho = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

        requisicao = requests.get(url, headers=cabecalho) 

        soup = BeautifulSoup(requisicao.text, 'html.parser') 

        corpo = soup.find('div', {'id': 'parent-fieldname-text'}) 

        elemento = corpo.findAll('tbody') # recebendo o corpo da tabela 'tbody' dentro da 'div'

        #conteudo = elemento.findAll('td') # recebendo as linhas da tabela

        lista = []

        for itens in elemento: # laço para obter os conteudo da agenda tributaria
            item = itens.findAll('td')
            for linhas in item:
                removedor = (linhas.text).replace('\xa0','').replace('\n','')
                lista.append(removedor)

        conteudo = {} # dicionario para armazenar os dados da agenda por dia

        conteudo[listaDia[0]] = lista
        listaDia.pop(0)

        print(conteudo)
        
