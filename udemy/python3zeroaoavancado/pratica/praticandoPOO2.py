class Funcionario:
    def __init__(self, nome, setor, salario):
        self.nome = nome
        self.setor = setor
        self.salario = salario


    def aumentarSalario(self, valorAumento):
        self.salario = self.salario + valorAumento
        return self.salario


    def diminuirSalario(self, valorReducao):
        novoSalario = self.salario - valorReducao

        if novoSalario <= 0:
            print('Não é possível deixar o valor abaixo de zero')
            return
        else: 
            self.salario = novoSalario
            return self.salario


    def informacoes(self):
        print('-' * 30)
        print('INFORMAÇÕES')
        print('-' * 30)

        print(f'Nome: {self.nome}')
        print(f'Setor: {self.setor}')
        print(f'Salario: {self.salario}')