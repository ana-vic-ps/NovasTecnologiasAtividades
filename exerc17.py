n = input("Digite o número da conta (sem o dígito verificador): ")

soma_digitos = sum(int(digito) for digito in n)

digito_verificador = soma_digitos % 10

numero_conta_completo = f"00{n}-{digito_verificador}"

print(f"O número de conta completo correspondente é: {numero_conta_completo}")
