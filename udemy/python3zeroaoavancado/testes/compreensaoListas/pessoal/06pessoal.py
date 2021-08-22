'''
Use compreensão em listas para criar uma lista das primeiras letras
de cada palavra na string abaixo:
'''

st = 'Create a list of the first letters of every word in this string'
palavrasSeparadas = st.split()
listaPrimeirasLetras = list()
for i in palavrasSeparadas:
    listaPrimeirasLetras.append(i[0])
print(listaPrimeirasLetras)