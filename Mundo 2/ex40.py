'''Média 2.0'''

nota_um = float(input('Digite a primeira nota: '))
nota_dois = float(input('Digite a segunda nota: '))

media = (nota_um + nota_dois) / 2

if media < 5:
    print(f'A média do aluno foi {media:.2f}, ele está reprovado!')

elif media >= 5 and media <= 6.9:
    print(f'A média do aluno é {media:.2f}, ele precisa fazer recuperação!')

else:
    print(f'O aluno está aprovado! Sua média final é: {media:.2f}')