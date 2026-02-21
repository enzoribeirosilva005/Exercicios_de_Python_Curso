'''Cadastro em grupo'''

i = True
c_idade = 0
c_homens = 0
c_mulher_nova = 0

while i == True:
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M/F]: '))

    if idade > 18:
        c_idade += 1

    if sexo in 'Mm':
        c_homens += 1

    if sexo in 'Ff' and idade < 20:
        c_mulher_nova += 1

    escolha = str(input('Quer continuar o cadastro? [S/N]: '))

    if escolha in 'Nn':
        break

    elif escolha in 'Ss':
        print('Armazenando escolha... ')

    else: 
        print('Opção inválida!')

print(f'Quantidade de pessoas com mais de 18 anos: {c_idade}')
print(f'Quantidade de homens cadastrados: {c_homens}')
print(f'Quantidade de mulheres com menos de 20 anos: {c_mulher_nova}')
