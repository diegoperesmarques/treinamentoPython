numero = int(input('Digite o número desejado: '))

multiplicador = 1
while multiplicador < 11:
    print('{} x {} = {}'.format(numero, multiplicador, numero*multiplicador))
    multiplicador += 1


