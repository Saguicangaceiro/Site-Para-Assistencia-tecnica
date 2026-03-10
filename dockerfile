# 1. Usar uma imagem oficial do Python (leve)
FROM python:3.10-slim

# 2. Definir o diretório dentro do container
WORKDIR /app

# 3. Copiar o arquivo de dependências e instalar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar todo o código do site para dentro do container
COPY . .

# 5. Informar que o container usará a porta 5000
EXPOSE 5000

# 6. Comando para iniciar o servidor Flask
CMD ["python", "app.py"]