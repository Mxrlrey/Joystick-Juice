# Guia de Desenvolvimento Django com Docker e PostgreSQL

## 1. Pré-requisitos
- Python 3.x instalado
- Docker e Docker Compose instalados
- Git instalado

## 2. Estrutura Recomendada do Projeto
```
Joystick-Juice/
├── app/
│   ├── manage.py
│   ├── joystickjuice/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── ...
│   ├── requirements.txt
│   └── Joy/           # Seu app Django
│       ├── models.py
│       ├── migrations/
│       └── ...
├── Dockerfile
├── docker-compose.yml
├── README.md
└── venv/              # Ambiente virtual (opcional, para desenvolvimento local)
```

## 3. Remover arquivos desnecessários
- Pode remover:
  - `db/migrations/` (usado apenas para Flyway)
  - `flyway.conf` (usado apenas para Flyway)
  - Qualquer referência ao Flyway no `docker-compose.yml`

## 4. Configuração do banco de dados no Django
No arquivo `app/joystickjuice/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('DB_HOST', 'db'),
        'PORT': '5432',
    }
}
```

## 5. Passo a passo para desenvolvimento

### 5.1. Subir o banco de dados com Docker
Na raiz do projeto:
```bash
docker-compose up db
```

### 5.2. Ativar ambiente virtual (opcional, recomendado para desenvolvimento local)
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r app/requirements.txt
```

### 5.3. Criar e registrar apps Django
```bash
cd app
python3 manage.py startapp Joy
```
Adicione 'Joy' em `INSTALLED_APPS` no `settings.py`.

### 5.4. Criar modelos e migrações
Edite `app/Joy/models.py` conforme necessário.
Depois rode:
```bash
python3 manage.py makemigrations Joy
python3 manage.py migrate
```

### 5.5. Rodar o servidor Django
```bash
python3 manage.py runserver
```

## 6. Desenvolvimento em equipe
- Todos devem usar o mesmo Docker Compose para subir o banco.
- Compartilhe o código via Git.
- Cada desenvolvedor pode rodar o Django localmente, conectando ao banco do Docker.

## 7. Dicas finais
- Não é necessário Flyway nem pasta `db/migrations` se usar apenas Django.
- Mantenha o ambiente virtual fora da pasta `app/` para facilitar o gerenciamento.
- Use variáveis de ambiente para senhas e configurações sensíveis.

---

Se precisar de exemplos de modelos, views ou configurações, peça ajuda!
