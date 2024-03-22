import pygame
import sys
import tkinter as tk
from tkinter import messagebox, simpledialog

def selecionar_nivel():
    # Cria uma nova janela Tkinter
    root = tk.Tk()
    root.title("Seleção de Nível")
    root.configure(bg='Khaki')  # Define a cor de fundo da janela
    root.resizable(False, False)  # Impede a maximização da janela

    # Centraliza a janela na tela
    window_width = 300
    window_height = 65
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    # Define o nível como uma string Tkinter
    nivel = tk.StringVar(root)

    # Função chamada quando um botão de nível é pressionado
    def escolher_nivel(n):
        nivel.set(n)
        root.destroy()  # Fecha a janela imediatamente

    # Função chamada quando a janela é fechada
    def on_close():
        nivel.set(None)
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)

    # Cria um frame para conter os botões
    frame_botoes = tk.Frame(root, bg='Khaki')
    frame_botoes.pack(pady=10)  # Adiciona um espaçamento vertical

    # Cria e posiciona os botões de nível lado a lado com espaçamento
    botoes_niveis = {
        "Fácil": (lambda: escolher_nivel('Fácil')),
        "Médio": (lambda: escolher_nivel('Médio')),
        "Difícil": (lambda: escolher_nivel('Difícil'))
    }
    for texto, comando in botoes_niveis.items():
        botao = tk.Button(frame_botoes, text=texto, command=comando, width=10, height=2,
                          bg='black', fg='Khaki')  # Define as cores do botão e do texto
        botao.pack(side='left', padx=5, pady=5)  # Adiciona espaçamento

    # Executa o loop principal da janela Tkinter
    root.mainloop()

    # Retorna o nível selecionado ou None se a janela for fechada
    return nivel.get()

# Inicializa o Pygame
pygame.init()

# Pergunta o nível antes de iniciar o jogo
nivel_escolhido = selecionar_nivel()

if nivel_escolhido != 'None':

    # Configurações da tela
    largura_tela = 800
    altura_tela = 600
    tela = pygame.display.set_mode((largura_tela, altura_tela))

    # Define o título da janela
    pygame.display.set_caption('Ping Pong')

    # Cores
    BRANCO = (255, 255, 255)
    PRETO = (0, 0, 0)
    GOLD = (255,215,0)
    KAKHI = (240,230,140)

    # Configurações baseadas no nível
    if nivel_escolhido == 'Fácil':
        barra_largura = 150
        bolinha_raio = 15
    elif nivel_escolhido == 'Médio':
        barra_largura = 110
        bolinha_raio = 10
    elif nivel_escolhido == 'Difícil':
        barra_largura = 70
        bolinha_raio = 5
    else:
        # Se não escolher nenhum nível, usa configurações padrão
        barra_largura = 110
        bolinha_raio = 10

    # Posição inicial da barra
    barra_altura = 15
    barra_x = (largura_tela - barra_largura) // 2
    barra_y = altura_tela - barra_altura - 10

    # Posição inicial da bolinha
    bolinha_x = largura_tela // 2
    bolinha_y = barra_y - bolinha_raio
    bolinha_vel_x = 5
    bolinha_vel_y = -5

    # Velocidade da barra
    velocidade_barra = 10

    # Função para desenhar a barra
    def desenha_barra():
        pygame.draw.rect(tela, PRETO, (barra_x, barra_y, barra_largura, barra_altura))

    # Função para desenhar a bolinha
    def desenha_bolinha():
        pygame.draw.circle(tela, PRETO, (bolinha_x, bolinha_y), bolinha_raio)

    # Função para mostrar a caixa de diálogo de fim de jogo
    def mostrar_caixa_dialogo():
        root = tk.Tk()
        root.withdraw()  # Esconde a janela principal do Tkinter
        resposta = messagebox.askyesno("Fim de Jogo", "Você perdeu! Deseja jogar novamente?")
        root.destroy()  # Fecha a janela do Tkinter
        return resposta

    # Loop principal do jogo
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Captura as teclas pressionadas
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and barra_x > 0:
            barra_x -= velocidade_barra
        if teclas[pygame.K_RIGHT] and barra_x < largura_tela - barra_largura:
            barra_x += velocidade_barra

        # Movimento da bolinha
        bolinha_x += bolinha_vel_x
        bolinha_y += bolinha_vel_y

        # Colisão da bolinha com as bordas da tela
        if bolinha_y - bolinha_raio <= 0:
            bolinha_vel_y *= -1
        if bolinha_x - bolinha_raio <= 0 or bolinha_x + bolinha_raio >= largura_tela:
            bolinha_vel_x *= -1

        # Colisão da bolinha com a barra
        if bolinha_y + bolinha_raio >= barra_y and barra_x <= bolinha_x <= barra_x + barra_largura:
            bolinha_vel_y *= -1

        # Verifica se a bolinha passou da barra
        if bolinha_y + bolinha_raio > altura_tela:
            if mostrar_caixa_dialogo():
                # Reinicia a posição da bolinha e da barra
                bolinha_x = largura_tela // 2
                bolinha_y = barra_y - bolinha_raio
                bolinha_vel_x = 5
                bolinha_vel_y = -5
                barra_x = (largura_tela - barra_largura) // 2
            else:
                pygame.quit()
                sys.exit()

        # Preenche a tela com preto
        tela.fill(KAKHI)

        # Desenha a barra e a bolinha
        desenha_barra()
        desenha_bolinha()

        # Atualiza a tela
        pygame.display.flip()

        # Controla a taxa de atualização da tela
        pygame.time.Clock().tick(60)
