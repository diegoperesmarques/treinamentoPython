'''
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do 
Campeonato Brasileiro de Futebol, na ordem de colocação, Depois
mostre:
a) Apenas os 5 primeiros colocados;
b) Os últimos 4 colocados da tabela;
c) Uma lista com os times em ordem alfabética;
d) Em que posição na tablea está o time da Chapecoense
'''
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta')

print('-'*30)
print('Os cinco primeiros times da tabela')
print(times[:5])
print('-'*30)
print('Os quatro (04) últimos colocados são: ')
print(times[-4:])
print('-'*30)
print('Lista em Ordem Alfabética')
print(sorted(times))
print('-'*30)
print(f"O Chapecoense está na posição {times.index('Chapecoense')+1}")