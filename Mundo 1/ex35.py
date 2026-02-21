'''Testando se o triângulo pode existir'''

c1 = float(input('Digite o comprimento do primeiro lado: '))
c2 = float(input('Digite o comprimento do segundo lado: '))
c3 = float(input('Digite o comprimento do terceiro lado: '))

lista = [c1, c2, c3]

maior = max(lista)

lista.remove(maior)

if lista[0] + lista[1] > maior:
    print('O triângulo pode existir')

else:
    print('O triângulo não pode existir')