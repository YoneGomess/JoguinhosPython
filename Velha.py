import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title('Jogo da Velha')
        self.janela.resizable(False, False)  # Desabilita a opção de maximizar
        self.janela.geometry("330x350")  # Define o tamanho da janela
        self.turno = 'X'
        self.tabuleiro = [['' for _ in range(3)] for _ in range(3)]
        self.botoes = [[None for _ in range(3)] for _ in range(3)]
        self.criar_interface()

    def criar_interface(self):
        for i in range(3):
            for j in range(3):
                self.botoes[i][j] = tk.Button(self.janela, text='', font='Arial 20', width=5, height=2,
                                              bg='pink', activebackground='lightblue',
                                              command=lambda i=i, j=j: self.jogada(i, j))
                self.botoes[i][j].grid(row=i, column=j, sticky='nsew')
        for i in range(3):
            self.janela.grid_rowconfigure(i, weight=1)
            self.janela.grid_columnconfigure(i, weight=1)

    def jogada(self, i, j):
        if not self.tabuleiro[i][j] and not self.verificar_vitoria():
            self.tabuleiro[i][j] = self.turno
            self.botoes[i][j].config(text=self.turno, fg='red' if self.turno == 'X' else 'blue')
            if self.verificar_vitoria():
                messagebox.showinfo('Fim de Jogo', f'Jogador {self.turno} venceu!')
                self.reiniciar_jogo()
            elif self.verificar_empate():
                messagebox.showinfo('Fim de Jogo', 'Empate!')
                self.reiniciar_jogo()
            else:
                self.turno = 'O' if self.turno == 'X' else 'X'

    def verificar_vitoria(self):
        for i in range(3):
            if self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2] != '':
                return True
            if self.tabuleiro[0][i] == self.tabuleiro[1][i] == self.tabuleiro[2][i] != '':
                return True
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != '':
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != '':
            return True
        return False

    def verificar_empate(self):
        for row in self.tabuleiro:
            if '' in row:
                return False
        return True

    def reiniciar_jogo(self):
        self.turno = 'X'
        self.tabuleiro = [['' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.botoes[i][j].config(text='', state=tk.NORMAL, fg='black')

if __name__ == '__main__':
    root = tk.Tk()
    jogo = JogoDaVelha(root)
    root.mainloop()
