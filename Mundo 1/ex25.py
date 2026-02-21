'''Identificação de um nome na entrada de Dados'''

nome = str(input('Digite seu nome completo: ')).strip().title()

if nome.find('Silva') != -1:
    print(f'A pessoa chamada de {nome}, possui o nome Silva.')

else:
    print(f'A pessoa chamada de {nome}, não possui o nome Silva.')