from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user
from app import app, db, lm


from app.models.tables import User
from app.models.forms import LoginForm

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash("Logged in.")
            return redirect(url_for("index"))
    else:
        flash("Login inválido.")

    return render_template('login.html', form=form)


@app.route("/teste/<info>")
@app.route("/teste", defaults={"info":None})
def teste(info):   
    return "OK"

@app.route("/logout")
def logout():
    logout_user()
    flash("Loggeg out")
    return redirect(url_for("index"))

# def teste(info):
#  Teste de leitura, qdo acessar um registro pode ver os parametros
#     r = User.query.filter_by(password="1234").all()
#  Updating um registro
#     r.name = "Vanessa"
#     db.session.add(r)
#     db.session.commit()
#     print(r.username, r.name)
#     return "OK"
#  Deleting um registro
#  db.session.delete(r)
#  db.session.commit()
#  Criação de registro no Banco de Dados
    # i = User("andressaaa", "1234", "Andressaaa DAgostini",
    # "dessaaa.dagostini@gmail.com")
    # db.session.add(i)
    # db.session.commit()

# @app.route("/index/<user>")
# @app.route("/", defaults={"user":None})
# def index(user):
#     return render_template('index.html', user=user)

# @app.route("/test/"])
# def test():
#     return "Oi!"

# @app.route("/test", defaults={'name': None})
# @app.route("/test/<name>")
# def test(name):
#     if name:
#         return "Olá, %s!" % name
#     else:
#         return "Olá, usuário!"