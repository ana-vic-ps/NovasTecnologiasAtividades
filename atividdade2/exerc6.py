lugares_vagos = [10, 2, 1, 3, 0]

def vender_bilhetes(sala, quantidade):
    if sala <= 0 or sala > len(lugares_vagos):
        print("Sala inválida.")
        return False
    elif lugares_vagos[sala - 1] >= quantidade:
        lugares_vagos[sala - 1] -= quantidade
        print("Bilhetes vendidos com sucesso!")
        return True
    else:
        print("Não há lugares suficientes nesta sala.")
        return False

while True:
    sala = int(input("Digite o número da sala (ou 0 para sair): "))
    if sala == 0:
        print("Programa encerrado.")
        break
    quantidade = int(input("Digite a quantidade de lugares solicitados: "))
    vender_bilhetes(sala, quantidade)
    print("Lugares vagos atualizados:", lugares_vagos)
