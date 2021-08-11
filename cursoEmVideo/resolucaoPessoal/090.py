'''
Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário. No final,
mostre o conteúdo da estrutura na tela.
'''
nomeAluno = str(input('Nome: '))
mediaAluno = float(input(f'Média de {nomeAluno}: '))
situacaoAluno = ''
if mediaAluno >= 7:
    situacaoAluno = 'Aprovado'
elif mediaAluno >= 5:
    situacaoAluno = 'Recuperação'
else:
    situacaoAluno = 'Reprovado'

infoAluno = {'nome':nomeAluno, 'media':mediaAluno, 'situacao':situacaoAluno}

print(f'Nome é igual a {infoAluno["nome"]}')
print(f'Média é igual a {infoAluno["media"]}')
print(f'Situação é igual a {infoAluno["situacao"]}')

