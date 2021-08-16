'''
Faça um programa que tenha um função chamada contador(), que receba
três parâmetro: início, fim e passo e realize a contagem.
Seu programa tem que realizar três contagens através da função
criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 1
c) uma contagem personalizada
'''

#funções
def linha():
    print('-=' * 40)

def contagem(inicio, fim, passo):
    if passo == 0 and fim < inicio:
        for i in range(inicio, fim, -1):
            print(f'{i} ', end='')
        print('FIM!')
    elif passo == 0 and inicio > fim:
        for i in range(inicio, fim):
            print(f'{i} ', end='')
        print('FIM!')
    elif fim < inicio and passo > 0:
        passo = passo * -1
        for i in range(inicio, fim+1, passo):
            print(f'{i} ', end='')
        print('FIM!')
    else:
        for i in range(inicio, fim+1, passo):
            print(f'{i} ', end='')
        print('FIM!')

linha()
print('Contagem de 1 até 10 de 1 em 1 ')
for i in range(1, 11):
    print(f'{i} ', end= '')
print('FIM!')

linha()
print('Contagem de 10 até 0 de 2 em 2')
for i in range(10, 0, -2):
    print(f'{i} ', end='')
print('FIM!')

linha()

print('Agora é a sua vez de personalizar a contagem! ')
inicioDigitado = int(input('Início: '))
fimDigitado = int(input('Fim: '))
passoDigitado = int(input('Passo: '))

linha()

print(f'Contagem de {inicioDigitado} até {fimDigitado} de {passoDigitado} em {passoDigitado}')
contagem(inicioDigitado, fimDigitado, passoDigitado)

