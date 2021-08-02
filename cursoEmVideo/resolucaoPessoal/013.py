'''
faça um algoritmo que leia o salário de um 
fucionário e mostre seu novo salário, com 
15% de aumento
'''
salario = float(input('Digite o seu salario: '))
aumento = salario * 0.15
novoSalario = salario + aumento
print('O salario é {}, com aumento de 15% vai {}'.format(salario, novoSalario))