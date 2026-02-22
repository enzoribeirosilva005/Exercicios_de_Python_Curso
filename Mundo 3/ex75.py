'''Análise de Dados em Tuplas'''

lista = []
par = 0

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite um valor: '))
num3 = int(input('Digite um valor: '))
num4 = int(input('Digite um valor: '))

tupla = (num1, num2, num3, num4)

print(f'O número 9 apareceu: {tupla.count(9)} vez(es)!')

try:
    pos_3 = tupla.index(3) + 1

except:
    print('O número três não foi digitado!')

else:
    if pos_3 >= 0:
        print(f'O número 3 apareceu na posição {pos_3}!')

    else:
        print('O número três não foi digitado!')


for i in range(0, 4):
    result = tupla[i] % 2

    if result == 0:
        par += 1
        lista.append(tupla[i])

print(f'{par} números são pares: {lista}')
