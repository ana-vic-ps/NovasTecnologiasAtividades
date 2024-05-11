from banco.Conta import Conta

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, tipo_conta, saldo, limite, cheque_especial):
        super().__init__(numero, cliente, tipo_conta, saldo, limite)
        self._cheque_especial = cheque_especial

    def utilizar_cheque_especial(self, valor):
        if self._cheque_especial:
            if self.saldo + self._limite >= valor:
                self.saldo -= valor
                self._historico._transacoes.append(f"Utilizou o cheque especial para cobrir o valor de {valor}.")
                return True
            else:
                self._historico._transacoes.append("Tentou utilizar o cheque especial, mas saldo insuficiente.")
                return False
        else:
            self._historico._transacoes.append("Tentou utilizar o cheque especial, mas não está disponível.")
            return False
