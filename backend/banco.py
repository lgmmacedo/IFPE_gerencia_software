
# SISTEMA BANCÁRIO

contas = []


def cadastrar_conta():
    numero = input("Digite o número da conta: ")

    for conta in contas:
        if conta["numero"] == numero:
            print("Essa conta já existe!")
            return

    try:
        saldo_inicial = float(
            input("Digite o saldo inicial: ").replace(",", ".")
        )
    except ValueError:
        print("Saldo inválido!")
        return

    conta = {
        "numero": numero,
        "saldo": saldo_inicial
    }

    contas.append(conta)
    print("Conta cadastrada com sucesso!")



def consultar_saldo():
    numero = input("Digite o número da conta: ")

    for conta in contas:
        if conta["numero"] == numero:
            print("Saldo: R$", conta["saldo"])
            return

    print("Conta não encontrada!")



def credito():
    numero = input("Digite o número da conta: ")
    valor = float(input("Digite o valor: ").replace(",", "."))

    if valor < 0:
        print("Erro: o valor não pode ser negativo!")
        return

    for conta in contas:
        if conta["numero"] == numero:
            conta["saldo"] += valor
            print("Crédito realizado!")
            return

    print("Conta não encontrada!")




def debito():
    numero = input("Digite o número da conta: ")
    valor = float(input("Digite o valor: ").replace(",", "."))

    if valor < 0:
        print("Erro: o valor não pode ser negativo!")
        return

    for conta in contas:
        if conta["numero"] == numero:
            if valor > conta["saldo"]:
                print("Saldo insuficiente!")
                return

            conta["saldo"] -= valor
            print("Débito realizado!")
            return

    print("Conta não encontrada!")


def transferencia():
    origem = input("Conta de origem: ")
    destino = input("Conta de destino: ")
    valor = float(input("Valor da transferência: ").replace(",", "."))

    if valor < 0:
        print("Erro: o valor não pode ser negativo!")
        return

    conta_origem = None
    conta_destino = None

    for conta in contas:
        if conta["numero"] == origem:
            conta_origem = conta
        if conta["numero"] == destino:
            conta_destino = conta

    if conta_origem is None or conta_destino is None:
        print("Conta não encontrada!")
        return

    if valor > conta_origem["saldo"]:
        print("Saldo insuficiente!")
        return

    conta_origem["saldo"] -= valor
    conta_destino["saldo"] += valor

    print("Transferência realizada!")
