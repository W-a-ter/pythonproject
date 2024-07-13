from src.external_api import my_transactions
from unittest.mock import patch


@patch('requests.get')
def test_my_transactions(mock_get, dict_list_my):
    mock_get.return_value.json.return_value = 9824.07
    assert my_transactions(dict_list_my) == 9824.07
