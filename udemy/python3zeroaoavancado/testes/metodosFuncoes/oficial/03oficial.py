'''
Escreva uma função Python que aceita uma string e calcule o número
de maiúscula e minúsculas
Exemplo: 'Olá Sr. Rogers, como você está bem, terça-feira?'
'''
def up_low(s):
    up = 0
    low = 0

    for i in s:
        if i.isupper():
            up += 1
        elif i.islower():
            low += 1
        else:
            continue
        
    print(f'Número de caracteres maiúsculos: {up}')
    print(f'Número de caracteres minúsculos: {low}')