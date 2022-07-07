# CodingTeam (Задание)

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
4. `graphene==2.1.8`

## Установка

---
#### Перед началом работы настройте виртуальное окружение: pyenv:
1. [Руководство по настройке PYENV](https://github.com/pyenv/pyenv)

### Зависимости
1. После настройки виртуального окружения устанавливаем зависимости из `requirements.txt`
    ```bash
    $(server) pip install -r requirements.txt
    ```
   

2. Перед запуском проекта необходимо добавить следующие файлы:
    * `.env` в каталог:`CodingTeam/api/`:
   
    ```
   SECRET_KEY = '7nvd^ezxpewn08bo$os3_yala-0xx=79h*@p+*0fn2k$6wnexu'
    ```
   
   * `config.ini` в каталог:`CodingTeam/api/server/server/`
    ```
   [Manage]
   PORT = 8000
   [DEBUG]
   STATUS = True
    ```

## Команды

---
### Запуск сервера
В папке проекта (например `CodingTeam/api/server/`):
```bash
$(server) python manage.py runserver
```

### Остановка сервера

В папке проекта (например `itresume/api/dev/server/`):
```bash
$ Прервать процесс нажатием (Ctrl + C)
```

## Мониторинг

---
**Логи** API сохраняются в течение 3-х дней и находятся в `server/Logs/`.
**Логи** последнего запуска в `server/Logs/API.log`

## Документация

1. Перейти в каталог `api/docs/`
2. Открыть файл `_build/html/index.html`

**Обновление документации:**

В случае обновления `docstrings`, приложений проекта, или же самой структуры `sphinx-docs`
**требуется обновление итогового файла**:

1. Проверить наличие [sphinx](https://pypi.org/project/Sphinx/) в ``env``, выполнить
   ```bash
   (env) pip install sphinx
   ```
2. В директории `api/docs/` выполнить
   ```bash
   (env) make html
   ```

## Тестирование

---
**Примечание** Запуск тестов, например из каталога: `itresume/api/dev/server/`

1. Проверка приватности задач:
```bash
   $(env_name) python tests/problems/private_problem_test.py
```
2. Создание userCV:
```bash
   $(env_name) python tests/cv/module_test.py
```
3. Тестирование Блога с помощью pytest:
```bash
   $type = <localhost | dev | debug | prod>
   $(env_name) pytest autotests/blog/tests_article_list.py --server_type $type 
```