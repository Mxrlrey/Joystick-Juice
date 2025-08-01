FROM python:3.13.5-slim

# Evita buffering no console (importante para logs no Docker)
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instala dependências do sistema necessárias para compilar o mysqlclient
RUN apt-get update && apt-get install -y gcc default-libmysqlclient-dev pkg-config

# Copia o requirements e instala
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copia o restante do código do projeto
COPY . .

# Expõe a porta do Django
EXPOSE 8000

# Comando padrão ao iniciar o container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
