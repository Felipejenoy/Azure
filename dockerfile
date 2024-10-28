# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo requirements.txt y lo instala
COPY requirements.txt .

# Instala las dependencias
RUN pip install -r requirements.txt

# Copia el resto de la aplicación
COPY . .

# Expone el puerto en el que la aplicación escucha, si tienes un servidor web
EXPOSE 5000


# Comando para iniciar la aplicación
CMD ["python", "app.py"]
