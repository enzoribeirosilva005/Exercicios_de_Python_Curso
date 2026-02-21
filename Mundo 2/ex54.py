'''Verificar Maioridade'''

from datetime import date

hoje = date.today().year
lista_maioridade = []
lista_menores = []

for i in range(0, 7):
    ano = int(input('Digite o ano de seu nascimento: '))
    idade = hoje - ano

    if idade >= 21:
        lista_maioridade.append(idade)

    else:
        lista_menores.append(idade)

print(f'{len(lista_maioridade)} pessoas que são maior de idade!\n{len(lista_menores)} pessoas que são menor de idade!')