def primo(num):
    """
    Método para checar se é primo
    """
    def divisivel(a, b):
        return a % b
    
    for n in range(2, num):
        if divisivel(num, n) == 0:
            print('Não é primo')
            break
    else:
        print('Primo')


primo(117)