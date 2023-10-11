#!/bin/sh
# sleep 2000
cd /djangoapp/

echo "/// Folders clear"
# очистка папок статики
rm -rf /djangoapp/app/static/*
rm -rf /djangoapp/app/media/*

# заливка репозитория App с GIThub в контейнер 
# git clone git@github.com:LevonAS/ProjectP.git /djangoapp

echo "/// GIT 1"
# Инициализируем пустой репозиторий в директории.
git init .
echo "/// GIT 2"
# Добавляем удаленный репозиторий. 
git remote add -f origin git@github.com:LevonAS/ProjectP.git
echo "/// GIT 3"
# Выбираем ветку с которой хотим работать.
git checkout main
echo "/// GIT 4"

cd /djangoapp/app

# touch .env
# echo 'SECRET_KEY="django-insecure-4jd-=sj^cxn283mibu0-#&i=ouih(ds_oxk61+^!yi^e%i$yyr"' >> ./.env
# echo 'DEBUG=1' >> ./.env
# echo 'POSTGRES_ENGINE=django.db.backends.sqlite3' >> ./.env

echo "/// Проверка на доступность DB Postgres..."
chmod +x ./entrypoint.sh
./entrypoint.sh

echo ' ///  Запуск миграций'
python ./manage.py migrate 
echo ' ///  Сборка статических файлов'
python ./manage.py collectstatic --noinput

echo ' ///  Запуск Django'

# python manage.py runserver 0.0.0.0:8000
# gunicorn --forwarded-allow-ips=* --bind 0.0.0.0:8080 -w 2 django_conf.wsgi:application
gunicorn django_conf.wsgi:application --bind 0.0.0.0:8000
