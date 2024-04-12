import math

a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

delta = b**2 - 4*a*c


if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("As raízes da equação são:")
    print(f"x' = {x1}")
    print(f"x'' = {x2}")
elif delta == 0:
    x = -b / (2*a)
    print("A equação possui raízes reais iguais:")
    print(f"x' = x'' = {x}")
else:
    parte_real = -b / (2*a)
    parte_imaginaria = math.sqrt(abs(delta)) / (2*a)
    print("As raízes da equação são complexas:")
    print(f"x' = {parte_real} + {parte_imaginaria}i")
    print(f"x'' = {parte_real} - {parte_imaginaria}i")