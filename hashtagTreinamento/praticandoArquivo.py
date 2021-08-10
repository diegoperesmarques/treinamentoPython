print('-=' * 20)
print(f'{"INICIO DO SISTEMA":^30}')
print('-=' * 20)

nomeDigitado = str(input('Digite o seu nome: ')).strip().upper()
idadeDigitado = input('Digite sua idade: ')

with open('cadastro.txt','w', encoding='utf-8') as cadastroInicial:
    cadastroInicial.write(nomeDigitado)
    cadastroInicial.write(',')
    cadastroInicial.write(idadeDigitado)

print('-' * 20)
print(f'{"CADASTRO REALIZADO COM SUCESSO":>20}')
print('-' * 20)
while True:
    print('')
    condicao = ' '
    while condicao not in 'SsNn':
        condicao = str(input('Quer continuar? ')).strip().upper()[0]

    if condicao in 'Nn':
        break

    print('')
    print('-' * 20)
    print(f'{"NOVO CADASTRO":^20}')
    print('-' * 20)
    nomeDigitado = str(input('Digite outro nome: ')).strip().upper()
    idadeDigitado = input('Digite a idade: ')
    with open('cadastro.txt','a', encoding='utf-8') as proximosCadastros:
        proximosCadastros.write('\n')
        proximosCadastros.write(nomeDigitado)
        proximosCadastros.write(',')
        proximosCadastros.write(idadeDigitado)

print('-=' * 20)
print(f'{"SISTEMA FINALIZADO":>20}')
print('-=' * 20)
