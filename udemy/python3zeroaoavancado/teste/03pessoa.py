'''
Use a compreensão de lista para criar uma lista de todos os números
entre 1 e 50 que são divisíveis por 3.
'''
lista = [i for i in range(1, 51) if i % 3 == 0]
print(lista)