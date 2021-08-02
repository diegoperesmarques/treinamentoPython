'''
Faça um programa que leia o nao de um nascimento
de um jovem e informe, de acordo com sua idade:

se ele ainda vai se alistar ao serviço militar.
se é a hora de se alistar.
se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que
falta ou que passou do prazo
'''
anoNascimento = int(input('Digite o seu ano de nascimento: '))
idade = 2021 - anoNascimento

if idade == 18:
    print('Está na hora de se alistar!')
elif idade > 18:
    print('Passou do prazo por {} anos'.format(idade-18))
else:
    print('Faltam {} anos para se alistar'.format(18-idade))