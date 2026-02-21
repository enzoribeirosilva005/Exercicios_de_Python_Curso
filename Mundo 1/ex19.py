'''Escolhendo um aluno aleatório'''

import random
aluno1 = input('Digite o nome do aluno 1: ')
aluno2 = input('Digite o nome do aluno 2: ')
aluno3 = input('Digite o nome do aluno 3: ')
aluno4 = input('Digite o nome do aluno 4: ')

lista_nomes = [aluno1, aluno2, aluno3, aluno4]

escolha = random.choice(lista_nomes)
print(f'O aluno escolhido foi: {escolha}.')