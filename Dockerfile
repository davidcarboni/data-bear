FROM python:alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

# Dockerignore filters out files that aren't needed
COPY . .

USER 1000

# This is isn't recommended, but it's enough to run a low-traffic api
# NB Flask defaults to looking for app.py
ENTRYPOINT flask run --host=0.0.0.0
