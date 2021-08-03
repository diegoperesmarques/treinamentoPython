'''
faça um programa que leia 5 valores numéricos e guarde-
os em uma lista.

No final, mostre qual foi o maior e o menr valor 
digitado e as suas respectivas posições na lista.
'''
listaNumeros = []
maiorNumero = menorNumero = posicaoMenorNumero = posicaoMaiorNumero = 0


for i in range(0, 5):
    numerosDigitados = int(input(f'Digite o número {i}: '))
    listaNumeros.append(numerosDigitados)
    print(f'{listaNumeros} como esta')

    if i == 0:
        menorNumero = listaNumeros[i]
        posicaoMenorNumero = i
    
    if listaNumeros[i] < menorNumero:
        menorNumero = listaNumeros[i]
        posicaoMenorNumero = i + 1
    
    if listaNumeros[i] > maiorNumero:
        maiorNumero = listaNumeros[i]
        posicaoMaiorNumero = i + 1


        

print(f'Você digitou os valores: {listaNumeros}')
print(f'O maior valor digitado foi {maiorNumero} nas posições {posicaoMaiorNumero}')
print(f'O menor valor digitado foi {menorNumero} nas posições {posicaoMenorNumero}')