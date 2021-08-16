'''
Faça um programa que tenha um fuhção chamada escreva(), que receva
um texto qualquer como parâmetro e mostre uma mensagem com 
tamanho adaptável.
'''
def escreva(texto):
    tamanhoTexto = len(texto)+4
    print('-' * tamanhoTexto)
    print(f'  {texto}  ')
    print('-' * tamanhoTexto)

textoDigitado = input('Digite alguma coisa: ')
escreva(textoDigitado)