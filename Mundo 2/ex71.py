'''Caixa Eletrônico'''

sacar_50 = 0
sacar_20 = 0
sacar_10 = 0
sacar_1 = 0
sacar = 0
total = 0


while True:
    num = float(input('Digite o valor a ser sacado: '))
    total += num
    sacar = total
    
    while True:
        if (sacar - 50) > -1:
            total -= 50
            sacar = total
            sacar_50 += 1

        else:
            break

    while True:
        if (sacar - 20) > -1:
            total -= 20
            sacar = total
            sacar_20 += 1

        else:
            break
    
    while True:
        if (sacar - 10) > -1:
            total -= 10
            sacar = total
            sacar_10 += 1

        else:
            break

    while True:
        if (sacar - 1) > -1:
            total -= 1
            sacar = total
            sacar_1 += 1

        else:
            break

    escolha = str(input('Você deseja retirar mais dinheiro? [S/N]: '))

    if escolha in 'Nn':
        break

    elif escolha in 'Ss':
        print('Entendido, retornando para as operações...')

    
    else:
        print('Essa opção não é válida!')

print(f'Você retirou {sacar_50} notas de R$50.\n{sacar_20} notas de R$20.\n{sacar_10} notas de R$10.\n{sacar_1} moedas de R$1.')