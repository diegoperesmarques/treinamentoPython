class Dog(object):
    species = 'mamifero'

    def __init__(self, raca):
        self.raca = raca
        print(len(self.species))

    
    def latir(self):
        print('Au au ')


sam = Dog('Huskie')
sam.latir()


class Circulo(object):
    pi = 1.14

    def __init__(self, raio=1):
        self.raio = raio
    

    def area(self):
        return self.raio ** 2 * self.pi

    
    def defRaio(self, raio):
        self.raio = raio
    

    def obtemRaio(self):
        return self.raio


c = Circulo(2)
c.defRaio(3)