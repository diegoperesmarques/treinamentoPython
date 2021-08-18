'''
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro
que indique o número a calcular e o outro chamado show, que será um valor lógico 
(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
'''
def fatorial(numero, show=False):
    """
    -> Função para calcular o fatorial de um número digitado
    :param numero: É o número que será calculado o fatorial
    :param show: (optional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    resultado = 1

    if show == True:
        for i in range(numero, 0, -1):
            print(f' {i} x', end='')
        print(' = ', end='')

        for i in range(numero, 0, -1):
            resultado *= i

        print(resultado)
    else:
        for i in range(numero, 0, -1):
            resultado *= i
        print(resultado)

#Programa principal
fatorial(5)
