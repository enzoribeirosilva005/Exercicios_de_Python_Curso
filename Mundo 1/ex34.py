'''Aumento de salário'''

s = float(input('Digite seu salário: '))

if s > 1250:
    a = s * 1.10
    print(f'Seu salário com aumento é: {a}R$')

elif s <= 1250:
    a = s * 1.15
    print(f'Seu salário com aumento é: {a}R$')

else:
    print('Algo deu errado, tente novamente!')