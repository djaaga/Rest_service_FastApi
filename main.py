from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from datetime import datetime, timedelta

app = FastAPI()
security = HTTPBasic()

# Пример базы данных с данными о сотрудниках
users_db = {
    "john": {"password": "password123", "salary": 5000,
             "next_promotion_date": "2023-01-01"
             },
    "jane": {"password": "password456", "salary": 6000,
             "next_promotion_date": "2023-02-01"
             }
}

# Хранение токенов
tokens = {}


def is_token_valid(token):
    '''Функция для проверки валидности токена'''
    return token in tokens and tokens[token] > datetime.now()


@app.post("/login")
def login(credentials: HTTPBasicCredentials = Depends(security)):
    '''Метод аутентификации'''
    username = credentials.username
    password = credentials.password

    if username not in users_db or users_db[username]["password"] != password:
        raise HTTPException(status_code=401,
                            detail="Неверный логин или пароль"
                            )

    # Создание токена, действующего в течение 1 часа
    token = datetime.now() + timedelta(hours=1)
    tokens[token] = username

    return {"token": token}


@app.get("/salary")
def get_salary(token: str):
    '''Защищенный маршрут для получения данных о
    зарплате и дате следующего повышения'''
    if not is_token_valid(token):
        raise HTTPException(status_code=401, detail="Неверный токен")

    username = tokens[token]
    user_data = users_db[username]
    salary = user_data["salary"]
    next_promotion_date = user_data["next_promotion_date"]

    return {"salary": salary, "next_promotion_date": next_promotion_date}
