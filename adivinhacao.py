import random

def jogar_adivinhacao():
    print("Bem-vindo ao jogo de adivinhação!")
    print("Estou pensando em um número entre 1 e 100.")

    numero_secreto = random.randint(1, 100)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina o nível: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print(f"Tentativa {rodada} de {total_de_tentativas}")
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = numero_secreto == chute
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if acertou:
            print(f"Parabéns! Você acertou e fez {pontos} pontos!")
            break
        else:
            if maior:
                print("O seu chute foi maior do que o número secreto!")
            elif menor:
                print("O seu chute foi menor do que o número secreto!")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

    print(f"Fim do jogo. Você fez {pontos} pontos.")
    jogar_novamente()

def jogar_novamente():
    resposta = input("Deseja jogar novamente? (sim/não) ")
    if resposta.lower() == 'sim':
        jogar_adivinhacao()
    else:
        print("Obrigado por jogar! Até a próxima.")

if __name__ == "__main__":
    jogar_adivinhacao()
