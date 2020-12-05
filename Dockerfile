FROM python:3.9-slim

MAINTAINER skapralov

RUN apt-get update && apt-get install -y --no-install-recommends \
    netcat \
    && rm -rf /var/lib/apt/lists/*

COPY gunicorn_conf.py start.sh start-reload.sh Pipfile app ./
RUN chmod +x start.sh && chmod +x start-reload.sh

RUN pip install --upgrade pip
RUN pip install pipenv==2018.11.26
RUN pipenv install --skip-lock --system --deploy

ENTRYPOINT /start-reload.sh
