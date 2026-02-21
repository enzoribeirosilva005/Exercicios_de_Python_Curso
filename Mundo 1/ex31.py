'''Preço da Gasolina em uma viagem'''

d = float(input('Digite a distância da sua viagem em km: '))

if d <= 200:
    p = d * 0.50
    print(f'O preço da gasolina para uma viagem de {d:.0f}Km é de: {p:.2f}R$')

else:
    p = d * 0.45
    print(f'O preço da gasolina para uma viagem de {d:.0f}Km é de {p:.2f}R$')