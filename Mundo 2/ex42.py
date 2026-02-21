'''Verificação de Existência do triângulo 2.0'''

l1 = float(input('Digite o lado 1: '))
l2 = float(input('Digite o lado 2: '))
l3 = float(input('Digite o lado 3: '))

lista = [l1, l2, l3]
maior = max(lista)
lista.remove(maior)

soma = lista[0] + lista[1]

if soma >= maior:
    print(f'O triangulo com os lados {l1}, {l2} e {l3}, pode ser formado!')

    if l1 == l2 and l2 == l3:
        print('O triângulo formado será um equilatero!')

    elif l1 == l2 or l1 == l3:
        print('O triângulo é isóceles')

    else: 
        print('O triângulo é escaleno!')

else:
    print(f'O triangulo com os lados {l1}, {l2} e {l3}, não pode ser formado!')