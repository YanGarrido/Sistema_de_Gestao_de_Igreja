from flask import Blueprint, render_template, request, redirect, make_response, flash, session
from models.membros import Membro
from flask_login import login_required, login_user, logout_user, current_user
from validation.validation_utils import validate_login_data
from configs.extensions import login_manager
from datetime import datetime
from models.ministerio import Ministerio
from models.eventos import Evento
from models.reunioes import Reuniao
membros_router = Blueprint("membros_router", __name__, template_folder="templates")

# Rota para listar todos os membros
@membros_router.get("/")
@login_required
def render_index():
    membro_name = current_user.nome
    ministerios = Ministerio.query.all()
    eventos = Evento.query.all()

    membro = Membro.query.get(current_user.id_membro)
    
    if membro.ministerios:
        id_ministerio = membro.ministerios[0].id_ministerio
        reunioes = Reuniao.query.filter_by(id_ministerio=id_ministerio).all()
    else:
        reunioes = []  # Caso o membro não tenha ministério associado
    return render_template("MENU.HTML", membro_name=membro_name, ministerios=ministerios, eventos=eventos, reunioes=reunioes)

@membros_router.get("/login")
def index():
    return render_template("login.html")

@membros_router.get("/register")
def render_register():
    return render_template("cadastroNOVO.html")

@membros_router.post("/register")
def register():
    print("Formulário recebido!")
    nome = request.form["nome"]
    email = request.form["email"]
    telefone = request.form["telefone"]
    endereco = request.form["endereco"]
    senha = request.form["senha"]
    confirma_senha = request.form["confirmarsenha"]
    datadenascimento = request.form["datadenascimento"]
    data_entrada = datetime.now()
    
    if senha == confirma_senha:
        exist_user = Membro.find_user_by_email(email=email)
        if exist_user == None:
            newUser = Membro(nome, email, telefone, endereco, datadenascimento, data_entrada, senha)
            newUser.set_password(senha)
            newUser.create_user()
            return make_response(redirect("/login"),302)
        return make_response("<h1>Erro 400 - campos invalidos</h1>",400)
    else:
        return make_response("<h1>Senha não confirmada</h1>",400)

@membros_router.post("/login")
def login():
    # Obtém os dados do formulário
    data = {
        'usuario': request.form.get("email"),  # assumindo que email é o campo usado para login
        'senha': request.form.get("senha")
    }

    # Chama a função de validação para verificar os dados de login
    is_valid, error_message = validate_login_data(data)
    if not is_valid:
        flash(error_message, "Danger!")
        return redirect("/login")

    membro = Membro.query.filter_by(email=data['usuario']).first()
    if membro is not None and membro.check_password(data['senha']):
        login_user(membro, remember=True)
        return redirect("/")

    flash("Email ou senha inválidos", "Danger!")
    return redirect("/login")

@membros_router.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")

@membros_router.get("/menu")
def render_menu():
    return render_template("MENU.HTML")





