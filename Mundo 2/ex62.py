'''Progressão Aritmética 3.0'''

c = 0
i = True
e = 0

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

while i == True:
    c += 1
    an = a1 + (c - 1) * r
    print(f'a{c} = {an}')

    if c == 10 or e == c:
        escolha = int(input('Você quer adicionar mais quantos termos? '))
        e = c + escolha

        if escolha == 0:
            print('Obrigado pór utilizar o programa!')
            break
