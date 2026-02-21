'''Conversão de um número inteiro para Binário, Hexadecimal e Octal'''

num = int(input('Digite um número para conversão: '))
escolha = int(input('[1] - Binário\n[2] - Octal\n[3] - Hexadecimal: '))

if escolha == 1:
    print(f'Conversão para Binário: {bin(num)[2:]}.')

elif escolha == 2:
    print(f'Conversão para Octal: {oct(num)[2:]}.')

elif escolha == 3:
    print(f'Conversão para Hexadecimal {hex(num)[2:]}.')

else:
    print('Opção Inválida, tente novamente!')