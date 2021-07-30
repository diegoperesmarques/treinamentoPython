'''
reçaa o desafio 009, mostrando a tabuada de um 
número que o usuário escolher, só que agora
utilizando o laço for.
'''

numero = int(input('Digite um número: '))

for i in range(1, 11):
    print('{} x {:2} = {}'.format(numero, i, numero*i))