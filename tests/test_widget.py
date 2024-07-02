import pytest
from src.widget import mask_account_card, get_data


@pytest.mark.parametrize(
    "card_account, masks_card_account",
    [("Visa 1234567890123456", "Visa 1234 56** **** 3456"),
     ("Счет 12345678901234567890", "Счет **7890")],
)
def test_mask_account_card(card_account, masks_card_account):
    assert mask_account_card(card_account) == masks_card_account


def test_get_data(data_info, exp_data):
    assert get_data(data_info) == exp_data
