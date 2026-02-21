'''Formas de analisar dados e realizar verificações'''

valor = input('Digite algo: ')
print('O tipo desse valor é: ', type(valor))
print('Só tem espaços? ', valor.isspace())
print('É alfábetico? ', valor.isalpha())
print('É um decimal? ', valor.isdecimal())
print('É um número? ', valor.isnumeric())
print('Está com letras maiúsculas? ', valor.isupper())
print('Está com letras minúsculas? ', valor.islower())
print('Está capitalizada? ', valor.istitle())