'''Ano bissexto'''

from datetime import date

ano = int(input('Digite o ano para saber se ele é bissexto: '))

a = str(ano)

if a.find('00'):
    teste2 = ano % 400

    if teste2 == 0:
        print(f'O ano {ano} é bissexto!')

    else:
        print('Seu número não termina com 00, o que significa que ele não pode ser dividido por 400, primeira validação descartada.')

print('Testando segunda condição...')
teste1 = ano % 4

if teste1 == 0:
    print(f'O ano {ano} é bissexto! Pode ser dividido por 4!')
                
else:
    print('Esse ano não é bissexto!')   


