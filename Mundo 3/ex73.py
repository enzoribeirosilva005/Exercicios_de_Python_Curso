'''Tuplas com Times de futebol'''

tupla = ('Palmeiras', 'São Paulo', 'Fluminense', 'Bahia', 'Corinthians', 'Atlético-PR', 'Bragantino', 'Chapecoense', 'Mirassol', 'Coritiba', 'Flamengo', 'Botafogo', 'Grêmio', 'Vitória', 'Atlético-MG', 'Remo', 'Vasco', 'Santos', 'Internacional', 'Cruzeiro')

print('='*70)
print('TABELA DOS PRIMEIROS COLOCADOS DO CAMPEONATO BRASILEIRO DE FUTEBOL')
print('='*70)

for i in range(0, len(tupla[:5])):
    print(f'{i + 1}° Lugar: {tupla[i]}')

print('='*70)
print('TABELA DOS ÚLTIMOS COLOCADOS DO CAMPEONATO BRASILEIRO DE FUTEBOL')
print('='*70)

for i, time in enumerate(tupla[16:]):
    print(f'{i + 17}° Lugar: {time}')

print(f'\nTimes em ordem alfabética: {sorted(tupla)}\n')

tupla.count('São Paulo')
print(f'O São Paulo está no {tupla.count('São Paulo') + 1}° Lugar da tabela')