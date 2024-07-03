import pytest
from src. generators import filter_by_currency, card_number_generator


def test_filter_by_currensy(dict_list):
    usd_transactions = filter_by_currency(dict_list, "USD")
    for _ in range(1):
        assert (next(usd_transactions)["id"]) == 939719570


def test_card_number_generator():
    for card_number in card_number_generator(1, 5):
        print(card_number)