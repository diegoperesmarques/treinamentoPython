'''
faça um programa que leia a largura e a
altura de uma parede em metros. calcule
a sua área e a quantidade de tinta 
necessária para pintá-la, sabendo que
cada tipo de tinta, pinta uma área de 2m2.
'''
largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))
area = largura * altura
quantidadeTinta = area / 2

print('A area da parede e {}, sao necessarios {} litros de tintas'.format(area, quantidadeTinta))