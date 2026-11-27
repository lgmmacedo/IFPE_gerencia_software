
import requests

URL = "http://127.0.0.1:5000/banco/conta/"


def enviar(metodo, caminho="", dados=None, parametros=None):
    try:
        resposta = requests.request(
            metodo,
            URL + caminho,
            json=dados,
            params=parametros,
            timeout=5
        )

        resultado = resposta.json()

        if resposta.ok:
            print("Operacao realizada com sucesso!")
            print(resultado)
        else:
            print("Erro:", resultado.get("erro", resultado))

    except requests.RequestException:
        print("Erro de comunicacao com a API.")


while True:
    print("\n===== SISTEMA BANCARIO =====")
    print("1 - Cadastrar conta")
    print("2 - Consultar saldo")
    print("3 - Credito")
    print("4 - Debito")
    print("5 - Transferencia")
    print("6 - Render juros")
    print("7 - Consultar conta")
    print("8 - Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        numero = input("Numero da conta: ")
        tipo = input("Tipo (simples/bonus/poupanca): ")

        dados = {
            "numero": numero,
            "tipo": tipo
        }

        if tipo in ("simples", "poupanca"):
            dados["saldo_inicial"] = input(
                "Saldo inicial: "
            ).replace(",", ".")

        enviar("POST", dados=dados)

    elif opcao == "2":
        numero = input("Numero da conta: ")
        enviar("GET", f"{numero}/saldo")

    elif opcao == "3":
        numero = input("Numero da conta: ")
        valor = input("Valor: ").replace(",", ".")
        enviar("PUT", f"{numero}/credito", {"valor": valor})

    elif opcao == "4":
        numero = input("Numero da conta: ")
        valor = input("Valor: ").replace(",", ".")
        enviar("PUT", f"{numero}/debito", {"valor": valor})

    elif opcao == "5":
        origem = input("Conta de origem: ")
        destino = input("Conta de destino: ")
        valor = input("Valor: ").replace(",", ".")

        enviar("PUT", "transferencia", {
            "from": origem,
            "to": destino,
            "amount": valor
        })

    elif opcao == "6":
        taxa = input("Taxa de juros: ").replace(",", ".")

        enviar("PUT", "rendimento", {
            "taxa": taxa
        })

    elif opcao == "7":
        numero = input("Numero da conta: ")
        enviar("GET", parametros={"numero": numero})

    elif opcao == "8":
        print("Sistema encerrado!")
        break

    else:
        print("Opcao invalida!")
