
# Это сервис, который принимает запрос с указанием кадастрового номера, широты и долготы, эмулирует отправку запроса на внешний сервер.
В ТЗ используется такие технологии как Python, Django, Django Rest Framework, Docker, PostgreSQL. 

Для теста сервиса понадобится приложение Postman способное тестировать API.

# Как запустить весь проект?

### Первый способ. Через Docker.

Скачав проект с гитхаба напишите в командную строку 


```bash
docker-compose build

```
```
docker-compose run web python manage.py migrate  
```

```bash
docker-compose up   
```
Вы можете добавить флаг -d к команде, чтобы запустить контейнеры в фоновом режиме. 

```bash
docker-compose up -d  
```
После запуска переходим на главную страницу DRF http://127.0.0.1:8000/
Перед вами будут доступные эндпоинты.
```bash
{
    "query": "http://127.0.0.1:8000/query/",
    "result": "http://127.0.0.1:8000/result/",
    "history": "http://127.0.0.1:8000/history/",
    "ping": "http://127.0.0.1:8000/ping/"
}
```

### Второй способ. Вручную через localhost. Для этого способа нужно установить postgresql и указать ваш пороль и имя бд. Ну или воспользоваться SQLite. 

Преждевсего вам нужно зайти в файл settings.py и раскомментировать убрав #
```
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'db',
#         'USER': 'postgres',
#         'PASSWORD': 'Password',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }
``` 
И закомментировать следующее. 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}
```
Создаем виртуально окружение. 
```bash
python -m venv venv

venv\Scripts\Activate.ps1
```

#### Установите все зависимости из requirements.txt написав:
```bash
pip install -r requirements.txt
```

#### Затем последовательно введите:
```bash
cd service_for_requests
```
#### Проведите миграции.
```bash
python manage.py makemigrations
python manage.py migrate
```
#### Создайте админа.
```bash
python manage.py createsuperuser 
```


#### После регистрации запустите локальный сервер.
```bash
python manage.py runserver
```
#### Затем перейдите по ссылке "http://127.0.0.1:8000"
Перед вами будут доступные эндпоинты.
```bash
{
    "query": "http://127.0.0.1:8000/query/",
    "result": "http://127.0.0.1:8000/result/",
    "history": "http://127.0.0.1:8000/history/",
    "ping": "http://127.0.0.1:8000/ping/"
}
```

## Тестирование
#### После всего отправляем POST запрос через postman по эндпоинту http://127.0.0.1:8000/query/ данные ввиде JSON.
```
{
   "cadastre_number":"77:01:0000000:1234",
   "latitude":"48.8566",
   "longitude":"2.3522"
}
```
 Ждем пока отправляется запрос рандомное количество секунд до 60. =) Отправляем еще запрос.
```
{
   "cadastre_number":"35:04:41414277:6666",
   "latitude":"-55.2588",
   "longitude":"52.9874"
}
```
#### После добовления в бд данных можно взаимодейсвовать с API с браузера к примеру введя http://127.0.0.1:8000/result/1 мы увидем результат полученный от сервера.
 
#### Используя следующий эндпоинт http://127.0.0.1:8000/history/. Вы увидете историю запросов.

#### Эндпоинт http://127.0.0.1:8000/ping/ покажет запущен ли сервер.

# Приятного использования.    
