'''Soma e quantidade de números digitados'''

i = True
cont = 0
soma = 0

while i == True:
    num = int(input('Digite um número: '))

    if num == 999:
        print(f'Você digitou {cont} números!')
        print(f'A soma entre os números digitados foi {soma}!')
        break

    cont += 1
    soma += num