import tkinter as tk
from tkinter import messagebox

class Calculadora:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora Avançada")
        self.master.geometry("400x500")

        # Variável para exibir os resultados
        self.resultado = tk.StringVar()

        # Tela de exibição
        self.tela = tk.Entry(master, textvariable=self.resultado, font=("Arial", 24), bd=10, insertwidth=2, width=14, justify="right")
        self.tela.grid(row=0, column=0, columnspan=4)

        # Botões da calculadora
        botoes = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", "=", "+"
        ]

        # Gerar os botões
        linha = 1
        coluna = 0
        for botao in botoes:
            comando = lambda x=botao: self.on_click(x)
            tk.Button(master, text=botao, padx=20, pady=20, font=("Arial", 18), command=comando).grid(row=linha, column=coluna)
            coluna += 1
            if coluna > 3:
                coluna = 0
                linha += 1

    def on_click(self, char):
        """Método para tratar os cliques dos botões."""
        if char == "=":
            try:
                expressao = self.resultado.get()
                resultado = eval(expressao)
                self.resultado.set(resultado)
            except Exception as e:
                messagebox.showerror("Erro", "Expressão inválida!")
                self.resultado.set("")
        elif char == "C":
            self.resultado.set("")
        else:
            self.resultado.set(self.resultado.get() + char)


# Inicializar a calculadora
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()
