'''
Crie um programa que vai ler vários números e colocar em 
uma lista.

Depois disso, crie duas listas extras que vão conter apenas
os valores pares e os valores ímpares digitados, 
respectivamente.
ao final, mostre o conteúdo das três listas geradas
'''
listaCompleta = []
listaNumerosPares = []
listaNumerosImpares = []
while True:
    numeroDigitado = int(input('Digite um número: '))
    listaCompleta.append(numeroDigitado)
    if numeroDigitado % 2 == 0:
        listaNumerosPares.append(numeroDigitado)
    elif numeroDigitado % 2 != 0:
        listaNumerosImpares.append(numeroDigitado)

    condicaoParada = ' '
    while condicaoParada not in 'SN':
        condicaoParada = str(input('Quer continuar? [S/N] ')).upper().strip()
    if condicaoParada == 'N':
        break

print(f'Lista completa: {listaCompleta}')
print(f'Números pares: {listaNumerosPares}')
print(f'Números impares: {listaNumerosImpares}')