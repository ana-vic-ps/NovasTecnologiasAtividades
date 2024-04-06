while True:
    print("Menu:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Divisão")
    print("4. Multiplicação")
    print("5. Sair")

    opcao = input("Escolha uma opção (1-5): ")

    if opcao == "5":
        print("Programa encerrado.")
        break
    elif opcao not in ["1", "2", "3", "4"]:
        print("Opção inválida. Por favor, escolha uma opção válida (1-5).")
        continue

    numero = int(input("Digite o número para ver a tabuada: "))

    for i in range(1, 11):
        if opcao == "1":
            resultado = numero + i
            operacao = "Adição"
        elif opcao == "2":
            resultado = numero - i
            operacao = "Subtração"
        elif opcao == "3":
            resultado = numero / i
            operacao = "Divisão"
        elif opcao == "4":
            resultado = numero * i
            operacao = "Multiplicação"
        print(f"{numero} {operacao} {i} = {resultado}")