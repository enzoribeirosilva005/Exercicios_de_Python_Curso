# Anotações

# Tuplas são Imutáveis!
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

print(lanche[:3])

for comida in lanche:
    print(f'Eu vou comer {comida}') # Formas de explorar os itens de uma tupla para a saída de dados

print()

for cont in range(0, len(lanche)):
    print(f'Vou comer comida {lanche[cont]} na posição {cont}') # Formas de explorar os itens de uma tupla para a saída de dados

print()

for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida} na posição {pos}') # Formas de explorar os itens de uma tupla para a saída de dados

print('Comi bastante! kkkkk')

print(sorted(lanche)) # Ordena os itens de uma tupla, transformando elas em listas

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b # Unindo duas tuplas - Lembrando que a ordem dos fatores, altera os produtos quando são tuplas

print(c)

print(c.count(5)) # Quantas vezes aparece o número

print(len(c)) # Quantidade de itens da tupla

print(c.index(2)) # Qual é a posição do elemento procurado - Somente a primeira ocorrência

pessoa = ('Gustavo', 39, 'M', 99.88) # Podemos ter dados de tipos diferentes na tupla

# del(pessoa) 
# A única coisa que é possível fazer com a tupla é apagar ela inteira

print(pessoa)