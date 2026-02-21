'''Área de uma parede'''

l = float(input('Digite a largura da sua parede em metros: '))
a = float(input('Digite a altura da sua parede em metros: '))

area = l * a

qt = area / 2

print(f'A área da sua parede é de {area:.2f} metros quadrados. Será necessário utilizar {qt:.2f} litros de tinta para pintá-la.')