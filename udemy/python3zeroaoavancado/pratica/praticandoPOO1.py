class Pessoa(object):
    def __init__(self, nome, idade, sexo):
        print(f'Nome: {nome}')
        print(f'Idade: {idade}')
        print(f'Sexo: {sexo}')


class Aluno(object):
    def __init__(self, nivel):
       # Pessoa.__init__(self)
        print(f'Nivel: {nivel}')
    
    
    def situacao(self, nota1, nota2, nota3, nota4):
        media = (nota1 + nota2 + nota3 + nota4)/4
        if media >= 7: 
            print('Aprovado')
        elif media >= 5:
            print('Recuperação')
        else:
            print('Reprovado')

    




diego = Aluno('Médio')
diego.situacao(2.2, 5.5, 7.7, 8.8)