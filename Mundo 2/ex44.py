'''Descontos e Pagamentos'''

preco = float(input('Digite o preço das compras: R$'))
escolha = int(input('Formas de pagamento:\n1 - À vista com Dinheiro/Cheque\n2 - À vista com o Cartão\n3 - 2x no Cartão\n4 - 3x ou mais no Cartão\nQual é a opção escolhida: '))

if escolha == 1:
    desconto = preco * 0.9
    print(f'Você ganhou 10% de desconto com essa forma de pagamento! O valor a ser pago pelo produto é de {desconto:.2f}R$')

elif escolha == 2:
    desconto = preco * 0.95
    print(f'Você ganhou 5% de desconto com essa forma de pagamento! O valor a ser pago pelo produto é de {desconto:.2f}R$')

elif escolha == 3:
    print(f'O preço a ser pago continua o mesmo, sem descontos! {preco:.2f}, porém você pagará duas parcelas de {preco/2:.2f}R$ sem juros!')

elif escolha == 4:
    juros = preco * 1.2
    escolha2 = int(input('Digite o número de vezes de parcelas no cartão: '))
    preco_final = juros / escolha2

    print(f'O valor da compra {preco:.2f}R$ com 20% de juros ficará {juros:.2f}R$, com parcelas de {preco_final:.2f}R$!')

else:
    print('Escolha inválida de pagamento, tente novamente!')