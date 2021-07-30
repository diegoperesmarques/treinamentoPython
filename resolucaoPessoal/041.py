'''
a confederação nacional de natação precisa de um 
programa que leia o ano de nascimento de 
um atleta e mostre sua categoria, de acordo com 
a idade:

até 9 ano: mirim
até 14 anos: infantil
até 19 anos: junior
até 20 anos: senior
acima: master
'''
anoNascimento = int(input('Digite o ano de nascimento: '))
idade = 2021 - anoNascimento

if idade >= 20:
    print('Categoria MASTER com {} anos'.format(idade))
elif idade >= 19:
    print('Categoria SENIOR {} anos'.format(idade))
elif idade >= 14:
    print('Categoria JUNIOR {} anos'.format(idade))
elif idade >= 9:
    print('Categoria INFANTIL {} anos'.format(idade))
else:
    print('Categoria MIRIM {} anos'.format(idade))