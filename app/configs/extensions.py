from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


login_manager = LoginManager()
login_manager.login_view = "membros_router.login"
db = SQLAlchemy()