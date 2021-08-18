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
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)

    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUIM'
    return r


#Programa Principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)