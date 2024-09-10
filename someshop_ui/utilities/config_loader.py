import json


def load_config():
    """
    Открывает json файл с данными зарегистрированного пользователя, служит для придания большей гибкости проекту
    :return:
    """
    with open('../config/data.json', 'r') as file:
        return json.load(file)