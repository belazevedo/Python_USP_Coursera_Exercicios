# -*- coding: utf-8 -*-
"""
Created on Wed May 21 21:12:53 2025

@author: bela_
"""

import math

n = int(input('Digite um número inteiro positivo: '))

#número primo é apenas divisível por ele mesmo e 1. Tirar raiz quadrada e divisão de todos os números até a raiz.

raiz = int(math.sqrt(n))
i = 2

while i <= raiz:
    prova = n % i
    teste = prova == 0
    if teste:
        i = raiz + 1
        print('não primo')
    else:
        i = i + 1
        if i > raiz:
            print('primo')
    
