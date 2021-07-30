'''
crie um programa que leia duas notas de um aluno
e calcule sua média, mostrando uma mensagem no final
de acordo com a média atingida:

média abaixo de 5.0: reprovado
média entre 5.0 e 6.0: recuperação
média 7.0 ou superior: aprovado
'''

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2

if media >= 7:
    print('O aluno está aprovado com média {}'.format(media))
elif media >= 5:
    print('O alunoe está de recuperação com média {}'.format(media))
else:
    print('O aluno está reprovado com média {}'.format(media))