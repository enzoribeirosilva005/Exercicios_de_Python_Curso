'''Idade do alistamento'''

from datetime import date
atual = date.today().year
ano = int(input('Digite seu ano de nascimento: '))

idade = atual - ano
tempo = 18 - idade
maior = idade - 18

if idade == 18:
    print(f'Você tem {idade} anos em 2026, está no momento de se alistar!\n')

elif idade > 18:
    periodo = atual - maior
    print(f'Você tem {idade} anos em 2026, já passou o seu período de alistamento!\nVocê se alistou em {periodo}.')
    
elif tempo == 1:
    print('Você possui 17 anos em 2026, ainda falta 1 ano para seu alistamento!\nSeu alistamento será em 2027!')

else:
    periodo = atual + tempo
    print(f'Você tem {idade} anos em 2026, faltam {tempo} anos para você se alistar!\nSeu alistamento será em {periodo}')