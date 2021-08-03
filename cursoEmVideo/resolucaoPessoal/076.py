'''
Crie um program que tenha um tupla única com nomes de produtos e seus
respectivos preços, na sequência
No final, mostre uma listagem de preços, organizando os dados em forma 
tabular
'''
produtos = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.9, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
print('-'*30)
print('Listagem de produtos: ')
print('-'*30)
for contador in range(0, len(produtos)):
    if contador % 2 == 0:
        print('{:.<20}R$ {:>4.2f}'.format(produtos[contador], produtos[contador+1]))
