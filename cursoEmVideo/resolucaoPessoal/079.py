'''
Crie um programa onde o usuário possa digitar vários valores numéricos e 
cadastre-os em uma lista. Caso o número já exista lá dentor, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''

listaNumeros = []
while True: 
    numeroDigitado = int(input('Digite um valor: '))
    if numeroDigitado in listaNumeros:
        print('Valor duplicado! Não vou adicionar ...')
    else: 
        listaNumeros.append(numeroDigitado)
        print('Valor adicionado com sucesso ...')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
listaNumeros.sort()
print(f'Você digitou os valores {listaNumeros}')