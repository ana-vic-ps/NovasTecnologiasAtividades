numero = int(input("Digite um número: "))
# redução no número de iterações necessárias para encontrar possíveis divisores.
if numero > 1:
    for i in range(2, numero // 2 + 1):
        if numero % i == 0:
            print(f"{numero} não é um número primo.")
            break
    else:
        print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")
