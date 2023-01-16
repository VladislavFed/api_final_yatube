# Проект api_final

 ## Описание:

>YaTube - социальная сеть для авторов. Здесь вы можете создавать свои записи, добавлять их в сообщества, подписываться на авторов и комментировать их записи.
___
  ## Как запустить прект:
    
+ Склонируйте репозиторий [тут](git@github.com:VladislavFed/api_final_yatube.git) и перейдите в него.
  
+ Установите виртуальное окружение

    ```python
    python -m venv venv
    ```

+ Запустите виртуальное окружение

    ```python
    source venv/Scripts/activate
    ```

+ Установите зависимости

    ```python
    pip install -r requirements.txt
    ```

+ Выполните миграции

    ```python
    python manage.py migrate
    ```
+ Запустите сервер

    ```python
    python manage.py runserver
    ```

+ Создайте пользователя

    ```python
    python manage.py createsuperuser
    ```
___
 ## Примеры запросов:

Все виды запросов можно посмотреть по [ссылке](http://127.0.0.1:8000/redoc)
___
## Автор [Владислав Федотов](https://t.me/vlad_ocean) :ok_hand:

   