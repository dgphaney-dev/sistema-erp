import os
from flask import Flask
from app.database.connection import init_db
from app.errors.handlers import register_error_handlers
from app.routes.auth_routes import auth_bp
from app.routes.dashboard_routes import dashboard_bp  # <-- Importa o blueprint do dashboard

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'chave-super-secreta')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa o banco de dados com SQL puro
    init_db(app)
    register_error_handlers(app)

    # Registra as rotas
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)  # <-- Registra o blueprint do dashboard

    return app