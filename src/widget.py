from src.masks.functions import get_mask_card_number, get_mask_account


def mask_account_card(account_information: str) -> str:
    """ Функция принимает номер карты или счета
    и возвращает строку с замаскированным
    номером карты\\счета
    """
    masks_account_information = ""
    account_number = ""

    for slice_info in account_information.split():
        if slice_info.isalpha() is True:
            masks_account_information += slice_info + " "
        elif slice_info.isdigit() is True:
            account_number += slice_info

    if masks_account_information == "Счет ":
        masks_account_information += get_mask_account(account_number)
    else:
        masks_account_information += get_mask_card_number(account_number)

    return masks_account_information


def get_data(data_string: str) -> str:
    """функция, которая принимает на вход строку"""
    return f"{data_string[8:10]}.{data_string[5:7]}.{data_string[0:4]}"
