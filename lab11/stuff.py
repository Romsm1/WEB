from redis import Redis
from core import config

BASE = "http://localhost:8000/api/api_v1"

r = Redis(port=config.REDIS_PORT, host=config.REDIS_HOST, db=config.REDIS_DB, decode_responses=True)
print(f"Redis ping: {r.ping()}")

# добавление токенов
r_tokens = Redis(port=config.REDIS_PORT, host=config.REDIS_HOST, db=config.REDIS_DB_TOKENS, decode_responses=True)
r_tokens.delete(config.REDIS_TOKENS_SET_NAME)
r_tokens.sadd(config.REDIS_TOKENS_SET_NAME, "foh2ef19-32eef432f4")  # api токен для тестов
print(f"Токен добавлен: {r_tokens.smembers(config.REDIS_TOKENS_SET_NAME)}")

# добавление пользователя и его пароля
r_users = Redis(port=config.REDIS_PORT, host=config.REDIS_HOST, db=config.REDIS_DB_USERS, decode_responses=True)
r_users.set("users:admin", "1234")
print(f"Пользователи в базе: {[key.replace('users:', '') for key in r_users.keys('users:*')]}")
