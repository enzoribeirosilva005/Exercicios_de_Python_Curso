'''Progressão Aritmética'''

termo1 = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Digite a razão de uma PA: '))

for i in range(0, 10, 1):
    i += 1
    an = termo1 + (i - 1) * razao
    print(f'a{i} é {an}')