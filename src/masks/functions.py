def get_mask_card_number(card_number):
    """Маскируем номер карты"""
    masked_number = ""
    for i in range(len(card_number)):
        if i < 6 or i >= len(card_number) - 4:
            masked_number += card_number[i]
        elif card_number[i] != " ":
            masked_number += "*"
        else:
            masked_number += " "

    return masked_number


def get_mask_account(account_number):
    """Маскируем номер счета"""
    masked_number = "**" + account_number[-4:]
    return masked_number
