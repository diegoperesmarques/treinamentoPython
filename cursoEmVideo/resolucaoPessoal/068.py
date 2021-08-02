'''
faça um program que jogue par ou impar com o computador
o jogo só será interrompido quando o jogador PERDER,
mostrando o total de vitórias consecutivas que ele
conquistou no final do jogo
'''
from random import randint
vitoriaUsuario = 0
numeroEParouImpart = 0
while True:
    numeroComputador = randint(0, 10)
    numeroDigitado = int(input('Digite um valor: '))
    opcaoEscolhida = str(input('Par ou Impar? [P/I] ')).upper().strip()
    somaNumeros = numeroDigitado + numeroComputador
    if somaNumeros % 2 == 0 and opcaoEscolhida == 'P':
        vitoriaUsuario +=1 
    elif somaNumeros % 2 != 0 and opcaoEscolhida == 'I':
        vitoriaUsuario +=1
    else:
        break

if somaNumeros % 2 == 0:
    numeroEParouImpart = 'DEU PAR'
else: 
    numeroEParouImpart = 'DEU IMPAR'

print(f'Você jogou {numeroDigitado} e o computador {numeroComputador}. Total de {somaNumeros} DEU PAR')
print('Você PERDEU! ')
print(f'GAME OVER ! Você venceu {vitoriaUsuario} vezes.')