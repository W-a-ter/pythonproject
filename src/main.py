from src.functions import get_mask_card_number, get_mask_account

credit_card_number = "8123456789112236"
masked_card_number = get_mask_card_number(credit_card_number)
print(masked_card_number)

account_number = "123456798446732"
masked_account = get_mask_account(account_number)
