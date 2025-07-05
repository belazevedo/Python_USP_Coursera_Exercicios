# -*- coding: utf-8 -*-
"""
Created on Tue May 20 00:00:06 2025

@author: bela_
"""

import math

a = int(input('Digite um valor para a: '))
b = int(input('Digite um valor para b: '))
c = int(input('Digite um valor para c: '))

delta = (b ** 2 - (4 * a * c))

if delta == 0:
    x1 = (- b + math.sqrt(delta)) / 2 * a
    print('A raiz desta equação é', x1)
elif delta > 0:
    x1 = (- b + math.sqrt(delta)) / 2 * a
    x2 = (- b - math.sqrt(delta)) / 2 * a
    x = [x1, x2]
    x.sort()
    print('As raízes da equação são', x[0], 'e', x[1])
else:  
    print('Esta equação não possui raízes reais')

