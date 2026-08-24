from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from app.database.connection import get_db_connection

auth_bp = Blueprint('auth', __name__)

# Rota raiz exibe o login
@auth_bp.route('/', methods=['GET'])
def pagina_login():
    return render_template('login.html')

# Adicionamos 'GET' aqui para que o clique em /login funcione via link
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    # Se o usuário acessou via link (clicou em Sair), mostra a tela de login
    if request.method == 'GET':
        return render_template('login.html')

    # Se enviou os dados via formulário ou fetch (POST), faz a validação
    if request.is_json:
        data = request.get_json()
        email = data.get('email')
        senha = data.get('senha')
        is_api = True
    else:
        email = request.form.get('email')
        senha = request.form.get('senha')
        is_api = False

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE email = ?', (email,))
    usuario = cursor.fetchone()
    conn.close()

    if usuario and usuario['senha_hash'] == senha:
        if is_api:
            return jsonify({"success": True, "message": "Login realizado com sucesso!"}), 200
        else:
            return redirect(url_for('dashboard.dashboard_home'))
    
    if is_api:
        return jsonify({"success": False, "message": "Credenciais inválidas."}), 401
    else:
        return "Credenciais inválidas. Volte e tente novamente.", 401