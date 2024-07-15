import json
import logging

""" создаем логгер для логирования функций и пишем логи в директорию logs"""
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s:%(name)s - %(levelname)s - %(message)s",
    filename="../logs/utils.log",  # Запись логов в файл
    filemode="w",
)  # Перезапись файла при каждом запуске
text = logging.getLogger("utils.py")


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
                text.info('функция отработала')
                return info
    except FileNotFoundError:
        text.warning('File_not_found')
        return []
    except json.decoder.JSONDecodeError:
        text.critical('json.DecodeError!!!')
        return []
