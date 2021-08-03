'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
em uma tupla. No final, mostre:
a) Quantas vezes apareceu o valor 9;
b) Em que posição foi digitado o primeiro valor 3;
c) Quais foram os números pares;
'''
numero1 = int(input('Digiteo primeiro número: '))
numero2 = int(input('Digite segundo número: '))
numero3 = int(input('Digite terceiro número: '))
numero4 = int(input('Digite quarto número: '))
numero5 = int(input('Digite quinto número: '))
tuplaCompleta = (numero1, numero2, numero3, numero4, numero5)
print('')
print('-'*30)
print('Você digitou os valores: ', end='')
for contador in range(0, len(tuplaCompleta)):
    print(f'{tuplaCompleta[contador]} ',end='')
print('')
print(f'O valor 9 apareceu {tuplaCompleta.count(9)} vezes')
print(f'O valor 3 aparece na {tuplaCompleta.index(3)+1}ª posição')
print('Os valores pares digitados foram: ', end='')
for contador in range(0, len(tuplaCompleta)):
    if tuplaCompleta[contador] % 2 == 0:
        print(f' {tuplaCompleta[contador]} ', end='')
print('')