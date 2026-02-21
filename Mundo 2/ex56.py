'''Cadastro da Família'''

lista_idade = []
lista_nome = []
lista_sexo = []

maioridade_homem = 0
idade_velho = 0

total_mulheres_menos = 0


print('PROGRAMA DA FAMÍLIA!!!')

for i in range(0, 4):
    nome = str(input('\nDigite um nome: ')).strip()
    idade = int(input('Digite uma idade: '))
    sexo = str(input('Digite seu sexo [M/F]: ')).strip()

    lista_nome.append(nome)
    lista_idade.append(idade)
    lista_sexo.append(sexo)

    if sexo in'Mm' and i == 0:
        maioridade_homem = idade
        nome_velho = nome

    if sexo in 'Mm' and idade > maioridade_homem:
        maioridade_homem = idade
        nome_velho = nome

    if sexo in 'Ff' and idade < 20:
        total_mulheres_menos += 1

media = (lista_idade[0] + lista_idade[1] + lista_idade[2] + lista_idade[3]) / 4

print(f'A média de idade do grupo é de: {media} anos!')
print(f'O homem mais velho tem {maioridade_homem} anos e se chama {nome_velho}')
print(f'A quantidade de mulheres menores de 20 anos é de {total_mulheres_menos} mulher/mulheres')
