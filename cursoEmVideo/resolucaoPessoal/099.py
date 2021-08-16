'''
Faça um programa que tenha um função chamada maior(), que receva
vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles
é o maior.
'''
def linha():
    print('-=' * 40)

def maior(* num):
    linha()
    maior = 0
    print('Analisando os valores passado ...')
    for i in num:
        print(f'{i} ', end='')
    print(f'Foram informados {len(num)} valores ao todo')
    for i in range(0, len(num)):
        if maior < num[i]:
            maior = num[i]
    print(f'O maior valor informado foi {maior}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2,)
maior(6)
maior()