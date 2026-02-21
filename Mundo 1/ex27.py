'''Identificando o primeiro e último nome inserido'''

nome = str(input('Digite seu nome completo: ')).strip().title()
achar = nome.rfind(' ')

divisao = nome.split()


print(f'Seu primeiro nome é: {divisao[0]}')
print(f'Seu último nome é: {nome[achar +1:]}')

# Outra forma de fazer! (Mais certa!)
# print(f'Seu último nome é: {divisao[len(divisao) - 1]}')