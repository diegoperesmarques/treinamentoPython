'''
Melhore o jogo do Desafio 028 opnde o computador vai 
"pensar" em um número entre 0 e 10. Só qeu agora o 
jogador vai tentar adivinhar até acertar, mostrando no final
quantos palpites foram necessários para vencer.
'''
from random import randint
computador = randint(0, 10)
print('Sou seu computador ... Acabei de pensar em um número entre 0 e 10')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais ...')
        elif jogador > computador: 
            print('Menos ...')
print('Acertou com {} palpites!'.format(palpites))