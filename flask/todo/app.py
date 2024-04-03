from flask import Flask
from flask import Flask, render_template
from flask import Flask, request
from flask import Flask, redirect, url_for, flash
from config import db
from models import User

app = Flask(__name__)

DB_NAME = "database.db"

app.config['SECRET_KEY'] = 'IFSC@TUB'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)

with app.app_context():
    db.create_all()

### Rotas ###

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha1 = request.form.get('senha1')
        senha2 = request.form.get('senha2')
        login = request.form.get('login')

        user = User(name = nome, email = email, login = login, password = senha1)
        db.session.add(user)
        db.session.commit()
        flash('Conta criada com sucesso!', category='success')
        return redirect(url_for('login'))

    return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug=True)