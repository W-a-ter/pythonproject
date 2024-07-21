import json
from collections import Counter



def get_info(my_transaction: list[dict], string_my: str) -> list[dict]:
    counter = []
    for i in my_transaction:
        if i.get('description', '') == string_my:
            counter.append(i)
    return counter


def category_search(transactions: list[dict], counter:list) -> dict:
    #category = Counter(transactions['description'])
    #counter = {}
    my_result = [transaction["description"] for transaction in transactions if transaction.get("description", "")
                in counter]
    return dict(Counter(my_result))


with open('../Data/operations.json', encoding="utf-8") as file:
    info = json.load(file)
print(category_search(info, 'Перевод'))
#print (type(info))
