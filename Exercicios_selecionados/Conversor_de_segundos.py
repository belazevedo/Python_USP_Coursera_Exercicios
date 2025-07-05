# -*- coding: utf-8 -*-
"""
Created on Sat May 17 16:56:14 2025

@author: bela_
"""

segundostotal = int(input("Por favor, entre com o número de segundos que deseja converter: "))

#1 hora = 60 min
#1 min = 60 s
#1 hora = 3600 s
#1 dia = 24 h = 24 * 3600 = 86400 s

dia = 86400
dias = segundostotal // dia
horas = (segundostotal % dia) // 3600
minutos = ((segundostotal % dia) % 3600) // 60
segundos = ((segundostotal % dia) % 3600) % 60

print(dias, "dias", horas, "horas", minutos, "minutos e", segundos, "segundos.")
