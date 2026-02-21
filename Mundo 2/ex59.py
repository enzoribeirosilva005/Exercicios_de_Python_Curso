'''Menu de Calculadora'''

from time import sleep

i = True

while i == True:  
    print('='*20)
    print('MENU DE OPÇÕES')
    print('='*20)

    num1 = int(input('\nDigite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))

    print('\n1 - Somar\n2 -  Multiplicar\n3 - Comparar\n4 - Novos números\n5 - Fechar o programa')
    escolha = int(input('\nDigite a escolha desejada: '))

    if escolha == 1:
        print('SOMA')
        soma = num1 + num2
        print(f'{num1} + {num2} = {soma}')

        escolha2 = str(input('Você deseja continuar a utilizar o programa? [S/ N]: '))

        if escolha2 in 'Ss':
                print('\nArmazenando escolha...\n')
                sleep(1)

        elif escolha2 in 'Nn':
            print('\nArmazenando escolha...')
            sleep(1)
            print('\nObrigado por utilizar nosso programa! Espero que tenha gostado!')
            break

        else:
            print('\nArmazenando escolha...')
            sleep(1)
            print('Opção inválida, tente novamente mais tarde!\n')

    elif escolha == 2:
        print('MULTIPLICAÇÃO')
        multi = num1 * num2
        print(f'{num1} * {num2} = {multi}')
        escolha2 = str(input('Você deseja continuar a utilizar o programa? [S/ N]: '))

        if escolha2 in 'Ss':
                print('\nArmazenando escolha...\n')
                sleep(1)

        elif escolha2 in 'Nn':
            print('\nArmazenando escolha...')
            sleep(1)
            print('\nObrigado por utilizar nosso programa! Espero que tenha gostado!')
            break

        else:
            print('\nArmazenando escolha...')
            sleep(1)
            print('Opção inválida, tente novamente mais tarde!\n')

    elif escolha == 3:
        print('COMPARAÇÃO')

        if num1 > num2:
            print(f'{num1} é maior que {num2}!')
            escolha2 = str(input('Você deseja continuar a utilizar o programa? [S/ N]: '))

            if escolha2 in 'Ss':
                    print('\nArmazenando escolha...\n')
                    sleep(1)

            elif escolha2 in 'Nn':
                print('\nArmazenando escolha...')
                sleep(1)
                print('\nObrigado por utilizar nosso programa! Espero que tenha gostado!')
                break

            else:
                print('\nArmazenando escolha...')
                sleep(1)
                print('Opção inválida, tente novamente mais tarde!\n')

        elif num1 == num2:
            print('Os dois números são iguais!')
            escolha2 = str(input('Você deseja continuar a utilizar o programa? [S/ N]: '))

            if escolha2 in 'Ss':
                    print('\nArmazenando escolha...\n')
                    sleep(1)

            elif escolha2 in 'Nn':
                print('\nArmazenando escolha...')
                sleep(1)
                print('\nObrigado por utilizar nosso programa! Espero que tenha gostado!')
                break

            else:
                print('\nArmazenando escolha...')
                sleep(1)
                print('Opção inválida, tente novamente mais tarde!\n')

        else:
            print(f'{num2} é maior que {num1}!')
            escolha2 = str(input('Você deseja continuar a utilizar o programa? [S/ N]: '))

            if escolha2 in 'Ss':
                    print('\nArmazenando escolha...\n')
                    sleep(1)

            elif escolha2 in 'Nn':
                print('\nArmazenando escolha...')
                sleep(1)
                print('\nObrigado por utilizar nosso programa! Espero que tenha gostado!')
                break

            else:
                print('\nArmazenando escolha...')
                sleep(1)
                print('Opção inválida, tente novamente mais tarde!\n')

    elif escolha == 4:
        print('\nArmazenando escolha...')
        sleep(1)
        print('Novos números serão escolhidos!\n')


    elif escolha == 5:
        print('Obrigado por utilizar esse programa!')
        break

    else:
        print('Opção inválida, tente novamente!\n')