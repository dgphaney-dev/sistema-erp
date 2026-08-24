import sqlite3
import os

# Define o caminho do arquivo do banco de dados na raiz do projeto
DB_PATH = os.path.join(os.path.dirname(__file__), '../../erp.db')

def get_db_connection():
    """Retorna uma conexão com o banco SQLite"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Permite acessar os campos pelo nome da coluna
    return conn

def init_db(app=None):
    """Cria fisicamente o arquivo do banco e todas as tabelas do ERP com SQL"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. Tabela de usuários
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_completo TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha_hash TEXT NOT NULL,
            cargo TEXT NOT NULL,
            status TEXT DEFAULT 'Ativo',
            criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # 2. Tabela de Fornecedores
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS fornecedores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cnpj TEXT UNIQUE NOT NULL,
            telefone TEXT,
            email TEXT,
            criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # 3. Tabela de Produtos (Materiais de Construção)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            categoria TEXT,
            preco_custo REAL NOT NULL,
            preco_venda REAL NOT NULL,
            criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # 4. Tabela de Estoque
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS estoque (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto_id INTEGER NOT NULL,
            quantidade INTEGER NOT NULL DEFAULT 0,
            localizacao TEXT,
            atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (produto_id) REFERENCES produtos (id)
        )
    ''')

    # --- INSERIR USUÁRIO ADMINISTRADOR PADRÃO (SE NÃO EXISTIR) ---
    cursor.execute('SELECT id FROM usuarios WHERE email = ?', ('admin@erp.com',))
    admin_existe = cursor.fetchone()

    if not admin_existe:
        cursor.execute('''
            INSERT INTO usuarios (nome_completo, email, senha_hash, cargo) 
            VALUES (?, ?, ?, ?)
        ''', ('Administrador ERP', 'admin@erp.com', '123', 'Administrador'))
        print("Usuário administrador padrão criado com sucesso!")

    conn.commit()
    conn.close()
    print("Banco de dados 'erp.db' e todas as tabelas criadas com sucesso via SQL!")

# Se quiser rodar direto este arquivo para testar a criação do banco
if __name__ == '__main__':
    init_db()