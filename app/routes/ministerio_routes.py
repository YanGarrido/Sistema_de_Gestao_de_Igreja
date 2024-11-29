from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_required, current_user 
from models.ministerio import Ministerio
from configs.extensions import db
from sqlalchemy import text
from models.membros import Membro


ministerios_router = Blueprint("ministerio_router", __name__, template_folder="templates")

# Rota para listar todos os ministérios
@ministerios_router.get("/ministerio")
@login_required
def listar_ministerios():
    # Obtendo ministérios do banco de dados
    ministerios = Ministerio.query.all() 
    
    # Renderizando o template correto
    return render_template("lista_ministerio.html", ministerios=ministerios)

@ministerios_router.post("/ministerio/entrar")
@login_required
def entrar_ministerio():
    # Obtendo o ID do ministério do formulário
    ministerio_id = request.form.get("ministerio_id")
    membro = Membro.query.get(current_user.id_membro)  # Obtém o membro atual (usuário logado)
    ministerio = Ministerio.query.get(ministerio_id)  # Obtém o ministério baseado no ID
    
    # Verificando se o membro já está no ministério
    if ministerio not in membro.ministerios:
        membro.ministerios.append(ministerio)  # Adiciona o membro ao ministério
        db.session.commit()
        flash(f'Você entrou no ministério {ministerio.nome}.', 'success')
    else:
        flash(f'Você já está no ministério {ministerio.nome}.', 'warning')

    return redirect(url_for('ministerio_router.listar_ministerios'))  # Redireciona de volta

@ministerios_router.get("/ministerio/cadastro")
@login_required
def entrar_cadastro():
    return render_template('ministerioNOVO.html')


# Rota para criar um novo ministério
@ministerios_router.post("/ministerio/cadastro")
@login_required
def create_ministerio():
    # Usando request.form para pegar os dados do formulário
    nome = request.form.get("nome")
    descricao = request.form.get("descricao")
    lider = request.form.get("lider")
    
    # Criando o novo ministério
    novo_ministerio = Ministerio(
        nome=nome,
        descricao=descricao,
        lider=lider,
    )

    db.session.add(novo_ministerio)
    db.session.commit()

    return redirect(url_for('ministerio_router.listar_ministerios'))


