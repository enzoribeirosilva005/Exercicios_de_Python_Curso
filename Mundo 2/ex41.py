'''Categorias de Atletas'''

from datetime import date

atual = date.today().year
nasc = int(input('Digite o ano de nascimento do atleta: '))

idade = atual - nasc

if idade <= 9:
    print(f'O atleta possui {idade} anos, participará da categoria MIRIM!')

elif idade > 9 and idade <=14:
    print(f'O atleta possui {idade} anos, portanto participará da categoria INFANTIL!')

elif idade > 14 and idade <= 19:
    print(f'O atleta possui {idade} anos, portanto participará da categoria JUNIOR!')

elif idade > 19 and idade <= 25:
    print(f'O atleta possui {idade} anos, portanto participará da categoria SÊNIOR!')

elif idade > 25 and idade <= 64:
    print(f'O atleta possui {idade} anos, portanto participará da categoria MASTER!')

elif idade > 64 and idade <=100:
    print(f'O atleta possui {idade} anos, por estar em um estágio avançado de idade, não poderá competir em nenhuma categoria!')

else:
    print('Idade inválida, tente novamente!')