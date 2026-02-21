'''Existe Santo na cidade digitada?'''

c = input('Digite o nome de uma cidade: ').strip().title()

inicial_c = c.split()

ler = inicial_c[0]

if ler == 'Santo':
    print(f'A cidade chamada de {c} começa com Santo!')

else:
    print(f'A cidade chamada {c}, não começa com Santo.')