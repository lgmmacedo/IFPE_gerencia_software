
contas = []


def consultar_conta(numero):
    for conta in contas:
        if conta["numero"] == str(numero):
            return conta

    raise ValueError("Conta nao encontrada!")


def cadastrar_conta(numero, tipo, saldo_inicial=None):
    numero = str(numero)

    if any(c["numero"] == numero for c in contas):
        raise ValueError("Essa conta ja existe!")

    if tipo not in ("simples", "bonus", "poupanca"):
        raise ValueError("Tipo de conta invalido!")

    if tipo in ("simples", "poupanca") and saldo_inicial is None:
        raise ValueError("Informe o saldo inicial!")

    saldo = float(saldo_inicial or 0)

    if saldo < 0:
        raise ValueError("Saldo inicial invalido!")

    conta = {
        "numero": numero,
        "tipo": tipo,
        "saldo": saldo
    }

    if tipo == "bonus":
        conta["pontos"] = 10

    contas.append(conta)
    return conta


def consultar_saldo(numero):
    conta = consultar_conta(numero)
    return conta["saldo"]


def credito(numero, valor):
    valor = float(valor)

    if valor <= 0:
        raise ValueError("Valor deve ser maior que zero!")

    conta = consultar_conta(numero)
    conta["saldo"] += valor

    if conta["tipo"] == "bonus":
        conta["pontos"] += int(valor // 100)

    return conta


def debito(numero, valor):
    valor = float(valor)

    if valor <= 0:
        raise ValueError("Valor deve ser maior que zero!")

    conta = consultar_conta(numero)

    limite = -1000 if conta["tipo"] in ("simples", "bonus") else 0

    if conta["saldo"] - valor < limite:
        raise ValueError("Limite de saldo excedido!")

    conta["saldo"] -= valor
    return conta


def transferencia(origem, destino, valor):
    valor = float(valor)

    if valor <= 0:
        raise ValueError("Valor deve ser maior que zero!")

    if str(origem) == str(destino):
        raise ValueError("As contas devem ser diferentes!")

    conta_origem = consultar_conta(origem)
    conta_destino = consultar_conta(destino)

    debito(origem, valor)
    conta_destino["saldo"] += valor

    if conta_destino["tipo"] == "bonus":
        conta_destino["pontos"] += int(valor // 150)

    return {
        "origem": conta_origem,
        "destino": conta_destino
    }


def render_juros(taxa):
    taxa = float(taxa)

    if taxa < 0:
        raise ValueError("Taxa invalida!")

    poupancas = []

    for conta in contas:
        if conta["tipo"] == "poupanca":
            conta["saldo"] += conta["saldo"] * taxa / 100
            poupancas.append(conta)

    return poupancas