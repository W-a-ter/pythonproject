from src.functions import get_mask_card_number, get_mask_account


def mask_account_card(card_type: str) -> str:
    '''функция, которая принимает на вход строку с информацией
     — тип карты/счета и номер карты/счета.'''
    masked_string = ""
    if "Visa Platinum" in card_type:
        num_card = card_type.replace("Visa Platinum ", "")
        masked_string += "Visa Platinum " + get_mask_card_number(num_card)
    elif "Maestro" in card_type:
        num_card = card_type.replace("Maestro ", "")
        masked_string += "Maestro " + get_mask_card_number(num_card)
    else:
        num_card = card_type.replace("Счет ", "")
        masked_string += "Счет " + get_mask_account(num_card)
    return masked_string


def get_data(data_string: str) -> str:
    '''функция, которая принимает на вход строку'''
    return f"{data_string[8:10]}.{data_string[5:7]}.{data_string[0:4]}"
