# 🔧 API de Gestão

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-em%20desenvolvimento-success)]()

API RESTful completa com autenticação **JWT**, CRUD de usuários e itens, ideal para sistemas de gestão, ERPs leves ou backends de painéis administrativos.

---

## 🔗 Demonstração local

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

---

## 📋 Funcionalidades

- Cadastro e autenticação de usuários (JWT + senha criptografada)
- Login com geração de token de acesso
- Endpoint para obter dados do usuário logado (`/auth/me`)
- CRUD completo de **itens** vinculados ao usuário autenticado
- Banco de dados **SQLite** local (simples de rodar)
- CORS liberado para integração com front-end (React/Next.js)

---

## 🛠 Tecnologias

- **Python 3.11+**
- **FastAPI**
- **Uvicorn**
- **SQLAlchemy**
- **Pydantic**
- **JWT (python-jose)**
- **Passlib (bcrypt)**
- **SQLite**

---

## 📂 Estrutura do Projeto

```bash
api-gestao/
├── app/
│   ├── main.py          # App FastAPI, CORS e inclusão de rotas
│   ├── database.py      # Conexão e sessão com o banco de dados
│   ├── models.py        # Modelos SQLAlchemy (User, Item)
│   ├── schemas.py       # Schemas Pydantic (User, Item, Token)
│   ├── auth.py          # Utilitários de autenticação (JWT, senha)
│   └── routers/
│       ├── users.py     # Rotas de autenticação (register, login, me)
│       └── items.py     # Rotas de itens (CRUD)
├── gestao.db            # Banco SQLite (gerado automaticamente)
├── requirements.txt     # Dependências do projeto
├── .env                 # Configurações sensíveis (SECRET_KEY, DB)
├── .gitignore
└── README.md

⚙️ Como rodar o projeto localmente

1. Clonar o
bash
git clone https://github.com/fabiomendes33/api-gestao.git
cd api-gestao


2. Criar e ativar o ambiente virtual
bash
python -m venv venv
venv\Scripts\activate    # Windows
# source venv/bin/activate  # Linux/Mac

3. Instalar as túnicas
bash
pip install -r requirements.txt

4. Configurar o.env
Crie um arquivo .envna raiz do projeto (se ainda não existir):

texto
SECRET_KEY=chave_super_secreta_fabio_2025
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=sqlite:///./gestao.db

5. Iniciar o servidor
bash
uvicorn app.main:app --reload
Arrogância:http://localhost:8000/docs

ReDoc:http://localhost:8000/redoc

📌 Pontos finais principais
🔐 Autenticação ( /auth)
Método	Rota	Descrição
PUBLICAR	/auth/register	Cria um novo usuário
PUBLICAR	/auth/login	Login e token JWT
PEGAR	/auth/me	Dados do usuário logado

Exemplo de register:

json
{
  "name": "Fabio Mendes",
  "email": "fabio@technote.com.br",
  "password": "senha123"
}

Exemplo de login(form-data no Swagger):

username:fabio@technote.com.br

password:senha123

Após o login, copie access_tokene clique em Autorizar no Swagger para testar rotas protegidas.

📦 Itens ( /items)
Todos os endpoints de itens desabilitam autenticação (Bearer Token JWT).

Método	Rota	Descrição
PUBLICAR	/items/	Cria um novo item
PEGAR	/items/	Lista de itens do usuário
PEGAR	/items/{id}	Detalhes de um item
EXCLUIR	/items/{id}	Remover um item do usuário

Exemplo de POST /items/:

json
{
  "title": "Notebook para manutenção",
  "description": "Equipamento entrando na fila de análise técnica"
}

☁️ Implantar
Não implantar ferrovia
Crie uma conta em: https://railway.app

Clique em Novo Projeto → Implantar do GitHub

Selecione oapi-gestao

Variáveis ​​Nas , configurar:

SECRET_KEY=chave_super_secreta_fabio_2025
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=sqlite:///./gestao.db
PORT=8000


Em Serviço → Configurações → Iniciar Comando , use:

bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT

Salve e aguarde o desdobramento. Uma URL será pública algo como:

https://api-gestao-production.up.railway.app

Sem Swagger remoto:
https://api-gestao-production.up.railway.app/docs

Implantar sem renderização
Crie conta em: https://render.com

Clique em Novo → Serviço Web

Conecte-se com o GitHub e escolhaapi-gestao

Configurar:

Ambiente :Python

Comando de compilação :

pip install -r requirements.txt

Comando de inicialização :

bash
uvicorn app.main:app --host 0.0.0.0 --port 8000

Em Variáveis ​​de Ambiente , adicione:

texto
SECRET_KEY=chave_super_secreta_fabio_2025
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=sqlite:///./gestao.db


Implantar → Renderizar gera uma URL semelhante a:
https://api-gestao.onrender.com

Arrogância:
https://api-gestao.onrender.com/docs

🚀 Possíveis usos
Backend para painel administrativo em Next.js / React

API para sistemas de tarefas, estoque ou tarefas

Base para estudos de autenticação com JWT + FastAPI

 Licença
Projeto desenvolvido porFabio Mendes – Desenvolvedor Full stack  de Sistemas e TI.
Sinta-se à vontade para usar como base em seus próprios projetos.

```
