from tkinter import * 

app = Tk()
app.title("CFB Cursos")
app.geometry("500x300")
app.configure(background="#dde")

#anchor => N= Norte, S= Sul, E=Leste, W=Oeste
Label(app, text='Nome', background="#dde", foreground="#009", anchor=W).place(x=10, y=10, width=100, height=20)
nome = Entry(app)
nome.place(x=10, y=30, width=200, height=20)

Label(app, text="Telefone", background="#dde", foreground="#009", anchor=W).place(x=10, y=60, width=200, height=20)
telefone = Entry(app)
telefone.place(x=10, y=80, width=200, height=20)

Label(app, text='Email', background="#dde", foreground="#009", anchor=W).place(x=10, y=100, width=200, height=20)
email = Entry(app)
email.place(x=10, y=120, width=200, height=20)

Label(app, text='OBS', background="#dde", foreground="#009", anchor=W).place(x=10, y=140, width=200, height=20)
obs = Text(app)
obs.place(x=10, y=160, width=200, height=200)

app.mainloop()