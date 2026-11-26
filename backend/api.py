
from flask import Flask, request, jsonify
from backend import banco

app = Flask(__name__)


@app.errorhandler(ValueError)
def tratar_erro(erro):
    return jsonify({"erro": str(erro)}), 400


@app.route("/banco/conta/", methods=["POST"])
def cadastrar():
    dados = request.get_json()
    conta = banco.cadastrar_conta(
        dados["numero"],
        dados["tipo"],
        dados.get("saldo_inicial")
    )
    return jsonify(conta), 201


@app.route("/banco/conta/", methods=["GET"])
def consultar():
    numero = request.args.get("numero")
    return jsonify(banco.consultar_conta(numero))


@app.route("/banco/conta/<numero>/saldo", methods=["GET"])
def saldo(numero):
    return jsonify({"saldo": banco.consultar_saldo(numero)})


@app.route("/banco/conta/<numero>/credito", methods=["PUT"])
def credito(numero):
    dados = request.get_json()
    return jsonify(banco.credito(numero, dados["valor"]))


@app.route("/banco/conta/<numero>/debito", methods=["PUT"])
def debito(numero):
    dados = request.get_json()
    return jsonify(banco.debito(numero, dados["valor"]))


@app.route("/banco/conta/transferencia", methods=["PUT"])
def transferencia():
    dados = request.get_json()
    return jsonify(banco.transferencia(
        dados["from"],
        dados["to"],
        dados["amount"]
    ))


@app.route("/banco/conta/rendimento", methods=["PUT"])
def rendimento():
    dados = request.get_json()
    return jsonify(banco.render_juros(
        dados["numero"],
        dados["taxa"]
    ))


if __name__ == "__main__":
    app.run(port=5000)
