'''Cálculo de Fatorial'''

# from math import factorial

# n = int(input('Digite um número: '))
# f = factorial(n)

# print(f'O fatorial de {n}! é {f}')

'''Ou'''

# n = int(input('Digite um número: '))
# c = n
# f = 1

# print(f'Calculando fatorial de {n}! = ', end='')
# while c > 0:
#     print(f'{c}', end='')
#     print(' x ' if c > 1 else ' = ', end='')
#     f *= c
#     c -= 1

# print(f)

'''Ou'''

n = int(input('Digite um número: '))
i = n
f = 1

print(f'Calculando o fatorial de {n}! = ', end='')
for i in range(n, 0, -1):
    print(f'{i}', end='')
    print(' X ' if i > 1 else ' = ', end='')
    f *= i
    i -= 1

print(f)