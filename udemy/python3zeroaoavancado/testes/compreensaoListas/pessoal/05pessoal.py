'''
Escreva um programa que imprima os números inteiros de 1 a 100. Para
múltiplos de três imprima 'Fizz" ao invés do números, e para os 
múltiplos de cinco imprima "Buzz". Para números que são múltiplas
de três e cinco impressões "FizzBuzz";
'''
for i in range(1, 101):
    if i % 3 == 0:
        print(f'{i} - Fizz')
    if i % 5 == 0:
        print(f'{i} - Buzz')
    if (i % 3 == 0) and (i % 5 == 0):
        print(f'{i} - FizzBuzz')