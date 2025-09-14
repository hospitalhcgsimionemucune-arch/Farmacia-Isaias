from flask import Flask, render_template, session, redirect, url_for, request
from models import catalogo

app = Flask(__name__)
app.secret_key = "isaia-secret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/medicamentos")
def lista_medicamentos():
    return render_template("medicamentos.html", catalogo=catalogo)

@app.route("/buscar", methods=["GET"])
def buscar():
    termo = request.args.get("q", "").lower()
    resultados = [m for m in catalogo if termo in m.nome.lower()]
    return render_template("medicamentos.html", catalogo=resultados)

@app.route("/adicionar/<int:id>")
def adicionar(id):
    if "carrinho" not in session:
        session["carrinho"] = []
    session["carrinho"].append(id)
    return redirect(url_for("lista_medicamentos"))

@app.route("/carrinho")
def carrinho():
    itens = [m for m in catalogo if m.id in session.get("carrinho", [])]
    total = sum(m.preco for m in itens)
    return render_template("carrinho.html", itens=itens, total=total)

@app.route("/confirmacao", methods=["POST"])
def confirmacao():
    nome = request.form["nome"]
    itens = [m for m in catalogo if m.id in session.get("carrinho", [])]
    total = sum(m.preco for m in itens)
    for item in itens:
        item.estoque -= 1
    session.clear()
    return render_template("pedido_finalizado.html", nome=nome, itens=itens, total=total)

if __name__ == "__main__":
    app.run(debug=True)

