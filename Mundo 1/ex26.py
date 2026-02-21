'''Identificação de letras em uma frase'''

frase = str(input('Digite uma frase: ')).strip().upper()
contagem = frase.count('A')
primeira = frase.find('A') + 1
u = frase.rfind('A') + 1


print(f'A letra A aparece {contagem} vezes na frase.')
print(f'A primeira letra A apareceu na posição {primeira}.')
print(f'A última letra A apareceu na posição {u}')
