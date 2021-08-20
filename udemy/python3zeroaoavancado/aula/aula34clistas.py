x = []
for i in range(0, 3):
    x += [i]

print (x)

x2 = [i for i in range(0, 10)]

print(x2)

x3 = []
for i in range(0, 20):
    if i % 2 == 0:
        x3 += [i]
print(x3)

x4 = [i for i in range(0, 20) if i % 2 == 0]
print(x4)

lista = []
lista = [letras for letras in 'word']
print(lista)

#conversão de temperaturas
celsius = [0, 10, 15, 20, 30, 50, 100]
faren = [(temp * (9/5) + 32) for temp in celsius]
print(faren)