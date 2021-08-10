'''
with open('email.txt', 'r') as arquivo:
    email = arquivo.read()
print(email)
'''

#para arquivo com mais de uma linha
with open('mensagem.txt', 'r', encoding='utf-8') as arquivo:
    mensagem = arquivo.readlines()

for linhas in mensagem:
    if 'faturamento' in linhas:
        print(linhas)