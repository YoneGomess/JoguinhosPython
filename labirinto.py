import tkinter as tk
import tkinter.messagebox

class JogoLabirinto:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title('Jogo de Labirinto')
        # Desabilita o botão de maximizar
        self.janela.resizable(False, False)
        self.canvas = tk.Canvas(self.janela, bg='white', width=600, height=600)
        self.canvas.pack()
        self.criar_labirinto()
        self.x, self.y = 1, 1  # Iniciar na posição inicial do labirinto
        self.desenhar_jogador()
        self.janela.bind('<KeyPress>', self.mover_jogador)

    def criar_labirinto(self):
        # Adiciona um espaço no final do labirinto para representar a saída
        self.labirinto = [
            "XXXXXXXXXXXXXXXXXXXX",
            "X     X    X       X",
            "X XXXXX XXXX XXXXX X",
            "X       X      X   X",
            "X XXXXX XXXXXX X X X",
            "X X   X        X X X",
            "X X XXXX XXXXXXXX X X",
            "X X    X X        X X",
            "X XXXX X X XXXXXX X X",
            "X      X X   X    X X",
            "XXXXXX XXXXX X XXXX X",
            "X      X   X X X    X",
            "X XXXXXX XXX X XXXX X",
            "X                X  X",
            "XXXXXXXXXXXXXXX  X  X",
            "X                X  X",
            "X XXXXXXXXXXXXXXXX  X",
            "X                    X",
            "XXXXXXXXXXXXXXXXXXXXX",
             "XXXXXXXXXXXXXXXXXXXXX",
        ]
        for i, linha in enumerate(self.labirinto):
            for j, coluna in enumerate(linha):
                if coluna == "X":
                    self.canvas.create_rectangle(j*30, i*30, j*30+30, i*30+30, fill='pink')

    def desenhar_jogador(self):
        self.jogador = self.canvas.create_rectangle(self.x*30, self.y*30, self.x*30+30, self.y*30+30, fill='red')

    def mover_jogador(self, event):
        if event.keysym == 'Up' and self.labirinto[self.y-1][self.x] == ' ':
            self.y -= 1
        elif event.keysym == 'Down' and self.labirinto[self.y+1][self.x] == ' ':
            self.y += 1
        elif event.keysym == 'Left' and self.labirinto[self.y][self.x-1] == ' ':
            self.x -= 1
        elif event.keysym == 'Right' and self.labirinto[self.y][self.x+1] == ' ':
            self.x += 1
        self.canvas.coords(self.jogador, self.x*30, self.y*30, (self.x+1)*30, (self.y+1)*30)
        # Verifica se o jogador chegou ao final do labirinto
        if self.x == len(self.labirinto[0]) - 1 and self.y == len(self.labirinto) - 2:
            resposta = tk.messagebox.askyesno("Parabéns", "Você ganhou! Deseja jogar novamente?")
            if resposta:
                self.criar_labirinto()
                self.x, self.y = 1, 1
                self.canvas.coords(self.jogador, self.x*30, self.y*30, self.x*30+30, self.y*30+30)
            else:
                self.janela.destroy()
                
        if self.x == len(self.labirinto[0]) - 1 and self.y == len(self.labirinto) - 3:
            resposta = tk.messagebox.askyesno("Parabéns", "Você ganhou! Deseja jogar novamente?")
            if resposta:
                self.criar_labirinto()
                self.x, self.y = 1, 1
                self.canvas.coords(self.jogador, self.x*30, self.y*30, self.x*30+30, self.y*30+30)
            else:
                self.janela.destroy()

if __name__ == "__main__":
    janela = tk.Tk()
    jogo = JogoLabirinto(janela)
    janela.mainloop()
