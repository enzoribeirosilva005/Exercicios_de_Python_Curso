'''Manipulação de Strings'''

nome = input('Digite seu nome completo para a coleta de informações: ').strip()

maiusculas = nome.upper()

minusculas = nome.lower()

corte = nome.split()
ler = len(corte[0])

remover = len(nome) - nome.count(' ')

print(f'O seu nome com todas as letras maiúsculas: {maiusculas}')
print(f'O seu nome com todas as letras minúsculas: {minusculas}')
print(f'Seu primeiro nome tem {ler} letras.')
print(f'O seu nome completo tem {remover} letras.')

