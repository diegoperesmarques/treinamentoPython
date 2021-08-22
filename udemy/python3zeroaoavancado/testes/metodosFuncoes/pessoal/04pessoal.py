'''
Escreva uma função Python que receba uma lista e retorna uma nova lista
com elementos exclusivos da primeira lista.
lista de amostra: [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]
lista única: [1, 2, 3, 4, 5]
'''
def unicoLista(numeros):
    novaLista = [1]
    #for indice, valor in enumerate(novaLista):
       # print(f'{indice}, {valor}')
    for indicePrincipal, valorPrincipal in enumerate(numeros):
        #if indicePrincipal == 0:
         #   novaLista.append(valorPrincipal)
        #if indicePrincipal > 0:
            for indice, valor in enumerate(novaLista):
                if valorPrincipal != valor:
                    print(f'{valorPrincipal}, {valor}')
    print(novaLista)
    pass

unicoLista([1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5])
