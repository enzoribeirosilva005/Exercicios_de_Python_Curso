# Empréstimo

casa = float(input('Digite o valor da casa: '))
salario = float(input('Qual é o salário do comprador? '))
tempo = int(input('Em quantos anos o comprador vai pagar? '))

p = (casa / tempo) / 12

if p > salario * 0.3:
    print(f'O valor da parcela é {p:.2f}R$, porém 30% do seu salário equivale a {salario * 0.3:.2f}R$, infelizmente o empréstimo foi negado!')

else:
    print(f'O empréstimo foi aceito! O valor das parcelas será de: {p:.2f}R$. Ficando abaixo dos 30% do seu salário que equivalem a {salario * 0.3:.2f}R$')