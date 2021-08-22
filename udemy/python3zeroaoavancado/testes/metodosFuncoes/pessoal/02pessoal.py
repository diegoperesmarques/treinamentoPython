'''
Escreva uma função que verifica se um número está em um determinado
intervalo (inclusive o máximo e o mínimo)
'''
def verificaIntervalo(numero, minimo, maximo):
    if (numero >= minimo) and (numero <= maximo):
        print('True')
    else:
        print('False')


verificaIntervalo(15,1, 10)