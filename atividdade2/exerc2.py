import random

def escolher_palavra():
    palavras = ["python", "programacao", "computador", "algoritmo", "desenvolvimento"]
    return random.choice(palavras)

def mostrar_palavra(palavra, letras_adivinhadas):
    resultado = ""
    for letra in palavra:
        if letra in letras_adivinhadas:
            resultado += letra
        else:
            resultado += "_"
    return resultado

def jogo_da_forca():
    palavra = escolher_palavra()
    letras_corretas = []
    tentativas = 6
    letras_erradas = []

    print("Bem-vindo ao Jogo da Forca!")
    print("A palavra tem", len(palavra), "letras.")
    print(mostrar_palavra(palavra, letras_corretas))

    while True:
        letra = input("Digite uma letra: ").lower()

        if letra in letras_corretas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if letra in palavra:
            letras_corretas.append(letra)
            print("Ótimo! Essa letra está na palavra.")
        else:
            letras_erradas.append(letra)
            tentativas -= 1
            print("Essa letra não está na palavra. Você tem", tentativas, "tentativas restantes.")

        print("Palavra: ", mostrar_palavra(palavra, letras_corretas))

        if tentativas == 0:
            print("Você perdeu! A palavra era:", palavra)
            break

        if mostrar_palavra(palavra, letras_corretas) == palavra:
            print("Parabéns! Você acertou a palavra:", palavra)
            break

jogo_da_forca()
