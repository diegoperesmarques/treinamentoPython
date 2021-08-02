'''
faça um programa que leia um número qualquer 
e mostre o seu fatorial.
'''
numero = int(input('Digite um número: '))

contador = 1
resultado = 1
print('{}'.format(numero), end="")
while contador < numero:
    print('x{}'.format(numero - contador), end = "")
    resultado = resultado * (numero - contador)
    contador += 1

resultado = numero * resultado
print('\n O resultado é {}'.format(resultado))