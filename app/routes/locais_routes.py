from flask import Blueprint, request, render_template
from flask_login import login_required
from models.locais import Local
from configs.extensions import db

locais_router = Blueprint("locais_router", __name__, template_folder="templates")

# Rota para listar todos os locais
@locais_router.get("/locais")
@login_required
def listar_locais():
    # Consulta todos os eventos no banco de dados
    locais = Local.query.all()
    return render_template("lista_locais.html", locais=locais)

@locais_router.get("/locais")
@login_required
def abrir_locais():
    return render_template("locais.html")

# Rota para criar um novo local
@locais_router.post("/locais")
@login_required
def create_local():
    nome=request.form.get("nome")
    endereco=request.form.get("endereco")
    capacidade=request.form.get("capacidade")
    descricao=request.form.get("descricao")

    novo_local = Local(
        nome=nome,
        endereco=endereco,
        capacidade=capacidade,
        descricao=descricao,
        
    )
    
    db.session.add(novo_local)
    db.session.commit()
