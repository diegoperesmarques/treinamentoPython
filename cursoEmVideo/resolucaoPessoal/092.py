'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho 
e cadastre-os (com idade) em um dicionário se por acaso o CTPS for diferente de
ZERO, o dicionário receberá também o ano de contração e o salário. Calcule e
acrescente, além da idade, com quantos anos a pessoa vai se aposentar
Para se aposentar são 35 anos de colaboração
{nome, idade, ctps, contracacao, salario, aposentadoria}
'''
infoUsuario = dict()
nomeDigitado = str(input('Nome: ')).strip()
anoNascimento = int(input('Ano de Nascimento: '))
idade = 2021 - anoNascimento
codCardeira = int(input('Carteira de Trabalho (0 não tem): '))

if codCardeira == 0:
    infoUsuario = {'nome':nomeDigitado, 'idade':idade, 'ctps':0}
    for info, valor in infoUsuario.items():
        print(f'{info} tem o valor {valor}')
else:
    anoContratacao = int(input('Ano de contratação: '))
    salario = int(input('Salário: R$ '))

    anosParaAposentadoria = 35 - (2021 - anoContratacao)
    aposentadoria = idade + anosParaAposentadoria

    
    infoUsuario = {'nome':nomeDigitado, 'idade':idade, 'ctps':codCardeira, 'contratacao':anoContratacao, 'salario':salario, 'aposentadoria':aposentadoria}
    for informacao, valor in infoUsuario.items():
        print(f'{informacao} tem o valor {valor}')