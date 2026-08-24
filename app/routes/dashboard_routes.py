from flask import Blueprint, render_template
from app.database.connection import get_db_connection

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
def dashboard_home():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Puxa o total de produtos cadastrados
    cursor.execute('SELECT COUNT(*) as total FROM produtos')
    total_produtos = cursor.fetchone()['total']

    # Puxa o total de fornecedores cadastrados
    cursor.execute('SELECT COUNT(*) as total FROM fornecedores')
    total_fornecedores = cursor.fetchone()['total']

    # Puxa a quantidade somada no estoque (ou verifica o status)
    cursor.execute('SELECT SUM(quantidade) as total FROM estoque')
    estoque_res = cursor.fetchone()
    total_estoque = estoque_res['total'] if estoque_res['total'] is not None else 0

    conn.close()

    # Define o status do estoque com base na quantidade total
    status_estoque = "Estável" if total_estoque > 0 else "Crítico / Vazio"

    return render_template(
        'dashboard.html', 
        produtos=total_produtos, 
        fornecedores=total_fornecedores,
        status_estoque=status_estoque
    )