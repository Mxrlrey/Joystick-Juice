FROM python:3.13-slim

# Variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8

WORKDIR /app

# Instala dependências do sistema para PostgreSQL
RUN apt-get update && \
    apt-get install -y gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Copia APENAS os requirements primeiro para melhor cache
COPY ./app/requirements.txt ./

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copia APENAS o código do Django (pasta app)
COPY ./app /app

EXPOSE 8000

CMD ["gunicorn", "joystickjuice.wsgi:application", "--bind", "0.0.0.0:8000"]