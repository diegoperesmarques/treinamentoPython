'''
Percorra a string abaixo e se o comprimento de uma palavra for 
par imprima 'é par!"
'''
st = 'Print every word in this sentence that has an even number of letters'
palavrasLista = st.split()
for palavra in palavrasLista:
    if len(palavra) % 2 == 0:
        print(f'{palavra} - é par')
