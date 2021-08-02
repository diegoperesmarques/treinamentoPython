'''
faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo 
usuário. O programa será interrompido quando o número
solicitado for negativo.
'''
numeroTabuada = int(input('Quer tabuada de qual valor? '))
while True:
    if numeroTabuada < 0:
        break
    contadorTabuada = 0
    while contadorTabuada < 11:
        print(f'{contadorTabuada} x {numeroTabuada} = {contadorTabuada*numeroTabuada}')
        contadorTabuada += 1 
    numeroTabuada = int(input('Quer tabuada de qual valor? '))
print('PROGRAMA TABUADA ENCERRADO. Volte sempre')