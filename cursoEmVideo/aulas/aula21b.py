def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: iniício da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM')


help(contador)
#contador(2, 10, 2)