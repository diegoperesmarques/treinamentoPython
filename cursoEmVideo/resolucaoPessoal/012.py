'''
faça um algoritmo que leia o preço de um 
produto e mostre seu novo preço, com 5% de 
desconto.
'''
preco = float(input('Digite o preço do produto: '))
desconto = preco * 0.05
novoPreco = preco - desconto
print('O preco é {}, com desconto de 5% vai para {}'.format(preco, novoPreco))
