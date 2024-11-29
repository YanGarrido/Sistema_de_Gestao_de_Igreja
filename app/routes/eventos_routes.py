from flask import Blueprint, request, render_template
from flask_login import login_required
from models.eventos import Evento
from configs.extensions import db
from flask import flash, redirect, url_for

eventos_router = Blueprint("eventos_router", __name__, template_folder="templates")

# Rota para listar todos os eventos
@eventos_router.get("/eventos")
@login_required
def listar_eventos():
    # Obtendo ministérios do banco de dados
    eventos = Evento.query.all() 
    
    # Renderizando o template correto
    return render_template("evento_lista.html", eventos=eventos)

@eventos_router.get("/eventos/cadastro")
@login_required
def entrar_cadastro():
    return render_template('eventosNOVO.html')

@eventos_router.post("/eventos/cadastro")
@login_required
def cadastrar_evento():
    try:
        # Coleta os dados enviados pelo formulário
        nome = request.form.get("nome")
        descricao = request.form.get("descricao")
        data_inicio = request.form.get("data_inicio")
        data_fim = request.form.get("data_fim")
        id_local = request.form.get("id_local")
        tipo = request.form.get("tipo")
        numero_participantes = request.form.get("numero_participantes")

        # Cria o objeto Evento
        novo_evento = Evento(
            nome = nome,
            descricao = descricao,
            tipo = tipo,
            data_inicio =data_inicio,
            data_fim = data_fim,
            id_local = id_local,
            numero_participantes = numero_participantes
        )

        # Adiciona e confirma a transação no banco de dados
        db.session.add(novo_evento)
        db.session.commit()

        return redirect(url_for('eventos_router.listar_eventos'))
    except Exception as e:
        db.session.rollback()  # Reverte caso haja erro
        return f"Erro ao cadastrar evento: {str(e)}", 400
