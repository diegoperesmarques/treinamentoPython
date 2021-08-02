'''
crie um programa que leia várias números inteiros pelo teclado. O 
programa só vai parar quando o usuário digitar o valor 999, que é a
condição de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre eles (desconsidernado o flag).
'''
soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += 1
print(f'A soma dos valores foi {soma}!')