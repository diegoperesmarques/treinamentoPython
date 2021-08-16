'''
Faça um programa que tenha um função chamada área(), que receba as 
dimensões de um terreno retangular (largura e comprimento) e 
mostre a área do terreno
'''
def area(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {largura*comprimento}m')

def linha():
    print('=' * 30)

print('Controle de Terrenos')
linha()
larguraDigitada = float(input('LARGURA (m): '))
comprimentoDigitado = float(input('COMPRIMENTO (m): '))
area(larguraDigitada, comprimentoDigitado)