'''
Use compreensão em listas para criar uma lista das primeiras letras
de cada palavra na string abaixo:
'''

st = 'Create a list of the first letters of every word in this string'
split_st = st.split()
[letter[0] for letter in split_st]