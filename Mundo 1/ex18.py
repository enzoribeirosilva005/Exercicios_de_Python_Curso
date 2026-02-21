'''Seno, Cosseno e Tangente'''

import math
an = float(input('Digite um angulo: '))
an_rad = math.radians(an)

seno = math.sin(an_rad)
cosseno = math.cos(an_rad)
tangente = math.tan(an_rad)

print(f'O Ângulo {an}, tem o seno de {seno:.2f}. O cosseno de {cosseno:.2f}. A tangente de {tangente:.2f}.')