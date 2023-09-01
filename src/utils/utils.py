from pathlib import Path

import yaml

from settings import USERS


class ChatLogger:
    def __init__(self):
        self.users = list()

    @staticmethod
    def load_file(file) -> dict:
        try:
            with open(file, "r", encoding="UTF-8") as yaml_file:
                data = yaml.safe_load(yaml_file)
        except FileNotFoundError:
            return dict()
        if data is None:
            return dict()
        return data

    def save_file(self, file: Path, new_data: dict) -> None:
        """
        Сохранение файла
        :param file:
        :param new_data:
        :return:
        """
        # если файла нет, то создадим
        if not Path(file).exists():
            Path.touch(file)

        data = self.load_file(file)
        data.update(new_data)
        with open(file, 'w', encoding='UTF-8') as yaml_file:
            yaml.safe_dump(data, yaml_file, sort_keys=False, allow_unicode=True)

    def save_user(self, message):
        user = message.from_user
        data = {user.id: {'is_bot': user.is_bot,
                          'username': user.username,
                          'first_name': user.first_name,
                          'last_name': user.last_name,
                          'language_code': user.language_code,
                          }}

        self.save_file(USERS, data)

