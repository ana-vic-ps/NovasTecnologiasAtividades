while True:
    num = input("Digite um número com cinco dígitos: ")

    if len(num) == 5:
        for i in num:
            print(i, end="   ")
        break
    else:
        print("Por favor, digite um número com cinco dígitos.")