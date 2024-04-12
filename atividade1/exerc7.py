segundos_total = int(input("Digite a quantidade de segundos: "))

dias = segundos_total // (24 * 3600)
segundos_restantes = segundos_total % (24 * 3600)
horas = segundos_restantes // 3600
segundos_restantes %= 3600
minutos = segundos_restantes // 60
segundos = segundos_restantes % 60

print(f"{dias} dias - {horas} horas - {minutos} minutos  - {segundos} segundos ")

