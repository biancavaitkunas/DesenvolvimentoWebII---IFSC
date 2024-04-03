from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "<h1>Hello Flask!!!</h1>"

@app.route("/nome/<nome>")
def nome(nome):
    return f"<h1>Hello {nome}!</h1>"

@app.route("/")
def home():
    return render_template("home.html", conteudo="Hello Jinja!", x=4)

if __name__ == "__main__":
    app.run(debug=True)