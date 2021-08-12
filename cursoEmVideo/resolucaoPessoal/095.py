'''
Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo
um sistema de visualização de detalhes do aproveitamenteo de cada jogador.
'''
quantidadeGols = list()
informacoes = dict()
completo = list()

while True:
    print('')
    print('-' * 30)
    nomeJogador = str(input('Nome do Jogador: ')).strip().upper()
    quantidadePartida = int(input(f'Quans partidas {nomeJogador} jogou? '))
    for i in range(0, quantidadePartida):
        quantidadeGols.append(int(input(f'Quantos gols na partida {i+1}? ')))

    informacoes['nome'] = nomeJogador
    informacoes['gols'] = quantidadeGols
    informacoes['partidas'] = quantidadePartida
    completo.append(informacoes.copy())
    
    condicaoSaida = ' '
    while condicaoSaida not in 'SsNn':
        condicaoSaida = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if condicaoSaida == 'N':
        break


print('')
print('-=' * 30)
print(f'{"cod":^3}{" nome":<10}{"gols":15}{"total":^4}')
print('-' * 30)
for i in range(0, len(completo)):
    print(f'{i:>3} {completo[i]["nome"]:<10}', end='')
    print(f"{completo[i]['gols']}   ", end='')
    print(f'{completo[i]["partidas"]:<4}')

