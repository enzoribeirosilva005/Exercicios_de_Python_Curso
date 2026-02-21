'''Velocidade do carro que vai ou não você fazer ser multado'''

v = float(input('Digite a velocidade do carro: '))

if v > 80:
    l = v - 80
    m = l * 7
    print(f'Você foi multado, sua dívida é de: {m:.2f}R$')

else:
    print('Continue assim!')