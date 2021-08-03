num = [2, 5, 9, 1]
num[2] = 3
print(num)
num.append(7)
print(num)
num.sort(reverse=True)
print(num)
print(f'Esta lista tem {len(num)} elementos.')
num.insert(2, 0)
print(num)
num.pop()
print(num)
num.remove(2)
print(num)

if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5')