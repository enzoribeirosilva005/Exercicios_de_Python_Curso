'''Dobro, Triplo e raiz de um número inserido no usuário'''

num = float(input('Digite um número: '))

dobro = num * 2
triplo = num * 3
raiz = num**(1/2)

print(f'O número escolhido foi {num}. Ele tem o dobro de {dobro}. O triplo de {triplo} e sua raiz quadrada é: {raiz:.2f}.')