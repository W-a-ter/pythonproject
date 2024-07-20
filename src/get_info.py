from collections import defaultdict
import json


def get_info(my_transaction: list[dict], string_my: str) -> list[dict]:
    counter = []
    for i in my_transaction:
        if i.get('description', '') == string_my:
            counter.append(i)
    return counter


def category_search(transactions: list[dict]) -> dict:
    category = defaultdict(list)
    #counter = []
    for transaction in transactions:
        if transaction.get('description', '') == category:
            transaction.append(transaction)
    return transactions


with open('../Data/operations.json', encoding="utf-8") as file:
    info = json.load(file)
print(category_search(info))
#print (type(info))
