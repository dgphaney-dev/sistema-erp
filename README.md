# 🏗️ ERP - Gestão de Materiais de Construção

Sistema ERP completo e modularizado para controle de estoque, cadastro de produtos, gestão de fornecedores e controle de acesso de funcionários em lojas de materiais de construção.

---

## 🛠️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23F7DF1E.svg?style=for-the-badge&logo=javascript&logoColor=black)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

---

## 📁 Estrutura do Projeto

A arquitetura foi organizada de forma modular para facilitar a manutenção e escalabilidade do código:

* `app/database/` - Conexão e scripts de migração do banco de dados.
* `app/errors/` - Tratamento global de exceções e respostas padronizadas de erro.
* `app/models/` - Modelagem de dados com SQLAlchemy (Usuários, Produtos, Estoque, Fornecedores).
* `app/routes/` - Endpoints e rotas divididos por módulo da aplicação.
* `app/static/` - Arquivos de estilo CSS e rotinas JavaScript isolados por tela.
* `app/templates/` - Interface do usuário construída com Jinja2 e HTML5.

---

## 🚀 Como Rodar o Projeto

### 1. Clonar o repositório
```bash
git clone [https://github.com/seu-usuario/erp_construcao.git](https://github.com/seu-usuario/erp_construcao.git)
cd erp_construcao