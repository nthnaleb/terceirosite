class ContaBancaria:
    def __init__(self, numero_conta: str, nome_titular: str, cpf_titular: str, agencia: str, tipo_conta: str, saldo_inicial: float = 0.0, situacao: str = "ativa"):
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.cpf_titular = cpf_titular
        self.agencia = agencia
        self.tipo_conta = tipo_conta
        self.saldo = max(0.0, float(saldo_inicial))
        self.situacao = situacao.lower()

    def apresentarDados(self):
        print("\n--- BANCO HORIZONTE ---")
        print(f"Conta: {self.numero_conta}")
        print(f"Titular: {self.nome_titular}")
        print(f"CPF: {self.cpf_titular}")
        print(f"Agência: {self.agencia}")
        print(f"Tipo: {self.tipo_conta.capitalize()}")
        print(f"Saldo: R$ {self.saldo:.2f}")
        print(f"Situação: {self.situacao.capitalize()}")
        print("-----------------------")

    def depositar(self, valor: float):
        if self.situacao == "bloqueada":
            print(f"[RECUSADO] Depósito de R$ {valor:.2f} não realizado: A conta {self.numero_conta} está bloqueada.")
            return False
        if valor <= 0:
            print(f"[RECUSADO] Depósito de R$ {valor:.2f} não realizado: O valor deve ser superior a zero.")
            return False
        
        self.saldo += valor
        print(f"[SUCESSO] Depósito de R$ {valor:.2f} realizado na conta {self.numero_conta}. Novo saldo: R$ {self.saldo:.2f}")
        return True

    def sacar(self, valor: float):
        if self.situacao == "bloqueada":
            print(f"[RECUSADO] Saque de R$ {valor:.2f} não realizado: A conta {self.numero_conta} está bloqueada.")
            return False
        if valor <= 0:
            print(f"[RECUSADO] Saque de R$ {valor:.2f} não realizado: O valor deve ser superior a zero.")
            return False
        if valor > self.saldo:
            print(f"[RECUSADO] Saque de R$ {valor:.2f} não realizado: Saldo insuficiente na conta {self.numero_conta} (Saldo atual: R$ {self.saldo:.2f}).")
            return False

        self.saldo -= valor
        print(f"[SUCESSO] Saque de R$ {valor:.2f} realizado na conta {self.numero_conta}. Novo saldo: R$ {self.saldo:.2f}")
        return True

    def consultarSaldo(self):
        print(f"[CONSULTA] Conta {self.numero_conta} ({self.nome_titular}) - Saldo atual: R$ {self.saldo:.2f}")
        return self.saldo

    def alterarTitular(self, novo_nome: str):
        if not novo_nome or not novo_nome.strip():
            print(f"[ERRO] Alteração de nome não realizada: O novo nome não pode estar vazio.")
            return False
        
        nome_antigo = self.nome_titular
        self.nome_titular = novo_nome.strip()
        print(f"[SUCESSO] Titular da conta {self.numero_conta} alterado de '{nome_antigo}' para '{self.nome_titular}'.")
        return True

    def bloquearConta(self):
        self.situacao = "bloqueada"
        print(f"[STATUS] A conta {self.numero_conta} ({self.nome_titular}) foi BLOQUEADA.")

    def desbloquearConta(self):
        self.situacao = "ativa"
        print(f"[STATUS] A conta {self.numero_conta} ({self.nome_titular}) foi DESBLOQUEADA.")

    def transferir(self, valor: float, conta_destino: 'ContaBancaria'):
        if valor <= 0:
            print(f"[RECUSADO] Transferência de R$ {valor:.2f} cancelada: O valor deve ser superior a zero.")
            return False
        if self.situacao != "ativa":
            print(f"[RECUSADO] Transferência cancelada: A conta de origem {self.numero_conta} não está ativa.")
            return False
        if conta_destino.situacao != "ativa":
            print(f"[RECUSADO] Transferência cancelada: A conta de destino {conta_destino.numero_conta} não está ativa.")
            return False
        if valor > self.saldo:
            print(f"[RECUSADO] Transferência cancelada: Saldo insuficiente na conta {self.numero_conta}.")
            return False

        self.saldo -= valor
        conta_destino.saldo += valor
        print(f"[SUCESSO] Transferência de R$ {valor:.2f} realizada da conta {self.numero_conta} ({self.nome_titular}) para a conta {conta_destino.numero_conta} ({conta_destino.nome_titular}).")
        return True

    def emitirRelatorio(self):
        print(f"\n================ RELATÓRIO DA CONTA ================")
        print(f" Número da Conta : {self.numero_conta}")
        print(f" Titular         : {self.nome_titular}")
        print(f" Agência         : {self.agencia}")
        print(f" Tipo de Conta   : {self.tipo_conta.capitalize()}")
        print(f" Saldo Disponível: R$ {self.saldo:.2f}")
        print(f" Situação Atual  : {self.situacao.capitalize()}")
        print(f"====================================================")