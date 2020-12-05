#!/bin/bash

set -e

echo 'Waiting for postgres...'
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 0.1
done
echo 'PostgreSQL started'

export APP_MODULE=${APP_MODULE:-'main:apps'}

HOST=${HOST:-0.0.0.0}
PORT=${PORT:-8000}
LOG_LEVEL=${LOG_LEVEL:-info}

exec uvicorn --reload --host $HOST --port $PORT --log-level $LOG_LEVEL $APP_MODULE
