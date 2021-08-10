print('-=' * 20)
print(f'{"INICIO DO SISTEMA":^30}')
print('-=' * 20)



while True:
    print('')
    print('1 - Cadastrar')
    print('2 - Listar')
    print('3 - Sair')
    condicao = int(input('Escolha uma opção: '))

    #Novo cadastro
    if condicao == 1:
        print('')
        print('-' * 20)
        print(f'{"NOVO CADASTRO":^20}')
        print('-' * 20)
        nomeDigitado = str(input('Digite outro nome: ')).strip().upper()
        idadeDigitado = input('Digite a idade: ')
        with open('cadastroPessoas.txt','a', encoding='utf-8') as proximosCadastros:
            proximosCadastros.write('\n')
            proximosCadastros.write(nomeDigitado)
            proximosCadastros.write(',')
            proximosCadastros.write(idadeDigitado)
        print('-' * 20)
        print(f'{"CADASTRO REALIZADO COM SUCESSO":>20}')
        print('-' * 20)

    #Listar cadastros
    if condicao == 2:
        with open('cadastroPessoas.txt','r', encoding='utf-8') as cadastroPessoas:
            listagemPessoas = cadastroPessoas.readlines()
        for listagem in listagemPessoas:
            if " " not in listagem:
                print(listagem)

    if condicao == 3:
        break




'''


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
'''