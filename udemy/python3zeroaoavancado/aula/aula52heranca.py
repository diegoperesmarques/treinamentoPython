class Animal(object):
    def __init__(self):
        print('Animal criado.')
    

    def quemSouEu(self):
        print('Eu sou um animal')
    

    def comer(self):
        print('Comendo...')


class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Cachorro criado.')


    def quemSouEu(self):
        print('Sou um cachorro.')


    def latir(self):
        print('Au au ')

animal = Animal()
animal.quemSouEu()
animal.comer()
sam = Cachorro()
sam.quemSouEu()
