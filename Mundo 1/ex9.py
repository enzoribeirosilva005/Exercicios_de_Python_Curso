'''Tabuada'''

num = int(input('Digite um número: '))
i = 0

print(f'A tábuada do número {num} é a seguinte:')
print(12*'=')

for i in range(10):
    tab = num * (i+1)
    print(f'{num} x {i+1} = {tab}')
print(12*'=')