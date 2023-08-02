# Shopland
  Интернет магазин одежды <br/>
  p.s. выполнение ТЗ 


# Установка и запуск

    Клонировать репозиторий: git clone https://github.com/ilgamkhisam/shopland.git
    Установить зависимости: pip install -r requirements.txt
    Применить миграции: python manage.py migrate
    Запустить сервер: python manage.py runserver

## Использование
  Эндпоинты API:

    GET / - Swagger UI для документации API.

    POST /singup/ - Регистрация нового пользователя.

    POST /login/ - Получение пары токенов аутентификации.

    POST /login/refresh/ - Обновление access token.

    GET /products/ - Получение списка всех товаров.

    GET /products/product/<int:pk>/ - Получение детальной информации о товаре по его идентификатору.

    POST /add_to_favorite/<int:product_id>/ - Добавление товара в список избранных.

    DELETE /remove_from_favorite/<int:product_id>/ - Удаление товара из списка избранных.

## Технологии

    Django 
    Django REST framework 
    Pillow 
    djangorestframework-simplejwt


## Авторы

    Ilgamkhsiam
