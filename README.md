  Проект 'Атомные привычки' - это трекер полезных привычек.
  ---
  
**Как использовать:**
+ Клонировать репозиторий
+ Заполнить файл .env-sample и переименовать его в .env
+ Установить зависимости
  + poetry install или pip install -r requirements.txt
+ Создть и применить мигации 
  + python manage.py makemigrations
  + python manage.py migrate
+ Заполнить фикстурами(при необходимости), которые лежат в папке fixtures
  + python manage.py loaddata fixtures/habits_data.json
  + python manage.py loaddata fixtures/users_data.json
+ Запустить сервис
  + python manage.py runserver
---
**Документация**
+ http://localhost:8000/redoc/
+ http://localhost:8000/swagger/
---
**Описание полей:**
+ **action** - действие, которое представляет собой привычка. Обязательное поле. (CharField)
+ **place** - место, в котором необходимо выполнять привычку. Обязательно поле. (CharField)
+ **duration** - время, которое предположительно потратит пользователь на выполнение привычки. Не более 120 секунд. Обязательное поле. (DurationField, default=60)
+ **related_habit** - связанная привычка. Может быть только приятной и указываться вместо вознаграждения. (ForeignKey)
+ **reward** - вознаграждение за выполнение привычки. Может указываться вместо связанной привычки. (CharField)
+ **is_pleasurable** - признак того, что привычка является приятной. Приятная привычка не может иметь вознаграждения или связанной привычки. (BooleanFild, default=False)
+ **is_public** - признак публичноси. Возможность попадания в список публичных привычек, для просмотра другими пользователсями. (BooleanFild, default=False)
+ **days_of_week** - словарь с днями недели, в которые будет выполняться привычка. Обязательное поле. Необходимо указать минимум 1 день недели.
  + **monday** - понедельник. (BooleanFild, default=False)
  + **tuesday** - вторник. (BooleanFild, default=False)
  + **wednesday** - среда. (BooleanFild, default=False)
  + **thursday** - четверг. (BooleanFild, default=False)
  + **friday** - пятница. (BooleanFild, default=False)
  + **saturday** - суббота. (BooleanFild, default=False)
  + **sunday** - воскресенье. (BooleanFild, default=False)
+ **runtime** - словарь с полями времени, когда необходимо выполнять привычку. Обязательное поле.
  + **time_1** - время. Обязательное поле. (TimeFild)
  + **time_2** - время. (TimeFild)
  + **time_3** - время. (TimeFild)
  + **time_4** - время. (TimeFild)
  + **time_5** - время. (TimeFild)
  
---
**Пример минимального запроса для создания одной привычки:**
<pre>
  {
    "action": "Чистить зубы",
    "place": "Ванная комната",
    "duration": 60,
    "runtime": {
        "time_1": "22:00"
    },
     "days_of_week": {
        "monday": true
    }
}
</pre>

**Пример ответа:**
<pre>
{
    "action": "Чистить зубы",
    "place": "Ванная комната",
    "days_of_week": {
        "monday": true,
        "tuesday": false,
        "wednesday": false,
        "thursday": false,
        "friday": false,
        "saturday": false,
        "sunday": false
    },
    "runtime": {
        "time_1": "22:00",
        "time_2": null,
        "time_3": null,
        "time_4": null,
        "time_5": null
    },
    "duration": "60",
    "reward": null,
    "is_pleasurable": false,
    "is_public": false,
    "related_habit": null
}
</pre>
