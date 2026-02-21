'''Tabuada 2.0'''

c = 1
num = int(input('Digite um número: '))

while num > 0:
    r = num * c
    print(f'{num} X {c} = {r}')
    c += 1

    if c == 11:
        escolha = str(input('\nO usuário quer continuar vendo tabuadas? [S/N]: '))

        if escolha in 'Ss':
            num = int(input('\nDigite um número: '))
            c = 1

        elif escolha in 'Nn':
            break

        else:
            print('Opção inválida!')
            break