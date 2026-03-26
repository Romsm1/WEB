from redis import Redis
from core import config
import requests

BASE = "http://localhost:8000/api/api_v1"

r = Redis(port=config.REDIS_PORT, host=config.REDIS_HOST, db=config.REDIS_DB, decode_responses=True)
print(f"Redis ping: {r.ping()}")

r.flushall()  # очищаем все бд перед тестами

# добавление токенов
r_tokens = Redis(port=config.REDIS_PORT, host=config.REDIS_HOST, db=config.REDIS_DB_TOKENS, decode_responses=True)
r_tokens.delete(config.REDIS_TOKENS_SET_NAME)
r_tokens.sadd(config.REDIS_TOKENS_SET_NAME, "foh2ef19-32eef432f4")  # api токен для тестов
print(f"Токен добавлен: {r_tokens.smembers(config.REDIS_TOKENS_SET_NAME)}")

# добавление пользователя и его пароля
r_users = Redis(port=config.REDIS_PORT, host=config.REDIS_HOST, db=config.REDIS_DB_USERS, decode_responses=True)
r_users.set("users:admin", "1234")
print(f"Пользователи в базе: {[key.replace('users:', '') for key in r_users.keys('users:*')]}")

# Просмотр всех книг
resp = requests.get(f"{BASE}/books/")
print(f"Все книги: {resp.json()}")

# Проверка API
# Удаление книги harry с APi-токеном И Basic Auth !!!некорректные данные!!!
resp = requests.delete(f"{BASE}/books/harry",
                       headers={"Authorization": "Bearer token492439449344342343"},
                       auth=("tolik", "1eewffe234"))
print(f"DELETE с токеном и Basic Auth: {resp.status_code}")

# Удаление книги harry с APi-токеном И Basic Auth
resp = requests.delete(f"{BASE}/books/harry",
                       headers={"Authorization": "Bearer foh2ef19-32eef432f4"},
                       auth=("admin", "1234"))
print(f"DELETE с токеном и Basic Auth: {resp.status_code}")

# Изменение книги со слагом ring !!!некорректные данные!!!
resp = requests.put(f"{BASE}/books/ring",
                    headers={"Authorization": "Bearer wdokqowkdowkdwwq2132132112421d232d33d23d32d23d23d23d32ddd23"},
                    auth=("admin", "1214214254643344756767567234"),
                    json={"title": "Test Title", "description": "книга про кольцо", "pages": 12345})
print(f"Все книги: {resp.json()}")

# Изменение книги со слагом ring
resp = requests.put(f"{BASE}/books/ring",
                    headers={"Authorization": "Bearer foh2ef19-32eef432f4"},
                    auth=("admin", "1234"),
                    json={"title": "Test Title", "description": "книга про кольцо", "pages": 12345})
print(f"Все книги: {resp.json()}")

# только редис
# r = Redis(port=config.REDIS_PORT, host=config.REDIS_HOST, db=config.REDIS_DB, decode_responses=True)
# print(f"Redis ping: {r.ping()}")

# r.flushall()

# добавление токенов
# r_tokens = Redis(port=config.REDIS_PORT, host=config.REDIS_HOST, db=config.REDIS_DB_TOKENS, decode_responses=True)
# r_tokens.delete(config.REDIS_TOKENS_SET_NAME)
# r_tokens.sadd(config.REDIS_TOKENS_SET_NAME, "foh2ef19-32eef432f4")
# print(f"Токен добавлен: {r_tokens.smembers(config.REDIS_TOKENS_SET_NAME)}")

# добавление пользователя
# r_users = Redis(port=config.REDIS_PORT, host=config.REDIS_HOST, db=config.REDIS_DB_USERS, decode_responses=True)
# r_users.set("users:admin", "1234")
# print(f"Пользователи в базе: {[key.replace('users:', '') for key in r_users.keys('users:*')]}")

# проверка наличия токена
# print(f"Проверка токена foh2ef19-32eef432f4: {r_tokens.sismember(config.REDIS_TOKENS_SET_NAME, 'foh2ef19-32eef432f4')}")
# print(f"Проверка токена invalid: {r_tokens.sismember(config.REDIS_TOKENS_SET_NAME, 'invalid')}")

# проверка пользователя
# print(f"Проверка пароля admin: {r_users.get('users:admin') == '1234'}")
# print(f"Проверка пароля admin с wrong: {r_users.get('users:admin') == 'wrong'}")
