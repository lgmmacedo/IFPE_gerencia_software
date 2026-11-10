
from backend.banco import (
    cadastrar_conta,
    consultar_saldo,
    credito,
    debito,
    transferencia
)

while True:
    print("\n===== SISTEMA BANCÁRIO =====")
    print("1 - Cadastrar conta")
    print("2 - Consultar saldo")
    print("3 - Crédito")
    print("4 - Débito")
    print("5 - Transferência")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_conta()
    elif opcao == "2":
        consultar_saldo()
    elif opcao == "3":
        credito()
    elif opcao == "4":
        debito()
    elif opcao == "5":
        transferencia()
    elif opcao == "6":
        print("Sistema encerrado!")
        break
    else:
        print("Opção inválida!")
