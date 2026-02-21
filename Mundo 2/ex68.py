'''ÍMPAR OU PAR? - JOGO'''

from random import randint

i = True
c = 0

while i == True:
    pc = randint(0, 99)
    num = int(input('Digite um número: '))
    escolha = str(input('PAR ou ÍMPAR? [I/P]: '))

    soma = pc + num
    teste = soma % 2

    print(f'Você jogou {num} e o computador {pc}. O total é {soma}.')

    if escolha in 'Ii' and teste == 0:
        print('O computador venceu!')
        break

    elif escolha in 'Ii' and teste != 0:
        print('Você venceu!')
        c += 1

    elif escolha in 'Pp' and teste == 0:
        print('Você venceu!')
        c += 1

    elif escolha in 'Pp' and teste != 0:
        print('O computador venceu!')
        break

    else:
        print('Escolha inválida, tente novamente!')

print(f'\nO total de vitórias do usuário: {c} vitória(s)')