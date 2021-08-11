'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde essees resultados em um dicionários. No final, coloque esse dicionário
em ordem, sabendo que o vencedor tirou o maior número no dado.
'''
from random import randint
from time import sleep
jogadores = dict()
for i in range(1, 5):
    jogadores[f'jogador{i}'] = randint(1,10)

for jogador, valor in jogadores.items():
    print(f'O {jogador} tirou {valor}')
    sleep(1)

print('Ranking dos jogadores: ')