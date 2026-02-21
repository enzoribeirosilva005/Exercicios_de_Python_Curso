'''Tabuada 2.0'''

num = int(input('Digite um número para saber a tabuada dele: '))

for i in range(0, 10):
    i += 1
    resu = num * i
    print(f'{num} X {i} = {resu}')