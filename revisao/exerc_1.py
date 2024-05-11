# Função para calcular a quantidade mínima de notas e moedas
def calcular_notas_moedas(valor):
    notas = [100, 50, 20, 10, 5, 2]
    moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
    notas_usadas = {}

    # Calcula notas
    for nota in notas:
        qtd_notas = int(valor / nota)
        notas_usadas[nota] = qtd_notas
        valor -= qtd_notas * nota

    # Calcula moedas
    for moeda in moedas:
        qtd_moedas = int(valor / moeda)
        notas_usadas[moeda] = qtd_moedas
        valor -= qtd_moedas * moeda

    return notas_usadas

# Função para imprimir a relação de notas e moedas


def imprimir_notas_moedas(notas_usadas):
    print("NOTAS:")
    for nota in [100, 50, 20, 10, 5, 2]:
        if notas_usadas[nota] > 0:
            print(f"{notas_usadas[nota]} nota(s) de R$ {nota}.00")
    print("MOEDAS:")
    for moeda in [1, 0.50, 0.25, 0.10, 0.05, 0.01]:
        if notas_usadas[moeda] > 0:
            print(f"{notas_usadas[moeda]:.0f} moeda(s) de R$ {moeda:.2f}")


# Entrada de dados
valor = float(input('Digite o valor a ser trocado: '))

# Calcula notas e moedas
notas_usadas = calcular_notas_moedas(valor)
print(notas_usadas)

# Imprime resultado
imprimir_notas_moedas(notas_usadas)