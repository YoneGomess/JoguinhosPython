# Autor: Yone Gomes
# Data: 20/03/2024

import random

def jogar():
    escolhas = ['pedra', 'papel', 'tesoura']
    computador = random.choice(escolhas)
    jogador = None

    while jogador not in escolhas:
        jogador = input("Escolha pedra, papel ou tesoura: ").lower()

    print(f"\nVocê escolheu {jogador}, e o computador escolheu {computador}.\n")

    if jogador == computador:
        print("Empate!")
    elif jogador == 'pedra':
        if computador == 'tesoura':
            print("Você ganhou!")
        else:
            print("Você perdeu.")
    elif jogador == 'papel':
        if computador == 'pedra':
            print("Você ganhou!")
        else:
            print("Você perdeu.")
    elif jogador == 'tesoura':
        if computador == 'papel':
            print("Você ganhou!")
        else:
            print("Você perdeu.")

    jogar_novamente = input("Quer jogar novamente? (sim/não): ").lower()
    if jogar_novamente == "sim":
        jogar()
    else:
        print("Obrigado por jogar!")

if __name__ == "__main__":
    jogar()
