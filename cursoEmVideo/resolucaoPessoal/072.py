'''
Crie um programa que tenha uma tupla totalmente preenchida com uma
contagem por extensão, de zero até vinte.

Seu programa deverá ler um número pelo teclado (entre 0 e 20) e 
mostrá-lo por extenso.
'''
numerosExtenso = ('Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze','Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
numero = int(input('Digite um número entre 0 e 20: '))
while numero > 20:
    numero = int(input('Tente novamente. Digite um número entre 0 e 20: '))

print(f'Você digitou o número {numerosExtenso[numero-1]}')