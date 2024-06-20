from flask import Flask, render_template
from validate_docbr import CPF, CNPJ

app = Flask("Minha App") # nome da minha aplicação/projeto - pode ser qualquer coisa
cpf = CPF()
cnpj = CNPJ()
# página do flask: rota + função

# /home page - página inicial
@app.route("/")
def home():
    return render_template("home.html")

# /contato - página de contato
@app.route("/contato")
def cont():
    return render_template("contato.html")

# /produtos - página de produtos
@app.route("/produtos")
def produtos():
    lista_produtos = [
        {"nome": "Percy Jackson", "descricao":"Mata a sede", "imagem": "https://www.intrinseca.com.br/upload/livros/ladrao-de-raios_243x349.jpg"},
        {"nome": "O ultimo demonio a morrer", "descricao":"Suja a mão", "imagem": "https://intrinseca.com.br/wp-content/uploads/2024/05/oultimodemonioamorrer-g.jpg"},
        {"nome": "Os heróris do Olimpo", "descricao":"Bom", "imagem": "https://intrinseca.com.br/wp-content/uploads/2023/05/BoxOsHeroisdoOlimpo-G.jpg"}
    ]
    return render_template("produtos.html", produtos=lista_produtos)

# /produtos - página de produtos
@app.route("/servicos")
def service():
    return "<h1>Nossos Serviços<h1>"

# /produtos - página de produtos
@app.route("/gerar-cpf")
def gcpf():
    envio = cpf.generate(True)
    return render_template("cpf.html", cpf =envio)
# /produtos - página de produtos
@app.route("/gerar-cnpj")
def gcnpj():
    envio = cnpj.generate(True)
    return render_template("cnpj.html", cnpj =envio)
app.run()
@app.route("/termo-de-uso")
def trmu():
    return render_template("termo.html")
@app.route("/politica-de-privacidade")
def plpv():
    return render_template("politica.html")
@app.route("/utilizacao")
def utlz():
    return render_template("utilizacao.html")