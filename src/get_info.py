from collections import Counter
import re


def get_info(my_transaction: list[dict], string_my: str) -> list[dict]:
    '''функция фильтрует транзакции по строке поиска'''
    counter = []
    for i in my_transaction:
        if re.search(string_my, i.get('description', '')):
            counter.append(i)
    return counter


def category_search(transactions: list[dict], counter: str) -> dict:
    """Функция читает исходный файл и преобразует его
        в список с правильно оформленными именами, без символов и пробелов"""
    my_result = [transaction['description'] for transaction in transactions
                 if counter in transaction.get('description', '')]
    return dict(Counter(my_result))
