'''Maior e menor número digitado'''

num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
num3 = int(input('Digite um número: '))

lista = [num1, num2, num3]

maior = max(lista)
menor = min(lista)

print(f'O maior número é: {maior}.')
print(f'O menor número é {menor}.')
