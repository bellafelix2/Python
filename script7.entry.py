import tkinter

# Criando a janela principal
janela = tkinter.Tk()
# título da janela
janela.title("Título do projeto")
# tamanho da janela
janela.geometry("650x650")
# Cor de fundo:
janela.configure(bg="blue")

# elementos dentro da janela:
# Estilos personalizados:

estilo_label = {
    "font": ("Open Sans", 20),
    "bg": "white",
    "padx": 5,
    "pady": 5,
    "bd": 2,
    "relief": "solid",
}

# Label nome:
label = tkinter.Label(janela, text="Qual o seu nome?", **estilo_label)
label.grid(row=0, column=0)

# Entry nome:
entry = tkinter.Entry(janela, width=25)
entry.grid(row=1, column=0)

# Label idade:
label_2 = tkinter.Label(janela, text="Qual a sua cidade?", **estilo_label)
label_2.grid(row=2, column=0)

# Entry idade:
entry_2 = tkinter.Entry(janela, width=25)
entry_2.grid(row=3, column=0)

# Label para exibir resultado:
label_3 = tkinter.Label(janela)
label_3.grid(row=4, column=0)


# Função para o botão:
def exibir():
    resultado = f"Resultado: {entry.get()}, {entry_2.get()}"
    label_3.configure(text=resultado)


# Botão:
botao = tkinter.Button(janela, text="Clique", fg="red", command=exibir)
botao.grid(row=2, column=1)

# Chamando a janela para exibir por meio de loop
janela.mainloop()