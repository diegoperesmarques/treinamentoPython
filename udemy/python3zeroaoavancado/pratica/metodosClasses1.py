class Pessoa:
    ano_atual = 2019

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)



p1 = Pessoa('Luiz', 32)
print(p1.ano_atual)