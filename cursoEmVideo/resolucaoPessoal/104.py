'''
Crie um programa que tenha a função leiaInt(), que vai funcionar de 
forma semelhante à função input() do Python, só que fazendo a validação
para aceitar apenas um valor numérico.
'''
def leiaInt(textoRecebido):
    while True:
        numero = input(textoRecebido)
        if numero.isnumeric():
            break
        else:
            print('ERRO! Digite um número válido!')
    return numero

#Programa principal
numero = leiaInt('Digite um número: ')
print(f'O número digitado foi {numero}')