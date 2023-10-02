# ProjectP
Сайт для онлайн-школы развития креативных навыков у детей и подростков.

### Сборка/запуск контейнера с проектом для разработки
Для сборки контейнера необходимы:
- папка git_con с содержимым
- Dockerfile.git
- docker-compose.yml

Сборка/запуск контейнера командой: \
    sudo docker-compose -f docker-compose.yml up --build

Запускается один контейнер.\
Содержимое папки проекта "app" подтягивается с Git непосредственно в контейнер на стадии сборки.\
Сайт работает с внутренней БД db.sqlite3 (SQLite).\
Сайт отвечает на порту 8000.\
Там правда PRIVATE KEY (/git_con/git_tw_rsa) в репозитории светится и GIT это не нравится

### Сборка/запуск контейнера в продакшене
Запускаются 4 контейнера:
- django-web
- DB Postgres
- pgAdmin - управление для Postgres
- nginx
\Будет позже.

### Окружение разработки
- asgiref==3.7.2
- Django==4.2.5
- django-bootstrap5==23.3
- psycopg2-binary==2.9.8
- requests==2.31.0
- pytz==2023.3
- sqlparse==0.4.3
- gunicorn==21.2.0

- python 3.11.5
- vUbuntu Server 22_04.

## Лицензия
MIT