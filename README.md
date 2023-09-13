 # Medical Exam Database
  
  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
  ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) 
  ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
  ![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)
  ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
  ![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)


## API для работы с базой данных медицинских тестов [DEMO](http://medtest.ddns.net)


### Техзадание:
Реализовать API медидицинской базы данных на стеке Python 3.10+, Django 4.2, DRF 3.14, PostgreSQL 14+

### Структура API эндпоинта:
<details>
```json
{
    "id": "1019d05d-8683-4410-b4c1-01014ee99575",
    "lab_id": "1fc0e364-0fbb-4884-99ce-93e9d541dbfd",
    "duration_seconds": 360,
    "results": [
        {
            "id": "4f394168-b88b-404f-a1d6-9c710f9ad752",
            "score": "0.12345",
            "indicator_name": "способность к усвоению информации",
            "metric_name": "cкорость реакции",
            "metric_unit": "секунды",
            "is_within_normal_range": true,
        },
        {
            "id": "ad03ba61-6f67-4776-b61d-6557e27ab3c1",
            "score": "99.00000",
            "indicator_name": "cпособность к усвоению информации",
            "metric_name": "доля ошибок",
            "metric_unit": "%",
            "is_within_normal_range": false,
        },
		…
    ],
}
```
</details>


- Фильтрация по lab_id.

- AutoUpdateTrigger.  

- Авторизация Token. 

- Документация Swagger.

- Docker compose.

- Функциональные тесты

- Git rep

- CI/github actions

- Инструкция по запуску

- Документация


<details>
  <summary>
    <h2>Запуск проекта</h2>
  </summary>


1. Клонировать репозиторий на linux host.
   ```
   $ git clone https://github.com/tr202/medical_exam.git
   ```
2. Перейти в папку проекта :
  
     ```
      $ cd /medical_exam/
     ```
 
3. Сделать скрипт запуска исполняемым:
    ```
      $ sudo chmod ugo+x start
      $ sudo chmod ugo+x stop
    ```
4. Запуск приложения:
    ```
      $ sudo ./start
    ```
    Содержимое файла
    ```
        #!/bin/bash
		docker-compose -f docker-compose.yml up -d
		docker-compose -f docker-compose.yml exec catalog python manage.py migrate
		docker-compose -f docker-compose.yml exec catalog python manage.py collectstatic
		docker-compose -f docker-compose.yml exec catalog cp -r /app/collected_static/. /static/static
		docker-compose -f docker-compose.yml exec catalog python manage.py loaddata db.json
		echo Test the endpoints
    ```
  
5. Остановка:
   ```
       $ sudo ./stop
   ```
     Содержимое файла:
   ```
        #!/bin/bash
		docker-compose -f docker-compose.yml down
        
   ```
</details>   
   
### После запуска доступны следующие эндпоинты:

```
http://host:8000/docs - Документация Swagger
http://host:8000/admin - Админ зона django
http://host:8000/api/tests - Эндпоинт тестов
http://host:8000/api/tests/?lab_id=UUID - Где UUID один из id лабораторий созданных в базе данных, можно посмотреть на предыдущем эндпоинте.  

```

### Регистрация нового пользователя
> Можно использовать Postman
```
Сделать POST запрос на: http://host:8000/users/
Payload:
  {
  "email": "user@example.com",
  "username": "string",
  "password": "string"
  }
При успешной регистрации будет возвращен id пользователя, теперь можно получить токен для этого:
Сделать POST запрос на: http://host:8000/auth/token/login/
Payload:
  (
  "password": "string",
  "username": "string"
  }
```
В ответе будет токен, теперь его можно поставить в Authorization header c префиксом Token
и делать авторизованные запросы к API.


