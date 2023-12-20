import tkinter as tk
from tkinter import messagebox

class Banco_de_Dados:
    def __init__(self):
        self.dado = []

    def Ordenar(self):
        self.dado.sort()

    def Ordenar_Decrescente(self):
        self.dado.sort(reverse=True)

    def Ordenar_Numericamente(self):
        try:
            self.dado = sorted(self.dado, key=lambda x: float(x))
        except ValueError:
            messagebox.showinfo("Aviso", "Há dados no banco que não são números!")

    def Verificar_se_mesmo_tipo(self): 
        if not self.dado:
            return True
        tipo_base = type(self.dado[0])
        for i in self.dado:
            if type(i) != tipo_base:
                return False
        return True

    def Inserir(self, dado):
        if dado == "":
            messagebox.showinfo("Aviso", "Campo de digitação vazio!")
        elif dado in self.dado:
            messagebox.showinfo("Aviso", f"O dado '{dado}' já existe no banco.")
        else:
            self.dado.append(dado)

    def Deletar(self, dado):
        if dado == "":
            messagebox.showinfo("Aviso", "Campo de digitação vazio!")
        elif dado in self.dado:
            self.dado.remove(dado)
        else:
            messagebox.showinfo("Aviso", f"O dado '{dado}' não existe no banco.")

    def Database_String(self):
        return "\n".join([f"Chave_[{index}], Dado_[{item}]" for index, item in enumerate(self.dado)])
    
    def Soma(self):
        try:
            resultado = sum(map(float, self.dado))
            messagebox.showinfo("Resultado", resultado)
        except ValueError:
            messagebox.showinfo("Aviso", "Erro, os dados podem não ser do mesmo tipo!")

    def Multiplicacao(self):
        try:
            resultado = 1
            for i in self.dado:
                resultado *= float(i)
            
            messagebox.showinfo("Resultado", resultado)
        except (ValueError, IndexError):
            messagebox.showinfo("Aviso", "Erro, verifique se há pelo menos dois dados numéricos no banco.")

    def Divisao(self):
        try:
            resultado = float(self.dado[0])
            for i in self.dado[1:]:
                resultado /= float(i)
            
            messagebox.showinfo("Resultado", resultado)
        except (ValueError, IndexError):
            messagebox.showinfo("Aviso", "Erro, verifique se há pelo menos dois dados numéricos no banco.")
        except ZeroDivisionError:
            messagebox.showinfo("Aviso", "Erro, divisão por zero.")

    def Media(self):
        try:
            resultado = sum(map(float, self.dado)) / len(self.dado)
            messagebox.showinfo("Resultado", resultado)
        except (ValueError, ZeroDivisionError):
            messagebox.showinfo("Aviso", "Erro, verifique se há dados numéricos no banco.")


class Interface:
    def __init__(self):
        self.janela = tk.Tk()
        self.database = Banco_de_Dados()

    def Janela_Principal(self):
        def Botao_Inserir():
            string = self.campo_dado.get()
            self.database.Inserir(string)
            self.Atualizar_Texto()
            self.campo_dado.delete(0, tk.END)

        def Botao_Deletar():
            string = self.campo_dado.get()
            self.database.Deletar(string)
            self.Atualizar_Texto()
            self.campo_dado.delete(0, tk.END)

        def Botao_Ordenar_Alfabeticamente():
            if not self.database.dado:
                messagebox.showinfo("Aviso", "Banco de dados vazio. Nada a ordenar.")
            else:
                if self.database.Verificar_se_mesmo_tipo():  
                    self.texto.delete("1.0", tk.END)
                    self.database.Ordenar()
                    self.Atualizar_Texto()
                else:
                    messagebox.showinfo("Aviso", "Há dados no banco que não são do mesmo tipo!")
            self.campo_dado.delete(0, tk.END)

        def Botao_Ordenar_Alfabeticamente_Decrescente():
            if not self.database.dado:
                messagebox.showinfo("Aviso", "Banco de dados vazio. Nada a ordenar.")
            else:
                if self.database.Verificar_se_mesmo_tipo():  
                    self.texto.delete("1.0", tk.END)
                    self.database.Ordenar_Decrescente()
                    self.Atualizar_Texto()
                else:
                    messagebox.showinfo("Aviso", "Há dados no banco que não são do mesmo tipo!")

        def Botao_Soma():
            self.database.Soma()

        def Botao_Multiplicacao():
            self.database.Multiplicacao()

        def Botao_Divisao():
            self.database.Divisao()

        def Botao_Media():
            self.database.Media()

        self.janela.title("Banco de Dados")
        self.janela.geometry("600x600")

        self.label_inserir_dados = tk.Label(self.janela, text="Inserir e deletar dados:")
        self.label_inserir_dados.place(x=0, y=0)

        self.label_dado = tk.Label(self.janela, text="Dado:")
        self.label_dado.place(x=0, y=30)

        self.campo_dado = tk.Entry(self.janela)
        self.campo_dado.place(x=40, y=30)

        self.botao_inserir = tk.Button(self.janela, text="Inserir", command=Botao_Inserir)
        self.botao_inserir.configure(background="lime green")
        self.botao_inserir.place(x=0, y=60)

        self.botao_deletar = tk.Button(self.janela, text="Deletar", command=Botao_Deletar)
        self.botao_deletar.configure(background="lime green")
        self.botao_deletar.place(x=70, y=60)

        self.label_operacoes = tk.Label(self.janela, text="Ordenamentos:")
        self.label_operacoes.place(x=0, y=95)

        self.botao_ordenar_alfabeticamente = tk.Button(self.janela, text="  Crescente  ", command=Botao_Ordenar_Alfabeticamente)
        self.botao_ordenar_alfabeticamente.configure(background="sky blue")
        self.botao_ordenar_alfabeticamente.place(x=5, y=120)

        self.botao_ordenar_alfabeticamente_decrescente = tk.Button(self.janela, text="Decrescente", command=Botao_Ordenar_Alfabeticamente_Decrescente)
        self.botao_ordenar_alfabeticamente_decrescente.configure(background="sky blue")
        self.botao_ordenar_alfabeticamente_decrescente.place(x=5, y=150)

        self.label_operacoes_matematicas = tk.Label(self.janela, text="Operações matemáticas:")
        self.label_operacoes_matematicas.place(x=5, y=180)

        self.botao_soma = tk.Button(self.janela, text="        Soma      ", command=Botao_Soma)
        self.botao_soma.configure(background="sky blue")
        self.botao_soma.place(x=5, y=210)

        self.botao_multiplicacao = tk.Button(self.janela, text="Multiplicação", command=Botao_Multiplicacao)
        self.botao_multiplicacao.configure(background="sky blue")
        self.botao_multiplicacao.place(x=5, y=240)

        self.botao_divisao = tk.Button(self.janela, text="     Divisão      ", command=Botao_Divisao)
        self.botao_divisao.configure(background="sky blue")
        self.botao_divisao.place(x=5, y=270)

        self.botao_media = tk.Button(self.janela, text="      Média       ", command=Botao_Media)
        self.botao_media.configure(background="sky blue")
        self.botao_media.place(x=5, y=300)

        self.texto = tk.Text(self.janela, relief='flat', state='disabled')
        self.texto.configure(background="gray80")
        self.texto.place(x=200, y=3, width=397, height=593)

        self.Atualizar_Texto()

        self.janela.mainloop()

    def Atualizar_Texto(self):
        self.texto.configure(state='normal')
        self.texto.delete("1.0", tk.END)
        self.texto.insert(tk.END, self.database.Database_String())
        self.texto.configure(state='disabled')

janela = Interface()
janela.Janela_Principal()
