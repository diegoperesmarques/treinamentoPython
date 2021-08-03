'''
Crie um programa que vai ler vários números e colocar 
em uma lista.

Depois disso, mostre:
a) Quantos números foram digitados;
b) A lista de valores, ordenada de forma decrescente;
c) Se o valor 5 foi digitado e está ou não 
'''

listaNumeros = []
contadorNumeros = contadorCinco = 0
while True:
    numeroDigitado = int(input('Digite um número: '))
    if numeroDigitado == 5:
        contadorCinco = 1
    listaNumeros.append(numeroDigitado)
    contadorNumeros += 1
    condicao = ' '
    while condicao not in 'SN':
        condicao = str(input('Quer continuar? [S/N] ')).upper().strip()
    if condicao == 'N':
        break

print(f'O total de números digitados foi {contadorNumeros}')
listaNumeros.sort(reverse=True)
print(f'Em ordem descrevente: {listaNumeros}')
if contadorCinco > 0:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')