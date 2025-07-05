# -*- coding: utf-8 -*-
"""
Created on Tue May 27 19:08:15 2025

@author: bela_
"""

def computador_escolhe_jogada(n, m): # número de peças removidas na jogada

    retirada = 1
    
    while retirada <= m:
        if n <= m:
            return n
        if (n - retirada) % (m + 1) == 0:
            return retirada
        else:
            retirada = retirada + 1
            if retirada > m:
                return m

def usuario_escolhe_jogada(n, m): # número de peças removidas na jogada
    
    retirada = 0
    
    while retirada < 1 or retirada > m:
        retirada = int(input('Por favor, escolha um número de 1 até o máximo permitido por rodada:' ))
    if n <= m:
        while retirada > n:
            retirada = int(input('Por favor, escolha um número de 1 até o número total de peças:' ))    
    return retirada

    
def partida():  
    # pergunta os valores de m e n
    # decide quem começa o jogo
    # responsável por ch1amar as outras def alternadamente
    # recebe o valor devolvido pelas def
    # identifica o final do jogo n == 0
   
    n = int(input('\nPor favor, diga o número inicial de peças no tabuleiro:'))
    m = int(input('Agora diga o número máximo de peças que o jogador da vez pode retirar a cada rodada: '))
    
    while m > n:
        m = int(input('Valor inválido. Por favor escolha outro valor: ')) 
    
    if n % (m + 1) == 0:
        print('Você começa!')
        primeiro = 1
    else:
        print('Computador começa!')
        primeiro = 2  
        
    if primeiro == 1:
        #retirada = 0
        while n > 0:
            retirada = usuario_escolhe_jogada(n, m)
            n = n - retirada
            print('\nQuantidade de peças removidas', retirada, '\nPeças restantes no tabuleiro:', n)
            if n == 0:
                print('Você ganhou!')
                vencedor = 1
            else:
                retirada = computador_escolhe_jogada(n, m)
                n = n - retirada
                print('\nQuantidade de peças removidas', retirada, '\nPeças restantes no tabuleiro:', n)
                if n == 0:
                    print('Computador ganhou!')     
                    vencedor = 2
    else:
        #retirada = 0
        while n > 0:
            retirada = computador_escolhe_jogada(n, m)
            n = n - retirada
            print('\nQuantidade de peças removidas', retirada, '\nPeças restantes no tabuleiro:', n)
            if n == 0:
                print('Computador ganhou!')
                vencedor = 2
            else: 
                retirada = usuario_escolhe_jogada(n, m)
                n = n - retirada
                print('\nQuantidade de peças removidas', retirada, '\nPeças restantes no tabuleiro:', n)
                if n == 0:
                    print('Você ganhou!')
                    vencedor = 1
   
    return vencedor
    
def campeonato():  # chamar def partida 3 vezes
    
    x = 0
    y = 0
    
    print('\n**Partida 1**')
    p1 = partida()
    if p1 == 1: 
        x = x + 1
    else: 
        y = y + 1
        
    print('\n**Partida 2**') 
    p2 = partida()
    if p2 == 1:
        x = x + 1
    else:
        y = y + 1
      
    print('\n**Partida 3**')    
    p3 = partida()
    if p3 == 1:
        x = x + 1
    else:
        y = y + 1
        
    placar = print('Placar: Você', x, 'X', y, 'Computador')
    
    return placar

    


print('Bem vindo ao jogo do NIM! Escolha:') 
i = int(input('1 - para jogar uma partida isolada.\n2 - para jogar um campeonato.\n '))
while i != 1 and i != 2:
    i = int(input('\nPor favor, escolha entre 1 ou 2\n1 - para jogar uma partida isolada.\n2 - para jogar um campeonato.\n '))
if i == 1:
    print('\nVocê escolheu uma partida isolada!')
    partida()
else:
    print('\nVocê escolheu um campeonato de três partidas!')
    placar = campeonato()
    
