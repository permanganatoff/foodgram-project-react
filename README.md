
# Foodgram - социальная сеть для публикации рецептов еды.
https://vm-permang.hopto.org/

Фудграм - веб-приложение и API для публикации рецептов еды.
В Фудграме вы можете публиковать собственные рецепты, подписываться на других пользователей, 
добавлять понравившиеся рецепты в Избранное, выгружать список продуктов для покупки их в магазине.

Документация по API доступна по адресу:
https://vm-permang.hopto.org/api/docs


## Инструкция по установке

### Локальная установка
1. Клонируйте репозиторий:
```
git clone git@github.com:permanganatoff/foodgram-project-react
cd foodgram-project-react
```

2. В корневой директории создайте .env файл с переменными.

3. Создайте виртуальное окружение:
```
python -m venv venv
```
4. Активируйте виртуальное окружение:
* for Linux/Mac:
```source venv/bin/activate```

* for Windows:
```source venv/Scripts/activate```

4. Установите зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```
5. В backend/setting.py замените PostgreSQL на SQLite:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

6. Примените миграции:
```
python manage.py migrate
```
7. Соберите статику:
```
python manage.py collectstatic --no-input
```
8. Создайте суперпользователя:
```
python manage.py createsuperuser
```
9. Загрузите базу данных игредиентов для рецептов:
```
python manage.py load_csv
```
10. В директории, где находится файл manage.py запустите сервер разработки:
```
python manage.py runserver
```
Документация по API доступна локально по адресу:
```
http://127.0.0.1:8000/api/docs/
```

### Деплой проекта в контейнерах:

1. Установите Докер
[Installation instructions (Win/Mac/Linux)](https://docs.docker.com/compose/install/)

- Linux:
```
sudo apt install curl                                   
curl -fsSL https://get.docker.com -o get-docker.sh      
sh get-docker.sh                                        
sudo apt-get install docker-compose-plugin              
```


2. В корневой директории создайте файл .env file и заполните его:
```
SECRET_KEY=django-insecure-**************************************
DEBUG=True
ALLOWED_HOSTS=ip-адрес-сервера,127.0.0.1,localhost,адрес-сайте.ру
POSTGRES_USER=foodgram_user
POSTGRES_PASSWORD=foodgram_password
POSTGRES_DB=foodgram_db
# Django
DB_HOST=db
DB_PORT=5432
DB_NAME=foodgram_db
```

3. Из папки infra/ folder, запустите контейнеры:
```
docker-compose up -d --build
```
4. Примените миграции:
```
docker-compose exec backend python manage.py migrate
```
5. Создайте суперпользователя:
```
docker-compose exec backend python manage.py createsuperuser
```
6. Соберите статику:
```
docker-compose exec backend python manage.py collectstatic --no-input
```
7. Загрузите в базу данные игредиенты для рецептов.
```
docker-compose exec backend python manage.py load_csv
```

## Стек технологий
- Python 3.10.11
- Django 4.2.5
- Django REST framework 3.14
- Nginx
- Docker
- PostgreSQL

## Разработчик 
Пономарев Павел, Ижевск, Россия
permanganatoff@gmail.com
https://github.com/permanganatoff/foodgram-project-react