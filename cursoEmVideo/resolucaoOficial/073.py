'''
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do 
Campeonato Brasileiro de Futebol, na ordem de colocação, Depois
mostre:
a) Apenas os 5 primeiros colocados;
b) Os últimos 4 colocados da tabela;
c) Uma lista com os times em ordem alfabética;
d) Em que posição na tablea está o time da Chapecoense
'''
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 
        'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 
        'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 
        'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 
        'Ponte Preta')

print('-=' * 30)
print(f'Lista de times: {times}')
print('-=' * 30)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 30)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 30)
print(f'Times com ordem alfebética: {sorted(times)}')
print('-=' * 30)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')