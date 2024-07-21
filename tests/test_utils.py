from src.utils import my_file, my_file_csv, my_file_xlsx
from unittest.mock import patch, mock_open, Mock
import pandas as pd


def test_my_file(info_transaction):
    assert my_file(1) == []
    assert my_file("") == []

    assert my_file("../Data/test.operations.json") == []


def test_my_file_(final_info, test_info_xlcx):
    info_csv = list(my_file_csv("../Data/transactions.csv"))
    assert info_csv[0] == final_info

    info_xlsx = list(my_file_xlsx("../Data/transactions_excel.xlsx"))
    assert info_xlsx[0] == test_info_xlcx


@patch("tests.test_utils.pd.read_csv")
def test_my_file_csv(test_info_csv, test_info_xlcx):
    Mock.return_value = pd.DataFrame()
    assert my_file_csv('foo') == []

    info_xlsx = list(my_file_xlsx("../Data/transactions_excel.xlsx"))
    assert info_xlsx[0] == test_info_xlcx


@patch("builtins.open", new_callable=mock_open, read_data="data")
def test_get_info_transactions_csv_xlsx(mock_file):
    assert open("../Data/test_transactions.csv").read() == "data"
    mock_file.assert_called_with("../Data/test_transactions.csv")

    assert open("../Data/transactions_excel.xlsx").read() == "data"
    mock_file.assert_called_with("../Data/transactions_excel.xlsx")







