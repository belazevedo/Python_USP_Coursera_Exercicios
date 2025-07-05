# -*- coding: utf-8 -*-
"""
Created on Wed May 21 20:19:54 2025

@author: bela_
"""

n = int(input('Digite um número: '))

soma = 0

while n > 0:
    x = n % 10
    n = n // 10
    soma = soma + x 
    
print(soma)