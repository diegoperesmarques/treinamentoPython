'''
crie um programa que leia vários números inteiros pelo
teclaod. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada. No 
final, mostre quantos números foram digitados e qual
foi a soma entre eles (desconsiderando o flag)
'''
contadorRepeticao = somaNumerosDigitados = 0
while True:
    numeroDigitado = int(input('Digite um número [999 parar] '))
    if numeroDigitado == 999:
        break
    somaNumerosDigitados = somaNumerosDigitados + numeroDigitado
    contadorRepeticao += 1
print(f'{contadorRepeticao} contados e a soma é {somaNumerosDigitados}')