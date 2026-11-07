
# SISTEMA BANCÁRIO

contas = []



def cadastrar_conta():
    numero = input("Digite o número da conta: ")

    for conta in contas:
        if conta["numero"] == numero:
            print("Essa conta já existe!")
            return

    print("Escolha o tipo de conta:")
    print("1 - Conta Simples")
    print("2 - Conta Poupança")

    tipo = input("Digite a opção: ")

    if tipo == "1":
        tipo_conta = "simples"
    elif tipo == "2":
        tipo_conta = "poupanca"
    else:
        print("Opção inválida!")
        return

    conta = {
        "numero": numero,
        "saldo": 0.0,
        "tipo": tipo_conta
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

    for conta in contas:
        if conta["numero"] == numero:
            conta["saldo"] += valor
            print("Crédito realizado!")
            return

    print("Conta não encontrada!")


def debito():
    numero = input("Digite o número da conta: ")
    valor = float(input("Digite o valor: ").replace(",", "."))

    for conta in contas:
        if conta["numero"] == numero:
            conta["saldo"] -= valor
            print("Débito realizado!")
            return

    print("Conta não encontrada!")


def transferencia():
    origem = input("Conta de origem: ")
    destino = input("Conta de destino: ")
    valor = float(input("Digite o valor: ").replace(",", "."))
    conta_origem = None
    conta_destino = None

    for conta in contas:
        if conta["numero"] == origem:
            conta_origem = conta

        if conta["numero"] == destino:
            conta_destino = conta

    if conta_origem and conta_destino:
        conta_origem["saldo"] -= valor
        conta_destino["saldo"] += valor
        print("Transferência realizada!")
    else:
        print("Conta não encontrada!")
