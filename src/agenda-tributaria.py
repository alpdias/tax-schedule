# -*- coding: utf-8 -*-

'''
Criado em 04/2020
@Autor: Paulo https://github.com/alpdias
'''

# bibliotecas python
import requests
from bs4 import BeautifulSoup
from pyfiglet import Figlet
from time import sleep
from datetime import date
import platform
import os
import csv

atual = date.today() # data atual
mes = atual.month # mes atual
ano = atual.year # ano atual
mesAtual = mes 
mesAnterior = mes - 1 # mes anterior ao atual
mesProximo = mes + 1 # proximo mes referente ao atual

verificacaoMes = [mesProximo, mesAtual, mesAnterior] # lista com os meses para verificar entrada escolhida
menuNumero = [mesProximo, mesAtual, mesAnterior] # lista com os meses para criar o menu

def mesCalendario(mes):
    
    """
    -> retornar o nome do mes equivalente ao numero
    :param mes: numero do mes
    :return: nome do mes
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


menuTexto = [] # lista para receber o nome dos meses
menuTexto.append(mesCalendario(mesProximo)) # funçao para criar o nome do mes
menuTexto.append(mesCalendario(mesAtual))          
menuTexto.append(mesCalendario(mesAnterior))

def arteNome(nome, timeSleep=0):

    """
    -> cria uma arte ASCII com o nome enviado
    :param nome: texto para criar a arte
    :para timeSleep: tempo de espera (opcional)
    :return: retorna arte ASCII
    """
    
    f = Figlet(font='slant') # recebe a funçao mais a fonte a ser utilizada
    nome = f.renderText(nome) # recebe o texto
    print(nome) # mostra o texto em forma de arte ASCII
    sleep(timeSleep)

    
print('')
arteNome('Agenda Tributaria', 1) # funçao com arte ASCII
print('')

for i, menuTexto in enumerate(menuTexto):  # loop para criar menu
    print(f'[{menuNumero[0]}] {menuTexto.title()}')
    menuNumero.pop(0)
    
print('')    
mes = int(input('Mês de referência: ')) # entrada do mes escolhido
print('')
nomeArquivo = str(input('Nome do arquivo: ')) # nome para o arquivo de saida
print('')

def pegarUrls(mes, ano):
    
    """
    -> obtem as url's dos dias da agenda tributaria
    :param mes: mes de referencia
    :param ano: ano de referencia
    return: retorna um dicionario com os dias e as url's dos eventos
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
    -> obtem os itens da agenda tributaria a partir das url's
    :param mes: mes de referencia
    :param ano: ano de referencia
    return: Retorna os eventos da agenda tributaria em um arquivo no modelo csv
    """

    calendario = pegarUrls(mesCalendario(mes), ano) # funçao para buscar um dicionario contendo a agenda do mes e ano selecionado
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
        lista = []

        for itens in elemento: # laço para obter os conteudo da agenda tributaria       
            item = itens.findAll('td')
            complemento = itens.find('strong')  
            quantidade = len(item)
            
            if quantidade % 3 != 0:
                pass

            else:
                for linhas in item:
                    itemTexto = (linhas.text).replace('\xa0','').replace('\n','')
                    lista.append(itemTexto)

        conteudo = {} # dicionario para armazenar os dados da agenda por dia
        conteudo[listaDia[0]] = lista
        listaDia.pop(0)
        qtd = len(lista)
        
        while qtd > 0:
            
            '''
            
            OPCAO COM FILTRO
            
            for k, v in conteudo.items():
                if v[0] == '1708':
                    print(f'{k}; {v[0]}; {v[1]}; {v[2]};')
                    
                elif v[0] == '5952':
                    print(f'{k}; {v[0]}; {v[1]}; {v[2]};')
                
                OU
                      
                print(f'{k}; {v[0]}; {v[1]}; {v[2]};')
                del conteudo[k][0]
                del conteudo[k][0]
                del conteudo[k][0]
                qtd = qtd - 3 
            '''
            
            meuSistema = platform.system() # verificar o sistema que esta rodando
            
            if meuSistema == 'Linux':
                caminhoSaida = os.getcwd() # caminho de saida para o arquivo em Linux
                novoArquivo = f'{nomeArquivo}.txt' # tipo de arquivo
                
            else:
                caminhoSaida = ('C:' + os.sep + 'Users' + os.sep + os.getlogin() + os.sep + 'Desktop' + os.sep) # caminho de saida para o arquivo em Windows    
                novoArquivo = caminhoSaida + f'{nomeArquivo}.txt' # tipo de arquivo
            
            with open(novoArquivo, 'a', newline='') as linhasSaida:
                escritaArquivo = csv.writer(linhasSaida, escapechar=' ', quoting=csv.QUOTE_NONE) 
                
                for k, v in conteudo.items():
                    saidaConteudo = (f'{k}; {v[0]}; {v[1]}; {v[2]};')
                    escritaArquivo.writerow([saidaConteudo]) # escrita do conteudo no arquivo
                    del conteudo[k][0]
                    del conteudo[k][0]
                    del conteudo[k][0]
                    qtd = qtd - 3                      

                       
if mes in verificacaoMes:
    
    try:
        calendario = itens(mes, ano) # funçao para buscar os itens da agenda tributaria
        
    except AttributeError:
        print('Mês de referência sem conteúdo!')

else:
    print('Mês de referência inválido!')

