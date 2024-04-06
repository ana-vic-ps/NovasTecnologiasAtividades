n = int(input("Digite um número maior ou igual a 3: "))

fibonacci_antecessor = 1
fibonacci_atual = 1

for _ in range(3, n + 1):
    fibonacci_proximo = fibonacci_antecessor + fibonacci_atual
    fibonacci_antecessor = fibonacci_atual
    fibonacci_atual = fibonacci_proximo

print(f"O {n}-ésimo termo da série de Fibonacci é {fibonacci_atual}.")
