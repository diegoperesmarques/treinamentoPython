'''
Dentro do pacoete utilidadesCeV que criamos no desafio 111, temos
um módulo chamado dado. Crie uma função chamada leiaDinheiro() que
seja capaz de funcionar como a funão input(), mas com uma validação
de dados para aceitar apenas valores que sejam monetários.
'''
from utilidadesCeV import moeda
from utilidadesCeV import dado

p = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(p, 25, 7)