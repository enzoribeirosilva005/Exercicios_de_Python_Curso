'''Sorteando nomes em ordem aleatória'''

import random

aluno1 = input('Digite o nome do aluno: ')
aluno2 = input('Digite o nome do aluno: ')
aluno3 = input('Digite o nome do aluno: ')
aluno4 = input('Digite o nome do aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(alunos) # Pode usar sample também, mas ai nós teriamos que usar len também

for i, aluno in enumerate(alunos, 1):
    print(f'{i}: {aluno}')