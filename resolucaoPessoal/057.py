'''
faça um programa que leia o sexo de uma
pessoa, mas só aceite os valores 'M' ou 
'F'. Caso esteja errado, peça a digitação
novamente até ter um valor correto
'''

sexo = input('Digite o sexo: ').strip()
while sexo not in 'Mm':
    print('Sexo errado, digite novamente!')
    sexo = input('Digit o sexo: ').strip()