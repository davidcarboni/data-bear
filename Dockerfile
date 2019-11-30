FROM python:alpine

# Git and dependencies for psycopg2
#RUN apk update && apk add git postgresql-dev gcc python3-dev musl-dev

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

# Dockerignore filters out files that aren't needed
COPY . .

RUN mkdir data && chown -R 1000 data
USER 1000

# This is isn't recommended, but it's enough to run a low-traffic wiki
# NB Flask defaults to looking for app.py
#ENTRYPOINT flask run --host=0.0.0.0
ENTRYPOINT python app.py
