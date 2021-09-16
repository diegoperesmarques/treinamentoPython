class sample(object): #por padrão tem que colocar object nos parenteses
    pass

x = sample()
print(type(x))


class Dog(object):
    species = 'mamifero'
    def __init__(self, raca):
        self.raca = raca
        print(len(self.species))

sam = Dog(raca='Lab')
frank = Dog('Huskie')
#ponto server para pussar atributos ou parâmetros da clase
print(sam.raca)
print(frank.raca)