from banco.Conta import Conta
from banco.Cliente import Cliente
from banco.ContaPoupanca import ContaPoupanca
from banco.ContaCorrente import ContaCorrente

# Criando instâncias de cliente
joao = Cliente("João", "Silva", "11111-1")
maria = Cliente("Maria", "Salgado", "22222-222")

# Criando instâncias de ContaPoupanca e ContaCorrente
conta_joao_poupanca = ContaPoupanca("123-6", joao, "Poupança", 5000.00, 1000.00, aniversario_conta=10)
conta_maria_corrente = ContaCorrente("123-7", maria, "Corrente", 3000.00, 2000.00, cheque_especial=True)

# Testando métodos específicos de ContaPoupanca
conta_joao_poupanca.calcular_juros_mensal(0.05)  # Exemplo com taxa de juros de 5%

# Testando métodos específicos de ContaCorrente
conta_maria_corrente.utilizar_cheque_especial(2500.00)

# Exibindo extratos e informações
print("Extrato da Conta Poupança de João:")
print(conta_joao_poupanca.extrato())

print("Extrato da Conta Corrente de Maria:")
print(conta_maria_corrente.extrato())

# Imprimindo o histórico de transações
print("Transações da Conta de João:")
for transacao in conta_joao_poupanca._historico._transacoes:
    print("-", transacao)

print("Transações da Conta de Maria:")
for transacao in conta_maria_corrente._historico._transacoes:
    print("-", transacao)
