from flask import Flask
from flask import Flask, render_template
from config import db

app = Flask(__name__)

DB_NAME = "database.db"

##from models import User

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

@app.route("/signup")
def signup():
    return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug=True)