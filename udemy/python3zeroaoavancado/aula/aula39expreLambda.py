#def square(num): return num ** 2
#print(square(2))

square = lambda num: num ** 2
print(square(2))

par = lambda x: x % 2 == 0
print(par(3))

primeirochar = lambda s: s[0]
print(primeirochar('Olá, mundo'))


inverter_string = lambda s: s[::-1]
print(inverter_string('Olá, mundo'))