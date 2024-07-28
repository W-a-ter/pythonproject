from src.get_info import get_info, category_search


def test_get_info(info_transaction):
    assert get_info(info_transaction, 'description') == []


def test_category_search(info_transaction):
    assert category_search(info_transaction, 'description') == {}
