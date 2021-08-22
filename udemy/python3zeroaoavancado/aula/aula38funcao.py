def primeira_funcao():
    """
    printa 'Olá, mundo'
    """
    print('Olá, mundo!')


primeira_funcao()

def somar(num1, num2):
    print(num1-num2)


somar(1, 2)

def somar2(num1, num2):
    return num1 + num2


x = somar2(3, 4)

def primo(num):
    """
    Método para checar se é primo
    """
    for n in range(2, num):
        if num % n == 0:
            print('Não é primo')
            break
    else:
        print('Primo')


primo(10)