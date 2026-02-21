'''Soma dos números pares'''

result = 0

for i in range(0, 6):
    num = int(input('Digite um número inteiro: '))
    par = num % 2

    if par == 0:
        result += num

print('A soma dos números pares digitados é:', result)