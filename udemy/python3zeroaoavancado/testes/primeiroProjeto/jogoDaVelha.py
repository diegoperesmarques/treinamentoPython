'''
2 jogadores devem poder jogar o jogo (ambos sentados no mesmo computador)
O quadro deve ser impresso sempre que um jogador faz uma jogada
Você deve ser capaz de aceitar a entrada da posição do jogador e, em seguida, colocar um símbolo na placa
'''
#importações
import os

#variáveis
posicaoJogada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
jogo = [[' ',' ',' '], [' ', ' ', ' '], [' ', ' ', ' ']]

#funções
def linhas(texto):
    tamanho = len(texto) + 4
    print('')
    print('-' * tamanho)
    print(f'  {texto}')
    print('-' * tamanho)


def imprimiTabuleiroOriginal():
    print('')
    for indice, posicao in enumerate(posicaoJogada):
        for i in range(0, 3):
            print(f'| {posicaoJogada[indice][i]} |', end='')
        print('')
    print('')


def imprimirTabuleiroAtual():
    print('')
    for indice, posicao in enumerate(jogo):
        for i in range(0, 3):
            print(f'| {jogo[indice][i]} |', end='')
        print('')
    print('')


def jogadas(nomeJogador1, nomeJogador2, escolhaJogador1, escolhaJogador2):
    print('')
    decisaoJogador1 = decisaoJogador2 = posicaoDigitada = 0
    incrementoGeral = 0
    while incrementoGeral < 9:
        if incrementoGeral == 0:
            decisaoJogador1 = 1
            decisaoJogador2 = 0
            posicaoDigitada = int(input(f'{nomeJogador1} digite a posição: '))
            if posicaoDigitada == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                jogo[0][0] = escolhaJogador1
                imprimirTabuleiroAtual()
            elif posicaoDigitada == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                jogo[0][1] = escolhaJogador1
                imprimirTabuleiroAtual()
            elif posicaoDigitada == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                jogo[0][2] = escolhaJogador1
                imprimirTabuleiroAtual()
            elif posicaoDigitada == 4:
                os.system('cls' if os.name == 'nt' else 'clear')
                jogo[1][0] = escolhaJogador1
                imprimirTabuleiroAtual()
            elif posicaoDigitada == 5:
                os.system('cls' if os.name == 'nt' else 'clear')
                jogo[1][1] = escolhaJogador1
                imprimirTabuleiroAtual()
            elif posicaoDigitada == 6:
                os.system('cls' if os.name == 'nt' else 'clear')
                jogo[1][2] = escolhaJogador1
                imprimirTabuleiroAtual()
            elif posicaoDigitada == 7:
                os.system('cls' if os.name == 'nt' else 'clear')
                jogo[2][0] = escolhaJogador1
                imprimirTabuleiroAtual()
            elif posicaoDigitada == 8:
                os.system('cls' if os.name == 'nt' else 'clear')
                jogo[2][1] = escolhaJogador1
                imprimirTabuleiroAtual()
            elif posicaoDigitada == 9:
                os.system('cls' if os.name == 'nt' else 'clear')
                jogo[2][2] = escolhaJogador1
                imprimirTabuleiroAtual()

        else:
            if decisaoJogador1 == 1:
                decisaoJogador2 = 1
                decisaoJogador1 = 0
                posicaoDigitada = int(input(f'{nomeJogador2} digite a posição: '))
                if posicaoDigitada == 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    jogo[0][0] = escolhaJogador2
                    imprimirTabuleiroAtual()
                elif posicaoDigitada == 2:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    jogo[0][1] = escolhaJogador2
                    imprimirTabuleiroAtual()
                elif posicaoDigitada == 3:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    jogo[0][2] = escolhaJogador2
                    imprimirTabuleiroAtual()
                elif posicaoDigitada == 4:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    jogo[1][0] = escolhaJogador2
                    imprimirTabuleiroAtual()
                elif posicaoDigitada == 5:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    jogo[1][1] = escolhaJogador2
                    imprimirTabuleiroAtual()
                elif posicaoDigitada == 6:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    jogo[1][2] = escolhaJogador2
                    imprimirTabuleiroAtual()
                elif posicaoDigitada == 7:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    jogo[2][0] = escolhaJogador2
                    imprimirTabuleiroAtual()
                elif posicaoDigitada == 8:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    jogo[2][1] = escolhaJogador2
                    imprimirTabuleiroAtual()
                elif posicaoDigitada == 9:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    jogo[2][2] = escolhaJogador2
                    imprimirTabuleiroAtual()

            else:
                decisaoJogador2 = 0
                decisaoJogador1 = 1
                posicaoDigitada = int(input(f'{nomeJogador1} digite a posição: '))
                if posicaoDigitada == 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    jogo[0][0] = escolhaJogador1
                    imprimirTabuleiroAtual()
                elif posicaoDigitada == 2:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    jogo[0][1] = escolhaJogador1
                    imprimirTabuleiroAtual()
                elif posicaoDigitada == 3:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    jogo[0][2] = escolhaJogador1
                    imprimirTabuleiroAtual()
                elif posicaoDigitada == 4:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    jogo[1][0] = escolhaJogador1
                    imprimirTabuleiroAtual()
                elif posicaoDigitada == 5:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    jogo[1][1] = escolhaJogador1
                    imprimirTabuleiroAtual()
                elif posicaoDigitada == 6:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    jogo[1][2] = escolhaJogador1
                    imprimirTabuleiroAtual()
                elif posicaoDigitada == 7:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    jogo[2][0] = escolhaJogador1
                    imprimirTabuleiroAtual()
                elif posicaoDigitada == 8:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    jogo[2][1] = escolhaJogador1
                    imprimirTabuleiroAtual()
                elif posicaoDigitada == 9:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    jogo[2][2] = escolhaJogador1
                    imprimirTabuleiroAtual()

        incrementoGeral += 1
    print('')


def resultado(nomeJogador1, nomeJogador2, escolhaJogador1, escolhaJogador2):
    if (jogo[0][0] == jogo[0][1] == jogo[0][2] == escolhaJogador1):
        print(f'{nomeJogador1} venceu a partida!')
    elif (jogo[1][0] == jogo[1][1] == jogo[1][2] == escolhaJogador1):
        print(f'{nomeJogador1} venceu a partida!')
    elif (jogo[2][0] == jogo[2][1] == jogo[2][2] == escolhaJogador1):
        print(f'{nomeJogador1} venceu a partida!')
    elif (jogo[0][2] == jogo[1][2] == jogo[2][2] == escolhaJogador1):
        print(f'{nomeJogador1} venceu a partida!')
    elif (jogo[0][1] == jogo[1][1] == jogo[2][1] == escolhaJogador1):
        print(f'{nomeJogador1} venceu a partida!')
    elif (jogo[0][0] == jogo[1][0] == jogo[2][0] == escolhaJogador1):
        print(f'{nomeJogador1} venceu a partida!')
    elif (jogo[0][0] == jogo[1][1] == jogo[2][2] == escolhaJogador1):
        print(f'{nomeJogador1} venceu a partida!')
    elif (jogo[0][2] == jogo[1][1] == jogo[2][0] == escolhaJogador1):
        print(f'{nomeJogador1} venceu a partida!')

    elif (jogo[0][0] == jogo[0][1] == jogo[0][2] == escolhaJogador2):
        print(f'{nomeJogador2} venceu a partida!')
    elif (jogo[1][0] == jogo[1][1] == jogo[1][2] == escolhaJogador2):
        print(f'{nomeJogador2} venceu a partida!')
    elif (jogo[2][0] == jogo[2][1] == jogo[2][2] == escolhaJogador2):
        print(f'{nomeJogador2} venceu a partida!')
    elif (jogo[0][2] == jogo[1][2] == jogo[2][2] == escolhaJogador2):
        print(f'{nomeJogador2} venceu a partida!')
    elif (jogo[0][1] == jogo[1][1] == jogo[2][1] == escolhaJogador2):
        print(f'{nomeJogador2} venceu a partida!')
    elif (jogo[0][0] == jogo[1][0] == jogo[2][0] == escolhaJogador2):
        print(f'{nomeJogador2} venceu a partida!')
    elif (jogo[0][0] == jogo[1][1] == jogo[2][2] == escolhaJogador2):
        print(f'{nomeJogador2} venceu a partida!')
    elif (jogo[0][2] == jogo[1][1] == jogo[2][0] == escolhaJogador2):
        print(f'{nomeJogador2} venceu a partida!')
    else:
        print('Deu velha :(')        


#Início do Programa
linhas('JOGO DA VELHA')
nomeJogador1 = input('Jogador 1, digite seu nome: ').upper().strip()
nomeJogador2 = input('Jogador 2, digite seu nome: ').upper().strip()
escolhaJogador1 = input('Jogador1, escolha X ou 0: ').upper().strip()
escolhaJogador2 = ''
if escolhaJogador1 == 'X':
    escolhaJogador2 = '0'
else:
    escolhaJogador2 = 'X'

#limpar tela
os.system('cls' if os.name == 'nt' else 'clear')

linhas('INFORMAÇÕES')
print(f'O jogador 1 é: {nomeJogador1} e escolheu: {escolhaJogador1}')
print(f'O jogador 2 é:  {nomeJogador2} e ficou com {escolhaJogador2}')

linhas('COMEÇANDO O JOGO')
linhas('REGRAS')
print('Você deverá digitar a posição da sua jogada de acordo com os números abaixo')
print('')

imprimiTabuleiroOriginal()

linhas('JOGANDO')

jogadas(nomeJogador1, nomeJogador2, escolhaJogador1, escolhaJogador2)


linhas('RESULTADO')
resultado(nomeJogador1, nomeJogador2, escolhaJogador1, escolhaJogador2)