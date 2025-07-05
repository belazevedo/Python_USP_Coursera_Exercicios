# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 14:09:47 2025

@author: bela_
"""

def remove_repetidos(lista):
    
    lista = sorted(lista)
    n = 0

    while n < len(lista) - 1:
        
        if lista[n] == lista[n + 1]:
            del lista[n + 1]
            
        else:
            n = n + 1

    return lista
