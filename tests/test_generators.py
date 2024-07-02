import pytest
from src. generators import filter_by_currency


def test_filter_by_currensy():
    usd_transactions = filter_by_currency(dict_list(), "USD")
    for _ in range(1):
        assert (next(usd_transactions)["id"]) == "939719570"