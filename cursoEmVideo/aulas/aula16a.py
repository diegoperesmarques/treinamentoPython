lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[-2])
print(lanche[1:3])
print(lanche[:2])
print(lanche[-3:])

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

print(len(lanche))

for cont in range(0, len(lanche)):
    print(lanche[cont])

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate (lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print(sorted(lanche))