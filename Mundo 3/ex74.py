'''Maior e menor valores em tupla'''

from random import randint

num1 = randint(0, 9)
num2 = randint(0, 9)
num3 = randint(0, 9)
num4 = randint(0, 9)
num5 = randint(0, 9)

tupla = (num1, num2, num3, num4, num5)

# Ou
'''tupla2 = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(tupla2)'''

print(tupla)

maior = max(tupla)
menor = min(tupla)

print(f'Maior número: {maior}')
print(f'Menor número: {menor}')