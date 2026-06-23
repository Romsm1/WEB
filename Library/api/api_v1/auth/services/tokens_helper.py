import secrets
from abc import ABC, abstractmethod


class AbstractTokensHelper(ABC):
    @abstractmethod
    def token_exists(
        self,
        token: str,     # Проверяет есть ли токен
    ) -> bool:
        """
        :param token:
        :return:
        """

    @abstractmethod
    def add_token(
        self,
        token: str,     # Добавляет токен
    ):
        """
        :param token:
        :return:
        """

    @abstractmethod
    def get_tokens(self) -> list[str]:      # Получает все токены
        pass

    @abstractmethod
    def delete_token(
        self,
        token: str,     # Удаляет токен
    ) -> bool:
        pass

    @classmethod
    def generate_token(cls):
        return secrets.token_urlsafe(16)    # Генерирует случайный токен

    def generate_and_save_token(self) -> str:
        token = self.generate_token()
        self.add_token(token)       # Генерирует и сохраняет токен
        return token
