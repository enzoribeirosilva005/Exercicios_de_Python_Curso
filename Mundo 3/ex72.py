'''Número por extenso!'''

tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:

    num = int(input('Digite um número de 0 a 20: '))

    if num <= 20 and num >= 0:
        print(f'O número {num} por extenso é: {tupla[num]}.')
        break

    elif num < 0:
        print('Número inválido!')

    else:
        print('Número inválido!')