
# SISTEMA BANCÁRIO

contas = []



def cadastrar_conta():
    numero = input("Digite o número da conta: ")

    for conta in contas:
        if conta["numero"] == numero:
            print("Essa conta já existe!")
            return

    print("1 - Conta Simples")
    print("2 - Conta Bônus")

    tipo = input("Escolha o tipo de conta: ")

    if tipo == "1":
        conta = {
            "numero": numero,
            "saldo": 0.0,
            "tipo": "simples"
        }

    elif tipo == "2":
        conta = {
            "numero": numero,
            "saldo": 0.0,
            "tipo": "bonus",
            "pontos": 10
        }

    else:
        print("Tipo de conta inválido!")
        return

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

            if conta["tipo"] == "bonus":
                pontos_ganhos = int(valor // 100)
                conta["pontos"] += pontos_ganhos
                print("Pontos ganhos:", pontos_ganhos)
                print("Total de pontos:", conta["pontos"])

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

    if valor <= 0:
        print("O valor deve ser maior que zero!")
        return

    if origem == destino:
        print("As contas devem ser diferentes!")
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

    if conta_origem["saldo"] < valor:
        print("Saldo insuficiente!")
        return

    conta_origem["saldo"] -= valor
    conta_destino["saldo"] += valor

    if conta_destino.get("tipo") == "bonus":
        pontos_ganhos = int(valor // 200)
        conta_destino["pontos"] += pontos_ganhos
        print("Pontos ganhos:", pontos_ganhos)
        print("Total de pontos:", conta_destino["pontos"])

    print("Transferência realizada!")
