'''Maior e meno peso'''

lista = []

for i in range(0, 5):
    peso = float(input('Digite o peso: '))
    lista.append(peso)

maior = max(lista)
menor = min(lista)

print(f'O maior peso é de : {maior:.2f}')
print(f'O menor peso é de: {menor:.2f}')