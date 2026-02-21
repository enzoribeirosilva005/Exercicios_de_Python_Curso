'''Jogo da Advinhação 2.0'''

from random import randint
from time import sleep

i = True
num = randint(0, 11)
c = 0

while i == True:
    tentar = int(input('Advinhe um número de 0 a 10: '))
    sleep(1)
    print('O resultado é...')
    sleep(1)

    if tentar == num:
        c += 1
        print(f'Você acertou o número, parabéns! Foram necessárias {c} tentativas!')
        break

    else:
        c += 1
        print(f'Você não acertou o número, tente novamente!\n')