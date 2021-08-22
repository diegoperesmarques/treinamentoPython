'''
Use for, split() e if para criar uma declaração que imprima as palavras que começam 
com 's':
st = 'Print only the words that start with s this sentence
'''
st = 'Print only the words that start with s this sentence'
nova = st.split()
for palavras in nova:
    if palavras[0] == 's':
        print(palavras)
