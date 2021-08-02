'''
arquivo = open('novo.txt')
print(arquivo.read())
arquivo.seek(0)
print(arquivo.read())
'''

arquivo = open('novo.txt','w+')
arquivo.write('Este é um novo texto')
print(arquivo.read())
