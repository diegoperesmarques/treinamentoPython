programas = {'design':'gimp', 'animacao':'enve'}
#print('Os programas de design são {}'.format(programas['design']))

tipos = {'primeiro':15, 'segundo':['primeiro', 'segundo'], 'ter':'novo'}
#print('Tipos: {}'.format(tipos['segundo'][0]))

dicionario = {}
dicionario['primeiro'] = 10
dicionario['primeiro'] = 15
dicionario['segundo'] = 'novo'
dicionario['segundo'] = 'acao'
print(dicionario)

alinhado = {'primeiro':{'n1':1, 'n2':2}, 'segundo':{'n3':3, 'n4':4}}
print(alinhado['primeiro']['n2'])
print(dicionario.keys())
print(dicionario.values())
print(dicionario.items())