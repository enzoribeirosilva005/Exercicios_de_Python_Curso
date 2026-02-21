'''Pedra, Papel e Tesoura'''

from random import randint
from time import sleep

lista = ['Pedra', 'Papel', 'Tesoura']
pc = randint(0, 2)
escolha = int(input('1 - Pedra\n2 - Papel\n3 - Tesoura\nQual é a sua escolha? '))

jogador = escolha - 1

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!\n')

print(f'O computador jogou {lista[pc]}')
print(f'O jogador jogou {lista[jogador]}\n')

if lista[jogador] == lista[pc]:
    print('EMPATE')

elif lista[pc] == 'Pedra' and lista[jogador] == 'Papel':
    print('O jogador ganhou!')

elif lista[pc] == 'Pedra' and lista[jogador] == 'Tesoura':
    print('O computador ganhou!')

elif lista[pc] == 'Papel' and lista[jogador] == 'Pedra':
    print('O computador ganhou!')

elif lista[pc] == 'Papel' and lista[jogador] == 'Tesoura':
    print('O jogador ganhou!')

elif lista[pc] == 'Tesoura' and lista[jogador] == 'Papel':
    print('O computador ganhou!')

elif lista[pc] == 'Tesoura' and lista[jogador] == 'Pedra':
    print('O jogador ganhou!')
