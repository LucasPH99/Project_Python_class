import random

def jogo_adivinhacao():
    # Gera um número aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Estou pensando em um número entre 1 e 100. Tente adivinhar.")

    while True:
        # Obtém a tentativa do jogador
        tentativa = int(input("Digite sua tentativa: "))
        tentativas += 1

        # Verifica se a tentativa está correta
        if tentativa == numero_secreto:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            break
        elif tentativa < numero_secreto:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")

if __name__ == "__main__":
    jogo_adivinhacao()
