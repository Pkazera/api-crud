# API CRUD - Produtos

API RESTful com FastAPI + MySQL + JWT, hospedada na AWS EC2.

## Tecnologias
- **Python** + FastAPI
- **MySQL** (banco de dados)
- **JWT** (autenticação)
- **SQLAlchemy** (ORM)

## Como rodar localmente

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

### 2. Crie e ative o ambiente virtual
```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure o `.env`
```bash
cp .env.example .env
# Edite o .env com suas credenciais MySQL
```

### 5. Crie o banco no MySQL
```sql
CREATE DATABASE crud_db;
```

### 6. Suba a API
```bash
uvicorn main:app --reload
```

Acesse: http://localhost:8000/docs

---

## Rotas

| Método | Rota            | Auth | Descrição         |
|--------|-----------------|------|-------------------|
| POST   | /auth/login     | ❌   | Gera token JWT    |
| GET    | /produtos       | ❌   | Lista produtos    |
| GET    | /produtos/{id}  | ❌   | Busca um produto  |
| POST   | /produtos       | ✅   | Cria produto      |
| PUT    | /produtos/{id}  | ✅   | Atualiza produto  |
| DELETE | /produtos/{id}  | ✅   | Remove produto    |

## Como autenticar

1. Faça `POST /auth/login` com `{"username": "admin", "password": "admin123"}`
2. Copie o `access_token` retornado
3. Nas rotas protegidas, envie o header: `Authorization: Bearer <token>`
