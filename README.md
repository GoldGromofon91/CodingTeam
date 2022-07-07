# CodingTeam ([Задание](https://gist.github.com/ir0nfelix/88095feccf59824a60deb0ddb3aa3f29))


1. [Требования](#Требования)
2. [Установка](#Установка)
3. [Команды](#Команды)
4. [Мониторинг](#Мониторинг)
5. [Тестирование](#Тестирование)
6. [Документация](#Документация)

## Требования 

---
1. `python==3.8.9`
2. `django==2.2`
3. `djangorestframework==3.13.1`
4. `graphene==2.1.8`
5. `sphinx`

## Установка

---
#### Перед началом работы настройте виртуальное окружение: pyenv:
1. [Руководство по настройке PYENV](https://github.com/pyenv/pyenv)

### Зависимости

1. После настройки виртуального окружения устанавливаем зависимости из `requirements.txt`
    ```bash
    $(env) pip install -r requirements.txt
    ```
   
2. Перед запуском проекта необходимо добавить следующие файлы:
    * `.env` в каталог:`CodingTeam/api/`:
   
    ```
   SECRET_KEY = 'ug2c+o7(8=bjpv1m*s=y7e$n*0k)79ubd()_)*@vvvg#n$76ne'
    ```
   
   * `config.ini` в каталог:`CodingTeam/api/server/server/`
    ```
   [Manage]
   PORT = 8080
   [DEBUG]
   STATUS = True
   [GRAPHQL]
   STATUS = True
    ```

## Команды
---
### Миграции
После скачивания репозитория, необходимо применить миграции проекта и приложений
В папке проекта (например `CodingTeam/api/server/`):
```bash
$(env) python manage.py migrate
```

### Заполнение БД
После установки миграций, необходимо заполнить тестовыми данными БД, для этого
в папке проекта (например `CodingTeam/api/server/`):
```bash
$(env) python manage.py fill_db
```

### Запуск сервера
В папке проекта (например `CodingTeam/api/server/`):
```bash
$(env) python manage.py runserver
```

### Проверка endpoint:
Для проверки работоспособности перейти на следующие url's:

```
   http://127.0.0.1:8080/api/v1/foods/ - для проверки DRF
   http://127.0.0.1:8080/api/graphql/ - для проверки GraphQl
```

### Остановка сервера

В папке проекта (например `CodingTeam/api/server/`):
```bash
$ Прервать процесс нажатием (Ctrl + C)
```

## Мониторинг

---
**Логи** API сохраняются в течение 3-х дней и находятся в `server/Logs/`.
**Логи** последнего запуска в `server/Logs/API.log`

## Документация

1. Перейти в каталог `CodingTeam/docs/`
2. Открыть файл `_build/html/index.html`


## Тестирование

---
Для запуска тестов в папке проекта (например `CodingTeam/api/server/`):

```bash
$(env) pytest
```