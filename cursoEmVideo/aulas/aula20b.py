def contador(* num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM')


def novas(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')

contador(2, 1, 7)
contador(8, 0)

novas(1, 2, 3)
novas(5, 2, 7, 8)