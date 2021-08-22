'''
Escreva uma função Python para verificar se uma string é um
pangrama ou não
'''
import string


def ispangram(str1, alphabet=string.ascii_lowercase):
    num = len(alphabet)
    count = 0

    for i in alphabet:
        if i in str1:
            count+=1
    
    return count == num