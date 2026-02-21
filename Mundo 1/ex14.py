'''Conversão de Temperatura'''

print('1 - Conversão de Graus Celsius.\n2 - Conversão de Fahrenheit.\n3 - Conversão de kelvin.')
escolha = int(input('Escolha o número da opção de calculo desejada: '))

if escolha == 1:
    c = float(input('Digite a temperatura em °C: '))
    f = (c * 9/5) + 32
    k = c + 273.15
    print(f'A temperatura {c:.2f}°C é {f:.2f} Fahrenheit. E {k:.2f} Kelvin.')

elif escolha == 2:
    f = float(input('Digite a temperatura em Fahrenheit: '))
    c = (f - 32) * 5/9
    k = c + 273.15
    print(f'A temperatura {f:.2f}Fahrenheit é {c:.2f}°C. E {k:.2f} Kelvin.')

elif escolha == 3:
    k = float(input('Digite um a temperatura em kelvin: '))
    c = k - 273.15
    f = (c) * 9/5 + 32
    print(f'A temperatura {k:.2f} Kelvin é {c:.2f}°C. E {f:.2f} Fahrenheit.')

else:
    print('Houve um problema, tente novamente!')