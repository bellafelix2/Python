import tkinter # palavra reservada

# janela principal:
janela = tkinter.Tk()
# titulo
janela.title('Bella')
# tamanho:
janela.geometry('650x450')
# cor de fundo
janela.configure(bg="orange")

# Labels:
nome = tkinter.Label(janela, text="Numero do pedido:")
nome.pack()

# Entrys
nome_entrada = tkinter.Entry(janela)
nome_entrada.pack()

janela.mainloop()  # start

