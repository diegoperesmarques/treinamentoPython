'''
Crie um programa que tenha uma tupla com várias palavras
(não user acentos). Depois disso, você deve mostrar,
para cada palavra, quais são as suas vogais
'''

palavras = ('aprender', 'programas','linguagem','python',
            'curso','gratis','estudar','praticar','trabalhar',
            'mercado','programador','futuro')

for p in palavras:
    print(f'\n Na palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end= ' ')
