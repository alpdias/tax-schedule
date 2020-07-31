# -*- coding: utf-8 -*-

'''
Criado em 07/2020
@Autor: Paulo https://github.com/alpdias
'''

# bibliotecas python
from time import sleep
from pyfiglet import Figlet

def arteNome(nome, timeSleep=0):

    """
    Cria uma arte ASCII com o nome enviado
    :param nome: Texto para criar a arte
    :para timeSleep: Tempo de espera (opcional)
    :return: Retorna arte ASCII
    """
    
    f = Figlet(font='slant') # recebe a funçao mais a fonte a ser utilizada
    nome = f.renderText(nome) # recebe o texto
    
    print(nome) # mostra o texto em forma de arte ASCII
    sleep(timeSleep)
    
    
