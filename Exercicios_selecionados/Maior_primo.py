# -*- coding: utf-8 -*-
"""
Created on Sat May 24 18:59:37 2025

@author: bela_
"""

import math

def eprimo(n):
    raiz = int(math.sqrt(n))
    i = 2
    if n == i:
        return n
    while i <= raiz:
        prova = n % i
        teste = prova == 0
        if teste:
            i = raiz + 1
            return False
        else:
            i = i + 1
            if i > raiz:
                n == True
                return n
        
            
def maior_primo(m):
    while eprimo(m) == False:
        m = m - 1
        eprimo(m)
    return m
   
    
    