import json


def my_file(my_str: str) -> list[dict]:
    """  принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(my_str) as file:
            info = json.load(file)
            if type(info) is not list:
                return []
            elif info is []:
                return []
            else:
                return info
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        return []
