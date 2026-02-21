'''Progressão Aritmética 2.0'''

c = 0
p1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

while c < 10:
    c += 1
    an = p1 + (c - 1) * r
    print(f'a{c} = {an}')