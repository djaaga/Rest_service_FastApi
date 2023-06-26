# Инструкция по запуску сервиса и взаимодействию с проектом

## Шаг 1: Установка зависимостей

1. Убедитесь, что на вашем компьютере установлен Python.
2. Создайте новую директорию для проекта и перейдите в нее через командную строку или терминал.
3. Создайте виртуальное окружение Python для проекта:
python -m venv myenv

4. Активируйте виртуальное окружение:

- Для Windows:

  ```
  myenv\Scripts\activate
  ```

- Для macOS и Linux:

  ```
  source myenv/bin/activate
  ```

5. Создайте файл `requirements.txt` и добавьте следующие строки:

fastapi
uvicorn

6. Установите зависимости с помощью команды:

pip install -r requirements.txt

## Шаг 2: Реализация и запуск сервиса

1. Создайте новый файл `main.py` и скопируйте в него код сервиса.
2. Сохраните файл `main.py`.

3. Запустите сервер FastAPI с помощью команды:

uvicorn main:app --reload

Здесь `main` - это имя файла (`main.py`), а `app` - это имя экземпляра FastAPI в вашем коде.

4. После запуска сервера вы увидите вывод, указывающий на то, что сервер работает и слушает определенный порт (обычно 8000).

## Шаг 3: Взаимодействие с сервисом

Теперь, когда ваш сервер работает, вы можете взаимодействовать с ним с помощью инструментов, таких как cURL или Postman.

- Для аутентификации и получения токена, отправьте POST-запрос на адрес `http://localhost:8000/login` с указанием в теле запроса логина и пароля сотрудника.

- После успешной аутентификации вы получите ответ с токеном.

- Для получения данных о зарплате, отправьте GET-запрос на адрес `http://localhost:8000/salary` и добавьте параметр `token` со значением полученного токена.
