'''Lista dos números pares de 2 a 50'''

lista = []

for i in range(1, 51):
    n = i % 2
    if n == 0:
        lista.append(i)
print(lista)