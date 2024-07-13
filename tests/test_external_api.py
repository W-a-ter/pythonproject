from src.external_api import my_transactions
from unittest.mock import Mock


def test_my_transactions(dict_list_my):
    mock_random = Mock(return_value=100.0)
    dict_list_my ['operationAmount']['amount'] = float(mock_random)
    assert my_transactions(dict_list_my) == 100.0
