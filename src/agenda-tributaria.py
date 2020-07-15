# -*- coding: utf-8 -*-

'''
Created in 04/2020
@Autor: Paulo https://github.com/alpdias
'''

import requests
from bs4 import BeautifulSoup

url = "https://receita.economia.gov.br/acesso-rapido/agenda-tributaria/agenda-tributaria-2020/agenda-tributaria-julho-2020"

cabeçalho = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

requisiçao = requests.get(url, headers=cabeçalho)

soup = BeautifulSoup(requisiçao.text, 'html.parser')

corpo = soup.find('div', {'id': 'parent-fieldname-text'})

elementos = corpo.find('ul')

links =  elementos.findAll('a', href=True)

lista = []

for a in links:
    
    lista.append(a['href'])
    
print(lista)

    
