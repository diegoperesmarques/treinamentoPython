'''
crie um programa que leia a idade e o sexo de várias
pessoas. A cada pessoa cadastrada, o programa 
deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
a) Quantas pessoas tem mais de 18 anos.
b) Quantos homens foram cadastrados.
c) Quantas mulheres tem menos de 20 anos
'''
contadorPessoas18 = 0
contadorHomens = 0
contadorMulheresMenos20 = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo: [M/F]')).upper().strip()
    sair = str(input('Deseja sair? [S/N] ')).upper().strip()

    if idade > 18:
        contadorPessoas18 += 1
    if sexo == 'M':
        contadorHomens += 1
    if idade < 20 and sexo == 'F':
        contadorMulheresMenos20 += 1
    if sair == 'S':
        break

print('-'*30)
print('Fim do programa')
print('-'*30)
print(f'{contadorPessoas18} pessoas com mais de 18 anos.')
print(f'{contadorHomens} homens foram cadastrados')
print(f'{contadorMulheresMenos20} mulheres com menos de 18 anos')