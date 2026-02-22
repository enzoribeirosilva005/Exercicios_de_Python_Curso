'''Contando vogais em Tuplas'''
palavras = ('Maça', 'Banana', 'Pessego', 'Uva', 'Morango')

for p in palavras:
    print(f'\nNa palavra {p}, temos: ', end='')

    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')