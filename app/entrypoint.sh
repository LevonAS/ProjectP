#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "/// Проверка на доступность DB Postgres..."

    # Проверяем доступность хоста и порта
    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "/// Postgres запущен"
fi

exec "$@"