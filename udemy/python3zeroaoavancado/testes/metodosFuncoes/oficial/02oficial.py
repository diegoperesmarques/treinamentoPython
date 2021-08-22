'''
Escreva uma função que verifica se um número está em um 
determinado intervalo (inclusive o máximo e o mínimo)
'''
def ran_check(num, low, high):
    if num in list(range(low, high+1)):
        return True
    else:
        return False