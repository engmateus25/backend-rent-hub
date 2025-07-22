# Defina a imagem base
FROM python:3.10-slim

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie o requirements.txt do diretório raiz para o container
COPY ../requirements.txt /app/requirements.txt

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copie o restante do código-fonte
COPY . /app/

# Exponha a porta que o Uvicorn vai usar
EXPOSE 8000

# Comando para iniciar a aplicação FastAPI
CMD ["python3", "-m", "uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
