from banco.Conta import Conta
from datetime import datetime

class ContaPoupanca(Conta):
    _total_poupanca = 0

    def __init__(self, numero, cliente, tipo_conta, saldo, limite, aniversario_conta):
        super().__init__(numero, cliente, tipo_conta, saldo, limite)
        self._aniversario_conta = aniversario_conta
        ContaPoupanca._total_poupanca += 1

    def calcular_juros_mensal(self, taxa_juros):
        # Verifica se a data atual é o aniversário da conta
        hoje = datetime.now().day
        if hoje == self._aniversario_conta:
            juros = self.saldo * taxa_juros
            self.saldo += juros
            self._historico._transacoes.append(f"Calculou e aplicou juros mensais no valor de {juros}.")
            return True
        else:
            return False

    @staticmethod
    def get_total_contas():
        return ContaPoupanca._total_poupanca
