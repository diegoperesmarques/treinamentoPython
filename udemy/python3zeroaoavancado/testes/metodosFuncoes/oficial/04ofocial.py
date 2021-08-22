'''
Escreva uma função Python que recebe uma lista e retorna uma nova
lista com elementos exclusivos da primeira lista.

exemplo: [1,1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4,5, 5, 5]
unica: [1, 2, 3, 4, 5]
'''
def unique_list(l):
    return list(set(l))