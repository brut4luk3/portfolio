# Usa uma imagem oficial do Python como base
FROM python:3.9

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório atual (/app) no contêiner
COPY requirements.txt .

# Instala as dependências
RUN pip install -r requirements.txt

# Copia todos os arquivos do diretório atual do projeto para o diretório /app no contêiner
COPY . .

# Coleta os arquivos estáticos
RUN python manage.py collectstatic --no-input

# Executa as migrações
RUN python manage.py migrate

# O comando para rodar a aplicação
CMD ["gunicorn", "-b", "0.0.0.0:8000", "portfolio.wsgi:application"]