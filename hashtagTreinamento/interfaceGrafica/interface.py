from tkinter import * 

def pegarCotacoes():
    texto = '''
        Dolar: 4.9885
        Euro: 5.9538
        BTC: 163681.5 
        '''
    return texto

janela = Tk()

janela.title('Cotação atual das moedas')
textoOrientacao = Label(janela, text='Clique no botão para ver as cotações')
textoOrientacao.grid(column=0, row=0)

botao = Button(janela, text='Buscar cotação', command=pegarCotacoes())
botao.grid(column=0, row=1)

texto_cotacoes = Label(janela, text='')
texto_cotacoes.grid(column=0, row=2)

janela.mainloop()
