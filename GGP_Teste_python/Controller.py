from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, json, session
import psycopg2
from DB import Inserir, Seleciona
import os

app = Flask(__name__)
app.secret_key = "GGp"

insert = Inserir()
select = Seleciona()

class Produtos():
    def __init__(self, codigo, descricao, valor, quantidade):
        self.codigo = codigo
        self.descricao = descricao
        self.valor = valor
        self.quantidade = quantidade

@app.route('/')
def index():
    objeto_produtos = []
    lista_produtos = []
    start = select.start()
    lista_produtos = select.selec_produtos(start)

    for dado in lista_produtos:
        tabela_produtos = Produtos(dado[0], dado[1], dado[2], dado[3])
        print(tabela_produtos)
        objeto_produtos.append(tabela_produtos)


    return render_template('index.html', lista_produtos=objeto_produtos)

@app.route('/cad_produto')
def cad_produto():
    return render_template('cadastra.html')

@app.route('/cadastro', methods = ['POST',])
def cadastra():
    descricao = request.form['descricao']
    valor = request.form['valor']
    quantidade = request.form['quantidade']

    start = insert.start()
    insert.inseri_dados_produtos(descricao, valor, quantidade, start)
    flash('Cadastro realizado com sucesso')
    
    return redirect(url_for('index'))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='127.0.0.1', port=port, debug=True)