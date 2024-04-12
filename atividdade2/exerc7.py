def imprimir_tabuleiro(tabuleiro):
    linhas = ["  " + " | ".join(linha) + " " for linha in tabuleiro]
    separador = "\n" + " " + "-" * 11 + "\n"
    tabuleiro_formatado = separador.join(linhas)
    print("\n")
    print("  0   1   2")
    print(" " + " " * 11)
    print(tabuleiro_formatado)
    print("\n")

def verificar_vitoria(tabuleiro, jogador):
    for linha in tabuleiro:
        if linha.count(jogador) == 3:
            return True

    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] == jogador:
            return True

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    return False

def jogar_jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"

    while True:
        print(f"Jogador {jogador_atual}, é sua vez.")
        imprimir_tabuleiro(tabuleiro)
        linha = int(input("Escolha a linha (0, 1, 2): "))
        coluna = int(input("Escolha a coluna (0, 1, 2): "))

        if tabuleiro[linha][coluna] != " ":
            print("\nESSA POSIÇÃO JÁ ESTÁ OCUPADA. ESCOLHA OUTRA. \n")
            continue

        tabuleiro[linha][coluna] = jogador_atual

        if verificar_vitoria(tabuleiro, jogador_atual):
            print(f"Parabéns, jogador {jogador_atual} venceu!")
            break

        if all(all(posicao != " " for posicao in linha) for linha in tabuleiro):
            print("O jogo empatou!")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"

jogar_jogo_da_velha()
