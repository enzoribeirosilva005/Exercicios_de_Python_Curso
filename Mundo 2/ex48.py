'''Soma dos múltiplos de 3 e Ímpares'''

s = 0
for i in range(1, 501):
    mult = i % 3
    impar = i % 2

    if mult == 0 and impar != 0:
        s += i

print('Resultado da soma:', s)