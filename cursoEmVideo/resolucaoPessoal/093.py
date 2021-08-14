'''
Crie um programa que gerencie o aproveitamenteo de um jogador de futebol. O 
programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a
quantidade de gols feitos em cada partida. No final, tudo isso será guardado em 
um dicionário, incluindo o total de gols feitos durante o campeonato.
'''
quantidadeGols = list()
infoJogador = dict()
somaGols = 0
nome = str(input('Nome do Jogador: ')).strip()
numeroPartidas = int(input(f'Quantas partidas {nome} jogou? '))

for i in range(0, numeroPartidas):
    quantidadeGols.append(int(input(f'Quantos gols na partida {i+1}? ')))
    somaGols = somaGols + quantidadeGols[i]


infoJogador = {'nome': nome, 'gols':quantidadeGols, 'total':somaGols}
print('-=' * 30)
print(infoJogador)
print('-=' * 30)
print('')

for chave, valor in infoJogador.items():
    print(f'O campo {chave} tem valor {valor}')

print('')
print('-=' * 30)

print(f'O jogador {nome} jogou {numeroPartidas}')
for posicao, valor in enumerate (quantidadeGols):
    print(f'Na partida {posicao}, fez {valor} gols')


print(f'Foi um total de {somaGols} gols')


print('')
    
