from flask import Flask
from validate_docbr import CPF, CNPJ

app = Flask("Minha App") # nome da minha aplicação/projeto - pode ser qualquer coisa
cpf = CPF()
cnpj = CNPJ()
# página do flask: rota + função

# /home page - página inicial
@app.route("/")
def home():
    return "<h1>Home Page<h1>"

# /contato - página de contato
@app.route("/contato")
def cont():
    return "<h1>Contato<h1>"

# /produtos - página de produtos
@app.route("/produtos")
def prods():
    return "<h1>Produtos<h1>"

# /produtos - página de produtos
@app.route("/servicos")
def service():
    return "<h1>Nossos Serviços<h1>"

# /produtos - página de produtos
@app.route("/gerar-cpf")
def gcpf():
    return cpf.generate(True)
# /produtos - página de produtos
@app.route("/gerar-cnpj")
def gcnpj():
    return cnpj.generate(True)
app.run()