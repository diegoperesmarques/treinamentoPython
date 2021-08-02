'''
escreve um programa para aprovar o empréstimo bancário
para a compra de uma casa. o programa vai perguntar
o valor da casa, o salário do comprador e em
quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que
ele não pode exceder 30% do salário ou então o 
empréstimo seré negado
'''

valorCasa = int(input('Digite o valor da casa: '))
salario = int(input('Digite o seu salário: '))
anos = int(input('Quantos anos vai pagar: '))
limiteParcela = salario * 0.3
valorParcela = valorCasa / (anos * 12)
situacao = False

if valorParcela < limiteParcela:
    print('A casa no valor de {} está aprovada, parcelas de {:.2f}'.format(valorCasa, valorParcela))
else:
    print('A casa no valor {} está reprovada, parcela de {:.2f} é maior que 30% do salario de {}'.format(valorCasa, valorParcela, salario))
