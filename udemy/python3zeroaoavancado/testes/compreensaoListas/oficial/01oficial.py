'''
Use for, split() e if para criar uma declaração que imprima as palavras que começam 
com 's':
st = 'Print only the words that start with s this sentence
'''
st = 'Print only the words that start with s this sentence'
split_string = st.split()
for letra in split_string:
    if letra[0] == 's':
        print(letra)

