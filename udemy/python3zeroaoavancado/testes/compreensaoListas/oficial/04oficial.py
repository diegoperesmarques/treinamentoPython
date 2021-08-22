'''
Percorra a string abaixo e se o comprimento de uma palavra for 
par imprima 'é par!"
'''
st = 'Print every word in this sentence that has an even number of letters'
split_string = st.split()
for i in split_string:
    for i in split_string:
        size = len(i)
        if size % 2 == 0:
            print(i, ': possui comprimento par!')