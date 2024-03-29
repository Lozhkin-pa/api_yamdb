# API YAMDb
## __Описание__
Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»). 

Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). 

Добавлять произведения, категории и жанры может только администратор.

Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.

Пользователи могут оставлять комментарии к отзывам.

Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.

## __Возможности API__
* Регистрация и авторизация пользователей при помощи токена (Simple JWT)
* Взаимодействие с учётными записями пользователей.
* Взаимодействие с категориями и жанрами произведений.
* Взаимодействие с комментариями и оценками.
* Взаимодействие с произведениями.

## __Установка__
1. Склонируйте репозиторий
```
> git clone https://github.com/Lozhkin-pa/api_yamdb.git
```
2. Установите и активируйте виртуальное окружение
```
> python -m venv venv
> source venv/Scripts/activate  - для Windows
> source venv/bin/activate - для Linux
```
3. Установите зависимости
```
> python -m pip install --upgrade pip
> pip install -r requirements.txt
```
4. Перейдите в папку api_yamdb и выполните миграции
```
> cd api_yamdb
> python manage.py migrate
```
5. Создайте суперпользователя
```
> python manage.py createsuperuser
```
6. Запустите проект
```
> python manage.py runserver
```

## __Примеры запросов к API__
После выполнения установки и запуска проекта будет доступна документация: `http://127.0.0.1:8000/redoc/`
Каждый ресурс API описан: указаны эндпоинты (адреса, по которым можно сделать запрос), разрешённые типы запросов, права доступа и дополнительные параметры, когда это необходимо.
```
> GET /api/v1/users/ - получение списка всех пользователей (в формате json):

{
  "count": 0,
  "next": "string",
  "previous": "string",
  "results": [
    {
      "username": "string",
      "email": "user@example.com",
      "first_name": "string",
      "last_name": "string",
      "bio": "string",
      "role": "user"
    }
  ]
}
```
```
> GET /api/v1/genres/ - получение списка всех жанров (в формате json):

{
  "count": 0,
  "next": "string",
  "previous": "string",
  "results": [
    {
      "name": "string",
      "slug": "string"
    }
  ]
}
```
```
> GET /api/v1/titles/ - получение списка всех произведений (в формате json):

{
  "count": 0,
  "next": "string",
  "previous": "string",
  "results": [
    {
      "id": 0,
      "name": "string",
      "year": 0,
      "rating": 0,
      "description": "string",
      "genre": [
        {
          "name": "string",
          "slug": "string"
        }
      ],
      "category": {
        "name": "string",
        "slug": "string"
      }
    }
  ]
}
```

## __Технологии__
![Python](https://img.shields.io/badge/Python-3.9.8-%23254F72?style=for-the-badge&logo=python&logoColor=yellow&labelColor=254f72)
![Django](https://img.shields.io/badge/Django-2.2.28-0C4B33?style=for-the-badge&logo=django&logoColor=white&labelColor=0C4B33)
![Django](https://img.shields.io/badge/Django%20REST-3.12.4-802D2D?style=for-the-badge&logo=django&logoColor=white&labelColor=802D2D)

## __Авторы__
* Category/Genre/Titles: [Павел Ложкин](https://github.com/Lozhkin-pa)<br>
* Auth/Users: [Андрей Толстопятов](https://github.com/AddSlash)<br>
* Reviews/Comments: [Брещайко Даниил](https://github.com/EuroGamesRu)<br>
