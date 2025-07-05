# -*- coding: utf-8 -*-
"""
Created on Fri May 30 16:45:49 2025

@author: bela_
"""

def soma_elementos(lista):
    
    x = len(lista) - 1
    soma = 0
        
    while x >= 0:
        soma = soma + lista[x]
        x = x - 1
    
    return soma



