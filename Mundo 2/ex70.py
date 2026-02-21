'''Compras'''

from time import sleep

i = True
total = 0
lista_precos = 0
lista = []
preco2 = 0
c = 0

while i == True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))

    lista.append(preco)
    menor = min(lista)

    c += 1
    total += preco

    if c == 1:
        barato = produto

    else:
        if preco < menor:
            barato = produto

    if preco > 1000:
        lista_precos += 1

    escolha = str(input('Você quer continuar o cadastro? [S/N]: '))

    if escolha in 'Ss':
        sleep(1)
        print('Armazenando escolha...')
        sleep(1)

    elif escolha in 'Nn':
        print('Obrigado por utilizar o programa!')
        break

    else:
        print('Opção inválida!')


print(f'O total gasto na compra: R${total}')
print(f'Quantidade de produtos que custam mais de R$1000: {lista_precos}')
print(f'Nome do produto mais barato: {barato}. O produto custou R${menor}')