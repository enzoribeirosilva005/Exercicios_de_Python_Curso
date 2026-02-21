'''Número Primo'''

num = int(input('Digite um número para a verificação: '))
tot = 0

for i in range(1, num + 1):
    if num % i == 0:
        print('\033[33m', end='')
        tot += 1

    else:
        print('\033[31m', end='')
    print(f'{i} ', end='')

        
print(f'\n\033[mO número {num} foi dividido {tot} vezes!')

if tot == 2:
    print('Por causa disso, ele é um número primo!')
else:
    print('Por causa disso ele não é um número primo!')