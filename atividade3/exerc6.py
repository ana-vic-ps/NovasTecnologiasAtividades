# Criando dicionários para representar informações sobre animais de estimação
animal1 = {
    "nome": "Rex",
    "tipo": "Cachorro",
    "dono": "João"
}

animal2 = {
    "nome": "Mia",
    "tipo": "Gato",
    "dono": "Maria"
}

animal3 = {
    "nome": "Bolt",
    "tipo": "Cachorro",
    "dono": "Pedro"
}

pets = [animal1, animal2, animal3]

for pet in pets:
    print("\nInformações sobre o animal de estimação:")
    print("Nome:", pet["nome"])
    print("Tipo:", pet["tipo"])
    print("Dono:", pet["dono"])
