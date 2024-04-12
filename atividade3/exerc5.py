pessoa1 = {
    "first_name": "Ana",
    "last_name": "Victoria",
    "age": 24,
    "city": "Brasília"
}

pessoa2 = {
    "first_name": "Maria",
    "last_name": "Santos",
    "age": 25,
    "city": "Rio de Janeiro"
}

pessoa3 = {
    "first_name": "Pedro",
    "last_name": "Oliveira",
    "age": 35,
    "city": "Salvador"
}

people = [pessoa1, pessoa2, pessoa3]

for pessoa in people:
    print("\nInformações sobre a pessoa:")
    print("Primeiro nome:", pessoa["first_name"])
    print("Sobrenome:", pessoa["last_name"])
    print("Idade:", pessoa["age"])
    print("Cidade:", pessoa["city"])
