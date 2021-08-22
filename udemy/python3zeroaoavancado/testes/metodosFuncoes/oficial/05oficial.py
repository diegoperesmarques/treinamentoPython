'''
Escreva uma fuçnão Python para multiplicar todos os números em
uma lista
'''
def multiply(numbers):
    total = 1
    for i in numbers:
        total *= i
    return total


multiply([1, 2, 3, -4])