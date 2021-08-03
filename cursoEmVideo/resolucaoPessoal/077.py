'''
Crie um programa que tenha uma tupla com várias palavras
(não user acentos). Depois disso, você deve mostrar,
para cada palavra, quais são as suas vogais
'''
palavras = ('aprender', 'programas','linguagem','python','curso','gratis','estudar','praticar','trabalhar','mercado','programador','futuro')

for contador in range(0, len(palavras)):
    print(f'A palavra {palavras[contador]} tem as vogais: ', end='')
    for i in range(0, len(palavras[contador])):
        if palavras[contador][i] in 'aeiou':
            print(f' {palavras[contador][i]} ', end='')
    print('')
'''
palavra2 = 'aprender'
for i in range(0, len(palavra2)):
    if palavra2[i] in 'aeiou':
        print(palavra2[i])
'''