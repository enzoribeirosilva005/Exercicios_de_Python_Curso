# Manipulação de Strings no python

frase = 'Curso em Vídeo Python'
print(frase[1:15:2])

print("""A amizade consegue ser tão complexa.
Deixa uns desanimados, outros bem felizes.
É a alimentação dos fracos
É o reino dos fortes.

Faz-nos cometer erros
Os fracos deixam se ir abaixo
Os fortes erguem sempre a cabeça
Os assim assumem-nos.

Sem pensar conquistamos
o mundo geral
e construímos o nosso pequeno lugar,
deixando brilhar cada estrelinha.

Estrelinhas.
Doces, sensíveis, frias, ternurentas.
Mas sempre presentes em qualquer parte.
Os donos da amizade.""")

'''Funções/Métodos acoplados no Python que são extremamente importantes!'''

leitura = len(frase)
print(leitura)

contar = frase.count('C')
print(contar)

achar = frase.find('deo')
print(achar)

verdade = 'Curso' in frase
print(verdade)

trocar = frase.replace('Python', 'Android')
print(trocar)

# Métodos
cima = frase.upper()
print(cima)

baixo = frase.lower()
print(baixo)

# Primeira letra maiúscula da primeira palavra
capitalismo = frase.capitalize()
print(capitalismo)

# Capitalize em todas as palavras
titulo = frase.title()
print(titulo)

# Remover espaço desnecessários

# r.strip() diminui apenas os espaços da direita, assim como o l.strip diminui só o da esquerda.
remover = frase.strip()
print(remover)

''' Divisão de strings '''

# Divide cada elemento como um item de uma lista/cada palavra
dividir = frase.split()
print(dividir[0][2])

juntar = ''.join(frase)
print(juntar)