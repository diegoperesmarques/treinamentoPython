'''
Crie um programa que leia noem, sexo e idade de várias pessoas, guardando
os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre: 
a) Quantas pessoas foram cadastradas 
b) A média de idade do grupo;
c) Uma lista com todas as mulhres;
d) Uma lista com todas as pessoas com idade acima da média;
'''
info = dict()
completo = list()
quantidadePessoas = 0
somaIdades = 0
mediaIdades = 0

while True:
    info['nome'] = str(input('Nome: ')).strip().upper()
    info['sexo'] = str(input('Sexo: ')).strip().upper()
    info['idade'] = int(input('Idade: '))
    completo.append(info.copy())
    quantidadePessoas += 1
    condicaoSaida = ' '
    while condicaoSaida not in 'SsNn':
        condicaoSaida = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if condicaoSaida == 'N':
        break


print('')
print(f'O grupo tem {quantidadePessoas} pessoas')

for i in range(0, len(completo)):
    somaIdades = somaIdades + completo[i]["idade"]

mediaIdades = somaIdades / quantidadePessoas
print(f'A média de idade é de {mediaIdades:.2f} anos')

print('As mulheres cadastradas foram: ', end='')
for i in range(0, len(completo)):
    if completo[i]['sexo'] == 'F':
        print(f'{completo[i]["nome"]} ', end='')
print('')

print('Lista das pessoas que estão acima da média')
for i in range(0, len(completo)):
    if completo[i]['idade'] > mediaIdades:
        print(f'nome = {completo[i]["nome"]}, sexo = {completo[i]["sexo"]};')

print('')

