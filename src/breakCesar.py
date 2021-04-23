"""
Uso: Rompe el cifrado César usando brute force
Creado: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 22 Abril 2020
"""

import os
from colorama import Fore
from colorama import Style
import pyfiglet as header
from termcolor import colored

os.system('cls')
   
banner = header.figlet_format('BREAK CESAR').upper()
print(colored(banner.rstrip('\n'), 'blue', attrs=['bold']))
print(colored('         By Andrés Hernández Mata | Versión 1.0.0 | LSTI \n', 'red', attrs=['bold']))
   
mensaje = input('Ingresa la cadena: ')
simbolos = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'    

for llave in range(len(simbolos)):
    resultado = ''
    for simbolo in mensaje:
        if simbolo in simbolos:
            indice_simbolo = simbolos.find(simbolo)
            indice_nuevo = indice_simbolo - llave                
            if indice_nuevo < 0:
                indice_nuevo = indice_nuevo + len(simbolos)                                
            resultado = resultado + simbolos[indice_nuevo]    
        else:
            resultado = resultado + simbolo
    print('Llave #%s: %s' % (llave, resultado))


