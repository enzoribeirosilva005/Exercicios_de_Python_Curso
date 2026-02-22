'''Manipulação de listas'''

lista = []

lista.append('Enzo') # Adiciona itens na lista
print(lista)

lista.insert(0, 'Henrique') # Entra na posição zero e empurra os elementos para as posições a seguir
print(lista)

'''Para apagar elementos de uma lista
del lista[1] 
print(lista)'''

# Ou

'''lista.pop() - Remove o último item de uma lista
print(lista)'''

'''lista.remove('Henrique') - Aqui a gente indica o valor que queremos eliminar
print(lista)'''

valor = list(range(4,11)) # Declarando uma lista com range
print(valor)

valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort() # Ordena os valores
print(valores)

valores.sort(reverse=True) # Ordem inversa
print(valores)

print(len(valores)) # Quantos elementos a lista possui