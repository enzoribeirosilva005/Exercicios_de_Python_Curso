'''Informando o Sexo'''

i = True

while i == True:
    sexo = str(input('Digite o sexo da pessoa [M/F]: '))

    if sexo in 'Ff' or sexo in 'Mm':
        print('Obrigado por informar seu sexo corretamente!')
        break

    else:
        print('Digite seu sexo corretamente!')