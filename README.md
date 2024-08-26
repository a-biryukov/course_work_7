  Проект 'Атомные привычки' - это трекер полезных привычек.
  ---
  
**Как использовать:**
+ Клонировать репозиторий
+ Заполнить файл .env-sample и переименовать его в .env
+ В settings заполнить ALLOWED_HOSTS, CORS_ALLOWED_ORIGINS и CSRF_TRUSTED_ORIGINS
+ Установить docker и docker-compose
+ Собрать образы и запустить контейнеры командой:
  + docker-compose up -d —build
---

**Описание полей:**
+ **action** - действие, которое представляет собой привычка. Обязательное поле. (CharField)
+ **place** - место, в котором необходимо выполнять привычку. Обязательно поле. (CharField)
+ **duration** - время, которое предположительно потратит пользователь на выполнение привычки. Не более 120 секунд. Обязательное поле. (DurationField, default=60)
+ **related_habit** - связанная привычка. Может быть только приятной и указываться вместо вознаграждения. (ForeignKey)
+ **reward** - вознаграждение за выполнение привычки. Может указываться вместо связанной привычки. (CharField)
+ **is_pleasurable** - признак того, что привычка является приятной. Приятная привычка не может иметь вознаграждения или связанной привычки. (BooleanField, default=False)
+ **is_public** - признак публичноси. Возможность попадания в список публичных привычек, для просмотра другими пользователсями. (BooleanField, default=False)
+ **days_of_week** - словарь с днями недели, в которые будет выполняться привычка. Обязательное поле. Необходимо указать минимум 1 день недели.
  + **monday** - понедельник. (BooleanField, default=False)
  + **tuesday** - вторник. (BooleanField, default=False)
  + **wednesday** - среда. (BooleanField, default=False)
  + **thursday** - четверг. (BooleanField, default=False)
  + **friday** - пятница. (BooleanField, default=False)
  + **saturday** - суббота. (BooleanField, default=False)
  + **sunday** - воскресенье. (BooleanField, default=False)
+ **runtime** - словарь с полями времени, когда необходимо выполнять привычку. Обязательное поле.
  + **time_1** - время. Обязательное поле. (TimeField)
  + **time_2** - время. (TimeField)
  + **time_3** - время. (TimeField)
  + **time_4** - время. (TimeField)
  + **time_5** - время. (TimeField)
  
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
    "duration": "60",
    "related_habit": null
    "reward": null,
    "is_pleasurable": false,
    "is_public": false,
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

}
</pre>
