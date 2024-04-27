import csv
import os

agenda = {}

def carregar_contatos():
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    arquivo_csv = os.path.join(desktop_path, 'agenda.csv')
    if os.path.exists(arquivo_csv):
        with open(arquivo_csv, mode='r') as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)  # Skip the header row
            for row in reader:
                nome = row[0]
                email = row[1]
                telefone = row[2]
                data_nasc = row[3]
                agenda[nome] = [email, telefone, data_nasc]
        print("Contatos carregados com sucesso!")


def adicionar_contato(nome, email, telefone, data_nasc):
    agenda[nome] = [email, telefone, data_nasc]
    print("Contato adicionado à agenda!")


def listar_contatos():
    if not agenda:
        print("Sem contatos na agenda!")
    else:
        for nome, dados in agenda.items():
            print(f"Nome: {nome}, Email: {dados[0]}, Telefone: {dados[1]}, Data de nascimento: {dados[2]}")


def buscar_contato(nome):
    if nome in agenda:
        dados = agenda[nome]
        print(f"Nome: {nome}, Email: {dados[0]}, Telefone: {dados[1]}, Data de nascimento: {dados[2]}")
    else:
        print("Contato não está na agenda.")


def excluir_contato(nome):
    if nome in agenda:
        respo = input("Realmente deseja excluir o contato?(S/N): ")
        if respo.lower() == 's':
            del agenda[nome]
            print("Contato removido com sucesso!")
    else:
        print("Contato não encontrado na agenda.")


def alterar_contato(nome, novo_nome=None, email=None, telefone=None, data_nasc=None):
    if nome in agenda:
        contato = agenda[nome]
        if novo_nome:
            agenda[novo_nome] = contato
            del agenda[nome]
            nome = novo_nome
        if email:
            contato[0] = email
        if telefone:
            contato[1] = telefone
        if data_nasc:
            contato[2] = data_nasc
        print("Contato alterado com sucesso!")
    else:
        print("Contato não encontrado na agenda.")


def salvar_contatos(agenda):
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    arquivo_csv = os.path.join(desktop_path, 'agenda.csv')
    with open(arquivo_csv, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')  # Specify the delimiter as ';'
        writer.writerow(['Nome', 'Email', 'Telefone', 'Data de Nascimento'])
        for nome, dados in agenda.items():
            writer.writerow([nome] + dados)


carregar_contatos()

while True:
    print("\n-----------MENU------------\n")
    print("Opção 0: Sair\nOpção 1: Adicionar contato\nOpção 2: Listar contatos\nOpção 3: Buscar contato\nOpção 4: Excluir contato\nOpção 5: Alterar contato\n\n--------------------------")
    opcao = int(input("\nEscolha uma opção: "))

    if opcao == 1:
        nome = input("Digite o nome do contato: ")
        email = input("Digite o email do contato: ")
        telefone = input("Digite o telefone do contato: ")
        data_nasc = input("Digite a data de nascimento do contato: ")
        adicionar_contato(nome, email, telefone, data_nasc)
    elif opcao == 2:
        listar_contatos()
    elif opcao == 3:
        nome = input("Nome do contato a ser buscado: ")
        buscar_contato(nome)
    elif opcao == 4:
        nome = input("Nome do contato a ser excluído: ")
        excluir_contato(nome)
    elif opcao == 5:
        nome = input("Nome do contato a ser alterado: ")
        buscar_contato(nome)
        if nome in agenda:
            novo_nome = input("Novo nome (deixe em branco para manter o mesmo): ")
            email = input("Novo email (deixe em branco para manter o mesmo): ")
            telefone = input("Novo telefone (deixe em branco para manter o mesmo): ")
            data_nasc = input("Nova data de nascimento (deixe em branco para manter a mesma): ")
            alterar_contato(nome, novo_nome, email, telefone, data_nasc)
        else:
            pass
    elif opcao == 0:
        salvar_contatos(agenda)
        print("Contatos salvos com sucesso. Saindo...")
        break
    else:
        print("Opção inválida! Escolha uma opção de 0 a 5")
