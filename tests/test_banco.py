
import pytest

from backend import banco


@pytest.fixture(autouse=True)
def limpar_contas():
    banco.contas.clear()
    yield
    banco.contas.clear()


def test_cadastrar_simples():
    conta = banco.cadastrar_conta("123", "simples", 500)
    assert conta["saldo"] == 500
    assert conta["tipo"] == "simples"


def test_cadastrar_bonus():
    conta = banco.cadastrar_conta("123", "bonus")
    assert conta["saldo"] == 0
    assert conta["pontos"] == 10


def test_cadastrar_poupanca():
    conta = banco.cadastrar_conta("123", "poupanca", 1000)
    assert conta["saldo"] == 1000
    assert conta["tipo"] == "poupanca"


@pytest.mark.parametrize("tipo", ["simples", "bonus", "poupanca"])
def test_consultar_conta(tipo):
    banco.cadastrar_conta("123", tipo, 0)
    conta = banco.consultar_conta("123")
    assert conta["numero"] == "123"
    assert conta["tipo"] == tipo


def test_consultar_saldo():
    banco.cadastrar_conta("123", "simples", 500)
    assert banco.consultar_saldo("123") == 500


def test_credito():
    banco.cadastrar_conta("123", "simples", 500)
    banco.credito("123", 200)
    assert banco.consultar_saldo("123") == 700


def test_credito_negativo():
    banco.cadastrar_conta("123", "simples", 500)

    with pytest.raises(ValueError):
        banco.credito("123", -100)

    assert banco.consultar_saldo("123") == 500


def test_credito_bonus():
    banco.cadastrar_conta("123", "bonus")
    banco.credito("123", 200)
    assert banco.consultar_conta("123")["pontos"] == 12


def test_debito():
    banco.cadastrar_conta("123", "simples", 500)
    banco.debito("123", 100)
    assert banco.consultar_saldo("123") == 400


def test_debito_negativo():
    banco.cadastrar_conta("123", "simples", 500)

    with pytest.raises(ValueError):
        banco.debito("123", -100)

    assert banco.consultar_saldo("123") == 500


def test_debito_sem_saldo():
    banco.cadastrar_conta("123", "poupanca", 100)

    with pytest.raises(ValueError):
        banco.debito("123", 200)

    assert banco.consultar_saldo("123") == 100


def test_limite_negativo():
    banco.cadastrar_conta("123", "simples", 0)
    banco.debito("123", 1000)

    assert banco.consultar_saldo("123") == -1000

    with pytest.raises(ValueError):
        banco.debito("123", 1)


def test_transferencia():
    banco.cadastrar_conta("123", "simples", 500)
    banco.cadastrar_conta("456", "simples", 0)

    banco.transferencia("123", "456", 200)

    assert banco.consultar_saldo("123") == 300
    assert banco.consultar_saldo("456") == 200


def test_transferencia_negativa():
    banco.cadastrar_conta("123", "simples", 500)
    banco.cadastrar_conta("456", "simples", 0)

    with pytest.raises(ValueError):
        banco.transferencia("123", "456", -100)

    assert banco.consultar_saldo("123") == 500
    assert banco.consultar_saldo("456") == 0


def test_transferencia_sem_saldo():
    banco.cadastrar_conta("123", "poupanca", 100)
    banco.cadastrar_conta("456", "simples", 0)

    with pytest.raises(ValueError):
        banco.transferencia("123", "456", 200)

    assert banco.consultar_saldo("123") == 100
    assert banco.consultar_saldo("456") == 0


def test_transferencia_bonus():
    banco.cadastrar_conta("123", "simples", 500)
    banco.cadastrar_conta("456", "bonus")

    banco.transferencia("123", "456", 150)

    assert banco.consultar_conta("456")["pontos"] == 11
    assert banco.consultar_saldo("456") == 150


def test_rendimento_poupancas():
    banco.cadastrar_conta("111", "poupanca", 1000)
    banco.cadastrar_conta("222", "poupanca", 2000)
    banco.cadastrar_conta("333", "simples", 500)

    banco.render_juros(10)

    assert banco.consultar_saldo("111") == 1100
    assert banco.consultar_saldo("222") == 2200
    assert banco.consultar_saldo("333") == 500


@pytest.mark.parametrize("valor", ["abc", "nan", "inf", "-inf"])
def test_valor_invalido(valor):
    banco.cadastrar_conta("123", "simples", 500)

    with pytest.raises(ValueError):
        banco.credito("123", valor)

    assert banco.consultar_saldo("123") == 500


def test_conta_duplicada():
    banco.cadastrar_conta("123", "simples", 500)

    with pytest.raises(ValueError):
        banco.cadastrar_conta("123", "simples", 500)


def test_taxa_negativa():
    banco.cadastrar_conta("123", "poupanca", 1000)

    with pytest.raises(ValueError):
        banco.render_juros(-10)

    assert banco.consultar_saldo("123") == 1000
