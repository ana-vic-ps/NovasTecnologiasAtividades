# Lista de pedidos de sanduíches
sandwich_orders = []

# Solicitar ao usuário que insira o nome do sanduíche até que ele deseje parar
while True:
    pedido = input("Digite o nome do sanduíche que deseja (ou 'sair' para encerrar): ")
    if pedido.lower() == 'sair':
        break
    sandwich_orders.append(pedido)

# Lista vazia para armazenar sanduíches prontos
finished_sandwiches = []

# Preparando cada sanduíche e movendo-o para a lista de sanduíches prontos
for pedido in sandwich_orders:
    print(f"Preparei seu sanduíche de {pedido}.")
    finished_sandwiches.append(pedido)

# Exibindo a lista de sanduíches prontos
print("\nSanduíches preparados:")
for sanduiche in finished_sandwiches:
    print("- " + sanduiche)
