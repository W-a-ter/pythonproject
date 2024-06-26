from typing import Any


def filter_by_currency(transactions: list, currency: str) -> Any:
    for i in transactions:
        if i["operationAmount"]["currency"]["code"] == currency:
            yield i


def transaction_descriptions(transactions: list) -> Any:
    for i in transactions:
        yield i["description"]


def card_number_generator(first: int, last: int) -> Any:
    """ генератор номеров карт в заданном диапазоне"""
    for card in range(first, last + 1):
        card_num = str(card)
        while len(card_num) < 16:
            card_num = "0" + card_num
        formatted_card_number = f"""""{card_num[0:4]} {card_num[4:8]}
        {card_num[8:12]} {card_num[-4:]}"""
        yield formatted_card_number
