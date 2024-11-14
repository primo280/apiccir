# Utilise une image Python officielle comme base
FROM python:3.8-slim

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie les fichiers de l'application dans le conteneur
COPY . /app

# Installe les dépendances nécessaires
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose le port 8000 (pour un serveur Django par exemple)
EXPOSE 8000

# Commande pour lancer l'application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
