'''
faça um progrma que calcule a soma entre todos
os números ímpares que são múltiplos de três
e que se encontram no intervalo de 1 até 500.
'''
resultado = 0
for i in range(1, 50):
    if i % 2 != 0:
        if i % 3 == 0:
            resultado = resultado + i
            print(i, end=' ')

print('\nO resultado é : {}'.format(resultado))