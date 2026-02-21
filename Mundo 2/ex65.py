'''Maior e menor valor'''

i = True
lista = []
c = 0
n = 0

while i == True:
    num = int(input('Digite um número: '))
    c += 1
    n += num
    lista.append(num)
    escolha = str(input('Você quer continuar digitando números? (S/N): '))

    if escolha in 'Nn':
       maior = max(lista)
       menor = min(lista)
       media = n / c
       print(f'Média do(s) {c} valor(es) digitado(s): {media:.2f}\nMaior valor digitado: {maior}.\nMenor valor digitado: {menor}.')
       break

    elif escolha in 'Ss':
        print() 

    else:
        print('Digite uma opção válida!\n')