'''Cálculo de IMC'''

peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em m: '))

imc = peso / (altura * altura)

print(f'Seu índice de massa coporal é: {imc:.1f}.')

if imc < 18.5:
    print('Status: Abaixo do peso')

elif imc >= 18.5 and imc < 25:
    print('Status: Peso Ideal')

elif imc >= 25 and imc < 30:
    print('Status: Sobrepeso')

elif imc >= 30 and imc <= 40:
    print('Staus: Obesidade')

elif imc > 40:
    print('Status: Obesidade mórbida')