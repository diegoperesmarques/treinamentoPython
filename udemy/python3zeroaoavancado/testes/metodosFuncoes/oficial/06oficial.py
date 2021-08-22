'''
Escreva uma função Python que verifica se uma string passada é
palindrome ou não.
'''
def palindrome(s):
    s = s.replace(' ', '')
    return s == s[::-1]


palindrome('helloh')