import os

import requests
from dotenv import load_dotenv

load_dotenv()

Apikey = os.getenv('API_KEY')
url = os.getenv('url')


def my_transactions(transaction: dict) -> float:
    """принимает на вход транзакцию и возвращает сумму транзакции
    (amount) в рублях"""
    if transaction['operationAmount']['currency']['code'] == 'RUB':
        return float(transaction['operationAmount']['amount'])
    else:
        payload = {
            'amount': transaction['operationAmount']['amount'],
            'from': transaction['operationAmount']['currency']['code'],
            'to': 'RUB',
        }
        headers = {"apikey": Apikey}
        response = requests.get(str(url), headers=headers, params=payload)
        return response.json()['result']
