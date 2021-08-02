'''
crie um programa que leia o nome e o preço de vários
produtos. O programa deverá perguntar se o usuário vai
continuar. No final, mostre:
a) qual é o total gasto na compra.
b) quantos produtos custam mais de R$ 1000.
c) Qual é o nome do produto mais barato.
'''
print('-'*30)
print('Sistema de compras')
print('-'*30)

sair = 'N'
totalGasto = contadorProdutosMais1000 = precoProdutoMaisBarato = contadorPrograma = 0
nomeProdutoMaisBarato = ''

while True:
    nomeProduto = str(input('Digite o nome do produto: ')).upper().strip()
    precoProduto = int(input('Digite o preço do produto: '))
    totalGasto = totalGasto + precoProduto
    sair = str(input('Digite sair do programa? [S/N] ')).upper().strip()
    contadorPrograma += 1

    if contadorPrograma == 1:
        nomeProdutoMaisBarato = nomeProduto
        precoProdutoMaisBarato = precoProduto
    if precoProdutoMaisBarato > precoProduto:
        nomeProdutoMaisBarato = nomeProduto
        precoProdutoMaisBarato = precoProduto

    if precoProduto > 1000:
        contadorProdutosMais1000 += 1

    if sair in 'S':
        break

print('-'*30)
print(f'O total gasto foi R$ {totalGasto}')
print(f'{contadorProdutosMais1000} custam mais de R$ 1000')
print(f'{nomeProdutoMaisBarato} é o produto mais barato com valor de {precoProdutoMaisBarato}')