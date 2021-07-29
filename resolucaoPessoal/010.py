'''
Crie um programa que leia quanto dinheiro 
uma pessoa tem na carteira e mostre quantos
dólares ela pode comprar.

considere 
U$ 1,00 = R$ 3,27
'''
dinheiroCarteira = float(input('Digite o valor na carteira: '))
valorDolar = 3.27
total = dinheiroCarteira / valorDolar
print('Você pode comprar {:.2f} dolares'.format(total))