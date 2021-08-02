numero = 1
while numero < 10:
    print('O valor de x e: {}'.format(numero))
    numero += 1


x = 1
y = 1
while x < 10 and y < 20:
    print('O valor de x * y é: {}'.format(x*y))
    x += 1
    y += 2
else:
    print('O valor de x*y é: {}'.format(x*y))

x = 1
lista = []
while True:
    lista += [x]
    x += 1
    if x > 10:
        break

print(lista)