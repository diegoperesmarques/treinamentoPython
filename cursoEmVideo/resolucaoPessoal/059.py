'''
crie um programa que leia dois valores e
mostre um menu na tela:

[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
seu programa deverá realizar a opção solicitada
em cada caso.
'''
numero1 = int(input('Digite o primeiro valor: '))
numero2 = int(input('Digite o segundo valor: '))

opcao = 0
while opcao != 5:
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    ''')
    opcao = int(input('Digite o número desejado: '))
    if opcao == 1:
        print('{} + {} = {}'.format(numero1, numero2, numero1+numero2))
    elif opcao == 2:
        print('{} x {} = {}'.format(numero1, numero2, numero1+numero2))
    elif opcao == 3:
        if numero1 > numero2:
            print('{} é o maior'.format(numero1))
        elif numero1 < numero2:
            print('{} é o maior'.format(numero2))
        else:
            print('Os números são iguais!')
    elif opcao == 4:
        numero1 = int(input('Digite o primeiro valor: '))
        numero2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        break
    else:
        print('Não é uma opção valida!')