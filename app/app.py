from flask import Flask
from configs.extensions import db, login_manager
from flask_login import LoginManager

from models.eventos import Evento
from models.locais import Local
from models.membros import Membro
from models.ministerio import Ministerio
from models.reunioes import Reuniao
from models.membros_ministerio import MembroMinisterio

from routes.eventos_routes import eventos_router
from routes.locais_routes import locais_router
from routes.membros_routes import membros_router
from routes.ministerio_routes import ministerios_router
from routes.reunioes_routes import reunioes_router

from dotenv import load_dotenv
from datetime import timedelta
import os


load_dotenv()


def create_app():

    app = Flask(__name__)

    app.register_blueprint(eventos_router)
    app.register_blueprint(locais_router)
    app.register_blueprint(membros_router)
    app.register_blueprint(ministerios_router)
    app.register_blueprint(reunioes_router)

    
    
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET_KEY")
    app.config['REMEMBER_COOKIE_DURATION'] = timedelta(hours= 1)
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=1)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "membros_router.login"
    
    @login_manager.user_loader
    def load_user(user_id):
        return Membro.query.get(int(user_id))
    db.init_app(app)
    


    with app.app_context():
        db.create_all()
    return app


app = create_app()
app.run(debug=True)