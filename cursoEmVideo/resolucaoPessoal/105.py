'''
Faça um programa que tenha uma função notas() que pode receber várias notas
de alunos e vai retornar um dicionários com as seguintes ifnormações:
-Quantidade de notas
-A maior notas
-A menor nota 
-A média da turma
-A a situação (opcional)
Adicione também as docstrings da função
'''
def notas(* n, sit=False):
    """
    ->Função para analisar notas e situaçẽos de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    maior = media = soma = situacao = 0
    menor = n[0]
    for i in n:
        soma = soma + i
        if maior < i:
            maior = i
        if menor > i:
            menor = i
    media = soma / len(n)
    if media >= 7:
        situacao = 'BOA'
    elif media >= 5:
        situacao  = 'REGULAR'
    else:
        situacao = 'RUIM'
    
    if sit:
        return {'maior': maior, 'menor': menor, 'media': media, 'situacao': situacao}
    else:
        return {'maior': maior, 'menor': menor, 'media': media}


#Programa principal
print(notas(2, 15, 35, 1, sit=True))
