'''
Faça um programa que tenha um afunção chamada ficha(), que receba 
dois parâmetros opcionais: O nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogaodr, mesmo 
que algum dado não tenha sido informado corretamente.
'''
def ficha(jogador=0, gols=0):
    if jogador == 0:
        jogadorExibicao = '<desconhecido>'
    else:
        jogadorExibicao = jogador
    
    print(f'O jogador {jogadorExibicao} fez {gols} gol(s) no campeonato.')


#Programa principal
nomeJogador = input('Nome do jogaodr: ')
numeroGols = input('Número de Gols: ')
ficha(nomeJogador, numeroGols)