class Book(object):
    def __init__(self, titulo, autor, paginas):
        print('Um livro foi criado.')
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    
    def __str__(self):
        return 'Titulo {a}'.format(a=self.titulo)
    

    def __len__(self):
        return self.paginas

    
    def __del__(self):
        print('Livro destruido')


livro = Book('Python', 'Diego', 100)
print(livro)
len(livro)
del livro