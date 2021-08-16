'''
Faça um programa que tenha um fuhção chamada escreva(), que receva
um texto qualquer como parâmetro e mostre uma mensagem com 
tamanho adaptável.
'''
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f' {msg}')
    print('~' * tam)


#Program principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')