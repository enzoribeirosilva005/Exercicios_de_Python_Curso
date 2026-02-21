'''Aluguel do carro'''

km = float(input('Digite a quantidade de km percorridos: '))
qt_dias = int(input('Digite a quantidade de dias que ele foi alugado: '))

aluguel = 60 * qt_dias + 0.15 * km
print(f'O aluguel do carro resultou no valor de: {aluguel:.2f}R$.')