def aumentar(num, porcentagem):
    resultado = ((num / 100) * porcentagem) + num
    return resultado


def diminuir(num, porcentagem):
    resultado = num - ((num / 100) * porcentagem)
    return resultado 


def dobro(num):
    resultado = num * 2
    return resultado


def metade(num):
    resultado = num / 2
    return resultado