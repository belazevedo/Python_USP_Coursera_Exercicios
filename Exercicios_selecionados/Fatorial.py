# -*- coding: utf-8 -*-
"""
Created on Tue May 20 20:08:32 2025

@author: bela_
"""

n = int(input('Digite o valor de n: '))

x = 1
y = n

while x < n:
    y = y * x
    x = x + 1
if n == 0:
    y = 1

print(y)