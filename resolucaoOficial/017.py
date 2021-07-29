'''
faça um programa que leia o comprimento do cateto oposto
e do cateto adjacente de um triângulo retângulo. Calcule e mostre
o comprimento da hipotenusa.
'''
import math
co = float(input('Comprimeiro do cateo oposto: '))
ca = float(input('Comprimeiro do cateo adijacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))