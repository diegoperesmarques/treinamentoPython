'''
Escreva uma função que calcula o volume de uma esfera dado
o seu raio
'''
def volume(raio):
    volume = (4 * 3.14 * (raio**3))/3
    return volume

raioDigitado = int(input('Digite o raio: '))
print(f'O volume é {volume(raioDigitado)}')