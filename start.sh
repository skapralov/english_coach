#!/bin/bash

set -e

echo "Waiting for postgres..."
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 0.1
done
echo "PostgreSQL started"

export APP_MODULE=${APP_MODULE:-'main:apps'}
export GUNICORN_CONF=${GUNICORN_CONF:-'/gunicorn_conf.py'}
export WORKER_CLASS=${WORKER_CLASS:-'uvicorn.workers.UvicornWorker'}

exec gunicorn -k $WORKER_CLASS -c $GUNICORN_CONF $APP_MODULE
