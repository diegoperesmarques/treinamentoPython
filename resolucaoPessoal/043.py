'''
desenvolva uma lógica que leia o peso e altura de uma 
pessoa, calcule seu IMC e mostre sue status, de acordo
com a tabela abaixo:

Abaixo de 18.5: Abaixo do peso
Entre 18.5 e 25: Peso ideal
25 até 30: Sobrepeso
30 até 40: Obesidade 
Acima de 40: Obesidade mórbida
'''
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura**2)

if imc > 40:
    print('Obsidade mórbida IMC {}'.format(imc))
elif imc >= 30:
    print('Obesidade IMC {}'.format(imc))
elif imc >= 25:
    print('Sobrepeso IMC {}'.format(imc))
elif imc >= 18.5:
    print('Peso ideal')
else:
    print('Abaixo do peso')