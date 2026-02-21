'''Quantidade de números e a Soma entre eles 2.0'''

c = 0
s = 0
num = int

while not num == 999:
    num = int(input('Digite um número: '))
    c += 1
    s += num

if num == 999:
    s -= num
    c -=1 
    
print(f'{c} números foram digitados, a soma entre eles é de {s}')
