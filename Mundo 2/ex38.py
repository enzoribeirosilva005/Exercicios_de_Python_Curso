'''Maior e menor número'''

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite um valor: '))


if num1 == num2:
    print('Os números são iguais!')

elif num1 > num2:
    print('O primeiro número é o maior!')

elif num2 > num1:
    print('O segundo número é o maior!')

else:
    print('Algo deu errado, tente novamente!')