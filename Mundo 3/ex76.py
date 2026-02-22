'''Lista de preços com Tuplas'''

lista = ('Livro', 49.99,
        'Estojo', 19.99,
        'Cadeira Gamer', 450,
        'PC', 2500,
        'Mesa', 250,
        'Caderno Chique', 99.87)

print('='*40)
print(f'{"LISTA DE PREÇOS!!!":^40}')
print('='*40)
for item in range(0, len(lista)):
    if item % 2 == 0:
        print(f'{lista[item]:.<30}', end='')
    else:
        print(f'R${lista[item]:>8.2f}')

print('-'*40)