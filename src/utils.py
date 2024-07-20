import json
import logging

import pandas as pd


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
        with open(my_str, encoding="utf-8") as file:
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


def my_file_csv(my_csv: str) -> list[dict]:
    """  принимает на вход путь до CSV -файла и
    возвращает список словарей с данными о финансовых транзакциях"""
    with open(my_csv, encoding='utf-8') as file:
        readed_file = pd.read_csv(file)
        return readed_file.to_dict(orient="records")


def my_file_xlsx(my_xlsx: str) -> list[dict]:
    """  принимает на вход путь до XLSX -файла и
    возвращает список словарей с данными о финансовых транзакциях"""
    xlsx_file = pd.read_excel(my_xlsx)
    return xlsx_file.to_dict(orient='records')
