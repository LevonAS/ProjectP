#!/bin/sh
cd ./app

# echo "/// Проверка на доступность DB Postgres..."
# ./entrypoint.sh

echo ' ///  Запуск миграций'
python ./manage.py migrate 
# echo ' ///  Сборка статических файлов'
# python ./manage.py collectstatic --noinput
echo ' ///  Загрузка фискур'
python ./manage.py  loaddata ./*/fixtures/*.json
# python ./manage.py  loaddata mainapp/fixtures/courses.json
# python ./manage.py  loaddata mainapp/fixtures/lesson.json
# python ./manage.py  loaddata mainapp/fixtures/mentor.json
# python ./manage.py  loaddata authapp/fixtures/studentuser.json

echo ' ///  Запуск Django'
python manage.py runserver 0.0.0.0:8000
# gunicorn --forwarded-allow-ips=* --bind 0.0.0.0:8080 -w 2 django_conf.wsgi:application
# gunicorn django_conf.wsgi:application --bind 0.0.0.0:8000
