'''JOGO DA ADIVINHAÇÃO'''

import random

num = random.randint(0,1000)

escolha = int(input('Digite um número entre 0 e 1000 e descubra: Qual foi o número sorteado pelo computador? '))

if escolha == num:
    print('Parabéns! Você descobriu o número sorteado!')

else: 
    print('Você não descobriu o número sorteado, tente novamente!')