'''
Escreva um programa que leia um valor
em metros e o exiba convertido em 
centímetros e milímetros
'''
tamanho = int(input('Digite o valor em metros: '))
print('Foi digitado {} metros, {} em centimetros e {} milimetros'.format(tamanho, tamanho*100, tamanho*1000))