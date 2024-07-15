from src.utils import my_file


def test_my_file(info_transaction):
    assert my_file('') == []
    assert my_file(1) == []
    assert my_file("../data/Test.json") == info_transaction
