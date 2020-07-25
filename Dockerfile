FROM python:3-slim

MAINTAINER skapralov

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PROJECT_PATH /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

COPY . ${PROJECT_PATH}
WORKDIR ${PROJECT_PATH}

RUN pipenv install --skip-lock --system --deploy
