# -*- coding: utf-8 -*-

'''
Criado em 07/2020
@Autor: Paulo https://github.com/alpdias
'''

# bibliotecas python
from time import sleep
from pyfiglet import Figlet

def artName(timeSleep=0):

    """
    Cria uma arte ASCII para com o nome do programa
    :para timeSleep: Tempo de espera
    :return: Retorna arte ASCII
    """
    
    f = Figlet(font='slant')
    agendaNome = f.renderText('Agenda Tributaria')
    
    print(agendaNome)
    sleep(timeSleep)
    
    
