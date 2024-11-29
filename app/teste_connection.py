from app import app, db
from models.membros import Membro

# Testando a conexão com o banco de dados
with app.app_context():  # Garante que o contexto da aplicação Flask está ativo
    membro = Membro.query.all()
    print(membro)


    membros = Membro.query.all()  # Lista todos os membros
    for membro in membros:
        print(membro.nome, membro.email) 
