'''
desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares.
se o valor digitado for impar, desconsidere-o
'''

resultado = 0
for i in range(1, 7):
    numero = int(input('Digite um número {}:'.format(i)))
    if numero % 2 == 0:
        resultado = resultado + numero

print(resultado)