'''
Crie um programa que tenha um função chamada voto() que vai receber como parâmetro o ano
de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto
NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
'''
def voto(idade):
    """
    -> Função utilizada para calcular se a pessoa tem idade para votar
    :param idade: Idade da pessoa
    """
    if idade >= 18:
        return 'OBRIGATÓRIO'
    elif idade >= 16:
        return 'OPCIONAL'
    else:
        return 'NEGADO'


anoDigitado = int(input('Em que ano você nasceu? '))
idade = 2021 - anoDigitado
print(f'Com {idade} anos: VOTO {voto(idade)}')